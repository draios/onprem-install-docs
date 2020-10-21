# Datastores as Kubernetes pod

Sysdig Cloud datastores can be deployed as Kubernetes pods. Each pod can be configured to use a
local volume (emptyDir) that is only persisted for the lifetime of the pod, or a persistent volume.

## Persistent Storage

All statefulset yamls need a proper storage class name pasted in the file.
Replace `<INSERT_YOUR_STORAGE_CLASS_NAME>` with your storage class name.

## Pod Affinity

Kubernetes has a way of setting affinity called podAffinity. These are fields in under Pod metadata and
take automatic or user-defined metadata to dictate where to schedule pods.
Some benefits of affinity or anti-affinity are:

* Schedule a pod based on which other pods are or are not running on a node
* Request without requiring that a pod be run on a node
* Specify a set of allowable values instead of a single value requirement

To enable pod anti-affinity, uncomment the given section in the applicable yaml files.

## MySQL Deployment or StatefulSet

### Deployment (without HA)

To create a MySQL deployment, the provided manifest under
`manifests/mysql/mysql-deployment.yaml` can be used. By default, it will
use a local non-persistent volume (emptyDir), but the manifest contains
commented snippets that can be uncommented when using persistent volumes
such as AWS EBS or GCE Disks (just replace the volume id from the cloud
provider in the snippet):

```bash
kubectl -n sysdigcloud create -f manifests/mysql/mysql-deployment.yaml
```

If testing at high scale, note the increased `max_connections` setting in
`manifests/mysql.yaml`.

This solution creates a single replica instance of MySQL. The
implementation is very robust and based on a stable MySQL release
(5.6), but it doesn't have HA capabilities, meaning that if the instance
running MySQL fails, the application will face downtime until Kubernetes
reschedules the pod on another healthy node and re-attaches to it the
persistent storage. This downtime can typically last from a few seconds to
a few minutes. If more HA is needed, a solution based on StatefulSets can
be used.

### StatefulSet (with HA, advanced)

This solution is based on StatefulSets and a more recent version of MySQL
(8.0.11) with significant capabilities in terms of HA.

Please Note that the volume claim template for the mysql cluster storage has been factored to account for 1.5GB per
day of binlog, 30days * 1.5g + 15g = 60GB

It can be deployed with:

```bash
kubectl -n sysdigcloud create -f manifests/mysql/mysql-cluster-statefulset.yaml
kubectl -n sysdigcloud create -f manifests/mysql/mysql-router-statefulset.yaml
```

This creates a MySQL InnoDB Cluster of 3 members in single-primary mode,
with automatic fail-over and replication. In this solution, users can incur
in a loss of one MySQL instance at a time without causing any significant
downtime, as the fail-over towards a healthy instance should be instantaneous.
Once the failed instance recovers, it will automatically join as secondary
replica to the existing cluster.

In front of the cluster, a stateless deployment of 3 instances of MySQL
Router is instantiated, so that clients can always be correctly routed
towards the current MySQL master.

Each MySQL instance is deployed with a sidecar agent that should take care
of the basic cluster membership administrative operations. Unless major
outages or particularly bad failures happen, it shouldn't be necessary for
the user to issue any manual intervention. However, with MySQL not being a
distributed system by nature, some circumstances can cause the cluster to
misbehave, and manual intervention might be needed. For example, to check
the status of the cluster, one can directly connect to the MySQL instances
and use MySQL Shell:

