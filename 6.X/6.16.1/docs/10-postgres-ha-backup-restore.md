<!-- Space: IONP -->
<!-- Parent: Installer -->
<!-- Parent: Git Synced Docs -->
<!-- Title: Postgres HA Backup Restore Runbook -->
<!-- Layout: plain -->

<br />

<!-- Include: ac:toc -->

<br />

## Postgres HA Backup - Restore Runbook

The purpose of this runbook is to instruct customers on how to use the backup and restore functionalities when Postgres HA is used in on-prem deployment.

## Use Cases

The tool can be leveraged in a few scenarios.

* Postgres cannot start, for example, due to corrupted data. Databases need to be restored in a new Postgres HA instance.
* Kubernetes cluster is not fully functional. Customer needs to recreate all Postgres databases in a new cluster for fast recovery.

## Backup

The backup component is intended to be deployed by using Installer in the cluster so it creates periodical backups to S3 or S3 compatible object storage. Later on, the most recent copy will be used to restore the databases.

### Requirements

A S3 or S3 compatible bucket is provisioned. The customer has an AWS Access Key ID and AWS Secret Access Key with proper privileges to use the bucket.

### Settings

| Name | Value | Example |
| :--- | :---  | :---    |
| `sysdig.postgresql.aws.logicalBackupS3Bucket` | S3 bucket name | example-bucket |
| `sysdig.postgresql.aws.logicalBackupS3Region` | Region where S3 bucket resides | us-east-1 |
| `sysdig.postgresql.aws.logicalBackupPath` | Path in which the backup files are stored | demo-path |
| `sysdig.postgresql.aws.logicalBackupProvider` | S3 | S3 |
| `sysdig.postgresql.aws.awsAccessKeyID` | Access Key ID | XXXXXXXXXX |
| `sysdig.postgresql.aws.awsSecretAccessKey` | Secret Access Key | YYYYYYYYYY |
| `sysdig.postgresql.aws.DeploymentEnvironment` | This variable is used to determine whether the backups includes all databases, or Sysdig only databases.<br />* If the value is left blank, then all databases will be backed up<br />* If the value is set to `sysdig_databases`, then the, `template0`, `template1` ,`postgres` databases will be skipped, all other are backed up | sysdig_databases|
| `sysdig.postgresql.backups.enabled` | This variable name is used to enable or disable backup. The value can be `enabled` or ` disabled`. Default to `enabled`. | enabled|
| `sysdig.postgresql.backups.schedule`              | Frequency to perform database backup                         | `"* */6 * * *"`  |
| `sysdig.postgresql.backups.version`              | Backup - Restore Image Version                         | 0.1.3  |

### Installation

There needed values for this component to be installed they are detailed below in a yaml example

```
aws:
    logicalBackupS3Bucket: ""
    logicalBackupS3Region: ""
    logicalBackupS3RetentionTime: ""
    logicalBackupPath: ""
    logicalBackupProvider: ""
    awsAccessKeyID: ""
    awsSecretAccessKey: ""
    deploymentEnvironment: ""
backups:
    enabled: false
    schedule: '* */6 * * *'
    imagePullSecret: sysdigcloud-pull-secret
    version: 0.1.3
```

After the values are setted please run a `installer diff` and check the changes, if the changes are good run `installer deploy` and the changes will be deployed.

### Manual Backups

The backup tool will be installed as a CronJob called `pg-backup-ha-cronjob` in the `sysdigcloud` namespace. By default it will run backups every 6 hours. Customers can also trigger the backup on-demand using the following command:

````
kubectl create job pg-backup --from=cronjob/pg-backup-ha-cronjob -n sysdigcloud
````

### Verifications

In the `sysdigcloud` namespace, you can run the following command to find the pod in which the latest backup job is executed. The log of the pod should provide the details about the backup operations.

```
kubectl get pods -n sysdigcloud | grep "pg-backup-ha-cronjob"
kubectl logs <backup-pod-name> -n sysdigcloud
```

A successful backup job should generate logs similar to this:

```
2023-11-07T23:06:21+00:00 - INFO - Checking envs
2023-11-07T23:06:21+00:00 - INFO - Validating S3 Bucket
2023-11-07T23:06:21+00:00 - INFO - Aws: S3 region is: us-east-1

2023-11-07T23:06:21+00:00 - INFO - Starting
2023-11-07T23:06:21+00:00 - INFO - Checking envs
2023-11-07T23:06:21+00:00 - INFO - Connecting to S3 and backing up
2023-11-07T23:06:21+00:00 - INFO - Done
```

The command to check the backup in the bucket is the following
```
aws s3 ls s3://bucketname/path --recursive
```

## Restore

### Assumptions

We assume that the most recent backup can be found in S3 bucket in the path as indicated in the `Backup` section.

### How to Use the Restore

The restore tool is based on Kubernetes Job, this job uses the latest backup on the S3 bucket. Since datastore restore is only performed on-demand, it is **NOT** included in the Installer binary. Customers can trigger the database restore by applying the following yaml. The restore time will vary depending on the size of databases.

