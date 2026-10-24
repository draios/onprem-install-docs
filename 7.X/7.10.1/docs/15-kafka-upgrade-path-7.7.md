<br />

<!-- Include: ac:toc -->

<br />

## Kafka Inter-Broker Protocol Upgrade Path for 7.7+

This runbook explains how to safely upgrade the Kafka `interBrokerProtocolVersion` when upgrading to Sysdig On-Prem installer version 7.7 or later.

### Overview

Starting from installer version 7.7, the default value for `kafka.interBrokerProtocolVersion` has changed from `3.4` to `3.9`. This setting controls the protocol version that Kafka brokers use to communicate with each other.

> [!IMPORTANT]
> If you are upgrading from installer versions **before 7.2** directly to **7.7+**, you must follow this runbook to avoid broker communication failures. The installer will detect this scenario and prompt you to follow this runbook.

### Background

The `interBrokerProtocolVersion` determines the wire protocol used for communication between Kafka brokers. Kafka requires that all brokers in a cluster be able to understand the protocol version in use. When upgrading:

1. All brokers must be running the newer Kafka binary before the protocol version can be increased
2. Jumping protocol versions without an intermediate upgrade can cause brokers to fail to communicate
3. This is a standard Kafka upgrade requirement to maintain cluster stability

### When This Runbook Applies

**Required** - You must follow this runbook if:
- Upgrading from installer version **before 7.2** directly to **7.7+**
- The installer will block the upgrade and prompt you to follow this runbook

**Not Required** - You may skip this runbook if:
- You are already on installer version >=7.2 and upgrading to 7.7+
- Your Kafka cluster is already running protocol version `3.9`

To check your current inter-broker protocol version:

```shell
kubectl get sts cp-kafka -n sysdigcloud -o jsonpath='{.spec.template.spec.containers[*].env[?(@.name=="KAFKA_INTER_BROKER_PROTOCOL_VERSION")].value}'
```

If the output shows `3.4` or earlier, follow this runbook. If it shows `3.9`, you can proceed with the upgrade normally.

### Prerequisites

Before starting, ensure:

1. You have `kubectl` access to the cluster with appropriate permissions
2. You have access to your installer `values.yaml` configuration
3. You have verified your current `KAFKA_INTER_BROKER_PROTOCOL_VERSION` (see command above)
4. You have a backup of your current configuration

### Step-by-Step Instructions

#### Step 1: Add Override in values.yaml

Before running the installer upgrade, add the following override to your `values.yaml` to pin the protocol version at `3.4`:

```yaml
kafka:
  interBrokerProtocolVersion: "3.4"
```

This ensures the protocol version remains at `3.4` during the initial Kafka binary upgrade.

#### Step 2: Run the Installer Upgrade

Run the installer upgrade to version 7.7 or later with your modified `values.yaml`:

```shell
./installer deploy
```

> [!NOTE]
> The installer will automatically handle the protocol upgrade:
> 1. First, it deploys the new Kafka image with protocol version `3.4`
> 2. After all brokers are running and healthy, it automatically upgrades the protocol to `3.9`
> 3. It waits for all Kafka pods to be ready after the protocol upgrade

You do not need to manually patch the StatefulSet or perform a rollout restart - the installer handles this automatically.

#### Step 3: Verify the Upgrade

After the installer completes, verify the following:

1. **All Kafka pods are running and ready:**

   ```shell
   kubectl get pods -n sysdigcloud | grep cp-kafka
   ```

   All pods should show `1/1 Running`.

2. **Protocol version is updated to 3.9:**

   ```shell
   kubectl get sts cp-kafka -n sysdigcloud -o jsonpath='{.spec.template.spec.containers[*].env[?(@.name=="KAFKA_INTER_BROKER_PROTOCOL_VERSION")].value}'
   ```

   Output should be `3.9`.

3. **Kafka cluster is healthy:**

   ```shell
   kubectl logs cp-kafka-0 -n sysdigcloud | tail -50
   ```

   Check that there are no protocol-related errors in the logs.

4. **StatefulSet shows all replicas ready:**

   ```shell
   kubectl get statefulset -n sysdigcloud | grep cp-kafka
   ```

   Should show `3/3` ready replicas.

#### Step 4: Remove the Override from values.yaml

Once the upgrade is complete and verified, remove the explicit override from your `values.yaml`:

```yaml
# Remove this section - no longer needed as 3.9 is now the default
# kafka:
#   interBrokerProtocolVersion: "3.4"
```

This ensures future upgrades use the default protocol version.

### Troubleshooting

If the installer fails during the protocol upgrade:

1. Check Kafka pod logs for errors:
   ```shell
   kubectl logs cp-kafka-0 -n sysdigcloud
   ```

2. Verify all Kafka pods are running:
   ```shell
   kubectl get pods -n sysdigcloud | grep cp-kafka
   ```

3. If pods are stuck, check for resource constraints or PVC issues

4. Contact Sysdig support if issues persist
