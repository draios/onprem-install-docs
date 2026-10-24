#!/usr/bin/env python3
"""Verify that an installer RBAC example is sufficient to run the installer.

These examples drifted silently for years because nothing checked them. This
script encodes the two rules that are easy to get wrong by hand:

  APPLY      the installer `kubectl apply`s every rendered object, so it needs
             get + create + patch on that resource, in the right scope
             (cluster-scoped kinds cannot be granted by a Role).

  ESCALATION Kubernetes RBAC privilege-escalation prevention: a ServiceAccount
             that creates a Role or ClusterRole must already hold every
             permission listed inside it. The installer creates RBAC for the
             Zalando Postgres operator and for the Patroni pods, so the
             installer's own rules must be a superset of theirs.

Usage:
    ./verify.py kubernetes-pgha           # vanilla Kubernetes + Postgres HA
    ./verify.py fullaccess --no-pgha      # vanilla Kubernetes, no Postgres HA

Requires `helm` on PATH and PyYAML. Exits non-zero if the example is short of
any permission.
"""

import argparse
import os
import subprocess
import sys
import tempfile

import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
CHART = os.path.normpath(os.path.join(HERE, "..", "..", "sysdig-chart", "charts", "postgres-ha"))

# Vanilla Kubernetes, Postgres in HA, chart defaults elsewhere.
PGHA_VALUES = """
global:
  apps: "monitor,secure"
  namespace: sysdigcloud
  deployment: kubernetes
  postgresql:
    ha:
      enabled: true
      replicas: 3
      tls: {enabled: false}
      networkPolicy: {enabled: false, ingresses: []}
postgresql:
  external: false
  ha:
    checkCRD: true
"""

# ---------------------------------------------------------------------------
# Requirements that do not come from the postgres-ha chart.
#
# IMPORTANT: unlike the Postgres HA requirements below, which are *derived* by
# rendering the chart, this set is hand-maintained. It is a FLOOR, not a
# complete model of a default install: 16 charts under sysdig-chart/charts ship
# RBAC or cluster-scoped objects, and which of them render depends on
# global.apps and a long tail of feature flags. Deriving all of that would risk
# reporting permissions as missing that a given install does not actually need,
# which is worse than reporting too few. So a pass in --no-pgha mode means "none
# of the known-required permissions are missing", not "this example is
# sufficient". Extend the set when you find something else the installer needs.
#
# Verified against the charts that render on a default vanilla install with
# global.apps = "monitor,secure": sysdig-common-config, haproxy-ingress,
# metadata-service, metadata-enricher, promqlator.
# ---------------------------------------------------------------------------
NON_PGHA_CLUSTER = (
    # (APPLY) charts/haproxy-ingress/templates/ingressclass.yaml creates the
    #         cluster-scoped IngressClass `haproxy`, gated on
    #         global.deployment == "kubernetes" -> vanilla only.
    # (GRANT) the `ingress-controller` ClusterRole lists ingressclasses under
    #         both apiGroups, so get/list/watch are needed on both to create it.
    {("extensions", "ingressclasses", v) for v in ("get", "list", "watch")}
    | {("networking.k8s.io", "ingressclasses", v) for v in ("get", "list", "watch")}
    | {("networking.k8s.io", "ingressclasses", v) for v in ("create", "patch")}
    # (APPLY) sysdig-common-config/templates/namespace.yaml renders a Namespace
    #         gated only on `not sysdigCommonConfig.skipNamespace`, which
    #         defaults to false -> always rendered.
    # (GRANT) namespaces:get is also listed by the ingress-controller ClusterRole.
    | {("", "namespaces", v) for v in ("get", "create", "patch")}
    # (GRANT) nodes are read by the ingress-controller, mds-manager and
    #         metadata-enricher ClusterRoles.
    | {("", "nodes", v) for v in ("get", "list", "watch")}
    # (APPLY) the installer applies CRDs itself ahead of each chart
    #         (charts.go:432-445); metadata-service ships one on a default
    #         install (metadataService.operatorEnabled defaults to true).
    | {("apiextensions.k8s.io", "customresourcedefinitions", v)
       for v in ("get", "create", "patch")}
    # (APPLY) every chart listed above ships a ClusterRole + ClusterRoleBinding.
    | {("rbac.authorization.k8s.io", r, v)
       for r in ("clusterroles", "clusterrolebindings")
       for v in ("get", "create", "patch")}
)
NON_PGHA_NAMESPACED = (
    # (APPLY) Ingress objects, plus delete for the orphaned-ingress cleanup the
    #         installer runs before applying a chart (deploy.go:3144-3156).
    {("networking.k8s.io", "ingresses", v) for v in ("get", "create", "patch", "delete")}
    # (APPLY) haproxy-ingress and metadata-service both ship Role + RoleBinding.
    | {("rbac.authorization.k8s.io", r, v)
       for r in ("roles", "rolebindings")
       for v in ("get", "create", "patch")}
    # (APPLY) the common namespaced kinds every one of those charts emits.
    | {("", r, v)
       for r in ("serviceaccounts", "configmaps", "secrets", "services")
       for v in ("get", "create", "patch")}
    | {("apps", r, v) for r in ("deployments", "daemonsets") for v in ("get", "create", "patch")}
    | {("networking.k8s.io", "networkpolicies", v) for v in ("get", "create", "patch")}
)

