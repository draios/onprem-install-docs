# Migrating MySQL to PostgreSQL Database

This topic is meant for the Support organization and Professional Services that will assist with deploying Sysdig On-Prem installations. For more information on our oversight services, see [Oversight Services for Installations and Upgrades](https://docs.sysdig.com/en/docs/administration/on-premises-deployments/on-premises-installation/#oversight-services-for-installations-and-upgrades).

## Migration

Sysdig consolidates all its databases by migrating all the existing databases running on MySQL to PostgreSQL. The database names remain the same except for `draios`: on PostgreSQL the database will be named`sysdig`.

The migration process is handled by the Installer. However, closely monitor the migration process at each stage as described in this document. The troubleshooting tips should help you fix specific migration issues.


### Prerequisites

The migration process is initiated by the Installer if the following requirements are met:

* Installer is running an upgrade, not a first-time installation.

* `sysdig.postgresql.primary: true` is set in `values.yaml`

* MySQL stateful sets (HA) or deployments (no HA) are running

* As a preflight check, we recommend that you run a SQL procedure on a MySQL pod and check for constraint violations:

```sql
DELIMITER $$
DROP PROCEDURE IF EXISTS ANALYZE_INVALID_FOREIGN_KEYS$$
CREATE
    PROCEDURE `ANALYZE_INVALID_FOREIGN_KEYS`(
        checked_database_name VARCHAR(64) CHARACTER SET utf8,
        checked_table_name VARCHAR(64) CHARACTER SET utf8,
        temporary_result_table ENUM('Y', 'N'))
    LANGUAGE SQL
    NOT DETERMINISTIC
    READS SQL DATA
    BEGIN
        DECLARE TABLE_SCHEMA_VAR VARCHAR(64);
        DECLARE TABLE_NAME_VAR VARCHAR(64);
        DECLARE COLUMN_NAME_VAR VARCHAR(64);
        DECLARE CONSTRAINT_NAME_VAR VARCHAR(64);
        DECLARE REFERENCED_TABLE_SCHEMA_VAR VARCHAR(64);
        DECLARE REFERENCED_TABLE_NAME_VAR VARCHAR(64);
        DECLARE REFERENCED_COLUMN_NAME_VAR VARCHAR(64);
        DECLARE KEYS_SQL_VAR VARCHAR(1024);
        DECLARE done INT DEFAULT 0;
        DECLARE foreign_key_cursor CURSOR FOR
            SELECT
                `TABLE_SCHEMA`,
                `TABLE_NAME`,
                `COLUMN_NAME`,
                `CONSTRAINT_NAME`,
                `REFERENCED_TABLE_SCHEMA`,
                `REFERENCED_TABLE_NAME`,
                `REFERENCED_COLUMN_NAME`
            FROM
                information_schema.KEY_COLUMN_USAGE
            WHERE
                `CONSTRAINT_SCHEMA` LIKE checked_database_name AND
                `TABLE_NAME` LIKE checked_table_name AND
                `REFERENCED_TABLE_SCHEMA` IS NOT NULL;
        DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = 1;
        IF temporary_result_table = 'N' THEN
            DROP TEMPORARY TABLE IF EXISTS INVALID_FOREIGN_KEYS;
            DROP TABLE IF EXISTS INVALID_FOREIGN_KEYS;
            CREATE TABLE INVALID_FOREIGN_KEYS(
                `TABLE_SCHEMA` VARCHAR(64),
                `TABLE_NAME` VARCHAR(64),
                `COLUMN_NAME` VARCHAR(64),
                `CONSTRAINT_NAME` VARCHAR(64),
                `REFERENCED_TABLE_SCHEMA` VARCHAR(64),
                `REFERENCED_TABLE_NAME` VARCHAR(64),
                `REFERENCED_COLUMN_NAME` VARCHAR(64),
                `INVALID_KEY_COUNT` INT,
                `INVALID_KEY_SQL` VARCHAR(1024)
            );
        ELSEIF temporary_result_table = 'Y' THEN
            DROP TEMPORARY TABLE IF EXISTS INVALID_FOREIGN_KEYS;
            DROP TABLE IF EXISTS INVALID_FOREIGN_KEYS;
            CREATE TEMPORARY TABLE INVALID_FOREIGN_KEYS(
                `TABLE_SCHEMA` VARCHAR(64),
                `TABLE_NAME` VARCHAR(64),
                `COLUMN_NAME` VARCHAR(64),
                `CONSTRAINT_NAME` VARCHAR(64),
                `REFERENCED_TABLE_SCHEMA` VARCHAR(64),
                `REFERENCED_TABLE_NAME` VARCHAR(64),
                `REFERENCED_COLUMN_NAME` VARCHAR(64),
                `INVALID_KEY_COUNT` INT,
                `INVALID_KEY_SQL` VARCHAR(1024)
            );
        END IF;
        OPEN foreign_key_cursor;
        foreign_key_cursor_loop: LOOP
            FETCH foreign_key_cursor INTO
            TABLE_SCHEMA_VAR,
            TABLE_NAME_VAR,
            COLUMN_NAME_VAR,
            CONSTRAINT_NAME_VAR,
            REFERENCED_TABLE_SCHEMA_VAR,
            REFERENCED_TABLE_NAME_VAR,
            REFERENCED_COLUMN_NAME_VAR;
            IF done THEN
                LEAVE foreign_key_cursor_loop;
            END IF;
            SET @from_part = CONCAT('FROM ', '`', TABLE_SCHEMA_VAR, '`.`', TABLE_NAME_VAR, '`', ' AS REFERRING ',
                 'LEFT JOIN `', REFERENCED_TABLE_SCHEMA_VAR, '`.`', REFERENCED_TABLE_NAME_VAR, '`', ' AS REFERRED ',
                 'ON (REFERRING', '.`', COLUMN_NAME_VAR, '`', ' = ', 'REFERRED', '.`', REFERENCED_COLUMN_NAME_VAR, '`', ') ',
                 'WHERE REFERRING', '.`', COLUMN_NAME_VAR, '`', ' IS NOT NULL ',
                 'AND REFERRED', '.`', REFERENCED_COLUMN_NAME_VAR, '`', ' IS NULL');
            SET @full_query = CONCAT('SELECT COUNT(*) ', @from_part, ' INTO @invalid_key_count;');
            PREPARE stmt FROM @full_query;
            EXECUTE stmt;
            IF @invalid_key_count > 0 THEN
                INSERT INTO
                    INVALID_FOREIGN_KEYS
                SET
                    `TABLE_SCHEMA` = TABLE_SCHEMA_VAR,
                    `TABLE_NAME` = TABLE_NAME_VAR,
                    `COLUMN_NAME` = COLUMN_NAME_VAR,
                    `CONSTRAINT_NAME` = CONSTRAINT_NAME_VAR,
                    `REFERENCED_TABLE_SCHEMA` = REFERENCED_TABLE_SCHEMA_VAR,
                    `REFERENCED_TABLE_NAME` = REFERENCED_TABLE_NAME_VAR,
                    `REFERENCED_COLUMN_NAME` = REFERENCED_COLUMN_NAME_VAR,
                    `INVALID_KEY_COUNT` = @invalid_key_count,
                    `INVALID_KEY_SQL` = CONCAT('SELECT ',
                        'REFERRING.', '`', COLUMN_NAME_VAR, '` ', 'AS "Invalid: ', COLUMN_NAME_VAR, '", ',
                        'REFERRING.* ',
                        @from_part, ';');
            END IF;
            DEALLOCATE PREPARE stmt;
        END LOOP foreign_key_cursor_loop;
    END$$
DELIMITER ;
CALL ANALYZE_INVALID_FOREIGN_KEYS('%', '%', 'Y');
DROP PROCEDURE IF EXISTS ANALYZE_INVALID_FOREIGN_KEYS;
SELECT * FROM INVALID_FOREIGN_KEYS;
```

If the query does not return any row, the migration process can be initiated. Otherwise, delete the orphaned rows before starting with the migration.


### Run the Installer

1. Run the following:

        installer deploy

2. Ensure that the PostgreSQL databases, users, and grants are initialized by the `postgres-init-job` job:

        deploy.go:1711] removing postgres db init job
        deploy.go:1714] running postgres db init job
        deploy.go:1726] waiting postgres db init job to finish... (attempt 1/10)
        deploy.go:1730] postgres db init finished correctly