```bash
$ kubectl exec -it -n sysdigcloud sysdigcloud-mysql-cluster-0 -- mysqlsh --uri root:password@sysdigcloud-mysql-cluster-0:3306 -i -e "dba.getCluster().status()"
Creating a session to 'root@sysdigcloud-mysql-cluster-0:3306'
Fetching schema names for autocompletion... Press ^C to stop.
Your MySQL connection id is 630
Server version: 8.0.11 MySQL Community Server - GPL
No default schema selected; type \use <schema> to set one.
{
    "clusterName": "Cluster",
    "defaultReplicaSet": {
        "name": "default",
        "primary": "sysdigcloud-mysql-cluster-0.sysdigcloud-mysql-cluster:3306",
        "ssl": "REQUIRED",
        "status": "OK",
        "statusText": "Cluster is ONLINE and can tolerate up to ONE failure.",
        "topology": {
            "sysdigcloud-mysql-cluster-0.sysdigcloud-mysql-cluster:3306": {
                "address": "sysdigcloud-mysql-cluster-0.sysdigcloud-mysql-cluster:3306",
                "mode": "R/W",
                "readReplicas": {},
                "role": "HA",
                "status": "ONLINE"
            },
            "sysdigcloud-mysql-cluster-1.sysdigcloud-mysql-cluster:3306": {
                "address": "sysdigcloud-mysql-cluster-1.sysdigcloud-mysql-cluster:3306",
                "mode": "R/O",
                "readReplicas": {},
                "role": "HA",
                "status": "ONLINE"
            },
            "sysdigcloud-mysql-cluster-2.sysdigcloud-mysql-cluster:3306": {
                "address": "sysdigcloud-mysql-cluster-2.sysdigcloud-mysql-cluster:3306",
                "mode": "R/O",
                "readReplicas": {},
                "role": "HA",
                "status": "ONLINE"
            }
        }
    },
    "groupInformationSourceMember": "mysql://root@sysdigcloud-mysql-cluster-0:3306"
}
```

Other useful information can usually be gathered by viewing at the
mysql-agent log:

```bash
$ kubectl logs -f sysdigcloud-mysql-cluster-0 mysql-agent -n sysdigcloud
I0622 00:13:10.170775       1 cluster_manager.go:206] MySQL instance is online
I0622 00:13:25.307142       1 cluster_manager.go:206] MySQL instance is online
I0622 00:13:40.438603       1 cluster_manager.go:206] MySQL instance is online
I0622 00:13:55.574488       1 cluster_manager.go:206] MySQL instance is online
...
```

Also the mysqld logs can be inspected:

```bash
$ kubectl logs -f sysdigcloud-mysql-cluster-0 mysql -n sysdigcloud
2018-06-22T21:11:03.398851Z 2 [Note] [MY-011670] [Repl] Plugin group_replication reported: 'Group Replication applier module successfully initialized!'
2018-06-22T21:11:03.422512Z 0 [Note] [MY-011735] [Repl] Plugin group_replication reported: '[GCS] XCom initialized and ready to accept incoming connections on port 33061'
2018-06-22T21:11:06.580221Z 0 [ERROR] [MY-011735] [Repl] Plugin group_replication reported: '[GCS] Error on opening a connection to mysql1:33061 on local port: 33061.'
2018-06-22T21:11:09.651869Z 0 [ERROR] [MY-011735] [Repl] Plugin group_replication reported: '[GCS] Error on opening a connection to mysql2:33061 on local port: 33061.'
2018-06-22T21:11:12.725023Z 0 [ERROR] [MY-011735] [Repl] Plugin group_replication reported: '[GCS] Error on opening a connection to mysql1:33061 on local port: 33061.'
2018-06-22T21:11:15.796127Z 0 [ERROR] [MY-011735] [Repl] Plugin group_replication reported: '[GCS] Error on opening a connection to mysql2:33061 on local port: 33061.'
...
```

The following additional resources can be used:

* <https://dev.mysql.com/doc/refman/8.0/en/mysql-innodb-cluster-working-with-cluster.html>

* <https://dev.mysql.com/doc/refman/8.0/en/mysql-innodb-cluster-production-deployment.html>

If the user doesn't want to incur into the maintenance overhead of a
replicated MySQL, simply using a single deployment instance with
persistence volume will work as well, with the reduced HA as explained in
the section below.

## Redis Deployment OR Statefulset

### Deployment

```bash
kubectl -n sysdigcloud create -f manifests/redis/redis-deployment.yaml
```

### Statefulset (Advanced)

To create a Redis statefulset, the provided manifest under `manifests/redis`
can be used. By default, it will use a local non-persistent volume (standard dir).
Apply all of the following at once. None of this will work standalone.

