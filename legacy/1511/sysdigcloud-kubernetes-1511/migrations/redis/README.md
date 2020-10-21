# Redis HA Migration (BETA)

Upgrading Redis to the HA/Statefulset requires a small amount of planned
 downtime and will incur a small amount of metric data loss during the outage. 
 The gain is that now Redis will be running in a mode where Redis will survive
 a master Redis pod failure.

### Prerequisites

1. Storage Class Name for PVC
2. Kubernetes cluster v1.9+
3. Namespace for the existing install of Sysdig-Onprem
4. Kubectl executable in your path
5. Kubectl context config for the cluster
6. Sysdig-Onprem version v1084+ running
7. Redis single replica deployment running

After all of the above are met, then upgrading Redis to 3.2/HA is possible.

## Steps to upgrade

These commands assume that you are at the root of this repo

1. Checkout latest release
    ```bash
    git checkout <release tag>
    ```

2. Update the ConfigMap and edit both the sections, Redis and Sysdig Onprem to enable Redis HA. 
    ```bash
    kubectl --context <context> -n <namespace> edit configmap sysdigcloud-config
    ```
    OR edit the yaml and reapply
    ```bash
    kubectl --context <context> -n <namespace> apply --force -f sysdigcloud/config.yaml
    ```
2. Update StorageClassName in the Redis yamls to a valid value
    ```bash
    datastores/as_kubernetes_pods/manifests/redis/redis-primary-statefulset.yaml
    datastores/as_kubernetes_pods/manifests/redis/redis-secondary-statefulset.yaml
    ```
3. Start the new HA Redis
    ```bash
    kubectl --context <context> -n <namespace> create -f <project_root>/datastores/as_kubernetes_pods/manifests/redis/redis-primary-statefulset.yaml
    kubectl --context <context> -n <namespace> create -f <project_root>/datastores/as_kubernetes_pods/manifests/redis/redis-primary-svc-statefulset.yaml
    kubectl --context <context> -n <namespace> create -f <project_root>/datastores/as_kubernetes_pods/manifests/redis/redis-secondary-statefulset.yaml
    kubectl --context <context> -n <namespace> create -f <project_root>/datastores/as_kubernetes_pods/manifests/redis/redis-secondary-svc-statefulset.yaml
    kubectl --context <context> -n <namespace> create -f <project_root>/datastores/as_kubernetes_pods/manifests/redis/redis-sentinel-statefulset.yaml
    kubectl --context <context> -n <namespace> create -f <project_root>/datastores/as_kubernetes_pods/manifests/redis/redis-sentinel-svc-statefulset.yaml
    ```
4. delete old redis pods
    ```bash
    kubectl --context <context> -n <namespace> delete svc sysdigcloud-redis
    kubectl --context <context> -n <namespace> delete deployment sysdigcloud-redis
    ```
5. restart all sysdig jvms