3. Ensure that the collector block for the new agent connections is enabled. If successful, you will see the following:

        deploy.go:1560] toggled collector block to true: Accepting new agent connections is OFF

   Under the hood, Installer sends the following HTTP request to the API to block new agent connections:

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


6. Ensure that the MySQL databases are migrated to PostgreSQL by the `mysql-to-postgresql-migration` job:

        deploy.go:1623] removing mysql to postgres migration job
        deploy.go:1626] running mysql to postgres migration job
        deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 1/3600)
        deploy.go:1685] waiting for mysql to postgres migration to finish... (attempt 2/3600)
        deploy.go:1636] mysql to postgres migration finished correctly


7. Ensure that the collector (running at this point) and the API server (not running at this point, as it was scaled it to 0 replicas earlier) are deployed by using the new manifests pointing to PostgreSQL:

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


8.  Ensure that the collector block for the new agent connections is disabled.
    Under the hood, Installer sends the following HTTP request to the API to block new agent connections: `GET /api/admin/agents/new/connections?block=false`

        deploy.go:1560] toggled collector block to false: Accepting new agent connections is ON


9. Ensure that the MySQL deployments (non-HA setup) or statefulsets (HA setup) and the services are deleted:

        deploy.go:1664] removing mysql deployments, stateful sets and services

   At this point, the migration is successfully concluded and installation will continue as usual.


10.  As the PVC is retained by default, delete it after the migration is completed.


**For the subsequent runs, Installer will always generate the manifests for `mysql-to-postgresql-migration` and `mysql-latest-migrations` jobs. The migration will not run again if it is completed once.**


## Troubleshooting

### PostgreSQL Initialization Job Failed

If the whole migration process will continue even if after 10 checks the `postgres-init-job` job has not finished correctly:

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

The whole migration process in this case might be terminated after 10 hours. It indicates that the `mysql-latest-migrations` job has not finished correctly.

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


1. Stop the Installer with `CTRL + C` instead of waiting for 10 hours. The migration will be retried on the next run because it's an idempotent operation.

2. Check which MySQL migration is failed. To do so, describe the pod related to the `mysql-latest-migrations` job:

    `kubectl -n sysdigcloud describe pod -l "job-name=mysql-latest-migrations"`

3. Find out which container in the pod is not terminated correctly by looking at `State` and `Reason` fields.

   It should indicate that `scanning-migrations` or `draios-migrations` are the failed containers.

4. Check the logs associated with the container that has failed to complete:

    `kubectl -n sysdigcloud logs -l "job-name=mysql-latest-migrations" -c draios-migrations`


### MySQL To PostgreSQL Migration Job Failed

The whole migration process might be terminated after 10 hours. It indicates that the `mysql-to-postgres-migration` job has not finished correctly.

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


1. Stop the Installer with `CTRL + C` instead of waiting for 10 hours. The migration will be retried on the next run because it is an idempotent operation.

2. Read the logs for the failed container:

    `kubectl -n sysdigcloud logs -l "job-name=mysql-to-postgresql-migration"`