```bash
kubectl -n sysdigcloud create -f manifests/redis/redis-primary-statefulset.yaml
kubectl -n sysdigcloud create -f manifests/redis/redis-primary-svc-statefulset.yaml
kubectl -n sysdigcloud create -f manifests/redis/redis-secondary-statefulset.yaml
kubectl -n sysdigcloud create -f manifests/redis/redis-secondary-svc-statefulset.yaml
kubectl -n sysdigcloud create -f manifests/redis/redis-sentinel-statefulset.yaml
kubectl -n sysdigcloud create -f manifests/redis/redis-sentinel-svc-statefulset.yaml
```

This creates a Redis cluster consisting of 1 primary pod, 2 secondary pods and 3 sentinel pods.
High availability in Redis is achieved through master-slave replication. A master Redis server
 can have multiple Redis servers as slaves, preferably deployed on different nodes across multiple
  data centers. When the master is unavailable, one of the slaves can be promoted to become the new
   master and continue to serve data with little or no interruption.
Redis Sentinel provides high availability for Redis. In practical terms this means that using Sentinel
 you can create a Redis deployment that resists without human intervention to certain kind of failures.
Redis Sentinel also provides other collateral tasks such as monitoring, notifications and acts as a
 configuration provider for clients.
This is the full list of Sentinel capabilities at a macroscopical level (i.e. the big picture):

* Monitoring. Sentinel constantly checks if your master and slave instances are working as expected.
* Notification. Sentinel can notify the system administrator, another computer programs, via an API,
 that something is wrong with one of the monitored Redis instances.
* Automatic fail-over. If a master is not working as expected, Sentinel can start a fail-over process
 where a slave is promoted to master, the other additional slaves are reconfigured to use the new master,
  and the applications using the Redis server informed about the new address to use when connecting.
* Configuration provider. Sentinel acts as a source of authority for clients service discovery:
 clients connect to Sentinels in order to ask for the address of the current Redis master responsible
  for a given service. If a fail-over occurs, Sentinels will report the new address.

## Cassandra Deployment OR Statefulset

### Statefulset (Easier to expand)

To create a Cassandra statefulset, the provided manifest under `manifests/cassandra/cassandra-statefulset.yaml`
can be used. By default, it will use a local non-persistent volume (standard dir).

```bash
kubectl -n sysdigcloud create -f manifests/cassandra/cassandra-service.yaml
kubectl -n sysdigcloud create -f manifests/cassandra/cassandra-statefulset.yaml
```

This creates a Cassandra cluster of size 3. To expand the Cassandra cluster, change the `replicas` to the
desired higher number.

#### Snitches

