# OpenShift SCC Nonroot-v2 Migration Guide

This document describes the changes required to migrate an existing Sysdig onprem instance from the current SCC configuration (mixed `privileged`/`nonroot-v2`) to the new configuration where **all workloads use nonroot-v2 SCC**.

## Background

- A customer requested this feature, that all workloads should use `nonroot-v2`

- By adding a script to report on SCC usage, we were able to detect the mixed use of `privileged` and `nonroot-v2` in our current setup

- It was determined that we still have one case where we need to run Opensearch using `priviliged`, when the VMMAP Kernel parameter must be set via an `initContainer`

- The alternative is to set this at Kube node level, in that case we can run Opensearch without the `initContainer` using the `nonroot-v2` SCC

- When Opensearch needs the `initContainer` and the `priviliged` SCC, this **must** be set in the values:

```YAML
global:
  elasticsearch:
    serviceAccount: sysdig-elasticsearch
elasticsearch:
  setVmMaxMapCount: false
```

- A validation has been added to the `installer`; if the values configuration is not correct, it will block during generation:

```YAML
provided configuration is not valid for the below reasons
When deployment is openshift and elasticsearch.setVmMaxMapCount is true, global.elasticsearch.serviceAccount must be set to 'sysdig-elasticsearch', but found 'sysdig'
```

## Overview of Changes

### Current State (Before Migration)

ServiceAccounts are split between two SCCs:

**privileged SCC** (allows root user, privileged containers):

- `sysdig` (widely used)
- `sysdigcloud-cassandra`
- `sysdig-elasticsearch`
- `postgres-pod`
- `sysdig-meerkat-api`
- `sysdig-meerkat-collector`
- `sysdig-meerkat-aggregator`
- `sysdig-meerkat-datastream`

**nonroot-v2 SCC** (non-root users with seccomp):

- `node-labels-to-files`
- `elasticsearch-pre-job`
- `elasticsearch-post-job`
- `ingress-controller`
- `sysdigcloud-postgres-operator`
- `metadata-service`
- `redis`
- `redis-upgrade-sa`
- `sysdigcloud-promqlator`
- `nats`
- `sysdig-certificate-exporter`
- `sysdig-scanrequestor`
- `neo4j`
- `sysdigcloud-metadata-enricher`

### Target State (After Migration)

**nonroot-v2 SCC** (ALL workloads):

- All ServiceAccounts from the current nonroot-v2 list
- **PLUS** all ServiceAccounts from the current privileged list:
  - `sysdig`
  - `sysdigcloud-cassandra`
  - `postgres-pod`
  - `sysdig-meerkat-api`
  - `sysdig-meerkat-collector`
  - `sysdig-meerkat-aggregator`
  - `sysdig-meerkat-datastream`

### **ELASTICSEARCH VMMAP: PLEASE READ, VERY IMPORTANT**

- To run Opensearch using `nonroot-v2` we need to disable the `elasticsearch-init-vmmaxmapcount` `initContainer`, because this can only run with `privileged` SCC
- When this `initContainer` is disabled, if the worker where Opensearch is executed does not have the required `vm.max_map_count=262144`, then Opensearch **will not start**
- The customer must make sure that the Kubernetes workers have the above setup **before** Opensearch is started

## Migration Steps for Existing Installations

## WARNING

- **this procedure will cause downtime**

- the extent of the downtime and any dataloss has not been quantified.

### Prerequisites

- OpenShift cluster version 4.11 or higher (provides nonroot-v2 SCC)
- Cluster admin access to manage SCC bindings
- Access to OpenShift nodes for kernel parameter verification
- Sysdig installer version from branch `OP-122-openshift-scc-goldman`

### Step 1: Verify OpenShift Version

```bash
oc version
# Ensure Server Version is OpenShift 4.11+ (Kubernetes 1.24+)
```

The nonroot-v2 SCC is only available in OpenShift 4.11 and later.

### Step 2: Backup Current SCC Configuration

Before making changes, document the current SCC bindings:

