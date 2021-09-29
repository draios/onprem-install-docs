# Upgrade

## Overview

From version 3.5.0, both installing and upgrading with the installer has been simplified. Upgrade differs from Install in that you run an installer diff to discover the differences between the old and new versions and then installer deploy for the new version.

Some guidance from Sysdig Support may be warranted in highly customized installations. 

Refer to the appropriate workflow, depending on your environment:

  - [Quickstart Install](README.md#quickstart-install)
  - [Airgapped Installation Options](README.md#airgapped-installation-options)

## Upgrade Notes

### Preflight checks

#### Elastic Search

Please verify the Elastic Search health before proceeding with upgrades.

The cluster being Green indicates that the cluster is healthy. If the cluster is yellow please check the unassigned shards and increase heap & requests/limits to help the cluster to Green state before upgrade.

```bash
curl -s --cacert /usr/share/elasticsearch/config/root-ca.pem         https://readonly:${ELASTICSEARCH_READONLY_PASSWORD}@$(hostname):9200/_cat/health?v
epoch      timestamp cluster     status node.total node.data shards pri relo init unassign pending_tasks max_task_wait_time active_shards_percent
1616713959 23:12:39  sysdigcloud green           3         3     11   4    0    0        0             0                  -                100.0%
```

#### Cassandra

Verifying cassandra health before upgrades. Nodetool status with nodes in `UN` is the desired state.

```bash
nodetool status
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address     Load       Tokens  Owns (effective)  Host ID                               Rack
UN  100.96.1.2  1.1 MB     256     100.0%            4fdfcb3c-b57a-421b-b615-61179136842d  rack1
UN  100.96.5.2  364.59 KB  256     100.0%            83579e1a-31b7-402e-9349-d936b545a15b  rack1
UN  100.96.8.2  307.72 KB  256     100.0%            f5766eec-e013-4ddd-9a01-149f5bd9975a  rack1
```


### Cassandra TLS Transition

With 4.x cassandra is run with `secure: true` and `ssl: true` by default.

The below config needs to be added to values.yaml. The clusters running secure and ssl should not have any impact. The others will be transitioned to secure and ssl.

```yaml
sysdig:
  cassandra:
    secure: true
    ssl: true
```

### MySQL to PostgreSQL migration

For consolidation and to meet higher performance requirements, upgrading to v4.0.4 from v3.x.x involves migrating MySQL to the PostgreSQL database. The migration process is seamless and no user intervention is expected. For migration instructions and troubleshooting tips, see [Migrating MySQL to PostgreSQL Database](./migration.md).

Please note that Installer will always generate the manifests for `mysql-to-postgresql-migration` and `mysql-latest-migrations` jobs: even if so, the migration will not run again if it has successfully completed once.

### Elasticsearch 6.8.6 upgrade

With Sysdig 3.6.0 install, Elasticsearch runs with `privileged: false` by default. In most cases this should work automatically.

There are some cases where Elasticsearch will fail with an error like below:

```bash
kubectl -n sysdig logs -f sysdigcloud-elasticsearch-0
...
+ grep cap_sys_admin
++ sysctl -nb vm.max_map_count
+ max_map_count=65530
+ [[ 65530 -ne 262144 ]]
+ echo 'sysctl vm.max_map_count is not set to the correct value, and I do not have the privileges to set it!'
+ exit 1
sysctl vm.max_map_count is not set to the correct value, and I do not have the privileges to set it!
```

There are 2 ways to fix this issue:

1. run systemctl command on hosts that run Elasticsearch,

    ```bash
    VM_MAX_MAP_COUNT=${VM_MAX_MAP_COUNT:-262144}; sysctl -w vm.max_map_count=${VM_MAX_MAP_COUNT}
    ```

2. An initContainer which runs as `privileged: true` and `root` and set vm.max_map_count [example overlay](examples/elasticsearch-init-vmmaxmapcount)

### Cassandra container now runs as non `root` and uses a new ServiceAccount `sysdig-cassandra`

- Cassandra will now run using a non-root, non privileged user within its container
- The only exception is the `initContainer` required when using `hostPath` storage: it still requires to run as `root` to be able to `chown` the mount point used by Cassandra
- The `ServiceAccount` changes to `sysdig-cassandra` from `sysdig-with-root`. 
- **PLEASE NOTE:** if the previous ServiceAccount was used in onPrem installs with local resources (such as PSPs for example), please make sure that these are updated using the new ServiceAccount.
- **PLEASE NOTE:** the ServiceAccount `sysdig-cassandra` is used to let Cassandra use the `nodes-labels-to-files` utility when the snitch is `customGossipingPropertyFileSnitch`.

## Release Notes

- See [Release Notes](release_notes.md) for upgrade matrix, supported platforms & link to full feature notes