# Rendered only under non-default configuration, so they are checked only with
# --strict to avoid reporting permissions as missing that an install may not
# need. storageclasses: sysdig-common-config/templates/storage-class.yaml needs
# skipStorageClass false AND a non-empty storageClassName AND a provisioner that
# is not hostPath/none. persistentvolumes: only when storageClassProvisioner is
# hostPath. priorityclasses: haproxy-ingress needs
# haproxyIngress.priorityClass.create, which defaults to false.
CONDITIONAL_CLUSTER = (
    {("storage.k8s.io", "storageclasses", v) for v in ("get", "create", "patch")}
    | {("", "persistentvolumes", v) for v in ("get", "create", "patch")}
    | {("scheduling.k8s.io", "priorityclasses", v) for v in ("get", "create", "patch")}
)

# Kubernetes kind -> (apiGroup, resource). Only kinds the postgres-ha chart emits.
KIND_TO_RESOURCE = {
    "ServiceAccount": ("", "serviceaccounts"),
    "Service": ("", "services"),
    "Secret": ("", "secrets"),
    "ConfigMap": ("", "configmaps"),
    "Role": ("rbac.authorization.k8s.io", "roles"),
    "RoleBinding": ("rbac.authorization.k8s.io", "rolebindings"),
    "ClusterRole": ("rbac.authorization.k8s.io", "clusterroles"),
    "ClusterRoleBinding": ("rbac.authorization.k8s.io", "clusterrolebindings"),
    "Deployment": ("apps", "deployments"),
    "StatefulSet": ("apps", "statefulsets"),
    "Job": ("batch", "jobs"),
    "CronJob": ("batch", "cronjobs"),
    "PodDisruptionBudget": ("policy", "poddisruptionbudgets"),
    "NetworkPolicy": ("networking.k8s.io", "networkpolicies"),
    "PrometheusRule": ("monitoring.coreos.com", "prometheusrules"),
    "Issuer": ("cert-manager.io", "issuers"),
    "Certificate": ("cert-manager.io", "certificates"),
    "CustomResourceDefinition": ("apiextensions.k8s.io", "customresourcedefinitions"),
    "OperatorConfiguration": ("acid.zalan.do", "operatorconfigurations"),
    "postgresql": ("acid.zalan.do", "postgresqls"),
}
CLUSTER_SCOPED_KINDS = {
    "ClusterRole", "ClusterRoleBinding", "CustomResourceDefinition",
    "Namespace", "StorageClass", "IngressClass", "PriorityClass",
    "PersistentVolume", "Node",
}


def load_all(text):
    return [d for d in yaml.safe_load_all(text) if d]


def rules_from(path, kinds):
    if not os.path.exists(path):
        return []
    out = []
    for doc in load_all(open(path).read()):
        if doc.get("kind") in kinds:
            out += doc.get("rules") or []
    return out


