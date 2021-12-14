# Upgrade

## Overview

From version 3.5.0, both installing and upgrading with the installer has been simplified. Upgrade differs from Install in that you run an installer diff to discover the differences between the old and new versions and then installer deploy for the new version.

Some guidance from Sysdig Support may be warranted in highly customized installations. 

Refer to the appropriate workflow, depending on your environment:

  - [Quickstart Install](README.md#quickstart-install)
  - [Airgapped Installation Options](README.md#airgapped-installation-options)

## Upgrade Notes

### Kubernetes 1.22 not yet supported

Version 5.0.3 does is not yet supported on Kubernetes 1.22 due to breaking changes to the Ingress Controller. We expect to add support for 1.22 in the near future.

### OpenShift `HostAlreadyClaimed` Error in Routes when Prometheus ingestion is enabled (workaround provided)

If Prometheus metric ingestion is enabled (`sysdig.beacon.platformMetricsEnabled` is `true`), an overlay is required to avoid an error in Routes which will prevent the `Collector` Route to be active and able to receive data from the agents.

This is what the error would look like:

```
oc get route
NAME                                                 HOST/PORT                                                       PATH                                             SERVICES                                             PORT    TERMINATION   WILDCARD
[omitted lines]
sysdigcloud-collector                                HostAlreadyClaimed
[omitted lines]
```

Use [this](examples/openshift-routes-overlay/overlays/patch.yaml) overlay to avoid the error `HostAlreadyClaimed`

The `domain_name` must be different from the name used for the Collectors endpoint and it must be used for Prometheus metrics ingestion.

### Cassandra 3 is now the default for fresh installs

Fresh installs by default will use Cassandra version 3.x.

### Known limitations for OpenShift 3.11 and Kubernetes < 1.16

PostgreSQL HA is not supported on OpenShift 3.11 and on clusters running Kubernetes < 1.16

### MySql removal (breaking change)

Any MySql related entry in the `values.yaml` must be removed or it will cause the installer to fail.

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

## Release Notes

- See [Release Notes](release_notes.md) for upgrade matrix, supported platforms & link to full feature notes
