# Migrating MySQL to PostgreSQL Database

This topic is meant for the Support organization and Professional Services that will assist with deploying Sysdig On-Prem installations. For more information on our oversight services, see [Oversight Services Now Offered for All Installs and Upgrades](https://docs.sysdig.com/en/on-premises-installation.html#UUID-7946fc46-b37c-24f4-f251-2f84ca3f5e1c_UUID-435c9483-c9b6-bacd-cb89-b587b1fe1558).


## Migration

Sysdig consolidates all its databases by migrating all the existing databases running on MySQL to PostgreSQL. The database names remain the same except for `draois`: on PostgreSQL the database will be named`sysdig`.

The migration process is handled by the Installer. However, closely monitor the migration process at each stage as described in this document. The troubleshooting tips should help you fix specific migration issues.


### Prerequisites

The migration process is initiated by the Installer if the following requirements are met:

* Installer is running an upgrade, not a first-time installation.

* `sysdig.postgresql.primary: true` is set in `values.yaml`

* MySQL stateful sets (HA) or deployments (no HA) are running


### Run the Installer

1. Run the following:

        installer deploy

2. Ensure that PostgreSQL databases, users, and grants are initialized by the `postgres-init-job` job:

        deploy.go:1711] removing postgres db init job
        deploy.go:1714] running postgres db init job
        deploy.go:1726] waiting postgres db init job to finish... (attempt 1/10)
        deploy.go:1730] postgres db init finished correctly


3. Ensure that collector block for the new agent connections is enabled. If successful, you will see the following:

        deploy.go:1560] toggled collector block to true: Accepting new agent connections is OFF

   Under the hood, Installer run this HTTP request to API to block new agent connections:

        HTTP GET /api/admin/agents/new/connections?block=true


4. Ensure that the following services on MySQL or PostgreSQL are scaled to 0 replicas.

    * Monitor services: `api`, `worker`, `alerter`, `prom-remote-write`
    * Secure services: `anchore-core`, `anchore-worker`, `events-forwarder`, `events-forwarder-api`, `events-gatherer`, `policy-advisor`, `scanning-api`, `scanning-alertmgr`, `scanning-analysiscollector`, `anchore-api`, `anchore-catalog`, `anchore-policy-engine`, `secure-overview-mgr`, `secure-overview-api`
    * Secure cronjobs are deleted: `scanning-retention-mgr`, `scanning-ve-janitor`

   If scaling down is successful, you will see the following:

        deploy.go:1427] scaling down alerter
        deploy.go:1432] scaling down api
        deploy.go:1447] scaling down worker
        deploy.go:1476] removing secure cronjobs
        deploy.go:1480] scaling down anchore
        kubectl.go:216] deployments.apps "sysdigcloud-anchore-api" not found
        kubectl.go:216] deployments.apps "sysdigcloud-anchore-catalog" not found
        kubectl.go:216] deployments.apps "sysdigcloud-anchore-policy-engine" not found
        deploy.go:1496] scaling down events
        deploy.go:1501] scaling down policy-advisor
        deploy.go:1504] scaling down scanning
        deploy.go:1510] scaling down overview
        deploy.go:1525] waiting pods to be terminated... (attempt 1/20)
        deploy.go:1525] waiting pods to be terminated... (attempt 2/20)
        deploy.go:1525] waiting pods to be terminated... (attempt 3/20)
        deploy.go:1521] pods terminated correctly


5. Ensure that the latest MySQL migrations are applied by the `mysql-latest-migrations` job:

        deploy.go:1567] removing mysql latest migrations job
        deploy.go:1570] running mysql latest migrations job
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 1/3600)
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 2/3600)
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 3/3600)
        deploy.go:1580] mysql latest migrations finished correctly


6. Ensure that MySQL databases are migrated to PostgreSQL by the mysql-to-postgresql-migration job:

        deploy.go:1623] removing mysql to postgres migration job
        deploy.go:1626] running mysql to postgres migration job
        deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 1/3600)
        deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 2/3600)
        deploy.go:1636] mysql to postgres migration finished correctly


7. Ensure that collector (running at this point) and the API server (not running at this point, as it was scaled it to 0 replicas earlier) are deployed using the new manifests pointing to PostgreSQL:

        deploy.go:1640] applying sysdigcloud-collector
        deploy.go:1645] applying sysdigcloud-api
        waitforpods.go:311] Waiting for deployment "sysdigcloud-collector" rollout to finish: 1 old replicas are pending termination...
        waitforpods.go:315] Waiting for deployment "sysdigcloud-api" rollout to finish: 0 of 1 updated replicas are available...
        waitforpods.go:311] Waiting for deployment "sysdigcloud-collector" rollout to finish: 1 old replicas are pending termination...
        waitforpods.go:315] Waiting for deployment "sysdigcloud-api" rollout to finish: 0 of 1 updated replicas are available...
        waitforpods.go:315] Waiting for deployment "sysdigcloud-api" rollout to finish: 0 of 1 updated replicas are available...
        waitforpods.go:311] Waiting for deployment "sysdigcloud-collector" rollout to finish: 1 old replicas are pending termination...
        waitforpods.go:311] Waiting for deployment "sysdigcloud-collector" rollout to finish: 1 old replicas are pending termination...
        waitforpods.go:315] Waiting for deployment "sysdigcloud-api" rollout to finish: 0 of 1 updated replicas are available...
        waitforpods.go:311] Waiting for deployment "sysdigcloud-collector" rollout to finish: 1 old replicas are pending termination...
        waitforpods.go:315] Waiting for deployment "sysdigcloud-api" rollout to finish: 0 of 1 updated replicas are available...
        waitforpods.go:311] Waiting for deployment "sysdigcloud-collector" rollout to finish: 1 old replicas are pending termination...
        waitforpods.go:311] Waiting for deployment "sysdigcloud-collector" rollout to finish: 1 old replicas are pending termination...
        waitforpods.go:315] Waiting for deployment "sysdigcloud-api" rollout to finish: 0 of 1 updated replicas are available...
        waitforpods.go:318] deployment "sysdigcloud-collector" successfully rolled out
        waitforpods.go:315] Waiting for deployment "sysdigcloud-api" rollout to finish: 0 of 1 updated replicas are available...
        waitforpods.go:315] Waiting for deployment "sysdigcloud-api" rollout to finish: 0 of 1 updated replicas are available...
        waitforpods.go:318] deployment "sysdigcloud-api" successfully rolled out
        waitforpods.go:74] waitforpods(sysdigcloud-collector,sysdigcloud-api) completed in 1m32s


