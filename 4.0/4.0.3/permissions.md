# Permissions

## General
* CRU on the sysdig namespace
* CRU on StorageClass (only Read is required if the storageClass already exists)
* CRUD on Secrets/ServiceAccount/ConfigMap/Deployment/CronJob/Job/StatefulSet/Service/DaemonSet in the sysdig namespace.
* CRUD on role/rolebinding in sysdig namespace (if sysdig ingress controller is deployed)
* CRU on the ingress-controller(this is the name of the object) ClusterRole/ClusterRoleBinding (if sysdig ingress controller is deployed)
* Get Nodes (for validations).

## MultiAZ enabled
* CRU on the node-labels-to-files(this is the name of the object) ClusterRole/ClusterRoleBinding (for multi-AZ deployments)

## HostPath
* CRU on PV
* CRU on PVC in sysdig namespace

## Openshift
* CRUD on route in the sysdig namespace
* CRUD on openshift SCC in the sysdig namespace

## Network policies enabled
* CRUD on networkpolicies in sysdig namespace (if networkpolicies are enabled, this is an alpha feature customers should not enable it)