Using a [Snitch](https://docs.datastax.com/en/archived/cassandra/2.1/cassandra/architecture/architectureSnitchesAbout_c.html) allows Cassandra to use place replicas in different racks to avoid losing all replicas if a specific group of hosts (i.e. physical rack or avaibility zone) are offline at the same time due to a network partition or other outage affecting an entire related group of hosts in the underlying infrastructure.

The Snitch configuration for the Sysdig Cassandra cluster can be set using variables in the [sysdigcloud-config ConfigMap](../../sysdigcloud/config.yaml).

Make sure to read the documenatation for the specific snitch you wish to use. You may need to set other specific options for it to work properly. For example, the [Ec2Snitch](https://docs.datastax.com/en/archived/cassandra/2.1/cassandra/architecture/architectureSnitchEC2_t.html) treats each availability zone as a rack, and requires that the Datacenter be specified as the region name without the suffix (i.e. `us-east` if you are deploying in `us-east-1`). In this case you would add the following in your `config.yaml`:

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: sysdigcloud-config
data:
...
  cassandra.endpoint.snitch: Ec2Snitch
  cassandra.datacenter.name: us-east
...
```

This will instruct the Sysdig application to use `us-east` as the datacenter when specifying the replication strategy for its keyspaces.

#### Specifying JVM Parameters for an Individual Pod

There are some instances where it may be necessary to specify a JVM option for only one pod in the Cassandra Statefulset. An optional configuration is provided for this purpose.

To specify JVM options for a specific pod first deploy the [cassandra-jvm-opts-configmap.yaml](manifests/cassandra/cassandra-jvm-opts-configmap.yaml) ConfigMap object. You will also need to modify the Cassandra [Statefulset](manifests/cassandra/cassandra-statefulset.yaml) to mount this configuration file into the Cassandra pods.

Add the following sections to the StatefulSet (examples are included in comments which can simply be uncommented):

```yaml
apiVersion: apps/v1beta1
kind: StatefulSet
metadata:
  name: sysdigcloud-cassandra
...
spec:
  template:
...
    spec:
...
    containers:
...
          volumeMounts:
            - name: cassandra-jvm-opts
              mountPath: /opt/cassandra/cassandra-jvm-opts.json
              subPath: cassandra-jvm-opts.json
...
    volumes:
    - name: cassandra-jvm-opts
      configmap:
        name: cassandra-jvm-options
...
```

For each pod specified in the `cassandra-jvm-opts` configuration it is possible to set one of two mutually exclusive options:

* `additional_jvm_options`: JVM parameters specified here will be appended to any other options set elsewhere in the Cassandra configuration.
* `override_jvm_options`: JVM parameters specified here will replace any other JVM parameters.

Only one of the above options can be set for a given pod. If both options are non-empty strings then the related pod will fail to start.

### Deployment

Before deploying the deployment object, the proper Cassandra headless service must be created (the headless
service will be used for service discovery when deploying a multi-node Cassandra cluster):

```bash
kubectl -n sysdigcloud create -f manifests/cassandra/cassandra-service.yaml
```

To create a Cassandra deployment, the provided manifest under `manifests/cassandra/cassandra-deployment.yaml`
can be used. By default, it will use a local non-persistent volume (emptyDir), but the manifest
contains commented snippets that can be uncommented when using persistent volumes such as AWS EBS or
GCE Disks (just replace the volume id from the cloud provider in the snippet):

```bash
kubectl -n sysdigcloud create -f manifests/cassandra/cassandra-deployment.yaml --namespace sysdigcloud
```

This creates a Cassandra cluster of size 1. To expand the Cassandra cluster, a new deployment must
be created for each additional Cassandra node in the cluster. You cannot simply scale the replicas of
the existing deployment because each Cassandra pod must get a different persistent volume, so in
that sense Cassandra pods are "pets" with unique identities and not "cattle".

In order for the new Cassandra deployment to automatically join the cluster, some conventions must
be followed. In particular, the Cassandra node number (1, 2, 3, ...) must be properly put in the
manifest `manifests/cassandra/cassandra-deployment.yaml` under the entries marked as `# Cassandra node number`.

For example, to scale a Cassandra cluster from 2 to 3 nodes, the manifest can be edited as such:

```yaml
...
metadata:
  name: sysdigcloud-cassandra-3 # Cassandra node number
...
      labels:
        instance: "3" # Cassandra node number
...
```

And then the deployment can be created as usual:

```bash
kubectl -n sysdigcloud create -f manifests/cassandra/cassandra-deployment.yaml
```

After each scaling activity, the status of the cluster can be checked by executing
`nodetool status` in one of the Cassandra pods. All the Cassandra nodes should be listed
as `UN` in order for the cluster to be fully up and running. Immediately after the scaling
activity, the new pod will be in joining phase:

```bash
$ kubectl -n sysdigcloud exec -it sysdigcloud-cassandra-1-2987866586-f5kgo -- nodetool status
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address    Load       Tokens  Owns (effective)  Host ID                               Rack
UN  10.52.2.4  1.88 MB    256     54.4%             99121365-4543-4e50-ae6f-a9a9cb720b7c  rack1
UJ  10.52.0.4  14.43 KB   256     ?                 4b084d81-21f1-45b6-add9-8fbea7392978  rack1
UN  10.52.1.7  917.91 KB  256     45.6%             9a7437e9-890f-477a-99be-3d8042ddd9d5  rack1
```

After the bootstrapping process terminates, the new pod will terminate the joining phase and the
cluster will be fully operational:

```bash
$ kubectl -n sysdigcloud exec -it sysdigcloud-cassandra-1-2987866586-f5kgo -- nodetool status
Datacenter: datacenter1
=======================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address    Load       Tokens  Owns (effective)  Host ID                               Rack
UN  10.52.2.4  1.88 MB    256     34.1%             99121365-4543-4e50-ae6f-a9a9cb720b7c  rack1
UN  10.52.0.4  14.43 KB   256     34.0%             4b084d81-21f1-45b6-add9-8fbea7392978  rack1
UN  10.52.1.7  917.91 KB  256     31.9%             9a7437e9-890f-477a-99be-3d8042ddd9d5  rack1
```

It is important for the number of deployments to be increased by no more than 1 at every scaling
activity, since Cassandra will refuse the joining of a new node in the Cluster if one joining
process is already in progress.

Maintaining a multi-node production Cassandra cluster requires some simple but mandatory housekeeping
procedures, best described in the official documentation.

## Elasticsearch

### Statefulset (Easier to expand)

To create a Elasticsearch statefulset, the provided manifest under
`manifests/elasticsearch/elasticsearch-statefulset.yaml`
can be used. By default, it will use a local non-persistent volume (standard dir).

```bash
kubectl -n sysdigcloud create -f manifests/elasticsearch/elasticsearch-service.yaml
kubectl -n sysdigcloud create -f manifests/elasticsearch/elasticsearch-statefulset.yaml
```

This creates a Elasticsearch cluster of size 3. To expand the Elasticsearch cluster, change the `replicas` to the
desired higher number.

### Deployment

Before deploying the deployment object, the proper Elasticsearch headless service must be created
(the headless service will be used for service discovery when deploying a multi-node Elasticsearch cluster):

```bash
kubectl -n sysdigcloud create -f manifests/elasticsearch/elasticsearch-service.yaml
```

To create an Elasticsearch deployment, the provided manifest under `manifests/elasticsearch-deployment.yaml`
can be used. By default, it will use a local non-persistent volume (emptyDir), but the manifest contains
commented snippets that can be uncommented when using persistent volumes such as AWS EBS or GCE Disks
(just replace the volume id from the cloud provider in the snippet):

```bash
kubectl -n sysdigcloud create -f manifests/elasticsearch/elasticsearch-deployment.yaml
```

This creates an Elasticsearch cluster of size 1. To expand the Elasticsearch cluster, a new deployment
must be created for each additional Elasticsearch node in the cluster. You can't just scale the replicas
of the existing deployment because each Elasticsearch pod must get a different persistent volume, so in
that sense Elasticsearch pods are "pets" with unique identities and not "cattle".

In order for the new Elasticsearch deployment to automatically join the cluster, some conventions must
be followed. In particular, the Elasticsearch node number (1, 2, 3, ...) must be properly put in the
manifest `manifests/elasticsearch/elasticsearch-deployment.yaml` under the entries marked as `# Elasticsearch node number`.

For example, to scale the Elasticsearch cluster from 2 to 3 nodes, the manifest can be edited as such:

```yaml
...
metadata:
  name: sysdigcloud-elasticsearch-3 # Elasticsearch node number
...
      labels:
        instance: "3" # Elasticsearch node number
...
```

And then the deployment can be created as usual:

```bash
kubectl -n sysdigcloud create -f manifests/elasticsearch-deployment.yaml
```

After each scaling activity, the status of the cluster can be checked by executing
`curl -sS http://127.0.0.1:9200/_cluster/health?pretty=true` in one of the Elasticsearch pods.

```bash
$ kubectl -n sysdigcloud exec -it sysdigcloud-elasticsearch-1-2660816362-tfht5 -- curl -sS http://127.0.0.1:9200/_cluster/health?pretty=true
{
  "cluster_name" : "sysdigcloud",
  "status" : "green",
  "timed_out" : false,
  "number_of_nodes" : 2,
  "number_of_data_nodes" : 2,
  "active_primary_shards" : 0,
  "active_shards" : 0,
  "relocating_shards" : 0,
  "initializing_shards" : 0,
  "unassigned_shards" : 0,
  "delayed_unassigned_shards" : 0,
  "number_of_pending_tasks" : 0,
  "number_of_in_flight_fetch" : 0,
  "task_max_waiting_in_queue_millis" : 0,
  "active_shards_percent_as_number" : 100.0
}
```