def covers(rules, group, resource, verb):
    """Mirror of k8s rbac.RuleAllows: does any rule permit (group, resource, verb)?"""
    for rule in rules:
        # A grant narrowed with resourceNames cannot satisfy a blanket requirement.
        if rule.get("resourceNames"):
            continue
        groups = rule.get("apiGroups") or [""]
        resources = rule.get("resources") or []
        verbs = rule.get("verbs") or []
        if (group in groups or "*" in groups) \
                and (resource in resources or "*" in resources) \
                and (verb in verbs or "*" in verbs):
            return True
    return False


def expand(rules):
    out = set()
    for rule in rules:
        for group in rule.get("apiGroups") or [""]:
            for resource in rule.get("resources") or []:
                for verb in rule.get("verbs") or []:
                    out.add((group, resource, verb))
    return out


def render_pgha_chart():
    with tempfile.NamedTemporaryFile("w", suffix=".yaml", delete=False) as fh:
        fh.write(PGHA_VALUES)
        values = fh.name
    try:
        proc = subprocess.run(
            ["helm", "template", "pgha", CHART, "-f", values, "--kube-version", "1.34.0"],
            capture_output=True, text=True,
        )
    finally:
        os.unlink(values)
    if proc.returncode != 0:
        sys.exit(f"helm template failed:\n{proc.stderr}")
    return load_all(proc.stdout)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("example",
                    help="directory name under examples/rbac (e.g. kubernetes-pgha), "
                         "or a path to any directory holding clusterrole.yaml/role.yaml")
    ap.add_argument("--no-pgha", action="store_true",
                    help="check only the non-Postgres-HA requirements")
    ap.add_argument("--strict", action="store_true",
                    help="also require the conditionally-rendered cluster-scoped objects "
                         "(storageclasses, persistentvolumes, priorityclasses)")
    args = ap.parse_args()

    example = args.example if os.path.isdir(args.example) else os.path.join(HERE, args.example)
    if not os.path.isdir(example):
        sys.exit(f"no such example: {args.example}")

    granted_cluster = rules_from(os.path.join(example, "clusterrole.yaml"), {"ClusterRole"})
    # A namespaced request is satisfied by either the Role or the ClusterRole.
    granted_ns = granted_cluster + rules_from(os.path.join(example, "role.yaml"), {"Role"})

    need_cluster = set(NON_PGHA_CLUSTER)
    need_ns = set(NON_PGHA_NAMESPACED)
    if args.strict:
        need_cluster |= CONDITIONAL_CLUSTER

    if not args.no_pgha:
        for doc in render_pgha_chart():
            kind = doc.get("kind")
            # ESCALATION: the installer must hold whatever this RBAC object grants.
            if kind == "ClusterRole":
                need_cluster |= expand(doc.get("rules") or [])
            elif kind == "Role":
                need_ns |= expand(doc.get("rules") or [])
            # APPLY: the installer must be able to apply the object itself.
            if kind in KIND_TO_RESOURCE:
                group, resource = KIND_TO_RESOURCE[kind]
                target = need_cluster if kind in CLUSTER_SCOPED_KINDS else need_ns
                target |= {(group, resource, v) for v in ("get", "create", "patch")}
            else:
                print(f"WARNING: kind {kind!r} is not mapped in KIND_TO_RESOURCE; not checked")

    missing = []
    for tup in sorted(need_cluster):
        if not covers(granted_cluster, *tup):
            missing.append(("cluster", *tup))
    for tup in sorted(need_ns):
        if not covers(granted_ns, *tup):
            missing.append(("namespaced", *tup))

    label = args.example
    label += " (no pgha)" if args.no_pgha else " (vanilla + Postgres HA)"
    if args.strict:
        label += " [strict]"
    if missing:
        print(f"FAIL {label}: {len(missing)} permission(s) missing")
        for scope, group, resource, verb in missing:
            print(f"  [{scope:10s}] {group or '(core)'}/{resource}: {verb}")
        return 1
    print(f"PASS {label}: none of the {len(need_cluster) + len(need_ns)} checked "
          f"permissions are missing")
    if not args.strict:
        print("     note: the non-Postgres requirements are a hand-maintained floor, not a "
              "complete\n           model of a default install - see the comment in this "
              "script. Re-run with\n           --strict to also require the conditionally-"
              "rendered cluster-scoped objects.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