8.  Ensure that collector block for the new agent connections is disabled (`GET /api/admin/agents/new/connections?block=false` HTTP request to API will be performed under the hood):

        deploy.go:1560] toggled collector block to false: Accepting new agent connections is ON


9. Ensure that MySQL deployments (non-HA setup) or stateful sets (HA setup) and services are deleted:

        deploy.go:1664] removing mysql deployments, stateful sets and services

   At this point, the migration is successfully concluded and installation will continue as usual.


10.  As the PVC is retained by default, delete it after the migration is completed.


**For the following runs, Installer will always generate the manifests for `mysql-to-postgresql-migration` and `mysql-latest-migrations` jobs: even if so, the migration will not run again if it has completed once.**


## Troubleshooting

### PostgreSQL Initialization Job Failed

The whole migration process will continue even if after 10 checks the `postgres-init-job` job has not finished correctly:

        deploy.go:1711] removing postgres db init job
        deploy.go:1714] running postgres db init job
        deploy.go:1726] waiting postgres db init job to finish... (attempt 1/10)
        deploy.go:1726] waiting postgres db init job to finish... (attempt 2/10)
        deploy.go:1726] waiting postgres db init job to finish... (attempt 3/10)
        deploy.go:1726] waiting postgres db init job to finish... (attempt 4/10)
        deploy.go:1726] waiting postgres db init job to finish... (attempt 5/10)
        deploy.go:1726] waiting postgres db init job to finish... (attempt 6/10)
        deploy.go:1726] waiting postgres db init job to finish... (attempt 7/10)
        deploy.go:1726] waiting postgres db init job to finish... (attempt 8/10)
        deploy.go:1726] waiting postgres db init job to finish... (attempt 9/10)
        deploy.go:1726] waiting postgres db init job to finish... (attempt 10/10)
        deploy.go:1726] waiting postgres db init job to finish... (attempt 10/10)
        deploy.go:1730] postgres-init-job failed


1. You can stop the installer with `CTRL + c` because the migration will fail later in any case.

2. Check which initialization failed. To do so, describe the pod related to the `postgres-init-job` job:

    `kubectl -n sysdigcloud describe pod -l "job-name=postgres-init-job"`

3. Find out which container in the pod is not terminated correctly by looking at `State` and `Reason` fields.
   
   It should indicate that failed containers are one or more of the following: `profiling-worker-init`, `scanning-anchore-init`, `scanning-init`, `padvisor-init`, `sysdig-init` and `quartz-init`.
   
4. Check the logs associated with the container that has failed to complete:

    `kubectl -n sysdigcloud logs -l "job-name=mysql-latest-migrations" -c sysdig-init`


### Latest MySQL Migrations Job Failed

The whole migration process in this case will stop if after 10 hours the `mysql-latest-migrations` job has not finished correctly.

        deploy.go:1567] removing mysql latest migrations job
        deploy.go:1570] running mysql latest migrations job
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 1/3600)
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 2/3600)
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 3/3600)
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 4/3600)
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 5/3600)
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 6/3600)
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 7/3600)
        ...
        deploy.go:1583] waiting mysql latest migrations job to finish... (attempt 3600/3600)
        deploy.go:1587] mysql-latest-migrations-job failed


1. It’s also safe to stop the Installer with `CTRL + c` instead of waiting for 10 hours: the migration will be retried on the next run, as it's an idempotent operation.

2. Check which MySQL migration failed. To do so, describe the pod related to the `mysql-latest-migrations` job:

    `kubectl -n sysdigcloud describe pod -l "job-name=mysql-latest-migrations"`

3. Find out which container in the pod is not terminated correctly by looking at `State` and `Reason` fields.

   It should indicate that `scanning-migrations` or `draios-migrations` are the failed containers.

4. Check the logs associated with the container that has failed to complete:

    `kubectl -n sysdigcloud logs -l "job-name=mysql-latest-migrations" -c draios-migrations`


### MySQL To PostgreSQL Migration Job Failed

The whole migration process will stop if after 10 hours the `mysql-to-postgres-migration` job has not finished correctly.

      deploy.go:1623] removing mysql to postgres migration job
      deploy.go:1626] running mysql to postgres migration job
      deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 1/3600)
      deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 2/3600)
      deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 3/3600)
      deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 4/3600)
      deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 5/3600)
      deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 6/3600)
      deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 7/3600)
      ...
      deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 3600/3600)
      deploy.go:1587] mysql-to-postgres-migration-job failed


1. It’s also safe to stop the Installer with `CTRL + c` instead of waiting for 10 hours: the migration will be retried on the next run, as it's an idempotent operation.

2. Read logs for the failed container:

    `kubectl -n sysdigcloud logs -l "job-name=mysql-to-postgresql-migration"`