The execution of the restore requires to scale down of all the deployments in the sysdig namespace and a StatefulSet, in order to have a smooth and error free database restoration, below you have a documentation how to do that, and also a scale up for setting back the environment.

#### Scale Down the Workloads - This step is required

Count the amount of replicas of the StatefulSet sysdigcloud-netsec-ingest using this command then note it down for future use.

```bash
kubectl get sts sysdigcloud-netsec-ingest -n sysdigcloud
```

Example output

```bash
NAME                        READY   AGE
sysdigcloud-netsec-ingest   1/1     4h11m
```

Also count the number of ready replicas for the all the sysdig deployments should be counted and noted for future, you can use this command

```bash
kubectl get deploy -n sysdigcloud
```

Example output

```bash
kubectl get deploy -n sysdigcloud
NAME                                               READY   UP-TO-DATE   AVAILABLE   AGE
ingress-default-backend                            1/1     1            1           4h7m
registry-scanner-api                               2/2     2            2           3h55m
sysdig-alert-manager                               1/1     1            1           4h4m
...........
```

Then scale down the workloads using these commands

```bash
kubectl scale deployment --replicas 0 --all -n sysdigcloud
```
```bash
kubectl scale sts sysdigcloud-netsec-ingest --replicas=0 -n sysdigcloud
```

Then apply this example yaml to the cluster in the sysdigcloud namespace.


```yaml
apiVersion: batch/v1
kind: Job
metadata:
  name: pg-restore-ha-job
  namespace: sysdigcloud
  generateName: pg-restore-ha
spec:
  ttlSecondsAfterFinished: 200
  template:
    spec:
      restartPolicy: Never
      containers:
        - image: quay.io/sysdig/postgres-backup-onprem:0.1.3
          name: pg-backup-ha
          command: ["/usr/local/bin/pg-restore.sh"]
          env:
            - name: TZ
              value: Etc/UTC
            - name: LOGICAL_BACKUP_PROVIDER
              value: s3
            - name: LOGICAL_BACKUP_S3_BUCKET
              value: example-bucket
            - name: LOGICAL_BACKUP_S3_REGION
              value: us-east-1
            - name: LOGICAL_BACKUP_PATH
              value: "demo-path"
            - name: PGPORT
              value: "5432"
            - name: PGHOST
              value: sysdigcloud-postgres-cluster
            - name: PGUSER
              valueFrom:
                secretKeyRef:
                  name: root.sysdigcloud-postgres-cluster.credentials.postgresql.acid.zalan.do
                  key: username
            - name: PGDATABASE
              value: postgres
            - name: PGSSLMODE
              value: require
            - name: PGPASSWORD
              valueFrom:
                secretKeyRef:
                  name: root.sysdigcloud-postgres-cluster.credentials.postgresql.acid.zalan.do
                  key: password
            - name: AWS_ACCESS_KEY_ID
              value: XXXXXXXXXX
            - name: AWS_SECRET_ACCESS_KEY
              value: YYYYYYYYYY
      imagePullSecrets:
        - name: sysdigcloud-pull-secret
```

### Settings

| Name                    | Value                                     | Example        |
| :---------------------- | :---------------------------------------- | :------------- |
| `logicalBackupS3Bucket` | S3 bucket name                            | example-bucket |
| `logicalBackupS3Region` | Region where S3 bucket resides            | us-east-1      |
| `logicalBackupPath`     | Path in which the backup files are stored | demo-path      |
| `logicalBackupProvider` | S3                                        | s3             |
| `awsAccessKeyID`        | Access Key ID                             | XXXXXXXXXX     |
| `awsSecretAccessKey`    | Secret Access Key                         | YYYYYYYYYY     |

### Post Job Completion

#### Scaling up the workloads

When the job is complete scale up the deployments one by one, using the number of replicas noted down in the previous step, please scale up each deployment accordingly.

```bash
kubectl scale deployment registry-scanner-api --replicas 2 -n sysdigcloud
kubectl scale deployment ingress-default-backend  --replicas 1 -n sysdigcloud
kubectl scale deployment sysdig-alert-manager --replicas 1 -n sysdigcloud
```

In the case of scaling this StatefulSet please use the number noted before on the Scale Down Workloads step, in this case is one.

```bash
kubectl scale sts sysdigcloud-netsec-ingest --replicas=1 -n sysdigcloud
```

### Verifications

When the job is complete, you can run the following command in the `sysdigcloud` namespace to get the name of the pod which runs the restore job. The pod logs provides the indication whether the job is completed successfully or not.

```bash
kubectl get pods -n sysdogcloud | grep "pg-restore-ha-job"
kubectl logs <restore-pod-name> -n sysdigcloud
```

```bash
2024-01-07T09:00:00+00:00 - INFO - Starting
2024-01-07T09:00:00+00:00 - INFO - Checking envs
2024-01-07T09:00:00+00:00 - INFO - Connecting to S3 and restoring
2024-01-07T09:20:00+00:00 - INFO - Done
```