```bash
cd scripts/openshift-scc-analyzer

# Generate a backup report of current SCC assignments
python main.py --namespace sysdigcloud \
  --output-format csv \
  --output-file scc-before-migration.csv

python main.py --namespace sysdigcloud \
  --output-format json \
  --output-file scc-before-migration.json
```

Save these files for rollback reference.

### Step 3: Verify Node-Level Kernel Configuration

Since the Elasticsearch initContainer (which sets `vm.max_map_count`) requires privileged access and won't work with nonroot-v2, the nodes must have this configured at the OS level.

**Check all nodes:**

```bash
# List all nodes
oc get nodes

# For each node, verify vm.max_map_count
oc debug node/<node-name>
chroot /host sysctl vm.max_map_count

# Expected output: vm.max_map_count = 262144 (or higher)
```

**If vm.max_map_count is too low (typically 65530):**

Work with your cluster administrators to apply the following MachineConfig:

```yaml
apiVersion: machineconfiguration.openshift.io/v1
kind: MachineConfig
metadata:
  labels:
    machineconfiguration.openshift.io/role: worker
  name: 99-worker-sysctl-elasticsearch
spec:
  config:
    ignition:
      version: 3.2.0
    storage:
      files:
      - contents:
          source: data:text/plain;charset=utf-8;base64,dm0ubWF4X21hcF9jb3VudD0yNjIxNDQK
        mode: 0644
        overwrite: true
        path: /etc/sysctl.d/99-elasticsearch.conf
```

Note: The base64 content decodes to `vm.max_map_count=262144`

After applying MachineConfig, nodes will reboot and apply the setting.

### Step 4: Update Elasticsearch Configuration in `values.yaml`

Since the VMMAP initContainer cannot run with `nonroot-v2` SCC, disable it in your values:

```yaml
elasticsearch:
  setVmMaxMapCount: false
```

This prevents the privileged initContainer from being created in the Elasticsearch StatefulSet.

### Step 4a: Execute the installer generate

- Execute `installer generate`

### Step 4b: Apply the manifests for the ES Statefulsets (master and worker)

- Is this going to work?

### Step 5: Update SCC Bindings

Remove privileged SCC from ServiceAccounts that are moving to nonroot-v2:

```bash
NAMESPACE="sysdigcloud"  # Adjust if needed

# ServiceAccounts moving from privileged to nonroot-v2
SERVICE_ACCOUNTS=(
  "sysdig"
  "sysdigcloud-cassandra"
  "postgres-pod"
  "sysdig-meerkat-api"
  "sysdig-meerkat-collector"
  "sysdig-meerkat-aggregator"
  "sysdig-meerkat-datastream"
)

# Remove privileged SCC
for sa in "${SERVICE_ACCOUNTS[@]}"; do
  echo "Removing privileged SCC from ${sa}..."
  oc adm policy remove-scc-from-user privileged -n ${NAMESPACE} -z ${sa}
done

# Add nonroot-v2 SCC
for sa in "${SERVICE_ACCOUNTS[@]}"; do
  echo "Adding nonroot-v2 SCC to ${sa}..."
  oc adm policy add-scc-to-user nonroot-v2 -n ${NAMESPACE} -z ${sa}
done

echo "SCC bindings updated successfully!"
```

### Step 6: Verify SCC Bindings

Check that the new bindings are in place:

- use the analyzer tool:

```bash
cd scripts/openshift-scc-analyzer
python main.py --namespace sysdigcloud --output-format table
```

Expected output should show all ServiceAccounts with `nonroot-v2`.

### Step 7: Rolling Restart of Workloads

Restart workloads so they pick up the new SCC assignments:

```bash
NAMESPACE="sysdigcloud"

echo "Restarting Deployments..."
oc rollout restart deployment -n ${NAMESPACE} -l app=sysdigcloud

echo "Restarting StatefulSets..."
# This will restart: 
# statefulset.apps/nats restarted
# statefulset.apps/sysdigcloud-cassandra restarted
# statefulset.apps/sysdigcloud-elasticsearch restarted
# statefulset.apps/sysdigcloud-netsec-ingest restarted
# statefulset.apps/sysdigcloud-postgresql12 restarted
oc rollout restart statefulset -n ${NAMESPACE} -l app=sysdigcloud
oc rollout restart statefulset -n ${NAMESPACE} -l role=zookeeper
oc rollout restart statefulset -n ${NAMESPACE} sysdigcloud-cassandra
oc rollout restart statefulset -n ${NAMESPACE} sysdigcloud-postgres-0
oc rollout restart statefulset -n ${NAMESPACE} redistls-node
oc rollout restart statefulset -n ${NAMESPACE} -l app=neo4j-cluster
# must delete the 3 pods one by one
#oc rollout restart statefulset -n ${NAMESPACE} sysdigcloud-elasticsearch
for i in 2 1 0; do
  echo "Restarting sysdigcloud-elasticsearch-$i"
  oc -n ${NAMESPACE} delete pod sysdigcloud-elasticsearch-$i
  sleep 45
done

echo "Restart initiated. Monitor pod status:"
echo "  oc get pods -n ${NAMESPACE} -w"
```

### Step 8: Monitor Pod Startup

Watch for pods to restart and check for any SCC-related errors:

```bash
# Watch pod status
oc get pods -n sysdigcloud -w

# In another terminal, watch for SCC violations
# Check for `events` mentioning "unable to validate against any security context constraint"
oc get events -n sysdigcloud -w | grep -i "scc\|security"
```


### Step 9: Verify Post-Migration State

Generate a post-migration report:

```bash
cd scripts/openshift-scc-analyzer

python main.py --namespace sysdigcloud \
  --output-format csv \
  --output-file scc-after-migration.csv

python main.py --namespace sysdigcloud \
  --output-format table \
  --compare-expected
```

Compare with the pre-migration report to verify changes.

### Step 10: Functional Testing

Perform basic functional tests to ensure services are operating correctly:

```bash
# Check all pods are running
oc get pods -n sysdigcloud | grep -v "Running\|Completed"

# Check critical services
oc exec -n sysdigcloud deployment/sysdigcloud-api -- curl -I http://localhost:8080/api/config

# Check Elasticsearch cluster health
oc exec -n sysdigcloud sysdigcloud-elasticsearch-0 -c elasticsearch -- \
  sh -c 'curl -s -k -u ${ELASTICSEARCH_ADMINUSER}:${ELASTICSEARCH_ADMIN_PASSWORD} https://$(hostname):9200/_cluster/health'| jq '.'

# Check Cassandra cluster status
for i in 2 1 0; do
  echo "Checking sysdigcloud-cassandra-$i"
  oc exec -n sysdigcloud sysdigcloud-cassandra-$i -c cassandra -- nodetool status
done
```

### Reverting these changes

- TBD

### Examples of reports

- Before the migration:

```bash
OSC 7.5.0


======================================================================================================================================================
OpenShift SCC Analysis Report (Workload View)
======================================================================================================================================================

+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Type        | Workload                                    | Namespace   | ServiceAccount                | Binding                         | Binding Type   | SCC        |   Priority | Notes      |
+=============+=============================================+=============+===============================+=================================+================+============+============+============+
| Deployment  | sysdig-alert-manager                        | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdig-alert-notifier                       | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdig-azure-metrics-converter              | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdig-certificate-exporter                 | sysdigcloud | sysdig-certificate-exporter   | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdig-meerkat-aggregator                   | sysdigcloud | sysdig-meerkat-aggregator     | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdig-meerkat-aggregator-worker            | sysdigcloud | sysdig-meerkat-aggregator     | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdig-meerkat-api                          | sysdigcloud | sysdig-meerkat-api            | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdig-meerkat-collector-0                  | sysdigcloud | sysdig-meerkat-collector      | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdig-meerkat-collector-1                  | sysdigcloud | sysdig-meerkat-collector      | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdig-plotter                              | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-activity-audit-api              | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-analytics-api                   | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-analytics-gatherer              | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-api                             | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-api-docs                        | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-beacon-prom-remote-write        | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-cloudsec-api                    | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-cloudsec-worker                 | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-collector                       | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-compliance-api                  | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-compliance-worker               | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-docs                            | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-events-activity-audit-gatherer  | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-events-api                      | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-events-dispatcher               | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-events-forwarder                | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-events-forwarder-api            | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-events-gatherer                 | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-events-ingestion                | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-falco-validator                 | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-fingerprints-files              | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-fingerprints-files-api          | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-helm-renderer                   | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-metadata-enricher               | sysdigcloud | sysdigcloud-metadata-enricher | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-metadata-service-0              | sysdigcloud | metadata-service              | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-metadata-service-1              | sysdigcloud | metadata-service              | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-metadata-service-collector      | sysdigcloud | metadata-service              | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-metadata-service-operator       | sysdigcloud | metadata-service              | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-netsec-api                      | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-onboarding-api                  | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-platform-service-api            | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-policies-api                    | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-policies-worker                 | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-process-tree-api                | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-process-tree-gatherer           | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-promchap                        | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-promqlator                      | sysdigcloud | sysdigcloud-promqlator        | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-rapid-response-connector        | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-response-actions-controller     | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-acvalidationengine   | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-agents-conf          | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-collector            | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-credentialstore      | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-imagesbomextractor   | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-notifier             | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-pkgmeta-api          | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-policies-api         | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-registry-scanner-api | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-reporting-api        | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-reporting-generator  | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-reporting-scheduler  | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-reporting-worker     | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-riskmanager-api      | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-runtimeview          | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-sbom-api             | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-scanengine-worker    | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-scanrequestor        | sysdigcloud | sysdig-scanrequestor          | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-scanresults-api      | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-scanningv2-vulns-api            | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-ticketing-api                   | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-vm-metadata-enricher            | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | sysdigcloud-worker                          | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | ui-admin                                    | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | ui-inspect                                  | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | ui-monitor                                  | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| Deployment  | ui-secure                                   | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| StatefulSet | cp-kafka                                    | sysdigcloud | node-labels-to-files          | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| StatefulSet | nats                                        | sysdigcloud | nats                          | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| StatefulSet | redistls-node                               | sysdigcloud | redis                         | system:openshift:scc:nonroot-v2 | RoleBinding    | nonroot-v2 |          5 |            |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| StatefulSet | sysdigcloud-cassandra                       | sysdigcloud | sysdigcloud-cassandra         | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| StatefulSet | sysdigcloud-elasticsearch                   | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| StatefulSet | sysdigcloud-netsec-ingest                   | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| StatefulSet | sysdigcloud-postgresql12                    | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+
| StatefulSet | zookeeper                                   | sysdigcloud | sysdig                        | system:openshift:scc:privileged | RoleBinding    | privileged |          0 | PRIVILEGED |
+-------------+---------------------------------------------+-------------+-------------------------------+---------------------------------+----------------+------------+------------+------------+


--------------------------------------------------------------------------------
SUMMARY
--------------------------------------------------------------------------------
Total ServiceAccounts analyzed: 13
Total SCC bindings found: 84
Unique SCCs in use: 2
  SCCs: nonroot-v2, privileged
ServiceAccounts without SCC bindings: 0
ServiceAccounts with multiple SCCs: 0
--------------------------------------------------------------------------------
```

- After the migration:

```bash

======================================================================================================================================================
OpenShift SCC Analysis Report (Workload View)
======================================================================================================================================================

+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Type        | Workload                                    | ServiceAccount                | Binding                         | SCC        |   Priority | Notes   |
+=============+=============================================+===============================+=================================+============+============+=========+
| Deployment  | secure-graph-gatherer                       | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | secure-graph-ingestion                      | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | secure-graph-query                          | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | secure-iac-agenthandler-deployment          | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | secure-iac-clusteranalysis-deployment       | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | secure-iac-compliance-deployment            | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | secure-iac-inventory-deployment             | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | secure-iac-policy-deployment                | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | secure-iac-scheduler-deployment             | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | secure-iac-workload-deployment              | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | secure-query-storage-api                    | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdig-alert-manager                        | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdig-alert-notifier                       | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdig-azure-metrics-converter              | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdig-certificate-exporter                 | sysdig-certificate-exporter   | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdig-meerkat-aggregator                   | sysdig-meerkat-aggregator     | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdig-meerkat-aggregator-worker            | sysdig-meerkat-aggregator     | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdig-meerkat-api                          | sysdig-meerkat-api            | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdig-meerkat-collector-0                  | sysdig-meerkat-collector      | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdig-meerkat-collector-1                  | sysdig-meerkat-collector      | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdig-plotter                              | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-activity-audit-api              | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-analytics-api                   | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-analytics-gatherer              | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-api                             | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-api-docs                        | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-beacon-prom-remote-write        | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-cloudsec-api                    | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-cloudsec-worker                 | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-collector                       | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-compliance-api                  | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-compliance-worker               | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-docs                            | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-events-activity-audit-gatherer  | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-events-api                      | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-events-dispatcher               | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-events-forwarder                | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-events-forwarder-api            | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-events-gatherer                 | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-events-ingestion                | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-falco-validator                 | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-fingerprints-files              | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-fingerprints-files-api          | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-helm-renderer                   | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-metadata-enricher               | sysdigcloud-metadata-enricher | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-metadata-service-0              | metadata-service              | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-metadata-service-collector      | metadata-service              | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-metadata-service-operator       | metadata-service              | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-netsec-api                      | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-onboarding-api                  | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-platform-service-api            | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-policies-api                    | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-policies-worker                 | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-process-tree-api                | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-process-tree-gatherer           | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-promchap                        | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-promqlator                      | sysdigcloud-promqlator        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-rapid-response-connector        | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-response-actions-controller     | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-acvalidationengine   | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-agents-conf          | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-collector            | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-credentialstore      | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-imagesbomextractor   | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-notifier             | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-pkgmeta-api          | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-policies-api         | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-registry-scanner-api | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-reporting-api        | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-reporting-generator  | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-reporting-scheduler  | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-reporting-worker     | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-riskmanager-api      | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-runtimeview          | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-sbom-api             | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-scanengine-worker    | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-scanrequestor        | sysdig-scanrequestor          | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-scanresults-api      | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-scanningv2-vulns-api            | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-ticketing-api                   | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-vm-metadata-enricher            | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysdigcloud-worker                          | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | sysql-api                                   | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | ui-admin                                    | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | ui-inspect                                  | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | ui-monitor                                  | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| Deployment  | ui-secure                                   | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| StatefulSet | cp-kafka                                    | node-labels-to-files          | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| StatefulSet | nats                                        | nats                          | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| StatefulSet | neo4j                                       | neo4j                         | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| StatefulSet | redistls-node                               | redis                         | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| StatefulSet | sysdigcloud-cassandra                       | sysdigcloud-cassandra         | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| StatefulSet | sysdigcloud-elasticsearch                   | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| StatefulSet | sysdigcloud-netsec-ingest                   | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| StatefulSet | sysdigcloud-postgresql12                    | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+
| StatefulSet | zookeeper                                   | sysdig                        | system:openshift:scc:nonroot-v2 | nonroot-v2 |          5 |         |
+-------------+---------------------------------------------+-------------------------------+---------------------------------+------------+------------+---------+


--------------------------------------------------------------------------------
SUMMARY
--------------------------------------------------------------------------------
Total ServiceAccounts analyzed: 14
Total SCC bindings found: 96
Unique SCCs in use: 1
  SCCs: nonroot-v2
ServiceAccounts without SCC bindings: 0
ServiceAccounts with multiple SCCs: 0
--------------------------------------------------------------------------------
```