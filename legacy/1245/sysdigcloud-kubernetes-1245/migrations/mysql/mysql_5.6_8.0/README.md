# Mysql upgrade to 8.0 HA/Statefulset (BETA)

This script upgrades a live cluster with no metric data loss, but has a potential of the following data loss:
1. Users or teams created or modified during the upgrade will be missing in the new database

This upgrade should be treated as planned maintenance during the fail-over.

## Prerequisites

1. Storage Class Name for PVC
2. Kubernetes cluster v1.9+
3. Namespace for the existing install of Sysdig-Onprem
4. Kubectl executable in your path
5. Kubectl context config for the cluster
6. Sysdig-Onprem version v1051+ running
7. Mysql 5.6 deployment running

After all of the above are met, then upgrading mysql to 8.0/HA is possible.

## Upgrade

```bash
pip install -r requirements.txt

python ./mysql_upgrade_5.6_to_8.0.py \
  --deployment-yaml <project_root>/datastores/as_kubernetes_pods/manifests/mysql/mysql-deployment.yaml \
  --router-yaml <project_root>/datastores/as_kubernetes_pods/manifests/mysql/mysql-router-statefulset.yaml \
  --cluster-yaml <project_root>/datastores/as_kubernetes_pods/manifests/mysql/mysql-cluster-statefulset.yaml \
  --upgrade-yaml <project_root>/migrations/mysql_5.6_8.0/mysql_upgrade.yaml \
  --namespace <namespace of the existing install> \
  --kube-context <kubernetes context value> \
  --storageclass-name <your storage class name> \
  --dry-run
```

Remove the `--dry-run` for the actual run.

### Notes

The old mysql database is left running behind a different service name in the cluster. Once the new 
HA database is stable, the old database and service can be deleted.

```bash
kubectl --context <context> -n sysdigcloud delete service sysdigcloud-mysql-old
kubectl --context <context> -n sysdigcloud delete deployment sysdigcloud-mysql
```

## Rollback

Point the mysql service at the original mysql deployment
```bash
./rollback.py \
  --deployment-yaml ../../datastores/as_kubernetes_pods/manifests/mysql/mysql-deployment.yaml \
  --namespace <namespace of the existing install> \
  --kube-context <kubernetes context value>
```
