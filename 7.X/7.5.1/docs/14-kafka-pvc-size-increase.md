<!-- Space: IONP -->
<!-- Parent: Installer -->
<!-- Parent: Git Synced Docs -->
<!-- Title: Kafka PVC size increase -->
<!-- Layout: plain -->

<br />

<!-- Include: ac:toc -->

<br />

## Increase Kafka Storage when upgrading to 7.5.0+

As of Sysdig On‑Prem 7.5.0 and later, each Kafka broker must use a larger PersistentVolumeClaim (PVC) by default. This is a mandatory prerequisite for upgrading to 7.5.0 or above. This runbook explains how to ensure and increase Kafka storage to desired PVC size, and can also be used outside of upgrades, for general use cases.

[!IMPORTANT]
**PVC size recommendations:**
* Small: 100Gi
* Medium: 200Gi
* Large: 500Gi

**Exceptions:** If on-prem installations are Secure-only, consider the current size of customer's data before increasing the PVC sizes. As a general rule, at least 40-50% of disk space should be free on all Kafka nodes, before upgrading to 7.5.0 or above.

### Background
- Kafka stores message logs, topic partitions, and replication data on persistent volumes.
- As data ingestion increases, Kafka disk usage can grow and eventually fill up.
- When Kafka disk space is critically low or full, it can impact message processing, data retention, and cluster stability.
- This runbook provides steps to increase PVC size pre-emptively for a Kafka cluster.
- For releases 7.5.0+, the required PVC size per Kafka broker is higher than before; ensure that PVC size is increased based on customer's environment and data size. Runbook uses 200Gi as an example.
- If any of the Kafka nodes' PVC is already full, please reach out to Data Infra team for assistance.

If Kafka disk fills up, you may observe the following symptoms:

```
ERROR [ReplicaManager broker=0] Error processing append operation on partition <topic> (kafka.server.ReplicaManager)
java.io.IOException: No space left on device
```

> [!IMPORTANT]
> Before increasing PVC size, ensure that the underlying storage has sufficient space available, especially for HostPath volumes.

Unfortunately, statefulset PVC templates cannot be patched directly and require additional steps.
Also, there are many factors at play when increasing the size of persistent volume dynamically.

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

Increasing the storage size to 200Gi (required for 7.5.0+) in this case is as follows.

Assuming `sysdigcloud` is the namespace name and kubectl context is set to correct cluster, following are the steps:

* List all Kafka persistent volume claims

```shell
~> kubectl get pvc -n sysdigcloud | grep cp-kafka
data-cp-kafka-0                 Bound    pvc-0e72d14c-5e457e14f34f       100Gi      RWO            gp3            45m
data-cp-kafka-1                 Bound    pvc-61d57410-ea029314bb25       100Gi      RWO            gp3            31m
data-cp-kafka-2                 Bound    pvc-85c367c5-17709d2b77b5       100Gi      RWO            gp3            21m
```

* Start with any one of the PVCs and patch it to increase the storage (e.g., from 100Gi to 200Gi)

```shell
~> kubectl patch pvc data-cp-kafka-0 -n sysdigcloud -p '{"spec":{"resources":{"requests":{"storage":"200Gi"}}}}'
persistentvolumeclaim "data-cp-kafka-0" patched
```

* Wait for a minute for PV to auto-resize. If it doesn't, restart the associated Kafka pod.

```shell
~> kubectl delete pod cp-kafka-0 -n sysdigcloud
pod "cp-kafka-0" deleted

~> kubectl get pvc -n sysdigcloud | grep cp-kafka
NAME                            STATUS   VOLUME                          CAPACITY   ACCESS MODES   STORAGECLASS   AGE
data-cp-kafka-0                 Bound    pvc-0e72d14c-5e457e14f34f       200Gi      RWO            gp3            45m
data-cp-kafka-1                 Bound    pvc-61d57410-ea029314bb25       100Gi      RWO            gp3            31m
data-cp-kafka-2                 Bound    pvc-85c367c5-17709d2b77b5       100Gi      RWO            gp3            21m
```

* Once the restarted pod is Running and `Ready`, repeat the above steps to patch remaining PVCs and restart 1 pod at a time. Final state should be:

```shell
~> kubectl get pvc -n sysdigcloud | grep cp-kafka
NAME                            STATUS   VOLUME                          CAPACITY   ACCESS MODES   STORAGECLASS   AGE
data-cp-kafka-0                 Bound    pvc-0e72d14c-5e457e14f34f       200Gi      RWO            gp3            45m
data-cp-kafka-1                 Bound    pvc-61d57410-ea029314bb25       200Gi      RWO            gp3            31m
data-cp-kafka-2                 Bound    pvc-85c367c5-17709d2b77b5       200Gi      RWO            gp3            21m

~> kubectl get pods -n sysdigcloud | grep cp-kafka
NAME                                                              READY   STATUS      RESTARTS      AGE
cp-kafka-0                                                        1/1     Running     0             132m
cp-kafka-1                                                        1/1     Running     0             121m
cp-kafka-2                                                        1/1     Running     0             22h
```

