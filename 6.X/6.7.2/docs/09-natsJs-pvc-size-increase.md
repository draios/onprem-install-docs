<!-- Space: TOOLS -->
<!-- Parent: Installer -->
<!-- Title: NatsJs PVC size increase for 6.7.0 release-->
<!-- Layout: plain -->

<br />

<!-- Include: ac:toc -->

<br />

## Increase persistent storage for NATS JetStream statefulset to 100Gi before upgrading on-prem to release 6.7.0

### Background
- NatsJs publishers allocate fixed number of bytes at the time of stream creation and cannot be modified later.
- As the number of publishers (services using NATS) grows, the storage requirement for NATS also increases.
- Due to fixed size of streams, the storage requirement is the same across Small, Medium or Large clusters.
- There are future improvements scoped towards configuring stream sizes based on cluster size, but that is not possible at the moment.
- We're bumping the storage to 100Gi to leave headroom for any new services in future upgrades while we work on improving stream allocation.

If an upgrade to `6.7` is performed without following the steps to increase the disk for NATS statefulset, it may lead to following error on secure services:

```
Caused by: org.springframework.beans.BeanInstantiationException: Failed to instantiate [io.nats.client.Connection]: Factory method 'natsConnection' threw exception; nested exception is io.nats.client.JetStreamApiException: no suitable peers for placement, insufficient storage [10005]
```

Unfortunately, statefulset PVC templates cannot be patched directly and require additional steps. 
Also, there are many factors at play when  increasing the size of persistent volume dynamically.

To check if storageclass supports volume expansion, run the following command and look for `ALLOWVOLUMEEXPANSION`:
```shell
~> kubectl get storageclass -o wide
NAME                      PROVISIONER             RECLAIMPOLICY   VOLUMEBINDINGMODE      ALLOWVOLUMEEXPANSION   AGE
default                   kubernetes.io/aws-ebs   Delete          Immediate              false                  22h
gp2                       kubernetes.io/aws-ebs   Delete          Immediate              false                  22h
kops-csi-1-21 (default)   ebs.csi.aws.com         Delete          WaitForFirstConsumer   true                   22h
```

