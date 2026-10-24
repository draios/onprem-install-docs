# RBAC for Installer

- RBAC resources required to run the `installer`

- each directory contains YAMLs for a specific case:

## Which one do I use?

| Platform | Postgres | Use |
|---|---|---|
| vanilla Kubernetes (`global.deployment: kubernetes`) | single instance, or external | [fullaccess](fullaccess) |
| vanilla Kubernetes | **HA** (`global.postgresql.ha.enabled: true`) | [kubernetes-pgha](kubernetes-pgha) |
| OpenShift | single instance, or external | [openshift](openshift) |
| OpenShift | **HA** | [openshift-pgha](openshift-pgha) |
| OpenShift, operator + CRDs pre-installed, agent deployed externally | HA, `checkCRD: false` | [openshift-nopgha-noagent](openshift-nopgha-noagent) |
| any | any | [readonly](readonly) — `generate` / `secure-diff` only |

Two rules of thumb when reading or extending these files:

- **Cluster-scoped resources cannot be granted by a `Role`.** `namespaces`,
  `nodes`, `persistentvolumes`, `storageclasses`, `ingressclasses`,
  `priorityclasses` and `customresourcedefinitions` must appear in
  `clusterrole.yaml`. A `Role` that lists them silently grants nothing.
- **RBAC privilege-escalation prevention applies.** A ServiceAccount that creates
  a `Role` or `ClusterRole` must already hold every permission listed inside it.
  The installer creates RBAC for the ingress controller, metadata-service,
  metadata-enricher and (in HA) the Zalando Postgres operator, so the installer's
  own rules have to be a superset of theirs. This is why some rules look
  redundant — they are there to satisfy the escalation check, not because the
  installer uses them directly.

## The cases

[readonly](readonly)
- readonly access to the namespace and minimal resources necessary for the installer to 
  `generate` and `secure-diff` the existing install (or for a new install)

[fullaccess](fullaccess)
- allows the execution of `installer` as-is, including rights for `StorageClass` and `IngressController`
- vanilla Kubernetes with a single-instance or external Postgres. If Postgres is
  deployed in HA, use [kubernetes-pgha](kubernetes-pgha) instead.
- `role.yaml` used to be written as `apiGroups: ['*']` and carried entries that
  granted nothing (`podsecuritypolicies`, removed in Kubernetes 1.25;
  `podpreset`, removed in 1.20; `pod/delete` and `pod/status` misspellings; and
  cluster-scoped `namespaces`/`storageclasses`, which a `Role` cannot grant). It
  now lists explicit apiGroups so it can be handed to a customer security review
  as-is. See the file header for the full list of what was dropped and why.

[kubernetes-pgha](kubernetes-pgha)
- same case as `fullaccess` but with Postgres in HA, so the installer SA also
  needs to apply the three `acid.zalan.do` CRDs, create the `postgresql` and
  `OperatorConfiguration` CRs, and create the RBAC used by the Zalando operator
  and by the Patroni pods.
- note this is **not** `openshift-pgha` minus the SCC bindings. That example is
  still missing `ingressclasses` (a vanilla-only object, so OpenShift never
  needed it) and `coordination.k8s.io/leases`, and it predates the move of the
  operator's RBAC from a cluster-wide `ClusterRole` to a namespaced `Role`, so it
  grants a large set of cluster-wide permissions the operator no longer uses.
- written with explicit `apiGroups` rather than `apiGroups: ['*']`, so it can be
  handed to a customer security review as-is.

[openshift](openshift)
- same base of `fullaccess` with some ocp specific bindings: the scc ones that give the installer the power of running `oc adm policy add-scc-to-user <scc> <installer-sa>`. Please be aware that this example will not work with openshift 3.11, in that case you need to create the scc roles first (with `use` as verb)

[openshift-pgha](openshift-pgha)
- same of `openshift` but the installer sa has more grants since it need to create a clusterroles for the zalando postgres operator service account.

[openshift-nopgha-noagent](openshift-nopgha-noagent)
- openshift case where we don't need rbac to deploy the agent since is done externally to the installer and we already have a zalando postgres operator installed so we just need to use it.

## Keeping these files correct

These examples are hand-maintained and drifted from what the charts actually
render (`extensions/v1beta1` ingresses, missing `ingressclasses`, missing
`customresourcedefinitions`). [verify.py](verify.py) checks an example against the
rendered charts for both of the rules of thumb above:

```console
$ ./verify.py kubernetes-pgha        # vanilla Kubernetes + Postgres HA
$ ./verify.py fullaccess --no-pgha   # vanilla Kubernetes, no Postgres HA
```

It exits non-zero and prints the missing `(scope, apiGroup, resource, verb)`
tuples. It needs `helm` on `PATH` and `PyYAML`; it renders the chart locally and
does not talk to a cluster.

The Postgres HA requirements are derived by rendering the chart. The
non-Postgres ones are a hand-maintained floor rather than a complete model of a
default install, so a pass means "none of the known-required permissions are
missing", not "this example is sufficient" — extend the set in the script when
you find something else the installer needs.

`--strict` additionally requires the cluster-scoped objects that only render
under non-default configuration. These are **not** granted by the examples by
default, so uncomment them if they apply to you:

| Grant | Needed when |
|---|---|
| `persistentvolumes` create/update/patch | `global.storageClassProvisioner: hostPath`, which makes sysdig-common-config render a PersistentVolume |
| `scheduling.k8s.io/priorityclasses` | `haproxyIngress.priorityClass.create: true` (defaults to false) |

## Instructions

- for each usecase we provide YAMLs to create the necessary RBAC resources

- this example assumes that Sysdig will be installed in the `sysdigcloud` namespace

- apply these YAMLs to your cluster from an `admin` level account

- create a `kubeconfig` for the ServiceAccount installer

- use the `kubeconfig` to execute the installer

- protip: if you have the openshift binary installed you can just use `oc serviceaccounts create-kubeconfig installer` and this will create the serviceaccount kubeconfig for you