* Now we need to backport the PVC increase to statefulset. Note the name for Kafka statefulset object

```shell
~> kubectl get statefulset -n sysdigcloud | grep kafka
cp-kafka                    3/3     19h
```

* Export statefulset definition in yaml format and make a backup as well.

```shell
~> kubectl get statefulset cp-kafka -n sysdigcloud -o yaml > kafka-sts.yaml
~> cp kafka-sts.yaml kafka-sts-backup.yaml
```

* Edit the sts yaml file

```shell
~> vi kafka-sts.yaml
```

* Make the following changes to the yaml file:

  * Update the `spec.volumeClaimTemplates.spec.resources.requests.storage` to `200Gi`

    ```yaml
    ...
    volumeClaimTemplates:
    - metadata:
        name: data
      spec:
        accessModes:
        - ReadWriteOnce
        resources:
          requests:
            storage: 200Gi
    ...
    ```

* This next step needs to be done extremely carefully. Please open a second terminal to keep a watch on Kafka pods. We're deleting the
  Kafka statefulset without deleting the pods so that the edited yaml can be applied. `--cascade=orphan` is mandatory and very important here.
  There should be no restarts on Kafka pods.

```shell
~> kubectl delete statefulset cp-kafka -n sysdigcloud --cascade=orphan
statefulset.apps "cp-kafka" deleted
```

* Apply the edited `kafka-sts.yaml` with changes to PVC template.
  Kafka pods may start rollout automatically as we've changed spec, but they should be `Ready` quickly.

```shell
~> kubectl apply -f kafka-sts.yaml -n sysdigcloud
statefulset.apps/cp-kafka created
```

