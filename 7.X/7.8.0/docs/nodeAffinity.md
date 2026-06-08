# Notes on using `nodeAffinity` in onprem

> [!WARNING]
> This is an internal note, it is not for external consumption.

## Global `nodeAffinity`

- Most or all of our workloads have the option to add  `nodeAffinity` to the appropriate manifests.
- `nodeAffinity` can be activated using the following keys in `values.yaml`

> [!WARNING]
> This will activate `nodeAffinity` FOR ALL WORKLOADS!

```YAML
global:
  nodeaffinityLabel:
    key: "beta.kubernetes.io/arch"
    value: "amd64"
```

## Local `nodeAffinity` options

- Some workloads, especially stateful ones, support an individual `nodeAffinity` option which is controlled by special `values.yaml` keys.
  - Normally, the workload-level `nodeAffinity` should override the above global one (TBC)

> [!WARNING]
> `postgres-ha` and `postgresql` ONLY use the `.global.nodeAffinityLabel` - no service-level `nodeAffinity`

### Charts with local `nodeAffinity` and detailed configuration

#### elasticsearch

```YAML
elasticsearch:
  nodeAffinityMode: required
  nodeaffinityLabel:
    key: "beta.kubernetes.io/arch"
    value: "amd64"
```

#### cassandra

```YAML
cassandra:
  nodeAffinityLabel:
    key: "sysdig.com/worker-pool-role"
    value: "cassandra"
  # Note: No nodeAffinityMode setting available
  # When set: uses preferredDuringSchedulingIgnoredDuringExecution
  # When not set: falls back to global.nodeaffinityLabel with requiredDuringSchedulingIgnoredDuringExecution
```

#### elasticsearch-exporter

```YAML
elasticsearchExporter:
  # Uses array-based nodeAffinity structure (different from standard pattern)
  nodeAffinity: []
  # Example:
  # - mode: preferred
  #   labels:
  #   - key: label-1
  #     value:
  #     - value1
  # - mode: required
  #   labels:
  #   - key: label-1
  #     value:
  #     - value1
```

#### Kafka & Zookeeper

```YAML
kafka:
  nodeaffinityLabel:
    key: sysdig.com/worker-pool-role
    value: kafka
  nodeAffinityMode: preferred  # "preferred" or "required"
```

```YAML
zookeeper:
  nodeAffinityLabel:
    key: sysdig.com/worker-pool-role
    value: cp-kafka
  nodeAffinityMode: preferred  # "preferred" or "required"
```

#### Redis

```YAML
global:
  legacyRedis:
    redisTls:
      nodeaffinityLabel:
        key:
        value:
```

#### Neo4j

```YAML
neo4j:
  podSpec:
    nodeAffinity:
      key:
      value:
```

## Important Notes

- **Mode Support Varies**: Not all workloads allow you to choose the `nodeAffinity` mode (`preferredDuringSchedulingIgnoredDuringExecution` or `requiredDuringSchedulingIgnoredDuringExecution`).

- **Naming Inconsistency**: Beware of the uses of both `nodeaffinityLabel` (lowercase 'a') and `nodeAffinityLabel` (camelCase).
  - `nodeaffinityLabel`: elasticsearch, kafka, zookeeper, helm-renderer, redis
  - `nodeAffinityLabel`: cassandra, postgres-ha (commented)

- **Persistence Across Upgrades**: Starting from 7.6.x, `nodeAffinity` is no longer imported from live clusters in runs 2+ of the installer (reruns or upgrades)
  - Make sure that the `nodeAffinity` entries remain always present in the `values.yaml`
  - Configuration must be explicitly maintained across upgrades

- **Override Hierarchy**: Workload-level `nodeAffinity` settings should override the global `global.nodeaffinityLabel` setting (TBC)

- **Alternative Configuration**: For special cases, `overlays` can also be used, but the `values.yaml` is the preferred, self-documenting way

## Usage Recommendations

1. **For Most Workloads**: Use `global.nodeaffinityLabel` to set node affinity for all services
2. **For Stateful Services**: Consider using workload-specific settings to isolate these services on dedicated node pools
