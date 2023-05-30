<!-- Space: TOOLS -->
<!-- Parent: Installer -->
<!-- Title: [BETA] Configuration Parameters -->
<!-- Layout: plain -->

# Beta Configuration Parameters

<br />

## **pvStorageSize.small.kafka**

**Required**: `false`<br />
**Description**: The size of the persistent volume assigned to Kafka in a
cluster of [`size`](#size) small. This option is ignored if
[`storageClassProvisioner`](#storageclassprovisioner) is `hostPath`.<br />
**Options**:<br />
**Default**: 20Gi<br />
**Example**:

```yaml
pvStorageSize:
  small:
    kafka: 100Gi
```

## **pvStorageSize.small.zookeeper**

**Required**: `false`<br />
**Description**: The size of the persistent volume assigned to ZooKeeper in a
cluster of [`size`](#size) small. This option is ignored if
[`storageClassProvisioner`](#storageclassprovisioner) is `hostPath`.<br />
**Options**:<br />
**Default**: 20Gi<br />
**Example**:

```yaml
pvStorageSize:
  small:
    zookeeper: 100Gi
```

## **pvStorageSize.medium.kafka**

**Required**: `false`<br />
**Description**: The size of the persistent volume assigned to Kafka in a
cluster of [`size`](#size) medium. This option is ignored if
[`storageClassProvisioner`](#storageclassprovisioner) is `hostPath`.<br />
**Options**:<br />
**Default**: 100Gi<br />
**Example**:

```yaml
pvStorageSize:
  medium:
    kafka: 100Gi
```

## **pvStorageSize.medium.zookeeper**

**Required**: `false`<br />
**Description**: The size of the persistent volume assigned to ZooKeeper in a
cluster of [`size`](#size) medium. This option is ignored if
[`storageClassProvisioner`](#storageclassprovisioner) is `hostPath`.<br />
**Options**:<br />
**Default**: 20Gi<br />
**Example**:

```yaml
pvStorageSize:
  medium:
    zookeeper: 100Gi
```

## **pvStorageSize.large.kafka**

**Required**: `false`<br />
**Description**: The size of the persistent volume assigned to Kafka in a
cluster of [`size`](#size) large. This option is ignored if
[`storageClassProvisioner`](#storageclassprovisioner) is `hostPath`.<br />
**Options**:<br />
**Default**: 500Gi<br />
**Example**:

```yaml
pvStorageSize:
  large:
    kafka: 100Gi
```

## **pvStorageSize.large.zookeeper**

**Required**: `false`<br />
**Description**: The size of the persistent volume assigned to ZooKeeper in a
cluster of [`size`](#size) large. This option is ignored if
[`storageClassProvisioner`](#storageclassprovisioner) is `hostPath`.<br />
**Options**:<br />
**Default**: 20Gi<br />
**Example**:

```yaml
pvStorageSize:
  large:
    zookeeper: 100Gi
```

## **sysdig.iks.privateCollectorDNSName**

**Required**: `false`<br />
**Description**: The hostname that will be used in the Ingress to access Collectors from the private IKS ALBs.<br />
**Default**: ""<br />

**Example**:

```yaml
sysdig:
  iks:
    privateCollectorDNSName: ingest.private.jp-osa.monitoring.cloud.ibm.com
```

## **sysdig.iks.privateAPIDNSName**

**Required**: `false`<br />
**Description**: The hostname that will be used in the Ingress to access APIs from the private IKS ALBs.<br />
**Default**: ""<br />

**Example**:

```yaml
sysdig:
  iks:
    privateAPIDNSName: private.jp-osa.monitoring.cloud.ibm.com
```

## **sysdig.iks.privateIngressALBs**

**Required**: `false`<br />
**Description**: a list of ALB IDs to use for private ingress on the IBM platform<br />
**Default**: []

**Example**:

```yaml
sysdig:
  iks:
    privateIngressALBs:
      - private-crbvutcu8o0ouk5qn43bbg-alb1
      - private-crbvutcu8o0ouk5qn43bbg-alb2
      - private-crbvutcu8o0ouk5qn43bbg-alb3
```

## **sysdig.iks.publicIngressALBsReplicaCount**

**Required**: `false`<br />
**Description**: the number of replicas for the public ALBs in the IKS deployment; if not specified, the implicit replica count is 2<br />
**Default**: ""<br />

**Example**:

```yaml
sysdig:
  iks:
    publicIngressALBsReplicaCount: 4
```

## **sysdig.iks.publicIngressALBs**

**Required**: `false`<br />
**Description**: a list of ALB IDs to use for public ingress on the IBM platform<br />
**Default**: []

**Example**:

```yaml
sysdig:
  iks:
    publicIngressALBs:
      - public-crbvutcu8o0ouk5qn43bbg-alb4
      - public-crbvutcu8o0ouk5qn43bbg-alb5
      - public-crbvutcu8o0ouk5qn43bbg-alb6
```

## **sysdig.iks.privateIngressALBsReplicaCount**

**Required**: `false`<br />
**Description**: the number of replicas for the private ALBs in the IKS deployment; if not specified, the implicit replica count is 2<br />
**Default**: ""<br />

**Example**:

```yaml
sysdig:
  iks:
    privateIngressALBsReplicaCount: 4
```

## **sysdig.collector.privateIngressALBs**

**Required**: `false`<br />
**Description**: list of ALB IDS to use for private ingress on the IBM platform<br />
**Default**: []

**Example**:

```yaml
sysdig:
  collector:
    privateIngressALBs:
      - alb-id-1
      - alb-id-2
      - alb-id-3
```

## **sysdig.meerkat.enabled**
**Required**: `false`<br />
**Description**: Enables Meerkat. Meerkat represents collections of components that make up Sysdig's new, more computationally efficient, metrics store.<br />
**Options**: `true|false`<br />
**Default**: `true`<br />
**Example**:

```yaml
sysdig:
  meerkat:
    enabled: true
```

## **sysdig.meerkatVersion**

**Required**: `false`<br />
**Description**: Docker image tag of Meerkat, relevant when `sysdig.meerkat.enabled` is `true`.<br />
**Options**:<br />
**Default**: [`sysdig.monitorVersion`](configuration_parameters.md#sysdigmonitorversion)<br />
**Example**:

```yaml
sysdig:
  meerkatVersion: 2.4.1.5032
```

## **sysdig.meerkatCollectorReplicaCount**

**Required**: `false`<br />
**Description**: Number of Meerkat collector replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 3     |
| large        | 5     |

## **sysdig.meerkatAggregatorReplicaCount**

**Required**: `false`<br />
**Description**: Number of Meerkat aggregator replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 3     |
| large        | 5     |

## **sysdig.meerkatApiReplicaCount**

**Required**: `false`<br />
**Description**: Number of Meerkat api replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 3     |
| large        | 5     |

## **sysdig.meerkatDatastreamReplicaCount**

**Required**: `false`<br />
**Description**: Number of Meerkat Datastream replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 2     |
| large        | 4     |

## **sysdig.secure.netsec.rateLimit**

**Required**: `false`<br />
**Description**: Netsec api rate limit.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 200   |
| medium       | 200   |
| large        | 200   |

## **sysdig.resources.meerkatApi.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule each Meerkat Api pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 1        |
| medium       | 2        |
| large        | 4        |

**Example**:

```yaml
sysdig:
  resources:
    meerkatApi:
      requests:
        cpu: 2
```

## **sysdig.resources.meerkatApi.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule each Meerkat Api pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 1Gi      |
| medium       | 2Gi      |
| large        | 4Gi      |

**Example**:

```yaml
sysdig:
  resources:
    meerkatApi:
      requests:
        memory: 2Gi
```

## **sysdig.resources.meerkatApi.limits.cpu**

**Required**: `false`<br />
**Description**: The max amount of cpu assigned to each Meerkat Api pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 4      |
| medium       | 8      |
| large        | 16     |

**Example**:

```yaml
sysdig:
  resources:
    meerkatApi:
      limits:
        cpu: 2
```

## **sysdig.resources.meerkatApi.limits.memory**

**Required**: `false`<br />
**Description**: The max amount of memory assigned to each Meerkat Api pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 4Gi    |
| medium       | 8Gi    |
| large        | 16Gi   |

**Example**:

```yaml
sysdig:
  resources:
    meerkatApi:
      requests:
        memory: 2Gi
```

## **sysdig.meerkatApi.jvmOptions**

**Required**: `false`<br />
**Description**: Custom configuration for Meerkat API JVM.<br />
**Options**:<br />
**Default**:

```
-Dlogging.level.org.springframework.transaction.interceptor=TRACE
-Dio.netty.leakDetection.level=advanced
-Dlogging.level.com.sysdig.meerkat.api.server.adapter.TimeSeriesGAdapter=DEBUG
-Dlogging.level.com.sysdig.meerkat.api.server.service.realtime.RealTimeQueryServiceImpl=DEBUG
-Dlogging.level.com.sysdig.meerkat.api.server.service.realtime.MeerkatClientDNSGrpcResolver=DEBUG
-Dsysdig.meerkat.cassandra.features.queryAllMetricDescriptorsEnabled=true
```

**Example**:

```yaml
sysdig:
  meerkatApi:
    jvmOptions: "-Dio.netty.leakDetection.level=advanced"
```

## **sysdig.resources.meerkatAggregator.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule each Meerkat Aggregator pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 1        |
| medium       | 2        |
| large        | 4        |

**Example**:

```yaml
sysdig:
  resources:
    meerkatAggregator:
      requests:
        cpu: 2
```

## **sysdig.resources.meerkatAggregator.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule each Meerkat Aggregator pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 1Gi      |
| medium       | 2Gi      |
| large        | 4Gi      |

**Example**:

```yaml
sysdig:
  resources:
    meerkatAggregator:
      requests:
        memory: 2Gi
```

## **sysdig.resources.meerkatAggregator.limits.cpu**

**Required**: `false`<br />
**Description**: The max amount of cpu assigned to each Meerkat Aggregator pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 4      |
| medium       | 8      |
| large        | 16     |

**Example**:

```yaml
sysdig:
  resources:
    meerkatAggregator:
      limits:
        cpu: 2
```

## **sysdig.resources.meerkatAggregator.limits.memory**

**Required**: `false`<br />
**Description**: The max amount of memory assigned to each Meerkat Aggregator pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 4Gi    |
| medium       | 8Gi    |
| large        | 16Gi   |

**Example**:

```yaml
sysdig:
  resources:
    meerkatAggregator:
      requests:
        memory: 2Gi
```

## **sysdig.meerkatAggregator.jvmOptions**

**Required**: `false`<br />
**Description**: Custom configuration for Meerkat Aggregator JVM.<br />
**Options**:<br />
**Default**:

```
-Dlogging.level.org.springframework.transaction.interceptor=TRACE
-Dio.netty.leakDetection.level=advanced
```

**Example**:

```yaml
sysdig:
  meerkatAggregator:
    jvmOptions: "-Dio.netty.leakDetection.level=advanced"
```

## **sysdig.resources.meerkatCollector.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule each Meerkat Collector pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 1        |
| medium       | 2        |
| large        | 4        |

**Example**:

```yaml
sysdig:
  resources:
    meerkatCollector:
      requests:
        cpu: 2
```

## **sysdig.resources.meerkatCollector.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule each Meerkat Collector pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 3Gi      |
| medium       | 8Gi      |
| large        | 12Gi     |

**Example**:

```yaml
sysdig:
  resources:
    meerkatCollector:
      requests:
        memory: 2Gi
```

## **sysdig.resources.meerkatCollector.limits.cpu**

**Required**: `false`<br />
**Description**: The max amount of cpu assigned to each Meerkat Collector pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 2      |
| medium       | 4      |
| large        | 8      |

**Example**:

```yaml
sysdig:
  resources:
    meerkatCollector:
      limits:
        cpu: 2
```

## **sysdig.resources.meerkatCollector.limits.memory**

**Required**: `false`<br />
**Description**: The max amount of memory assigned to each Meerkat Collector pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 8Gi    |
| medium       | 16Gi   |
| large        | 24Gi   |

**Example**:

```yaml
sysdig:
  resources:
    meerkatCollector:
      requests:
        memory: 2Gi
```

## **sysdig.meerkatCollector.jvmOptions**

**Required**: `false`<br />
**Description**: Custom configuration for Meerkat Collector JVM.<br />
**Options**:<br />
**Default**:

```
-Dsysdig.cassandra.auto-schema=true
-Dlogging.level.org.springframework.transaction.interceptor=TRACE
-Dio.netty.leakDetection.level=advanced
-Dlogging.level.com.sysdig.meerkat.collector.kafka.epochstate.ShardEpochState=DEBUG
-Dlogging.level.com.sysdig.meerkat.collector.service.GPartBuilderImpl=DEBUG
-Dlogging.level.com.sysdig.meerkat.collector.service.MeerkatIndexer=DEBUG
-Dlogging.level.com.sysdig.meerkat.collector.kafka.MeerkatWorker=DEBUG
-Dlogging.level.com.sysdig.meerkat.collector.grpc.GPartsQueryServiceGrpcImpl=DEBUG
```

**Example**:

```yaml
sysdig:
  meerkatCollector:
    jvmOptions: "-Dsysdig.cassandra.auto-schema=true"
```

## **sysdig.meerkat.datastreamEnabled**

**Required**: `false`<br />
**Description**: Enables Meerkat Datastrem. Meerkat Datastream enables streaming of metric data via Kafka .<br />
**Options**: `true|false`<br />
**Default**: `false`<br />
**Example**:

```yaml
sysdig:
  meerkat:
    datastreamEnabled: true
```

## **sysdig.resources.meerkatDatastream.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule each Meerkat Datastream pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 1        |
| medium       | 2        |
| large        | 4        |

**Example**:

```yaml
sysdig:
  resources:
    meerkatDatastream:
      requests:
        cpu: 2
```

## **sysdig.resources.meerkatDatastream.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule each Meerkat Datastream pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 512Mi    |
| medium       | 1Gi      |
| large        | 2Gi      |

**Example**:

```yaml
sysdig:
  resources:
    meerkatDatastream:
      requests:
        memory: 2Gi
```

## **sysdig.resources.meerkatDatastream.limits.cpu**

**Required**: `false`<br />
**Description**: The max amount of cpu assigned to each Meerkat Datastream pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 2      |
| medium       | 4      |
| large        | 8      |

**Example**:

```yaml
sysdig:
  resources:
    meerkatDatastream:
      limits:
        cpu: 2
```

## **sysdig.resources.meerkatDatastream.limits.memory**

**Required**: `false`<br />
**Description**: The max amount of memory assigned to each Meerkat Datastream pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 1Gi    |
| medium       | 2Gi    |
| large        | 3Gi    |

**Example**:

```yaml
sysdig:
  resources:
    meerkatDatastream:
      requests:
        memory: 2Gi
```

## **sysdig.meerkatDatastream.jvmOptions**

**Required**: `false`<br />
**Description**: Custom configuration for Meerkat Datastream JVM.<br />
**Options**:<br />
**Default**:

```
-Xms1g -Xmx1g
```

**Example**:

```yaml
sysdig:
  meerkatDatastream:
    jvmOptions: "-Xms1g -Xmx1g"
```

## **sysdig.kafkaVersion**

**Required**: `false`<br />
**Description**: Docker image tag of Kafka, relevant when `sysdig.meerkat.enabled` is `true` or `sysdig.fastpathAggregator.enabled` is `true`.<br />
**Options**:<br />
**Default**: 5.3.1.1<br />
**Example**:

```yaml
sysdig:
  kafkaVersion: 5.3.1.1
```

## **sysdig.kafkaReplicaCount**

**Required**: `false`<br />
**Description**: Number of Kafka replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 3     |
| medium       | 3     |
| large        | 5     |

## **sysdig.kafka.enabled**

**Required**: `false`<br />
**Description**: Enables kafka and zookeeper, if they are required by the apps.<br />
**Options**: `true|false`<br />
**Default**: `true`<br />
**Example**:

```yaml
sysdig:
  kafka:
    enabled: true
```

## **sysdig.kafka.jvmOptions**

**Required**: `false`<br />
**Description**: The custom configuration for Kafka JVM.<br />
**Options**:<br />
**Default**: Empty (Kafka will implicitly assume `-Xms1G -Xmx1G`<br />
**Example**:

```yaml
sysdig:
  kafka:
    jvmOptions: -Xms4G -Xmx4G
```

## **sysdig.kafka.secure.enabled**

**Required**: `false`<br />
**Description**: WARNING: If this is `true`, `sysdig.monitorVersion` must be `2.4.1.5032`. Enables TLS for Kafka cluster.<br />
**Options**: `true|false`<br />
**Default**: `false`<br />
**Example**:

```yaml
sysdig:
  kafka:
    secure:
      enabled: true
```

## **sysdig.kafka.secure.zookeeper.user**

**Required**: `false`<br />
**Description**: Username for Zookeeper auth to secure Kafka cluster.<br />
**Options**:<br />
**Default**: `kafka`<br />
**Example**:

```yaml
sysdig:
  kafka:
    secure:
      zookeeper:
        user: kafka
```

## **sysdig.kafka.secure.zookeeper.password**

**Required**: `false`<br />
**Description**: Password for Zookeeper auth to secure Kafka cluster.<br />
**Options**:<br />
**Default**: Auto-generated 16 random alphanumeric characters.<br />
**Example**:

```yaml
sysdig:
  kafka:
    secure:
      zookeeper:
        password: GFDg4t3$tfe4
```

## **sysdig.kafka.secure.broker.user**

**Required**: `false`<br />
**Description**: Username for Kafka broker auth to secure Kafka cluster.<br />
**Options**:<br />
**Default**: `kafkabroker`<br />
**Example**:

```yaml
sysdig:
  kafka:
    secure:
      broker:
        user: kafka
```

## **sysdig.kafka.secure.broker.password**

**Required**: `false`<br />
**Description**: Password for Kafka broker auth to secure Kafka cluster.<br />
**Options**:<br />
**Default**: Auto-generated 16 random alphanumeric characters.<br />
**Example**:

```yaml
sysdig:
  kafka:
    secure:
      broker:
        password: eFSuhrt3$tfe4
```

## **sysdig.resources.kafka.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule each Kafka pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 200m     |
| medium       | 1        |
| large        | 2        |

**Example**:

```yaml
sysdig:
  resources:
    kafka:
      requests:
        cpu: 2
```

## **sysdig.resources.kafka.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule each Kafka pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 512Mi    |
| medium       | 3Gi      |
| large        | 6Gi      |

**Example**:

```yaml
sysdig:
  resources:
    kafka:
      requests:
        memory: 2Gi
```

## **sysdig.resources.kafka.limits.cpu**

**Required**: `false`<br />
**Description**: The max amount of cpu assigned to each Kafka pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 500m   |
| medium       | 4      |
| large        | 8      |

**Example**:

```yaml
sysdig:
  resources:
    kafka:
      limits:
        cpu: 2
```

## **sysdig.resources.kafka.limits.memory**

**Required**: `false`<br />
**Description**: The max amount of memory assigned to each Kafka pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 1Gi    |
| medium       | 8Gi    |
| large        | 16Gi   |

**Example**:

```yaml
sysdig:
  resources:
    kafka:
      requests:
        memory: 2Gi
```

## **sysdig.zookeeperVersion**

**Required**: `false`<br />
**Description**: Docker image tag of Zookeeper, relevant when `sysdig.meerkat.enabled` is `true` or `sysdig.fastpathAggregator.enabled` is `true`.<br />
**Options**:<br />
**Default**: 5.3.1.1<br />
**Example**:

```yaml
sysdig:
  zookeeperVersion: 5.3.1.1
```

## **sysdig.zookeeperReplicaCount**

**Required**: `false`<br />
**Description**: Number of Zookeeper replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 3     |
| medium       | 3     |
| large        | 3     |

## **sysdig.zookeeper.nodeAffinityLabel**

**Required**: `false`<br />
**Description**: The key and the value of the label that is used to configure the nodes that the
Zookeeper pods are expected to run on.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
sysdig:
  zookeeper:
    nodeAffinityLabel:
      key: sysdig/worker-pool
      value: zookeeper
```

## **sysdig.zookeeper.nodeAffinityMode**

**Required**: `false`<br />
**Description**: Make nodeAffinity "required" or "preferred" for Zookeeper<br />
**Options**: `required|preferred`<br />
**Default**: `preferred`<br />
**Example**:

```yaml
sysdig:
  zookeeper:
    nodeAffinityMode: preferred
```

## **sysdig.zookeeper.secure.super.user**

**Required**: `false`<br />
**Description**: Zookeeper's super user's username if Kafka cluster is TLS-enabled.<br />
**Options**:<br />
**Default**: `super`<br />
**Example**:

```yaml
sysdig:
  zookeeper:
    secure:
      super:
        user: super
```

## **sysdig.zookeeper.secure.super.password**

**Required**: `false`<br />
**Description**: Zookeeper's super user's password if Kafka cluster is TLS-enabled.<br />
**Options**:<br />
**Default**: Auto-generated 16 random alphanumeric characters.<br />
**Example**:

```yaml
sysdig:
  zookeeper:
    secure:
      super:
        password: F3a4raW#$Rw3e
```

## **sysdig.resources.zookeeper.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule each Zookeeper pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 100m     |
| medium       | 200m     |
| large        | 400m     |

**Example**:

```yaml
sysdig:
  resources:
    zookeeper:
      requests:
        cpu: 2
```

## **sysdig.resources.zookeeper.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule each Zookeeper pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 128Mi    |
| medium       | 256Mi    |
| large        | 512Mi    |

**Example**:

```yaml
sysdig:
  resources:
    zookeeper:
      requests:
        memory: 2Gi
```

## **sysdig.resources.zookeeper.limits.cpu**

**Required**: `false`<br />
**Description**: The max amount of cpu assigned to each Zookeeper pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 250m   |
| medium       | 500m   |
| large        | 1      |

**Example**:

```yaml
sysdig:
  resources:
    zookeeper:
      limits:
        cpu: 2
```

## **sysdig.resources.zookeeper.limits.memory**

**Required**: `false`<br />
**Description**: The max amount of memory assigned to each Zookeeper pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 500m   |
| medium       | 1Gi    |
| large        | 2Gi    |

**Example**:

```yaml
sysdig:
  resources:
    zookeeper:
      requests:
        memory: 2Gi
```

## **sysdig.beacon.enabled** (**Deprecated**)

**Required**: `false`<br />
**Description**: Enables (IBM Platform Metrics version of) beacon, the components that allow Sysdig to natively ingest Prometheus metrics via remote write.<br />
**Options**: `true|false`<br />
**Default**: `false`<br />
**Example**:

```yaml
sysdig:
  beacon:
    enabled: true
```

## **sysdig.beacon.platformMetricsEnabled**

**Required**: `false`<br />
**Description**: Enables IBM Platform Metrics version of beacon, the components that allow Sysdig to natively ingest Prometheus metrics via remote write.<br />
**Options**: `true|false`<br />
**Default**: Previously, this was called `beacon.enabled` and it defaults to that deprecated value, which defaults to `false`<br />
**Example**:

```yaml
sysdig:
  beacon:
    platformMetricsEnabled: true
```

**WARNING**
**`HostAlreadyClaimed` Error in Openshift**
To use this feature on Openshift an overlay is required to avoid an error in Routes which will prevent the `Collector`
Route to be active and able to receive data from the agents.
This is what the error would look like:

```
oc get route
NAME                                                 HOST/PORT                                                       PATH                                             SERVICES                                             PORT    TERMINATION   WILDCARD
[omitted lines]
sysdigcloud-collector                                HostAlreadyClaimed
[omitted lines]
```

Use this overlay to avoid the error:

```
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: sysdigcloud-beacon-prom-remote-write
  namespace: sysdigcloud
spec:
  host: domain_name
```

The `domain_name` must be different from the name used for the Collectors endpoint and it must be used for Prometheus metrics ingestion.

## **sysdig.beacon.promEnabled**

**Required**: `false`<br />
**Description**: Enables Generalized Beacon for Prometheus, the components that allow Sysdig to natively ingest Prometheus metrics via remote write.<br />
**Options**: `true|false`<br />
**Default**: `false`<br />
**Example**:

```yaml
sysdig:
  beacon:
    promEnabled: true
```

## **sysdig.beacon.token**

**Required**: `false`<br />
**Description**: Set the Beacon access token, used by the Beacon components to authenticate against the API server.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
sysdig:
  beacon:
    token: change_me
```

## **sysdig.promRemoteWriteVersion**

**Required**: `false`<br />
**Description**: Docker image tag of prom-remote-write, relevant when `sysdig.beacon.promEnabled` or `sysdig.beacon.platformMetricsEnabled` is `true`.<br />
**Options**:<br />
**Default**: [`sysdig.monitorVersion`](configuration_parameters.md#sysdigmonitorversion)<br />
**Example**:

```yaml
sysdig:
  promRemoteWriteVersion: 2.4.1.5032
```

## **sysdig.promRemoteWriteBeaconReplicaCount**

**Required**: `false`<br />
**Description**: Number of beacon-prom-remote-write replicas for Generalized Beacon.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 3     |
| large        | 5     |

**Example**:

```yaml
sysdig:
  promRemoteWriteBeaconReplicaCount: 5
```

## **sysdig.promRemoteWritePlatformMetricsReplicaCount**

**Required**: `false`<br />
**Description**: Number of prom-remote-write replicas for IBM Platform Metrics.<br />
**Options**:<br />
**Default**: Previously, this was called `promRemoteWriteReplicaCount` and it defaults to that deprecated value.<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 3     |
| large        | 5     |

**Example**:

```yaml
sysdig:
  promRemoteWritePlatformMetricsReplicaCount: 5
```

## **sysdig.promRemoteWriteBeacon.jvmOptions**

**Required**: `false`<br />
**Description**: The custom configuration for the Generalized Beacon beacon-prom-remote-write JVM.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
sysdig:
  promRemoteWriteBeacon:
    jvmOptions: -Xms4G -Xmx4G
```

## **sysdig.promRemoteWritePlatformMetrics.jvmOptions**

**Required**: `false`<br />
**Description**: The custom configuration for the IBM Platform Metrics prom-remote-write JVM. Note that the profile is actually implicit.<br />
**Options**:<br />
**Default**: Previously, this was called `promRemoteWrite.jvmOptions` and it defaults to that deprecated value.<br />
**Example**:

```yaml
sysdig:
  promRemoteWritePlatformMetrics:
    jvmOptions: -Xms4G -Xmx4G -Dspring.profiles.active=beacon-ibm
```

## **sysdig.serviceOwnerManagement.enabled**

**Required**: `false`<br />
**Description**: Enables ServiceOwnerManagement, the microservice that IBM Service Owners will use to manage their assets.<br />
**Options**: `true|false`<br />
**Default**: `false`<br />
**Example**:

```yaml
sysdig:
  serviceOwnerManagement:
    enabled: true
```

## **sysdig.serviceOwnerManagement.legacyToken**

**Required**: `false`<br />
**Description**: Set the ServiceOwnerManagement-to-Legacy access token, used by this service to authenticate against the API server.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
sysdig:
  serviceOwnerManagement:
    legacyToken: change_me
```

## **sysdig.serviceOwnerManagement.beaconToken**

**Required**: `false`<br />
**Description**: Set the ServiceOwnerManagement-to-Beacon access token, used by this service to authenticate against the Beacon server.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
sysdig:
  serviceOwnerManagement:
    beaconToken: change_me
```

## **sysdig.serviceOwnerManagementVersion**

**Required**: `false`<br />
**Description**: Docker image tag of ServiceOwnerManagement, relevant when `sysdig.serviceOwnerManagement.enabled` is `true`.<br />
**Options**:<br />
**Default**: [`sysdig.monitorVersion`](configuration_parameters.md#sysdigmonitorversion)<br />
**Example**:

```yaml
sysdig:
  serviceOwnerManagementVersion: 2.4.1.5032
```

## **sysdig.serviceOwnerManagementReplicaCount**

**Required**: `false`<br />
**Description**: Number of ServiceOwnerManagement replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 3     |
| large        | 5     |

**Example**:

```yaml
sysdig:
  serviceOwnerManagementReplicaCount: 2
```

## **sysdig.serviceOwnerManagement.jvmOptions**

**Required**: `false`<br />
**Description**: The custom configuration for the ServiceOwnerManagement JVM.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
sysdig:
  serviceOwnerManagement:
    jvmOptions: -Xms4G -Xmx4G
```

## **sysdig.resources.promRemoteWriteBeacon.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule each Generalized Beacon beacon-prom-remote-write pod.<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 1        |
| medium       | 2        |
| large        | 4        |

**Example**:

```yaml
sysdig:
  resources:
    promRemoteWriteBeacon:
      requests:
        cpu: 2
```

## **sysdig.resources.promRemoteWriteBeacon.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule each Generalized Beacon beacon-prom-remote-write pod.<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 3Gi      |
| medium       | 8Gi      |
| large        | 12Gi     |

**Example**:

```yaml
sysdig:
  resources:
    promRemoteWriteBeacon:
      requests:
        memory: 2Gi
```

## **sysdig.resources.promRemoteWriteBeacon.limits.cpu**

**Required**: `false`<br />
**Description**: The max amount of cpu assigned to each Generalized Beacon beacon-prom-remote-write pod.<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 2      |
| medium       | 4      |
| large        | 8      |

**Example**:

```yaml
sysdig:
  resources:
    promRemoteWriteBeacon:
      limits:
        cpu: 2
```

## **sysdig.resources.promRemoteWriteBeacon.limits.memory**

**Required**: `false`<br />
**Description**: The max amount of memory assigned to each Generalized Beacon beacon-prom-remote-write pod.<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 8Gi    |
| medium       | 16Gi   |
| large        | 24Gi   |

**Example**:

```yaml
sysdig:
  resources:
    promRemoteWriteBeacon:
      requests:
        memory: 2Gi
```

## **sysdig.resources.promRemoteWritePlatformMetrics.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule each IBM Platform Metrics prom-remote-write pod.<br />
**Options**:<br />
**Default**:

Previously, this was called `promRemoteWrite.requests.cpu` and it defaults to that deprecated value which has these defaults:<br />

| cluster-size | requests |
| ------------ | -------- |
| small        | 1        |
| medium       | 2        |
| large        | 4        |

**Example**:

```yaml
sysdig:
  resources:
    promRemoteWritePlatformMetrics:
      requests:
        cpu: 2
```

## **sysdig.resources.promRemoteWritePlatformMetrics.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule each IBM Platform Metrics prom-remote-write pod.<br />
**Options**:<br />
**Default**:

Previously, this was called `promRemoteWrite.requests.memory` and it defaults to that deprecated value which has these defaults:<br />

| cluster-size | requests |
| ------------ | -------- |
| small        | 3Gi      |
| medium       | 8Gi      |
| large        | 12Gi     |

**Example**:

```yaml
sysdig:
  resources:
    promRemoteWritePlatformMetrics:
      requests:
        memory: 2Gi
```

## **sysdig.resources.promRemoteWritePlatformMetrics.limits.cpu**

**Required**: `false`<br />
**Description**: The max amount of cpu assigned to each IBM Platform Metrics prom-remote-write pod.<br />
**Options**:<br />
**Default**:

Previously, this was called `promRemoteWrite.limits.cpu` and it defaults to that deprecated value which has these defaults:<br />

| cluster-size | limits |
| ------------ | ------ |
| small        | 2      |
| medium       | 4      |
| large        | 8      |

**Example**:

```yaml
sysdig:
  resources:
    promRemoteWritePlatformMetrics:
      limits:
        cpu: 2
```

## **sysdig.resources.promRemoteWritePlatformMetrics.limits.memory**

**Required**: `false`<br />
**Description**: The max amount of memory assigned to each IBM Platform Metrics prom-remote-write pod.<br />
**Options**:<br />
**Default**:

Previously, this was called `promRemoteWrite.limits.memory` and it defaults to that deprecated value which has these defaults:<br />

| cluster-size | limits |
| ------------ | ------ |
| small        | 8Gi    |
| medium       | 16Gi   |
| large        | 24Gi   |

**Example**:

```yaml
sysdig:
  resources:
    promRemoteWritePlatformMetrics:
      requests:
        memory: 2Gi
```

## **sysdig.prometheus.enabled**
**Required**: `false`<br />
**Description**: Enables Prometheus services.<br />
**Options**: `true|false`<br />
**Default**: `true`<br />
**Example**:

```yaml
sysdig:
  prometheus:
    enabled: true
```

## **sysdig.promchapVersion**

**Required**: `false`<br />
**Description**: Docker image tag of Sysdig Prometheus Chaperone service, relevant when `sysdig.prometheus.enabled` is `true`.<br />
**Options**:<br />
**Default**: 0.99.0-2022-07-04T12-52-09Z.d68003f677<br />
**Example**:

```yaml
sysdig:
  promchapVersion: 0.99.0-2022-07-04T12-52-09Z.d68003f677
```

## **sysdig.promqlatorVersion**

**Required**: `false`<br />
**Description**: Docker image tag of Sysdig Promqlator service, relevant when `sysdig.prometheus.enabled` is `true`.<br />
**Options**:<br />
**Default**: 0.99.0-2022-07-12T09-19-16Z.93c0642b55<br />
**Example**:

```yaml
sysdig:
  promqlatorVersion: 0.99.0-2022-07-12T09-19-16Z.93c0642b55
```

## **sysdig.streamsnapVersion**

**Required**: `false`<br />
**Description**: Docker image tag of Sysdig Streamsnap service, relevant when `sysdig.streamsnap.enabled` is `true`.<br />
**Options**:<br />
**Default**: 0.99.0-staging.2022-07-29T13-34-18Z.2d308b4<br />
**Example**:

```yaml
sysdig:
  streamsnapVersion: 0.99.0-staging.2022-07-29T13-34-18Z.2d308b4
```

## **sysdig.fastpathAggregatorVersion**

**Required**: `false`<br />
**Description**: Docker image tag of Sysdig Fastpath Aggregator service, relevant when `sysdig.fastpathAggregator.enabled` is `true`.<br />
**Options**:<br />
**Default**: 0.99.0-staging.2022-07-29T13-34-18Z.2d308b4<br />
**Example**:

```yaml
sysdig:
  fastpathAggregatorVersion: 0.99.0-staging.2022-07-29T13-34-18Z.2d308b4
```

## **sysdig.promqlatorReplicaCount**

**Required**: `false`<br />
**Description**: Number of Promqlator services replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 3     |
| large        | 5     |

## **sysdig.resources.prometheus.redis.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule Prometheus Redis pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 1        |
| medium       | 2        |
| large        | 3        |

**Example**:

```yaml
sysdig:
  resources:
    prometheus:
      redis:
        requests:
          cpu: 2
```

## **sysdig.resources.prometheus.redis.limits.cpu**

**Required**: `false`<br />
**Description**: The max amount of cpu assigned to Prometheus Redis pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 1      |
| medium       | 2      |
| large        | 3      |

**Example**:

```yaml
sysdig:
  resources:
    prometheus:
      redis:
        limits:
          cpu: 2
```

## **sysdig.resources.prometheus.redis.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule Prometheus Redis pod<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 600Mi    |
| medium       | 1.2Gi    |
| large        | 2.2Gi    |

**Example**:

```yaml
sysdig:
  resources:
    prometheus:
      redis:
        requests:
          memory: 1.2Gi
```

## **sysdig.resources.prometheus.redis.limits.memory**

**Required**: `false`<br />
**Description**: The max amount of memory assigned to Prometheus Redis pod<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 800Mi  |
| medium       | 1.5Gi  |
| large        | 2.5Gi  |

**Example**:

```yaml
sysdig:
  resources:
    prometheus:
      redis:
        requests:
          memory: 1.5Gi
```

## **sysdig.prometheus.redis.maxmemory**

**Required**: `false`<br />
**Description**: The max amount of memory used by Redis cache<br />
**Default**:<br />

| cluster-size | size  |
| ------------ | ----- |
| small        | 500Mb |
| medium       | 1Gb   |
| large        | 2Gb   |

**Example**:

```yaml
sysdig:
  prometheus:
    redis:
      maxmemory: 1Gb
```

## **sysdig.resources.promchap.limits.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu assigned to Promchap containers<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 1      |
| medium       | 2      |
| large        | 3      |

**Example**:

```yaml
sysdig:
  resources:
    promchap:
      limits:
        cpu: 1
```

## **sysdig.resources.promchap.limits.memory**

**Required**: `false`<br />
**Description**: The amount of memory assigned to Promchap containers<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 1Gi    |
| medium       | 2Gi    |
| large        | 4Gi    |

**Example**:

```yaml
sysdig:
  resources:
    promchap:
      limits:
        memory: 1Gi
```

## **sysdig.resources.promchap.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule Promchap containers<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 250m     |
| medium       | 500m     |
| large        | 1        |

**Example**:

```yaml
sysdig:
  resources:
    promchap:
      requests:
        cpu: 250m
```

## **sysdig.resources.promchap.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule Promchap containers<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 300Mi    |
| medium       | 500Mi    |
| large        | 1Gi      |

**Example**:

```yaml
sysdig:
  resources:
    promchap:
      requests:
        memory: 300Mi
```

## **sysdig.streamsnapReplicaCount**

**Required**: `false`<br />
**Description**: Number of Streamsnap replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 2     |
| large        | 3     |

**Example**:

```yaml
sysdig:
  streamsnapReplicaCount: 2
```

## **sysdig.fastpathAggregatorReplicaCount**

**Required**: `false`<br />
**Description**: Number of Fastpath Aggregator replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 2     |
| large        | 3     |

**Example**:

```yaml
sysdig:
  fastpathAggregatorReplicaCount: 2
```

## **sysdig.streamsnap.enabled**

**Required**: `false`<br />
**Description**: Whether to enable Streamsnap or not.<br />
**Options**: `true|false`<br />
**Default**: `false`<br />

**Example**:

```yaml
sysdig:
  streamsnap:
    enabled: true
```

## **sysdig.streamsnap.jvmOptions**

**Required**: `false`<br />
**Description**: Custom configuration for Streamsnap jvm.<br />
**Options**: <br />
**Default**:

| cluster-size | jvmOptions |
| ------------ | ---------- |
| small        | -Xmx=4g    |
| medium       | -Xmx=12g   |
| large        | -Xmx=18g   |

**Example**:

```yaml
sysdig:
  streamsnap:
    jvmOptions: "-Xmx=4g"
```

## **sysdig.streamsnap.numThreadsForInterval60**

**Required**: `false`<br />
**Description**: Number of threads Streamsnap uses for the 1-minute snapshots.<br />
**Options**: <br />
**Default**:

| cluster-size | numThreadsForInterval60 |
| ------------ | ----------------------- |
| small        | 2                       |
| medium       | 4                       |
| large        | 6                       |

**Example**:

```yaml
sysdig:
  streamsnap:
    numThreadsForInterval60: 4
```

## **sysdig.streamsnap.numThreadsForInterval600**

**Required**: `false`<br />
**Description**: Number of threads Streamsnap uses for the 10-minutes snapshots.<br />
**Options**: <br />
**Default**:

| cluster-size | numThreadsForInterval600 |
| ------------ | ------------------------ |
| small        | 1                        |
| medium       | 2                        |
| large        | 6                        |

**Example**:

```yaml
sysdig:
  streamsnap:
    numThreadsForInterval600: 2
```

## **sysdig.streamsnap.numThreadsForInterval3600**

**Required**: `false`<br />
**Description**: Number of threads Streamsnap uses for the 1-hour snapshots.<br />
**Options**: <br />
**Default**:

| cluster-size | numThreadsForInterval3600 |
| ------------ | ------------------------- |
| small        | 1                         |
| medium       | 2                         |
| large        | 6                         |

**Example**:

```yaml
sysdig:
  streamsnap:
    numThreadsForInterval3600: 2
```

## **sysdig.streamsnap.numThreadsForInterval86400**

**Required**: `false`<br />
**Description**: Number of threads Streamsnap uses for the 1-day snapshots.<br />
**Options**: <br />
**Default**:

| cluster-size | numThreadsForInterval86400 |
| ------------ | -------------------------- |
| small        | 1                          |
| medium       | 2                          |
| large        | 6                          |

**Example**:

```yaml
sysdig:
  streamsnap:
    numThreadsForInterval86400: 2
```

## **sysdig.resources.streamsnap.limits.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu assigned to Streamsnap containers<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 2      |
| medium       | 4      |
| large        | 8      |

**Example**:

```yaml
sysdig:
  resources:
    streamsnap:
      limits:
        cpu: 8
```

## **sysdig.resources.streamsnap.limits.memory**

**Required**: `false`<br />
**Description**: The amount of memory assigned to Streamsnap containers<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 8g     |
| medium       | 16g    |
| large        | 24g    |

**Example**:

```yaml
sysdig:
  resources:
    streamsnap:
      limits:
        memory: 8Gi
```

## **sysdig.resources.streamsnap.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule Streamsnap containers<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 2        |
| medium       | 4        |
| large        | 8        |

**Example**:

```yaml
sysdig:
  resources:
    streamsnap:
      requests:
        cpu: 2
```

## **sysdig.resources.streamsnap.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule Streamsnap containers<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 8g       |
| medium       | 16g      |
| large        | 24g      |

**Example**:

```yaml
sysdig:
  resources:
    streamsnap:
      requests:
        memory: 2Gi
```

## **sysdig.fastpathAggregator.enabled**

**Required**: `false`<br />
**Description**: Whether to enable Fastpath Aggregator or not.<br />
**Options**: `true|false`<br />
**Default**: `false`<br />

**Example**:

```yaml
sysdig:
  fastpathAggregator:
    enabled: true
```

## **sysdig.fastpathAggregator.jvmOptions**

**Required**: `false`<br />
**Description**: Custom configuration for the Fastpath Aggregator jvm.<br />
**Options**: <br />
**Default**:

| cluster-size | jvmOptions |
| ------------ | ---------- |
| small        | -Xmx=4g    |
| medium       | -Xmx=12g   |
| large        | -Xmx=16g   |

**Example**:

```yaml
sysdig:
  fastpathAggregator:
    jvmOptions: "-Xmx=4g"
```

## **sysdig.fastpathAggregator.numThreadsForInterval60**

**Required**: `false`<br />
**Description**: Number of threads Fastpath Aggregator uses for the 1-minute snapshots.<br />
**Options**: <br />
**Default**:

| cluster-size | numThreadsForInterval60 |
| ------------ | ----------------------- |
| small        | 2                       |
| medium       | 4                       |
| large        | 4                       |

**Example**:

```yaml
sysdig:
  fastpathAggregator:
    numThreadsForInterval60: 4
```

## **sysdig.fastpathAggregator.numThreadsForInterval600**

**Required**: `false`<br />
**Description**: Number of threads Fastpath Aggregator uses for the 10-minutes snapshots.<br />
**Options**: <br />
**Default**:

| cluster-size | numThreadsForInterval600 |
| ------------ | ------------------------ |
| small        | 1                        |
| medium       | 2                        |
| large        | 2                        |

**Example**:

```yaml
sysdig:
  fastpathAggregator:
    numThreadsForInterval600: 2
```

## **sysdig.fastpathAggregator.numThreadsForInterval3600**

**Required**: `false`<br />
**Description**: Number of threads Fastpath Aggregator uses for the 1-hour snapshots.<br />
**Options**: <br />
**Default**:

| cluster-size | numThreadsForInterval3600 |
| ------------ | ------------------------- |
| small        | 1                         |
| medium       | 2                         |
| large        | 2                         |

**Example**:

```yaml
sysdig:
  fastpathAggregator:
    numThreadsForInterval3600: 2
```

## **sysdig.fastpathAggregator.numThreadsForInterval86400**

**Required**: `false`<br />
**Description**: Number of threads Fastpath Aggregator uses for the 1-day snapshots.<br />
**Options**: <br />
**Default**:

| cluster-size | numThreadsForInterval86400 |
| ------------ | -------------------------- |
| small        | 1                          |
| medium       | 2                          |
| large        | 2                          |

**Example**:

```yaml
sysdig:
  fastpathAggregator:
    numThreadsForInterval86400: 2
```

## **sysdig.resources.fastpathAggregator.limits.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu assigned to Fastpath Aggregator containers<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 2      |
| medium       | 4      |
| large        | 8      |

**Example**:

```yaml
sysdig:
  resources:
    fastpathAggregator:
      limits:
        cpu: 8
```

## **sysdig.resources.fastpathAggregator.limits.memory**

**Required**: `false`<br />
**Description**: The amount of memory assigned to Fastpath Aggregator containers<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 8g     |
| medium       | 16g    |
| large        | 24g    |

**Example**:

```yaml
sysdig:
  resources:
    fastpathAggregator:
      limits:
        memory: 8Gi
```

## **sysdig.resources.fastpathAggregator.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule Fastpath Aggregator containers<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 2        |
| medium       | 4        |
| large        | 8        |

**Example**:

```yaml
sysdig:
  resources:
    fastpathAggregator:
      requests:
        cpu: 2
```

## **sysdig.resources.fastpathAggregator.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule Fastpath Aggregator containers<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 8g       |
| medium       | 16g      |
| large        | 24g      |

**Example**:

```yaml
sysdig:
  resources:
    fastpathAggregator:
      requests:
        memory: 2Gi
```

## **sysdig.secureOnly**

**Required**: `false`<br />
**Description**: Enable product optimizations for secure that break monitor.<br />
**Options**: `true|false`<br />
**Default**: `false`

**Example**:

```yaml
sysdig:
  secureOnly: true
```

## **sysdig.secure.eventsForwarder.proxy.enable**

**Required**: `false`<br />
**Description**: Set proxy settings for secure forwarding (overrides global settings)<br />
**Options**: `true|false`<br />
**Default**:

**Example**:

```yaml
sysdig:
  secure:
    eventsForwarder:
      proxy:
        enable: false
```

## **sysdig.secure.eventsForwarder.proxy.host**

**Required**: `false`<br />
**Description**: The address of the web proxy, this could be a domain name or
an IP address. This is required if [`sysdig.secure.eventsForwarder.proxy.enable`](#sysdigsecureeventsforwarderproxyenable)
is configured.<br />
**Options**:<br />
**Default**:<br />

**Example**:

```yaml
sysdig:
  secure:
    eventsForwarder:
      proxy:
        enable: true
        host: my-awesome-proxy.my-awesome-domain.com
```

## **sysdig.secure.eventsForwarder.proxy.noProxy**

**Required**: `false`<br />
**Description**: Comma separated list of addresses or domain names
that can be reached without going through the configured web proxy. This is
only relevant if [`sysdig.secure.eventsForwarder.proxy.enable`](#sysdigsecureeventsforwarderproxyenable) is configured and
appended to the list in
[`sysdig.proxy.defaultNoProxy`](#sysdigproxydefaultnoproxy]).<br />
**Options**:<br />
**Default**: `127.0.0.1, localhost, sysdigcloud-anchore-core, sysdigcloud-anchore-api`<br />

**Example**:

```yaml
sysdig:
  secure:
    eventsForwarder:
      proxy:
        enable: true
        noProxy: my-awesome.domain.com, 192.168.0.0/16
```

## **sysdig.secure.eventsForwarder.proxy.password**

**Required**: `false`<br />
**Description**: The password used to access the configured
[`sysdig.secure.eventsForwarder.proxy.host`](#sysdigsecureeventsforwarderproxyhost).<br />
**Options**:<br />
**Default**:<br />

**Example**:

```yaml
sysdig:
  secure:
    eventsForwarder:
      proxy:
        enable: true
        password: F00B@r!
```

## **sysdig.secure.eventsForwarder.proxy.port**

**Required**: `false`<br />
**Description**: The port the configured
[`sysdig.secure.eventsForwarder.proxy.host`](#sysdigsecureeventsforwarderproxyhost) is listening on. If this is not
configured it defaults to 80.<br />
**Options**:<br />
**Default**: `80`<br />

**Example**:

```yaml
sysdig:
  secure:
    eventsForwarder:
      proxy:
        enable: true
        port: 3128
```

## **sysdig.secure.eventsForwarder.proxy.protocol**

**Required**: `false`<br />
**Description**: The protocol to use to communicate with the configured
[`sysdig.secure.eventsForwarder.proxy.host`](#sysdigsecureeventsforwarderproxyhost) .<br />
**Options**: `http|https`<br />
**Default**: `http`<br />

**Example**:

```yaml
sysdig:
  secure:
    eventsForwarder:
      proxy:
        enable: true
        protocol: https
```

## **sysdig.secure.eventsForwarder.proxy.user**

**Required**: `false`<br />
**Description**: The user used to access the configured
[`sysdig.secure.eventsForwarder.proxy.host`](#sysdigsecureeventsforwarderproxyhost).<br />
**Options**:<br />
**Default**:<br />

**Example**:

```yaml
sysdig:
  secure:
    eventsForwarder:
      proxy:
        enable: true
        user: alice
```

## **sysdig.postgresDatabases.PRWSInternalIngestion**

**Required**: `false`<br />
**Description**: A map containing database connection details for external postgresql instance used as `prwsInternalIngestion` database. To use in conjunction with `sysdig.postgresql.external`.<br />
**Example**:

```yaml
sysdig:
  postgresql:
    external: true
  postgresDatabases:
    rapidResponse:
      host: my-prw-internal-ingestion-db-external.com
      port: 5432
      db: prws_internal_ingestion
      username: prws_internal_ingestion_user
      password: my_prws_internal_ingestion_password
      sslmode: disable
      admindb: root_db
      adminusername: root_user
      adminpassword: my_root_user_password
```

## **sysdig.beacon.prwsInternalIngestionEnabled**

**Required**: `false`<br />
**Description**: Enable Prom Remote Write Internal Ingestion<br />
**Options**:<br />
**Default**:`false`<br />
**Example**:

```yaml
sysdig:
  beacon:
    prwsInternalIngestionEnabled: true
```

## **sysdig.prwsInternalIngestionReplicaCount**

**Required**: `false`<br />
**Description**: Number of PRWS Internal Ingestion replicas<br />
**Options**:<br />
**Default**:<br />

**Example**:

```yaml
sysdig:
  prwsInternalIngestionReplicaCount: 5
```

## **sysdig.prwsInternalIngestion.jvmOptions**

**Required**: `false`<br />
**Description**: Custom JVM configuration for PRWS Internal Ingestion<br />
**Options**:<br />
**Default**:<br />

**Example**:

```yaml
sysdig:
  prwsInternalIngestion:
    jvmOptions: |-
      -Xms12g -Xmx12g
```

## **sysdig.prwsInternalIngestion.ingress**

**Required**: `false`<br />
**Description**: Add a custom Ingress for PRWS Internal Ingestion<br />
**Options**:<br />
**Default**:<br />

**Example**:

```yaml
sysdig:
  prwsInternalIngestion:
    ingress:
      - name: my-prws-internal-ingestion
        omitBaseAnnotations: true
        annotations:
          haproxy-ingress.github.io/timeout-server: 20s
          haproxy-ingress.github.io/config-backend: |
            retries 2
        labels:
          app.kubernetes.io/managed-by: ingress-config
          app.kubernetes.io/name: ingress-config
          app.kubernetes.io/part-of: sysdigcloud
          role: ingress-config
          tier: infra
        hosts:
          - host: my-app.my-domain.com
            sslSecretName: ssl-secret
            paths:
              - path: /api
                serviceName: my-service-name
                servicePort: 9510
```

## **sysdig.prwsInternalIngestion.privateEndpointCommunicationEnforcement**

**Required**: `false`<br />
**Description**: Enable private endpoint communication for PRWS Internal Ingestion
**Options**: `true|false`<br />
**Default**: <br />
**Example**:

```yaml
sysdig:
  prwsInternalIngestion:
    privateEndpointCommunicationEnforcement: false
```

## **sysdig.prwsInternalIngestion.privateEndpointCommunicationEnforcementExclusions**

**Required**: `false`<br />
**Description**: Comma separated list of addresses or domain names that can
override the `privateEndpointCommunicationEnforcement`.
**Options**:<br />
**Default**:<br />

**Example**:

```yaml
sysdig:
  prwsInternalIngestion:
    privateEndpointCommunicationEnforcement: false
    privateEndpointCommunicationEnforcementExclusions: my-awesome.domain.com, 192.168.0.0/16 
```