* [Verify](#verification)


### Volumes use hostpath or storageclass does not support resizing

Increasing the storage size to 200Gi (required for 7.5.0+) in this case requires statefulset patching beforehand. Also, we need to check for:

* IF the volumes use HostPath, verify that the host filesystem has enough space available before increasing PV size. Check with `df -h` on each host node to ensure sufficient headroom.
* IF the volumes are dynamically provisioned but do not allow resizing (example: gp2 storageclass)

Once confirmed, we can proceed.

Assuming `sysdigcloud` is the namespace name and kubectl context is set to correct cluster, following are the steps:

* Note the name for Kafka statefulset object

```shell
~> kubectl get statefulset -n sysdigcloud | grep cp-kafka
cp-kafka                    3/3     19h
```

* Export statefulset definition in yaml format and make a backup as well.

```shell
~> kubectl get statefulset cp-kafka -n sysdigcloud -o yaml > kafka-sts.yaml
~> cp kafka-sts.yaml kafka-sts-backup.yaml
```

* Edit the sts yaml file

```shell
~> vi kafka-sts.yaml
```

* Make the following changes to the yaml file:

  * Update the `spec.volumeClaimTemplates.spec.resources.requests.storage` to `200Gi`

    ```yaml
    ...
    spec:
      volumeClaimTemplates:
      - metadata:
          name: data
        spec:
          resources:
            requests:
              storage: 200Gi
    ...
    ```

* This next step needs to be done extremely carefully. Please open a second terminal to keep a watch on Kafka pods. We're deleting the
Kafka statefulset without deleting the pods so that the edited yaml can be applied. `--cascade=orphan` is mandatory and very important here.
There should be no restarts on Kafka pods.

```shell
~> kubectl delete statefulset cp-kafka -n sysdigcloud --cascade=orphan
statefulset.apps "cp-kafka" deleted
```

* Apply the edited `kafka-sts.yaml` with changes to PVC template.
Kafka pods will not restart automatically.

```shell
~> kubectl apply -f kafka-sts.yaml -n sysdigcloud
statefulset.apps/cp-kafka created
```

Please follow the further steps according to cluster's volume setup:
* [HostPath](#hostpath-volumes)
* [Dynamic Non-scalable](#dynamic-non-scalable-volumes)

#### HostPath volumes

> [!IMPORTANT]
> Before proceeding, verify that the host filesystem has sufficient space. SSH to each node hosting Kafka pods and run `df -h` to check available space on the filesystem where the HostPath is located. Ensure there is enough space beyond the target PVC size to avoid disk full issues.

* List all PersistentVolumes and watch for those bound to Kafka PersistentVolumeClaims.

```shell
~> kubectl get pv | grep data-cp-kafka

NAME                            CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                                       STORAGECLASS   REASON   AGE
pvc-0e72d14c-5e457e14f34f       100Gi      RWO            Retain           Bound    sysdigcloud/data-cp-kafka-0                 local-disk              21h
pvc-61d57410-ea029314bb25       100Gi      RWO            Retain           Bound    sysdigcloud/data-cp-kafka-1                 local-disk              21h
pvc-85c367c5-17709d2b77b5       100Gi      RWO            Retain           Bound    sysdigcloud/data-cp-kafka-2                 local-disk              21h
```

* List all PersistentVolumeClaims for Kafka:

```shell
~> kubectl get pvc -n sysdigcloud | grep data-cp-kafka
NAME                            STATUS   VOLUME                          CAPACITY   ACCESS MODES   STORAGECLASS   AGE
data-cp-kafka-0                 Bound    pvc-0e72d14c-5e457e14f34f       100Gi      RWO            local-disk     45m
data-cp-kafka-1                 Bound    pvc-61d57410-ea029314bb25       100Gi      RWO            local-disk     31m
data-cp-kafka-2                 Bound    pvc-85c367c5-17709d2b77b5       100Gi      RWO            local-disk     21m
```

* Pick a pod, say cp-kafka-0. Delete its PVC. PVC will stay in Terminating State until Pod is killed, so we add `&` to the command:

```shell
~> kubectl delete pvc data-cp-kafka-0 -n sysdigcloud &
persistentvolumeclaim "data-cp-kafka-0" deleted
```

* Delete the pod (cp-kafka-0 in this case). Wait for the PVC to get deleted. If a new PVC is not created automatically, delete the pod a second time.
The PVC will be in `Pending` state because there's no HostPath volume with the new size. We need to make adjustments now.

```shell
~> kubectl delete pod cp-kafka-0 -n sysdigcloud
pod "cp-kafka-0" deleted

~> kubectl get pvc -n sysdigcloud | grep data-cp-kafka
NAME                            STATUS   VOLUME                          CAPACITY   ACCESS MODES   STORAGECLASS   AGE
data-cp-kafka-0                 Pending                                  0          RWO                           2m
data-cp-kafka-1                 Bound    pvc-61d57410-ea029314bb25       100Gi      RWO            local-disk     31m
data-cp-kafka-2                 Bound    pvc-85c367c5-17709d2b77b5       100Gi      RWO            local-disk     21m
```

* Pick the PV from the first step that was `Bound` to the deleted PVC (it will be in `Released` state). Edit the PV to increase the size and remove claimRef.

```shell
~> kubectl edit pv pvc-0e72d14c-5e457e14f34f
persistentvolume/pvc-0e72d14c-5e457e14f34f edited
```

* Make the following changes to the PV yaml file:
  * Update the `spec.capacity.storage` to `200Gi`
  * Delete the entire section for `spec.claimRef`

    **Before edit**

    ```yaml
    ...
    spec:
      accessModes:
      - ReadWriteOnce
      capacity:
        storage: 100Gi
      claimRef:
        apiVersion: v1
        kind: PersistentVolumeClaim
        name: data-cp-kafka-0
        namespace: sysdigcloud
        resourceVersion: "328616"
        uid: a88c55fa-0f38-4bf1-b677-e472c8297af3
      hostPath:
        path: <existing-path>
        type: DirectoryOrCreate
    ...
    ```

    **After edit**

    ```yaml
    ...
    spec:
      accessModes:
      - ReadWriteOnce
      capacity:
        storage: 200Gi
      hostPath:
        path: <existing-path>
        type: DirectoryOrCreate
    ...
    ```

* If the newly created cp-kafka-0 PVC is in `Bound` state we can skip this next step. Else, we need to edit the PVC to specify the VolumeName.

```shell
~> kubectl edit pvc data-cp-kafka-0 -n sysdigcloud
persistentvolumeclaim/data-cp-kafka-0 edited
```

* Make the following changes to the PVC yaml file:
  * Add `spec.volumeName` with value as the name of PersistentVolume (here: pvc-0e72d14c-5e457e14f34f) that we patched in previous step after `spec.volumeMode`
  * Delete the section for `status`

    **Before edit**

    ```yaml
    ...
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 200Gi
      storageClassName: local-disk
      volumeMode: Filesystem
    status:
      phase: Pending
    ```

    **After edit**

    ```yaml
    ...
    spec:
      accessModes:
      - ReadWriteOnce
      resources:
        requests:
          storage: 200Gi
      storageClassName: local-disk
      volumeMode: Filesystem
      volumeName: pvc-0e72d14c-5e457e14f34f
    ```

* The PVC should now be in `Bound` state and Pod should be running. Wait for Kafka pod to be `Ready`. This will take time because new volume will need to stream data from existing pods.

* Once the pod is `Ready`, repeat the steps from deleting PVC and pod for remaining 2 statefulset pods.

```shell
~>  kubectl get pvc -n sysdigcloud | grep data-cp-kafka
NAME                            STATUS   VOLUME                          CAPACITY   ACCESS MODES   STORAGECLASS   AGE
data-cp-kafka-0                 Bound    pvc-0e72d14c-5e457e14f34f       200Gi      RWO            local-disk     10m
data-cp-kafka-1                 Bound    pvc-61d57410-ea029314bb25       200Gi      RWO            local-disk     5m
data-cp-kafka-2                 Bound    pvc-85c367c5-17709d2b77b5       200Gi      RWO            local-disk     2m
```

* [Verify](#verification)

#### Dynamic Non-Scalable Volumes

* List all PersistentVolumes for Kafka:

```shell
~> kubectl get pv | grep data-cp-kafka
NAME                              CAPACITY   ACCESS MODES   RECLAIM POLICY   STATUS   CLAIM                                       STORAGECLASS   REASON   AGE
pvc-95413869-81de2bc30b5f         100Gi      RWO            Delete           Bound    sysdigcloud/data-cp-kafka-2                 gp2                     48m
pvc-8d381527-fcb3689f7588         100Gi      RWO            Delete           Bound    sysdigcloud/data-cp-kafka-1                 gp2                     48m
pvc-266e6b46-cb235a99b805         100Gi      RWO            Delete           Bound    sysdigcloud/data-cp-kafka-0                 gp2                     48m
```

* List all PersistentVolumeClaims for Kafka:

```shell
~> kubectl get pvc -n sysdigcloud | grep data-cp-kafka
NAME                            STATUS   VOLUME                      CAPACITY   ACCESS MODES   STORAGECLASS   AGE
data-cp-kafka-0                 Bound    pvc-95413869-81de2bc30b5f   100Gi      RWO            gp2            58m
data-cp-kafka-1                 Bound    pvc-8d381527-fcb3689f7588   100Gi      RWO            gp2            58m
data-cp-kafka-2                 Bound    pvc-266e6b46-cb235a99b805   100Gi      RWO            gp2            58m
```

* Pick a pod, say cp-kafka-0. Delete the PVC and associated PV. Both will stay in Terminating State until Pod is killed, so we add `&` to the command:

```shell
~> kubectl delete pvc data-cp-kafka-0 -n sysdigcloud &
persistentvolumeclaim "data-cp-kafka-0" deleted
~> kubectl delete pv pvc-95413869-81de2bc30b5f &
persistentvolume "pvc-95413869-81de2bc30b5f" deleted
```

* Delete the pod (cp-kafka-0 in this case). Wait for the PVC and PV to get deleted. If a new PVC is not created automatically, delete the pod a second time.
  Cluster will dynamically provision a volume with the new size, and the PVC will be Bound.

```shell
~> kubectl delete pod cp-kafka-0 -n sysdigcloud
pod "cp-kafka-0" deleted

~> kubectl get pvc -n sysdigcloud | grep data-cp-kafka
NAME                            STATUS   VOLUME                      CAPACITY   ACCESS MODES   STORAGECLASS   AGE
data-cp-kafka-0                 Bound    pvc-NEWUID-NEWUID           200Gi      RWO            gp2            1m
data-cp-kafka-1                 Bound    pvc-8d381527-fcb3689f7588   100Gi      RWO            gp2            58m
data-cp-kafka-2                 Bound    pvc-266e6b46-cb235a99b805   100Gi      RWO            gp2            58m
```

* Once the above steps are successful, wait for Kafka pod to be `Ready`. This will take time because new volume will need to stream data from existing pods.

* Proceed to repeat the steps of deleting PVC, PV and Pod for remaining 2 Kafka pods.
  Perform operation for 1 pod at a time and wait for each pod to report `Ready`, before moving on to the next one.

* If the PVC or Pod is stuck in `Pending` state, do not move ahead and investigate the root-cause. Depending on the Events/Errors, we may
  need to investigate volume provisioner to understand why new volume was not automatically created.

* [Verify](#verification)

### Verification

* Verify the following:
  * All pods are `Ready`: `kubectl get pods -n sysdigcloud | grep cp-kafka`
  * Statefulset is created and shows `3` Ready replicas: `kubectl get statefulset -n sysdigcloud | grep cp-kafka`
  * Statefulset spec shows volumeClaimTemplate storage size as updated size (200Gi for 7.5.0+): `kubectl get statefulset cp-kafka -n sysdigcloud -o yaml`
  * All PVCs are `Bound` and show 200Gi capacity (for 7.5.0+): `kubectl get pvc -n sysdigcloud | grep data-cp-kafka`
  * Kafka cluster is healthy and in-sync: Check that all brokers are online and under-replicated partitions count is zero
  * Kafka Pod logs do not show any disk space errors or critical issues