* If PVC uses storageclass with `ALLOWVOLUMEEXPANSION` set to True: [Dynamic](#volumes-are-dynamically-provisioned-and-storageclass-supports-resizing)
* If PVC uses storageclass with `ALLOWVOLUMEEXPANSION` set to False or uses `HostPath`: [Static or Hostpath](#volumes-use-hostpath-or-storageclass-does-not-support-resizing)

### Volumes are dynamically provisioned and storageclass supports resizing

Increasing the storage size in this case is as follows.

Assuming `sysdigcloud` is the namespace name and kubectl context is set to correct cluster, following are the steps:

* List all nats persistent volume claims
```shell
~> kubectl get pvc -n sysdigcloud | grep nats-js
nats-js-pvc-nats-0                 Bound    nats-js-pvc-nats-0                 50Gi       RWO            local-disk     74m
nats-js-pvc-nats-1                 Bound    nats-js-pvc-nats-1                 50Gi       RWO            local-disk     74m
nats-js-pvc-nats-2                 Bound    nats-js-pvc-nats-2                 50Gi       RWO            local-disk     74m
```
* Start with any one of the PVCs and patch it to increase the storage to 100Gi
```shell
~> kubectl patch pvc nats-js-pvc-nats-0 -n sysdigcloud -p '{"spec":{"resources":{"requests":{"storage":"100Gi"}}}}'
persistentvolumeclaim "nats-js-pvc-nats-0" patched
```

* Wait for a minute for PV to auto-resize. If it doesn't, restart the associated nats pod.
```shell
~> kubectl delete pod nats-0 -n sysdigcloud 
pod "nats-0" deleted

~> kubectl get pvc -n sysdigcloud | grep nats-js
NAME                               STATUS   VOLUME                             CAPACITY   ACCESS MODES   STORAGECLASS   AGE
nats-js-pvc-nats-0                 Bound    nats-js-pvc-nats-0                 100Gi      RWO            default        45m
nats-js-pvc-nats-1                 Bound    nats-js-pvc-nats-1                 50Gi       RWO            default        31m
nats-js-pvc-nats-2                 Bound    nats-js-pvc-nats-2                 50Gi       RWO            default        21m
```

* Once the restarted pod is Running and `Ready 3/3`, repeat the above steps to patch remaining PVCs and restart 1 pod at a time. Final state should be:
```shell
~> kubectl get pvc -n sysdigcloud | grep nats-js
NAME                               STATUS   VOLUME                             CAPACITY   ACCESS MODES   STORAGECLASS   AGE
nats-js-pvc-nats-0                 Bound    nats-js-pvc-nats-0                 100Gi      RWO            default        45m
nats-js-pvc-nats-1                 Bound    nats-js-pvc-nats-1                 100Gi      RWO            default        31m
nats-js-pvc-nats-2                 Bound    nats-js-pvc-nats-2                 100Gi      RWO            default        21m

~> kubectl get pods -n sysdigcloud | grep nats
NAME                                                              READY   STATUS      RESTARTS      AGE
nats-0                                                            3/3     Running     0             132m
nats-1                                                            3/3     Running     0             121m
nats-2                                                            3/3     Running     0             22h
```

* Now we need to backport the PVC increase to statefulset. Note the name for nats statefulset object
```shell
~> kubectl get statefulset -n sysdigcloud | grep nats
nats                        3/3     19h
```

* Export statefulset definition in yaml format and make a backup as well.
```shell
~> kubectl get statefulset nats -n sysdigcloud -o yaml > nats-sts.yaml
~> cp nats-sts.yaml nats-sts-backup.yaml
```
* Edit the sts yaml file
```shell
~> vi nats-sts.yaml
```
* Make the following changes to the yaml file:
    1. Update the `spec.volumeClaimTemplates.spec.resources.requests.storage` to `100Gi`
  ```yaml
  ...
  volumeClaimTemplates:
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 100Gi
  ...
    ```
* This next step needs to be done extremely carefully. Please open a second terminal to keep a watch on nats pods. We're deleting the
  nats statefulset without deleting the pod so that the edited yaml can be applied. `--cascade=orphan` is mandatory and very important here.
  There should be no restarts on nats pods.
```shell
~> kubectl delete statefulset nats -n sysdigcloud --cascade=orphan
statefulset.apps "nats" deleted
```
* Apply the edited `nats-sts.yaml` with changes to PVC template.
  Nats pods may start rollout automatically as we've changed spec, but they should be `Ready 3/3` quickly.
```shell
~> kubectl apply -f nats-sts.yaml -n sysdigcloud
statefulset.apps/nats created
```
* [Verify](#verification)


### Volumes use hostpath or storageclass does not support resizing

Increasing the storage size in this case requires some statefulset patching beforehand. Also, we need to check for:

* IF the volumes use HostPath, can they be expanded to 100Gi i.e., is there enough headroom on the host?
* IF the volumes are dynamically provisioned but do not allow resizing (example: gp2 storageclass)

Once confirmed, we can proceed.

Assuming `sysdigcloud` is the namespace name and kubectl context is set to correct cluster, following are the steps:

* Note the name for nats statefulset object
```shell
~> kubectl get statefulset -n sysdigcloud | grep nats
nats                        3/3     19h
```

* Export statefulset definition in yaml format and make a backup as well.
```shell
~> kubectl get statefulset nats -n sysdigcloud -o yaml > nats-sts.yaml
~> cp nats-sts.yaml nats-sts-backup.yaml
```

* Edit the sts yaml file
```shell
~> vi nats-sts.yaml
```

* Make the following changes to the yaml file:
  1. Update the `spec.volumeClaimTemplates.spec.resources.requests.storage` to `100Gi`
  ```yaml
  spec:
    volumeClaimTemplates:
      spec:
        resources:
          requests:
            storage: 100Gi
    ```
* This next step needs to be done extremely carefully. Please open a second terminal to keep a watch on nats pods. We're deleting the
nats statefulset without deleting the pod so that the edited yaml can be applied. `--cascade=orphan` is mandatory and very important here.
There should be no restarts on nats pods.
```shell
~> kubectl delete statefulset nats -n sysdigcloud --cascade=orphan
statefulset.apps "nats" deleted
```

* Apply the edited `nats-sts.yaml` with changes to PVC template.
Nats pods will not restart automatically.
```shell
~> kubectl apply -f nats-sts.yaml -n sysdigcloud
statefulset.apps/nats created
```

Please follow the further steps according to cluster's volume setup:
* [HostPath](#hostpath-volumes)
* [Dynamic Non-scalable](#dynamic-non-scalable-volumes)

#### HostPath volumes

* List all PersistentVolumes and watch for those bound to Nats PersistentVolumeClaims.
```shell
~> kubectl get pv | grep nats-js

NAME                               CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                                          STORAGECLASS   REASON   AGE
nats-js-pvc-nats-0                 50Gi       RWO            Retain           Bound    sysdigcloud/nats-js-pvc-nats-0                 local-disk              21h
nats-js-pvc-nats-1                 50Gi       RWO            Retain           Bound    sysdigcloud/nats-js-pvc-nats-1                 local-disk              21h
nats-js-pvc-nats-2                 50Gi       RWO            Retain           Bound    sysdigcloud/nats-js-pvc-nats-2                 local-disk              21h
```

* List all PersistentVolumeClaims for nats:
```shell
~> kubectl get pvc -n sysdigcloud | grep nats-js
NAME                               STATUS   VOLUME                             CAPACITY   ACCESS MODES   STORAGECLASS   AGE
nats-js-pvc-nats-0                 Bound    nats-js-pvc-nats-0                 50Gi       RWO            local-disk     45m
nats-js-pvc-nats-1                 Bound    nats-js-pvc-nats-1                 50Gi       RWO            local-disk     31m
nats-js-pvc-nats-2                 Bound    nats-js-pvc-nats-2                 50Gi       RWO            local-disk     21m
```

* Pick a pod, say nats-0. Delete its PVC. PVC will stay in Terminating State until Pod is killed, so we add `&` to the command:
```shell
~> kubectl delete pvc nats-js-pvc-nats-0 -n sysdigcloud &
persistentvolumeclaim "nats-js-pvc-nats-0" deleted
``` 

* Delete the pod (nats-0 in this case). Wait for the PVC to get deleted. If a new PVC is not created automatically, delete the pod a second time.
The PVC will be in `Pending` state because there's no HostPath volume with 100Gi size. We need to make adjustments now.
```shell
~> kubectl delete pod nats-0 -n sysdigcloud 
pod "nats-0" deleted

~> kubectl get pvc -n sysdigcloud | grep nats-js
NAME                               STATUS   VOLUME                             CAPACITY   ACCESS MODES   STORAGECLASS   AGE
nats-js-pvc-nats-0                 Pending                                     0          RWO                           2m
nats-js-pvc-nats-1                 Bound    nats-js-pvc-nats-1                 50Gi       RWO            default        31m
nats-js-pvc-nats-2                 Bound    nats-js-pvc-nats-2                 50Gi       RWO            default        21m
```

* Pick the PV from the first step that was `Bound` to the deleted PVC (it will be in `Released` state). Edit the PV to increase the size and remove claimRef.
```shell
~> kubectl edit pv nats-js-pvc-nats-0
persistentvolume/nats-js-pvc-nats-0 edited
```
* Make the following changes to the PV yaml file:
  1. Update the `spec.capacity.storage` to `100Gi`
  2. Delete the entire section for `spec.claimRef`

  *Before edit*  
  ```yaml
  ...
  spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 50Gi
  claimRef:
    apiVersion: v1
    kind: PersistentVolumeClaim
    name: nats-js-pvc-nats-0
    namespace: sysdigcloud
    resourceVersion: "328616"
    uid: a88c55fa-0f38-4bf1-b677-e472c8297af3
  hostPath:
    path: /var/lib/nats-js-1
    type: DirectoryOrCreate
  ...
  ```
  *After edit*
  ```yaml
  ...
  spec:
  accessModes:
  - ReadWriteOnce
  capacity:
    storage: 100Gi
  hostPath:
    path: /var/lib/nats-js-1
    type: DirectoryOrCreate
  ...
  ```

* If the newly created nats-0 PVC is in `Bound` state we can skip this next step. Else, we need to edit the PVC to specify the VolumeName.
```shell
~> kubectl edit pvc nats-js-pvc-nats-0 -n sysdigcloud
persistentvolumeclaim/nats-js-pvc-nats-0 edited
```
* Make the following changes to the PVC yaml file:
  1. Add `spec.volumeName` with value as the name of PersistentVolume (here: nats-js-pvc-nats-0) that we patched in previous step after `spec.VolumeMode`
  2. Delete the section for `status`
     *Before edit*
  ```yaml
  ...
  spec:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 100Gi
    storageClassName: local-disk
    volumeMode: Filesystem
  status:
    phase: Pending
  ```
  *After edit*
  ```yaml
  ...
  spec:
    accessModes:
    - ReadWriteOnce
    resources:
      requests:
        storage: 100Gi
    storageClassName: local-disk
    volumeMode: Filesystem
    volumeName: nats-js-pvc-nats-0
  ```
* The PVC should now be in `Bound` state and Pod should be running. Once the pod is `Ready 3/3`, repeat the steps from deleting PVC and pod for remaining 2 statefulset pods.
```shell
~>  kubectl get pvc -n sysdigcloud | grep nats-js
NAME                               STATUS   VOLUME                             CAPACITY   ACCESS MODES   STORAGECLASS   AGE
nats-js-pvc-nats-0                 Bound    nats-js-pvc-nats-0                 100Gi      RWO            local-disk     85m
nats-js-pvc-nats-1                 Bound    nats-js-pvc-nats-1                 50Gi       RWO            local-disk     21h
nats-js-pvc-nats-2                 Bound    nats-js-pvc-nats-2                 50Gi       RWO            local-disk     21h
```
* [Verify](#verification)

#### Dynamic Non-Scalable Volumes

* List all PersistentVolumes for nats:
```shell
~> kubectl get pv | grep nats-js
NAME                                       CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                                          STORAGECLASS   REASON   AGE
pvc-266e6b46-dc07-45aa-b52f-cb235a99b805   50Gi       RWO            Delete           Bound    sysdigcloud/nats-js-pvc-nats-2                 gp2                     48m
pvc-8d381527-dee5-438e-b307-fcb3689f7588   50Gi       RWO            Delete           Bound    sysdigcloud/nats-js-pvc-nats-1                 gp2                     48m
pvc-95413869-b940-4435-affc-81de2bc30b5f   50Gi       RWO            Delete           Bound    sysdigcloud/nats-js-pvc-nats-0                 gp2                     48m
```

* List all PersistentVolumeClaims for nats:
```shell
~> kubectl get pvc -n sysdigcloud | grep nats-js
NAME                               STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
nats-js-pvc-nats-0                 Bound    pvc-95413869-b940-4435-affc-81de2bc30b5f   50Gi       RWO            gp2            58m
nats-js-pvc-nats-1                 Bound    pvc-8d381527-dee5-438e-b307-fcb3689f7588   50Gi       RWO            gp2            58m
nats-js-pvc-nats-2                 Bound    pvc-266e6b46-dc07-45aa-b52f-cb235a99b805   50Gi       RWO            gp2            58m
```

* Pick a pod, say nats-0. Delete the PVC and associated PV. Both will stay in Terminating State until Pod is killed, so we add `&` to the command:
```shell
~> kubectl delete pvc nats-js-pvc-nats-0 -n sysdigcloud &
persistentvolumeclaim "nats-js-pvc-nats-0" deleted
~> kubectl delete pv pvc-95413869-b940-4435-affc-81de2bc30b5f -n sysdigcloud &
persistentvolume "pvc-95413869-b940-4435-affc-81de2bc30b5f" deleted  
```

* Delete the pod (nats-0 in this case). Wait for the PVC and PV to get deleted. If a new PVC is not created automatically, delete the pod a second time.
  Cluster will dynamically provision a 100Gi volume, and the PVC will be Bound.
```shell
~> kubectl delete pod nats-0 -n sysdigcloud 
pod "nats-0" deleted

~> kubectl get pvc -n sysdigcloud | grep nats-js
NAME                               STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
nats-js-pvc-nats-0                 Bound    pvc-95413869-b940-4435-affc-81de2bc30b5f   100Gi      RWO            gp2            5m
nats-js-pvc-nats-1                 Bound    pvc-8d381527-dee5-438e-b307-fcb3689f7588   70Gi       RWO            gp2            58m
nats-js-pvc-nats-2                 Bound    pvc-266e6b46-dc07-45aa-b52f-cb235a99b805   70Gi       RWO            gp2            58m
```
* Once the above steps are successful, proceed to repeat the steps of deleting PVC, PV and Pod for remaining 2 Nats pods.
  Perform operation for 1 pod at a time and wait for each pod to report `Ready 3/3`, before moving on to the next one.
* If the PVC or Pod is stuck in `Pending` state, do not move ahead and investigate the root-cause. Depending on the Events/Errors, we may
  need to investigate volume provisioner to understand why new volume was not automatically created.

* [Verify](#verification)

### Verification

* Verify the following:
  1. All pods are `Ready 3/3`: `kubectl get pods -n sysdigcloud | grep nats`
  2. Statefulset is created and shows `3` Ready replicas: `kubectl get statefulset -n sysdigcloud | grep nats`
  3. Statefulset spec shows volumeClaimTemplate storage size as 100Gi: `kubectl get statefulset nats -n sysdigcloud -o yaml`
  4. All PVCs are `Bound` and showing up as `100Gi` size: `kubectl get pvc -n sysdigcloud`
  5. NATS Pod logs do not show any errors (Errors like `no route to host` or `connection refused` are expected during pod restarts).