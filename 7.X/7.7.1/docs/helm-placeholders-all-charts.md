# activity-audit

![Version: 5.1.0-260216155728-main-v5b1fbd7](https://img.shields.io/badge/Version-5.1.0--260216155728--main--v5b1fbd7-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Activity Audit

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| activityAudit.activityAuditApiReplicaCount | int | `1` |  |
| activityAudit.audit.enabled | bool | `true` |  |
| activityAudit.authorizationService.enabled | bool | `false` |  |
| activityAudit.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| activityAudit.elasticsearch.compressedRequestBody | bool | `true` |  |
| activityAudit.elasticsearch.disableRetry | bool | `true` |  |
| activityAudit.elasticsearch.maxRetry | int | `5` |  |
| activityAudit.elasticsearch.nodeDiscoveryInterval | string | `"10m"` |  |
| activityAudit.elasticsearch.nodeDiscoveryOnStart | bool | `true` |  |
| activityAudit.elasticsearch.retryHTTPStatuses | string | `"429,500,502,503,504"` |  |
| activityAudit.elasticsearch.retryOnTimeout | bool | `true` |  |
| activityAudit.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| activityAudit.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| activityAudit.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| activityAudit.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| activityAudit.enabled | bool | `true` |  |
| activityAudit.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-activity-audit-api-v1"` |  |
| activityAudit.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-activity-audit-api-v1"` |  |
| activityAudit.ingress[0].hosts[0].paths[0].path | string | `"/api/v1/activityAudit"` |  |
| activityAudit.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-activity-audit-api"` |  |
| activityAudit.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| activityAudit.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-activity-audit-api-v2"` |  |
| activityAudit.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-activity-audit-api-v2"` |  |
| activityAudit.ingress[0].hosts[0].paths[1].path | string | `"/api/v2/activityAudit"` |  |
| activityAudit.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-activity-audit-api"` |  |
| activityAudit.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| activityAudit.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| activityAudit.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| activityAudit.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| activityAudit.ingress[0].labels.role | string | `"ingress-config"` |  |
| activityAudit.ingress[0].labels.tier | string | `"infra"` |  |
| activityAudit.ingress[0].name | string | `"sysdigcloud-activity-audit"` |  |
| activityAudit.janitor.connectionRetentionDays | int | `7` |  |
| activityAudit.janitor.cronjob | string | `"0 3 * * *"` |  |
| activityAudit.janitor.fileRetentionDays | int | `7` |  |
| activityAudit.janitor.quickwit.apiBased | bool | `false` |  |
| activityAudit.janitor.quickwit.debug | bool | `false` |  |
| activityAudit.janitor.quickwit.dryRun | bool | `true` |  |
| activityAudit.janitor.quickwit.enabled | bool | `false` |  |
| activityAudit.janitor.retentionDays | int | `90` |  |
| activityAudit.janitor.suspend | bool | `false` |  |
| activityAudit.quickwit.cutoffTime | string | `""` |  |
| activityAudit.quickwit.enabled | bool | `false` |  |
| activityAudit.quickwit.verifySSL | bool | `false` |  |
| activityAudit.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| activityAudit.repositoryPrefix | string | `"secure"` |  |
| activityAudit.resources.activityAuditApi.limits.cpu | int | `1` |  |
| activityAudit.resources.activityAuditApi.limits.memory | string | `"500Mi"` |  |
| activityAudit.resources.activityAuditApi.requests.cpu | string | `"250m"` |  |
| activityAudit.resources.activityAuditApi.requests.memory | string | `"50Mi"` |  |
| activityAudit.resources.activityAuditJanitor.limits.cpu | string | `"250m"` |  |
| activityAudit.resources.activityAuditJanitor.limits.memory | string | `"250Mi"` |  |
| activityAudit.resources.activityAuditJanitor.requests.cpu | string | `"250m"` |  |
| activityAudit.resources.activityAuditJanitor.requests.memory | string | `"250Mi"` |  |
| activityAudit.sdauthCacheTTL | string | `"5m"` |  |
| activityAudit.serviceAccountName | string | `"sysdig"` |  |
| activityAudit.zones.enabled | bool | `true` |  |
| activityAudit.zones.v2 | bool | `true` |  |
| global.api.serviceTokens.activityAudit.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","hostname":"sysdigcloud-elasticsearch","port":9200,"scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.quickwit.auth.basicAuth.password | string | `nil` |  |
| global.quickwit.auth.basicAuth.username | string | `nil` |  |
| global.quickwit.indexer.endpoint | string | `nil` |  |
| global.quickwit.searcher.endpoint | string | `nil` |  |
| global.secure.iac.policyService.endpoint | string | `"secure-iac-policy-service:8080"` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.zones.platformService.endpoint | string | `"sysdigcloud-platform-zones-service-grpc:8091"` |  |
| global.zones.platformService.tlsSkip | string | `"true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# admissioncontroller

![Version: 1.0.0-260226163614-main-v4bedc65](https://img.shields.io/badge/Version-1.0.0--260226163614--main--v4bedc65-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Admission Controller

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| admissioncontroller.audit.enabled | string | `"true"` |  |
| admissioncontroller.authorizationService.enabled | bool | `false` |  |
| admissioncontroller.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| admissioncontroller.enabled | bool | `true` |  |
| admissioncontroller.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-admissioncontroller-api"` |  |
| admissioncontroller.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-admissioncontroller-api"` |  |
| admissioncontroller.ingress[0].hosts[0].paths[0].path | string | `"/api/admissionController/v1"` |  |
| admissioncontroller.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-admissioncontroller-api"` |  |
| admissioncontroller.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| admissioncontroller.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| admissioncontroller.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| admissioncontroller.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| admissioncontroller.ingress[0].labels.role | string | `"ingress-config"` |  |
| admissioncontroller.ingress[0].labels.tier | string | `"infra"` |  |
| admissioncontroller.ingress[0].name | string | `"sysdigcloud-admissioncontroller-ingress"` |  |
| admissioncontroller.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| admissioncontroller.replicaCount | int | `1` |  |
| admissioncontroller.repositoryPrefix | string | `"secure"` |  |
| admissioncontroller.resources.admissioncontrollerApi.limits.cpu | int | `4` |  |
| admissioncontroller.resources.admissioncontrollerApi.limits.memory | string | `"2Gi"` |  |
| admissioncontroller.resources.admissioncontrollerApi.requests.cpu | int | `2` |  |
| admissioncontroller.resources.admissioncontrollerApi.requests.memory | string | `"1Gi"` |  |
| admissioncontroller.serviceAccountName | string | `"sysdig"` |  |
| admissioncontroller.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 200\n  essentials:\n    limit: 100\nfeatureEndpointToggles:\n  tierDependent: true\n  default:\n    enabled: true"` |  |
| global.api.serviceTokens.admissionController.serviceToken | string | `"change_me"` |  |
| global.apps | string | `"secure"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.admissionController.admindb | string | `"anchore"` |  |
| global.legacyPostgres.postgresDatabases.admissionController.adminpassword | string | `"change_me"` |  |
| global.legacyPostgres.postgresDatabases.admissionController.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.admissionController.db | string | `"admissioncontroller"` |  |
| global.legacyPostgres.postgresDatabases.admissionController.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.admissionController.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.admissionController.password | string | `"change_me"` |  |
| global.legacyPostgres.postgresDatabases.admissionController.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.admissionController.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.admissionController.username | string | `"admissioncontroller_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.13"` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# alert-manager

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig Alert Manager

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| alertManager.internalIngestion.accessToken | string | `nil` |  |
| alertManager.jvmOptions | string | `"-Xms1g -Xmx1g -Dsysdig.redismq.watermark.consumer.threads=2"` |  |
| alertManager.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| alertManager.replicaCount | int | `1` |  |
| alertManager.repositoryPrefix | string | `"monitor"` |  |
| alertManager.resources.alertManager.limits.cpu | int | `1` |  |
| alertManager.resources.alertManager.limits.memory | string | `"1Gi"` |  |
| alertManager.resources.alertManager.requests.cpu | int | `1` |  |
| alertManager.resources.alertManager.requests.memory | string | `"1Gi"` |  |
| alertManager.serviceAccountName | string | `"sysdig"` |  |
| alertManager.systemAlertManager.enabled | bool | `false` |  |
| alertManager.systemAlertManager.jvmOptions | string | `"-Xms1g -Xmx1g -Dsysdig.redismq.watermark.consumer.threads=2"` |  |
| alertManager.systemAlertManager.replicaCount | int | `1` |  |
| alertManager.systemAlertManager.resources.systemAlertManager.limits.cpu | int | `1` |  |
| alertManager.systemAlertManager.resources.systemAlertManager.limits.memory | string | `"1Gi"` |  |
| alertManager.systemAlertManager.resources.systemAlertManager.requests.cpu | int | `1` |  |
| alertManager.systemAlertManager.resources.systemAlertManager.requests.memory | string | `"1Gi"` |  |
| global.alertingSystem.enabled | bool | `true` |  |
| global.api.serviceTokens.alertManager.serviceToken | string | `nil` |  |
| global.apps | string | `"monitor"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.dnsName | string | `"change-me.com"` |  |
| global.legacyRedis.redisClientsMonitor.alerting.tls | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.cache.tls | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.common.tls | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.prometheusAlert.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `true` |  |
| global.legacyRedis.redisTls.enabled | bool | `true` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` |  |
| global.legacyRedis.sysdigRedis.password | string | `"change-me"` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.prometheus.enabled | bool | `true` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# alert-notifier

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig Alert Notifier

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| alertNotifier.jvmOptions | string | `"-Xms1g -Xmx1g -Dsysdig.redismq.notifier.consumer.threads=2"` |  |
| alertNotifier.nats.secureHealth.dryRun | bool | `true` |  |
| alertNotifier.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| alertNotifier.replicaCount | int | `1` |  |
| alertNotifier.repositoryPrefix | string | `"monitor"` |  |
| alertNotifier.resources.alertNotifier.limits.cpu | int | `1` |  |
| alertNotifier.resources.alertNotifier.limits.memory | string | `"1Gi"` |  |
| alertNotifier.resources.alertNotifier.requests.cpu | int | `1` |  |
| alertNotifier.resources.alertNotifier.requests.memory | string | `"1Gi"` |  |
| alertNotifier.sage.enabled | bool | `true` |  |
| alertNotifier.serviceAccountName | string | `"sysdig"` |  |
| global.alertingSystem.enabled | bool | `true` |  |
| global.api.serviceTokens.alertNotifier.serviceToken | string | `""` |  |
| global.apps | string | `"monitor"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.dnsName | string | `"change-me.com"` |  |
| global.legacyRedis.redisHa | bool | `true` |  |
| global.legacyRedis.redisTls.enabled | bool | `true` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` |  |
| global.legacyRedis.sysdigRedis.password | string | `"change-me"` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.smtpFromAddress | string | `"notifications@sysdig.com"` |  |
| global.smtpFromName | string | `"Sysdig Notifications"` |  |
| global.smtpPassword | string | `""` |  |
| global.smtpProtocolSSL | bool | `false` |  |
| global.smtpProtocolTLS | bool | `false` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# analytics

![Version: 1.1.0-260310131059-main-v6e97bcf](https://img.shields.io/badge/Version-1.1.0--260310131059--main--v6e97bcf-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Analytics

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| analytics.analyticsApiReplicaCount | int | `2` |  |
| analytics.analyticsGathererReplicaCount | int | `1` |  |
| analytics.blacklistedCustomer | string | `"none"` |  |
| analytics.elasticsearch.compressedRequestBody | bool | `true` |  |
| analytics.elasticsearch.disableRetry | bool | `true` |  |
| analytics.elasticsearch.maxRetry | int | `5` |  |
| analytics.elasticsearch.retryHTTPStatuses | string | `"429,500,502,503,504"` |  |
| analytics.elasticsearch.retryOnTimeout | bool | `true` |  |
| analytics.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| analytics.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| analytics.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| analytics.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| analytics.enabled | bool | `true` |  |
| analytics.gatherer.autoscaler.enabled | bool | `true` |  |
| analytics.gatherer.autoscaler.maxReplicaCount | int | `6` |  |
| analytics.gatherer.autoscaler.minReplicaCount | int | `2` |  |
| analytics.gatherer.autoscaler.percentOfUnreadMessagesThreshold | int | `5` |  |
| analytics.gatherer.envVars | string | `nil` |  |
| analytics.homeDashboard | string | `""` |  |
| analytics.ingestion.runtime.enabled | bool | `true` |  |
| analytics.ingestion.vm.enabled | bool | `true` |  |
| analytics.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-analytics-api"` |  |
| analytics.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-analytics-api"` |  |
| analytics.ingress[0].hosts[0].paths[0].path | string | `"/api/secure-metrics/v1"` |  |
| analytics.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-analytics-api"` |  |
| analytics.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| analytics.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| analytics.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| analytics.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| analytics.ingress[0].labels.role | string | `"ingress-config"` |  |
| analytics.ingress[0].labels.tier | string | `"infra"` |  |
| analytics.ingress[0].name | string | `"sysdigcloud-analytics-ingress"` |  |
| analytics.janitor.schedule | string | `"0 3 * * *"` |  |
| analytics.natsjs.runtime.policy.durable | string | `"analytics-gatherer-events"` |  |
| analytics.natsjs.runtime.policy.handleTimeout | string | `"30s"` |  |
| analytics.natsjs.runtime.policy.maxDeliver | int | `15` |  |
| analytics.natsjs.runtime.policy.maxInFlight | int | `1024` |  |
| analytics.natsjs.runtime.policy.name | string | `"runtime-policy-events"` |  |
| analytics.natsjs.runtime.policy.queue | string | `"analytics-gatherer-events"` |  |
| analytics.natsjs.runtime.policy.streamName | string | `"events"` |  |
| analytics.natsjs.runtime.policy.subject | string | `"events.source.events.policy.>"` |  |
| analytics.natsjs.tls.enabled | bool | `true` |  |
| analytics.natsjs.url | string | `"nats"` |  |
| analytics.natsjs.vm.scans.durable | string | `"analytics-gatherer-scanresult"` |  |
| analytics.natsjs.vm.scans.handleTimeout | string | `"30s"` |  |
| analytics.natsjs.vm.scans.maxDeliver | int | `15` |  |
| analytics.natsjs.vm.scans.maxInFlight | int | `1024` |  |
| analytics.natsjs.vm.scans.name | string | `"analytics-gatherer"` |  |
| analytics.natsjs.vm.scans.pullBatch | int | `16` |  |
| analytics.natsjs.vm.scans.queue | string | `"analytics-gatherer-scanresult"` |  |
| analytics.natsjs.vm.scans.streamName | string | `"secure-vm-scanner-scan-response"` |  |
| analytics.natsjs.vm.scans.subject | string | `"secure.vm.scanner.scan.response.*.*.success"` |  |
| analytics.natsjs.workersPoolSize | int | `8` |  |
| analytics.opensearch.host | string | `"opensearch:9200"` |  |
| analytics.opensearch.nodeDiscovery | bool | `false` |  |
| analytics.opensearch.nodeDiscoveryInterval | int | `0` |  |
| analytics.opensearch.password | string | `""` |  |
| analytics.opensearch.tlsencryption.verifySSL | bool | `true` |  |
| analytics.opensearch.useDedicated | bool | `false` |  |
| analytics.opensearch.username | string | `""` |  |
| analytics.osWriteEnable | bool | `true` |  |
| analytics.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| analytics.remotebody.enabled | bool | `false` |  |
| analytics.remotebody.pullerBackends | string | `"s3"` |  |
| analytics.remotebody.s3.accessKeyId | string | `""` |  |
| analytics.remotebody.s3.cloudProvider | string | `""` |  |
| analytics.remotebody.s3.endpoint | string | `""` |  |
| analytics.remotebody.s3.region | string | `""` |  |
| analytics.remotebody.s3.secretAccessKey | string | `""` |  |
| analytics.repositoryPrefix | string | `"secure"` |  |
| analytics.resources.analyticsApi.limits.cpu | int | `1` |  |
| analytics.resources.analyticsApi.limits.memory | string | `"2Gi"` |  |
| analytics.resources.analyticsApi.requests.cpu | int | `1` |  |
| analytics.resources.analyticsApi.requests.memory | string | `"1Gi"` |  |
| analytics.resources.analyticsGatherer.limits.cpu | int | `2` |  |
| analytics.resources.analyticsGatherer.limits.memory | string | `"2Gi"` |  |
| analytics.resources.analyticsGatherer.requests.cpu | int | `1` |  |
| analytics.resources.analyticsGatherer.requests.memory | string | `"1Gi"` |  |
| analytics.resources.analyticsJanitor.limits.cpu | string | `"250m"` |  |
| analytics.resources.analyticsJanitor.limits.memory | string | `"250Mi"` |  |
| analytics.resources.analyticsJanitor.requests.cpu | string | `"250m"` |  |
| analytics.resources.analyticsJanitor.requests.memory | string | `"250Mi"` |  |
| analytics.runtimeDashboard | string | `""` |  |
| analytics.serviceAccountName | string | `"sysdig"` |  |
| analytics.vmDashboard | string | `"1"` |  |
| analytics.zones.runtime | bool | `true` |  |
| analytics.zones.v2 | bool | `true` |  |
| analytics.zones.vm | bool | `true` |  |
| global.api.serviceTokens.analytics.serviceToken | string | `""` |  |
| global.apps | string | `"secure"` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","hostname":"sysdigcloud-elasticsearch","nodeDiscovery":true,"nodeDiscoveryInterval":"10m","port":9200,"scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.secure.iac.policyService.endpoint | string | `"secure-iac-policy-service:8080"` |  |
| global.zones.platformService.endpoint | string | `"sysdigcloud-platform-zones-service-grpc:8091"` |  |
| global.zones.platformService.tlsSkip | string | `"true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# api-docs

![Version: 4.1.0-260312162907-main-v39a9586](https://img.shields.io/badge/Version-4.1.0--260312162907--main--v39a9586-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure API Docs

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| apiDocs.authorizationService.enabled | bool | `false` |  |
| apiDocs.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| apiDocs.enabled | bool | `true` |  |
| apiDocs.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-secure-api-docs"` |  |
| apiDocs.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-secure-api-docs"` |  |
| apiDocs.ingress[0].hosts[0].paths[0].openshiftTargetPort | int | `12345` |  |
| apiDocs.ingress[0].hosts[0].paths[0].path | string | `"/api/docs/secure"` |  |
| apiDocs.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-api-docs"` |  |
| apiDocs.ingress[0].hosts[0].paths[0].servicePort | int | `80` |  |
| apiDocs.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| apiDocs.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| apiDocs.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| apiDocs.ingress[0].labels.role | string | `"ingress-config"` |  |
| apiDocs.ingress[0].labels.tier | string | `"infra"` |  |
| apiDocs.ingress[0].name | string | `"sysdigcloud-api-docs"` |  |
| apiDocs.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| apiDocs.replicaCount | int | `1` |  |
| apiDocs.repositoryPrefix | string | `"secure"` |  |
| apiDocs.resources.apiDocs.limits.cpu | string | `"500m"` |  |
| apiDocs.resources.apiDocs.limits.memory | string | `"256Mi"` |  |
| apiDocs.resources.apiDocs.requests.cpu | string | `"200m"` |  |
| apiDocs.resources.apiDocs.requests.memory | string | `"50Mi"` |  |
| global.apps | string | `"secure"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# api

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig API

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| api.apiTokens.encryptionKeyBase64 | string | `""` | Random generated AES-GCM 256 bit long key (encoded in base64), can be generated with `openssl rand -base64 32` |
| api.apiTokens.encryptionKeyBase64Rotating | string | `""` |  |
| api.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| api.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| api.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| api.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| api.enabled | bool | `true` |  |
| api.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-api-ui"` |  |
| api.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-api-ui"` |  |
| api.ingress[0].hosts[0].paths[0].openshiftTargetPort | int | `8080` |  |
| api.ingress[0].hosts[0].paths[0].path | string | `"/ui"` |  |
| api.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-api"` |  |
| api.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| api.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-api-api"` |  |
| api.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-api-api"` |  |
| api.ingress[0].hosts[0].paths[1].openshiftTargetPort | int | `8080` |  |
| api.ingress[0].hosts[0].paths[1].path | string | `"/api"` |  |
| api.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-api"` |  |
| api.ingress[0].hosts[0].paths[1].servicePort | int | `8080` |  |
| api.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-api-platform"` |  |
| api.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-api-platform"` |  |
| api.ingress[0].hosts[0].paths[2].openshiftTargetPort | int | `8080` |  |
| api.ingress[0].hosts[0].paths[2].path | string | `"/platform"` |  |
| api.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-api"` |  |
| api.ingress[0].hosts[0].paths[2].servicePort | int | `8080` |  |
| api.ingress[0].hosts[0].paths[3].apiGatewayRouteName | string | `"sysdigcloud-api-monitor"` |  |
| api.ingress[0].hosts[0].paths[3].openshiftRouteName | string | `"sysdigcloud-api-monitor"` |  |
| api.ingress[0].hosts[0].paths[3].openshiftTargetPort | int | `8080` |  |
| api.ingress[0].hosts[0].paths[3].path | string | `"/monitor"` |  |
| api.ingress[0].hosts[0].paths[3].serviceName | string | `"sysdigcloud-api"` |  |
| api.ingress[0].hosts[0].paths[3].servicePort | int | `8080` |  |
| api.ingress[0].hosts[0].paths[4].apiGatewayRouteName | string | `"sysdigcloud-promql-ui"` |  |
| api.ingress[0].hosts[0].paths[4].openshiftRouteName | string | `"sysdigcloud-promql-ui"` |  |
| api.ingress[0].hosts[0].paths[4].path | string | `"/api/v2/promql"` |  |
| api.ingress[0].hosts[0].paths[4].serviceName | string | `"sysdigcloud-promql-ui"` |  |
| api.ingress[0].hosts[0].paths[4].servicePort | int | `8080` |  |
| api.ingress[0].hosts[0].paths[5].apiGatewayRouteName | string | `"sysdigcloud-api-docs"` |  |
| api.ingress[0].hosts[0].paths[5].openshiftRouteName | string | `"sysdigcloud-api-docs"` |  |
| api.ingress[0].hosts[0].paths[5].path | string | `"/apidocs"` |  |
| api.ingress[0].hosts[0].paths[5].serviceName | string | `"sysdigcloud-api"` |  |
| api.ingress[0].hosts[0].paths[5].servicePort | int | `8080` |  |
| api.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| api.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| api.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| api.ingress[0].labels.role | string | `"ingress-config"` |  |
| api.ingress[0].labels.tier | string | `"infra"` |  |
| api.ingress[0].name | string | `"sysdigcloud-api"` |  |
| api.ipAllowlistFilter.enabled | bool | `false` |  |
| api.ipAllowlistFilter.noEnforce | bool | `false` |  |
| api.jvmOptions | string | `""` |  |
| api.k8sCommands.enabled | bool | `false` |  |
| api.liveLogs.enabled | bool | `false` |  |
| api.livenessProbe.failureThreshold | int | `10` |  |
| api.livenessProbe.initialDelaySeconds | int | `0` |  |
| api.livenessProbe.periodSeconds | int | `15` |  |
| api.livenessProbe.successThreshold | int | `1` |  |
| api.livenessProbe.timeoutSeconds | int | `3` |  |
| api.monitorAdvisor.enabled | bool | `false` |  |
| api.readinessProbe.failureThreshold | int | `3` |  |
| api.readinessProbe.initialDelaySeconds | int | `0` |  |
| api.readinessProbe.periodSeconds | int | `10` |  |
| api.readinessProbe.successThreshold | int | `1` |  |
| api.readinessProbe.timeoutSeconds | int | `2` |  |
| api.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| api.replicaCount | int | `1` |  |
| api.repositoryPrefix | string | `"monitor"` |  |
| api.resources.api.limits.cpu | int | `4` |  |
| api.resources.api.limits.memory | string | `"4Gi"` |  |
| api.resources.api.requests.cpu | int | `1` |  |
| api.resources.api.requests.memory | string | `"1Gi"` |  |
| api.serviceAccountName | string | `"sysdig"` |  |
| api.serviceAccounts.encodingSecret | string | `""` |  |
| api.startupProbe.failureThreshold | int | `18` |  |
| api.startupProbe.initialDelaySeconds | int | `30` |  |
| api.startupProbe.periodSeconds | int | `10` |  |
| api.startupProbe.successThreshold | int | `1` |  |
| api.startupProbe.timeoutSeconds | int | `5` |  |
| api.teamZones.maxZonesPerTeam | int | `20` |  |
| global.admin.password | string | `"test"` |  |
| global.admin.username | string | `"test@sysdig.com"` |  |
| global.api.serviceTokens.activityAudit.serviceToken | string | `nil` |  |
| global.api.serviceTokens.admissionController.serviceToken | string | `nil` |  |
| global.api.serviceTokens.alertManager.serviceToken | string | `nil` |  |
| global.api.serviceTokens.alertNotifier.serviceToken | string | `nil` |  |
| global.api.serviceTokens.analytics.serviceToken | string | `nil` |  |
| global.api.serviceTokens.api.serviceToken | string | `nil` |  |
| global.api.serviceTokens.azureMetricsConverter.serviceToken | string | `nil` |  |
| global.api.serviceTokens.billingWorker.serviceToken | string | `nil` |  |
| global.api.serviceTokens.certman.serviceToken | string | `nil` |  |
| global.api.serviceTokens.cloudWatch.serviceToken | string | `nil` |  |
| global.api.serviceTokens.cloudauth.serviceToken | string | `nil` |  |
| global.api.serviceTokens.cloudsec.serviceToken | string | `nil` |  |
| global.api.serviceTokens.cloudwatchMetricConverter.serviceToken | string | `nil` |  |
| global.api.serviceTokens.compliance.serviceToken | string | `nil` |  |
| global.api.serviceTokens.controlPlaneShield.api.serviceToken | string | `nil` |  |
| global.api.serviceTokens.copilot.serviceToken | string | `nil` |  |
| global.api.serviceTokens.costDigest.serviceToken | string | `nil` |  |
| global.api.serviceTokens.eventMonitor.serviceToken | string | `nil` |  |
| global.api.serviceTokens.events.serviceToken | string | `nil` |  |
| global.api.serviceTokens.eventsForwarder.serviceToken | string | `nil` |  |
| global.api.serviceTokens.falcocloud.serviceToken | string | `nil` |  |
| global.api.serviceTokens.findingsApi.serviceToken | string | `nil` |  |
| global.api.serviceTokens.fingerprints.serviceToken | string | `nil` |  |
| global.api.serviceTokens.integrations.serviceToken | string | `nil` |  |
| global.api.serviceTokens.internalTools.serviceToken | string | `nil` |  |
| global.api.serviceTokens.jira.serviceToken | string | `nil` |  |
| global.api.serviceTokens.machineLearningProfiling.serviceToken | string | `nil` |  |
| global.api.serviceTokens.meerkat.serviceToken | string | `nil` |  |
| global.api.serviceTokens.meerkatAggregator.serviceToken | string | `nil` |  |
| global.api.serviceTokens.meerkatApi.serviceToken | string | `nil` |  |
| global.api.serviceTokens.meerkatCostAdvisor.serviceToken | string | `nil` |  |
| global.api.serviceTokens.metadataEnricher.serviceToken | string | `nil` |  |
| global.api.serviceTokens.metadataService.serviceToken | string | `nil` |  |
| global.api.serviceTokens.metricsAggregator.serviceToken | string | `nil` |  |
| global.api.serviceTokens.natsExternal.serviceToken | string | `nil` |  |
| global.api.serviceTokens.netsec.serviceToken | string | `nil` |  |
| global.api.serviceTokens.olapdbReporting.serviceToken | string | `nil` |  |
| global.api.serviceTokens.olapdbReportingWorker.serviceToken | string | `nil` |  |
| global.api.serviceTokens.onboarding.serviceToken | string | `nil` |  |
| global.api.serviceTokens.overview.serviceToken | string | `nil` |  |
| global.api.serviceTokens.padvisor.serviceToken | string | `nil` |  |
| global.api.serviceTokens.platformAudit.serviceToken | string | `nil` |  |
| global.api.serviceTokens.platformService.alerts.serviceToken | string | `nil` |  |
| global.api.serviceTokens.platformService.automations.serviceToken | string | `nil` |  |
| global.api.serviceTokens.platformService.zones.serviceToken | string | `nil` |  |
| global.api.serviceTokens.plotter.serviceToken | string | `nil` |  |
| global.api.serviceTokens.policies.serviceToken | string | `nil` |  |
| global.api.serviceTokens.posture.serviceToken | string | `nil` |  |
| global.api.serviceTokens.profiling.serviceToken | string | `nil` |  |
| global.api.serviceTokens.promRemoteWrite.serviceToken | string | `nil` |  |
| global.api.serviceTokens.promchap.serviceToken | string | `nil` |  |
| global.api.serviceTokens.rapidResponse.serviceToken | string | `nil` |  |
| global.api.serviceTokens.regionSync.serviceToken | string | `nil` |  |
| global.api.serviceTokens.regionSyncRead.serviceToken | string | `nil` |  |
| global.api.serviceTokens.remoteStorage.serviceToken | string | `nil` |  |
| global.api.serviceTokens.responseActions.serviceToken | string | `nil` |  |
| global.api.serviceTokens.rulesDeployer.serviceToken | string | `nil` |  |
| global.api.serviceTokens.scanning.serviceToken | string | `nil` |  |
| global.api.serviceTokens.secureDspm.serviceToken | string | `nil` |  |
| global.api.serviceTokens.secureGraphIngestion.serviceToken | string | `nil` |  |
| global.api.serviceTokens.secureGraphQuery.serviceToken | string | `nil` |  |
| global.api.serviceTokens.secureIac.serviceToken | string | `nil` |  |
| global.api.serviceTokens.secureIacCloudcollector.serviceToken | string | `nil` |  |
| global.api.serviceTokens.secureIacPolicy.serviceToken | string | `nil` |  |
| global.api.serviceTokens.secureNetworkExposureService.serviceToken | string | `nil` |  |
| global.api.serviceTokens.secureResourceComposer.serviceToken | string | `nil` |  |
| global.api.serviceTokens.secureResourceIngestion.serviceToken | string | `nil` |  |
| global.api.serviceTokens.secureRisk.serviceToken | string | `nil` |  |
| global.api.serviceTokens.sfdc.serviceToken | string | `nil` |  |
| global.api.serviceTokens.som.serviceToken | string | `nil` |  |
| global.api.serviceTokens.statefulDetections.serviceToken | string | `nil` |  |
| global.api.serviceTokens.telecaster.serviceToken | string | `nil` |  |
| global.api.serviceTokens.threats.serviceToken | string | `nil` |  |
| global.api.serviceTokens.ticketing.serviceToken | string | `nil` |  |
| global.api.serviceTokens.todo.serviceToken | string | `nil` |  |
| global.api.serviceTokens.worker.serviceToken | string | `nil` |  |
| global.apps | string | `"monitor"` |  |
| global.beacon.enabled | bool | `false` |  |
| global.beacon.promEnabled | bool | `true` |  |
| global.captures.cassandra.storage | bool | `true` |  |
| global.cassandra.datacenterName | string | `"DC1"` |  |
| global.cassandra.endpoint | string | `"sysdigcloud-cassandra"` |  |
| global.cassandra.port | int | `9042` |  |
| global.cassandra.replicaCount | int | `3` |  |
| global.cassandra.replicationStrategy | string | `"SimpleStrategy"` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.cassandra.sslVerify | bool | `false` |  |
| global.cassandra.useCertManager | bool | `false` |  |
| global.collectorPort | int | `6443` |  |
| global.credentialsEncryption.token | string | `""` | Randomly generated uuid |
| global.deployment | string | `"kubernetes"` |  |
| global.dnsName | string | `""` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","clientsConfigs":{"discovery":true,"signAWSRequests":false},"hostname":"sysdigcloud-elasticsearch","scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.helmDeploy | bool | `false` |  |
| global.iks.activityTrackerEnabled | bool | `false` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.quartz.db | string | `"quartz"` |  |
| global.legacyPostgres.postgresDatabases.quartz.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.quartz.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.quartz.username | string | `"quartz_user"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.db | string | `"sysdig"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.sysdig.username | string | `"sysdig_user"` |  |
| global.legacyRedis.redisClientsMonitor.agent.tls | bool | `true` |  |
| global.legacyRedis.redisClientsMonitor.cache.tls | bool | `true` |  |
| global.legacyRedis.redisClientsMonitor.common.tls | bool | `true` |  |
| global.legacyRedis.redisClientsMonitor.distributedJobs.tls | bool | `true` |  |
| global.legacyRedis.redisClientsMonitor.metering.tls | bool | `true` |  |
| global.legacyRedis.redisTls.enabled | bool | `true` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.legacyS3.s3.enabled | bool | `false` |  |
| global.meerkat.defaultNumCustomerShards | int | `8` |  |
| global.meerkat.enabled | bool | `false` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.prometheus.enabled | bool | `false` |  |
| global.sageUsageFetching.url | string | `"http://sysdig-copilot:80"` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.secure.sysqlApi.enabled | bool | `true` |  |
| global.secure.sysqlApi.serviceToken | string | `nil` | sysqlApi token, if value is provided it will use that value. Otherwise it will try to do a helm lookup of the secret managed by the sysql-api chart to get the correct value. In the umbrella chart scenario it will mount the secret from the sysql-api chart. |
| global.smtpProtocolSSL | bool | `false` |  |
| global.smtpProtocolTLS | bool | `false` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# azure-metrics-converter

![Version: 1.0.20260311-v8955b8c](https://img.shields.io/badge/Version-1.0.20260311--v8955b8c-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Service to pull metrics from Azure querying Azure API, convert to Prometheus format and send to a Prometheus Remote Write

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| azureMetricsConverter.azureEnabled | bool | `true` |  |
| azureMetricsConverter.cloudauth.maxReceiveSizeBytes | int | `8388608` |  |
| azureMetricsConverter.cloudauth.token | string | `nil` |  |
| azureMetricsConverter.enabled | bool | `true` |  |
| azureMetricsConverter.gcpConcurrentFetchesPerJob | int | `50` |  |
| azureMetricsConverter.gcpDescriptorsCacheTtl | string | `"24h"` |  |
| azureMetricsConverter.gcpDescriptorsCacheWithMetricsTtl | string | `"1h"` |  |
| azureMetricsConverter.gcpEnabled | bool | `true` |  |
| azureMetricsConverter.gcpMaxDescriptorsPerJob | int | `200` |  |
| azureMetricsConverter.jobQueue.concurrency | int | `10` |  |
| azureMetricsConverter.jobQueue.exporterCount | int | `100` |  |
| azureMetricsConverter.jobQueue.pollIntervalMinutes | int | `5` |  |
| azureMetricsConverter.metricQueryTimespan | string | `"-5m"` |  |
| azureMetricsConverter.providersCacheTtl | string | `"24h"` |  |
| azureMetricsConverter.quotaFlagUrl | string | `"http://sysdigcloud-api:8080/ui/customerSettings/%v/azureIntegration/quota/enabled"` |  |
| azureMetricsConverter.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| azureMetricsConverter.remoteWrite.insecureSkipVerify | bool | `true` |  |
| azureMetricsConverter.remoteWrite.url | string | `"http://sysdigcloud-beacon-prom-remote-write:80/prometheus/remote/write"` |  |
| azureMetricsConverter.replicaCount | int | `2` |  |
| azureMetricsConverter.repositoryPrefix | string | `"monitor"` |  |
| azureMetricsConverter.resources.azureMetricsConverter.limits.cpu | int | `2` |  |
| azureMetricsConverter.resources.azureMetricsConverter.limits.memory | string | `"1Gi"` |  |
| azureMetricsConverter.resources.azureMetricsConverter.requests.cpu | string | `"500m"` |  |
| azureMetricsConverter.resources.azureMetricsConverter.requests.memory | string | `"512Mi"` |  |
| azureMetricsConverter.timeseriesPerRequest | int | `10000` |  |
| global.api.serviceTokens.azureMetricsConverter.serviceToken | string | `nil` |  |
| global.clusterDomain | string | `"cluster.local"` |  |
| global.ingressNetworking | string | `""` |  |
| global.legacyPostgres.postgresDatabases.sysdig.db | string | `"sysdig"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.host | string | `"sysdig-staging-rds-encrypted.cj3wzscjzdo0.us-east-1.rds.amazonaws.com"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.sysdig.username | string | `"sysdig"` |  |
| global.legacyRedis.redisClientsMonitor.distributedJobs.tls | bool | `true` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"localhost"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.sysdigRedis.poolMaxActive | int | `10` |  |
| global.legacyRedis.sysdigRedis.poolMaxIdle | int | `1` |  |
| global.legacyRedis.sysdigRedis.username | string | `""` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.secure.cloudauth.enabled | bool | `true` |  |
| global.secure.cloudauth.tls.enabled | bool | `false` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# beacon-prom-remote-write

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Beacon Prom Remote Write Server

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| beaconPromRemoteWrite.enablePromMetadata | bool | `true` |  |
| beaconPromRemoteWrite.hpa.enabled | bool | `false` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-beacon-prom-remote-write-beacon"` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[0].apiGatewayStickySession | bool | `false` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-beacon-prom-remote-write-beacon"` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[0].openshiftTargetPort | int | `9210` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[0].path | string | `"/api/beacon"` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-beacon-prom-remote-write"` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[0].servicePort | int | `80` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-beacon-prom-remote-write-write"` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[1].apiGatewayStickySession | bool | `false` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-beacon-prom-remote-write-write"` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[1].openshiftTargetPort | int | `9210` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[1].path | string | `"/prometheus/remote/write"` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-beacon-prom-remote-write"` |  |
| beaconPromRemoteWrite.ingress[0].hosts[0].paths[1].servicePort | int | `80` |  |
| beaconPromRemoteWrite.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| beaconPromRemoteWrite.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| beaconPromRemoteWrite.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| beaconPromRemoteWrite.ingress[0].labels.role | string | `"ingress-config"` |  |
| beaconPromRemoteWrite.ingress[0].labels.tier | string | `"infra"` |  |
| beaconPromRemoteWrite.ingress[0].name | string | `"sysdigcloud-beacon-prom-remote-write"` |  |
| beaconPromRemoteWrite.javaGCParameters | string | `nil` |  |
| beaconPromRemoteWrite.jvmOptions | string | `"-Xmx8G"` |  |
| beaconPromRemoteWrite.privateEndpointCommunicationEnforcement | bool | `false` |  |
| beaconPromRemoteWrite.redis.timeout | int | `10000` |  |
| beaconPromRemoteWrite.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| beaconPromRemoteWrite.replicaCount | int | `1` |  |
| beaconPromRemoteWrite.repositoryPrefix | string | `"monitor"` |  |
| beaconPromRemoteWrite.resources.beaconPromRemoteWrite.limits.cpu | string | `"2"` |  |
| beaconPromRemoteWrite.resources.beaconPromRemoteWrite.limits.memory | string | `"8Gi"` |  |
| beaconPromRemoteWrite.resources.beaconPromRemoteWrite.requests.cpu | string | `"1"` |  |
| beaconPromRemoteWrite.resources.beaconPromRemoteWrite.requests.memory | string | `"3Gi"` |  |
| beaconPromRemoteWrite.serviceAccountName | string | `"sysdig"` |  |
| global.api.serviceTokens.promRemoteWrite | string | `nil` |  |
| global.apps | string | `"monitor"` |  |
| global.beacon.promEnabled | bool | `true` |  |
| global.grpc.auth.enabled | bool | `false` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.kafka.broker.externalPort | int | `9093` |  |
| global.kafka.name | string | `"cp-kafka"` |  |
| global.kafka.namespace | string | `"sysdigcloud"` |  |
| global.kafka.secure.enabled | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.promBeacon.admindb | string | `"sysdig"` |  |
| global.legacyPostgres.postgresDatabases.promBeacon.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.promBeacon.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.promBeacon.db | string | `"prom_beacon"` |  |
| global.legacyPostgres.postgresDatabases.promBeacon.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.promBeacon.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.promBeacon.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.promBeacon.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.promBeacon.username | string | `"pbeacon_user"` |  |
| global.legacyRedis.redisClientsMonitor.cache.tls | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.common.tls | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.ibmCache.tls | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.prws.tls | bool | `true` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.secretsManagement.generate | bool | `true` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# cassandra

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 4.1.10](https://img.shields.io/badge/AppVersion-4.1.10-informational?style=flat-square)

the Sysdig Cassandra Datastore helm chart

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| cassandra.auditLog | bool | `false` |  |
| cassandra.caCertExpiry | string | `"87660h"` | set ca cert expiry in hours |
| cassandra.caCertRenewBefore | string | `"360h"` | renew before how many hours of cert expiration |
| cassandra.cassandraExporterVersion | string | `"v1.0.21-ubi"` |  |
| cassandra.cassandraImage | string | `"cassandra"` |  |
| cassandra.cassandraVersion | string | `"4.1.10-0.2.29"` |  |
| cassandra.certificateIssuer | string | `"sysdig-selfsigned-issuer"` | certificate issuer to use, keep this empty if creating an issuer |
| cassandra.certificateIssuerKind | string | `"ClusterIssuer"` | certificate issuer kind, this can be an Issuer or ClusterIssuer |
| cassandra.clusterName | string | `"sysdig"` |  |
| cassandra.createIssuer | bool | `false` | create a cassandra certificate issuer |
| cassandra.customOverrides | string | `""` | line delimited list of config file overrides in this form "key1: value1" |
| cassandra.enableMetrics | bool | `false` | Enable prometheus metrics container |
| cassandra.endpoint | string | `"cassandra"` | set endpoint name |
| cassandra.extraAnnotations."cluster-autoscaler.kubernetes.io/safe-to-evict" | string | `"false"` |  |
| cassandra.extraAntiAffinity | list | `[]` |  |
| cassandra.extraLabels | object | `{}` | {key1: label1, key2: label2} |
| cassandra.fsGroup | int | `1000` |  |
| cassandra.jvmOptions | string | `"-Xmx1500m -Xms1500m"` | JVM options for Cassandra - Ensure max and min are set to same values |
| cassandra.multiCluster.createLB | bool | `false` |  |
| cassandra.multiCluster.enabled | bool | `false` |  |
| cassandra.multiCluster.lbAnnotations | list | `[]` |  |
| cassandra.multiCluster.overlayNetworkInitImage | string | `"us-docker.pkg.dev/sysdig-artifact-registry-prod/gar-docker/infra/network-multitool:0.0.2"` |  |
| cassandra.multiCluster.proxyTimeout | string | `"600m"` |  |
| cassandra.multiCluster.seedIP | string | `""` |  |
| cassandra.multiCluster.sidecarProxy.limits.cpu | int | `2` |  |
| cassandra.multiCluster.sidecarProxy.limits.memory | string | `"2Gi"` |  |
| cassandra.multiCluster.sidecarProxy.requests.cpu | int | `2` |  |
| cassandra.multiCluster.sidecarProxy.requests.memory | string | `"2Gi"` |  |
| cassandra.multiCluster.sidecarProxyImage | string | `"quay.io/sysdig/nginx:6.12.25"` |  |
| cassandra.multiCluster.sourceLBIP | string | `""` |  |
| cassandra.multiCluster.targetLBIP | string | `""` |  |
| cassandra.multiCluster.useOverlayNetwork | bool | `false` |  |
| cassandra.podManagementPolicy | string | `"Parallel"` |  |
| cassandra.privateKeyAlgorithm | string | `"RSA"` | private key algorithm to use |
| cassandra.privateKeySize | int | `4096` | private key size to use |
| cassandra.pvStorageSize.cassandra | string | `"1Gi"` |  |
| cassandra.readinessProbe | object | `{"cassandra":{"timeout":30},"cassandra_exporter":{"timeout":30}}` | Set the readiness probe timeout for the cassandra and/or exporter container. |
| cassandra.runAsGroup | int | `1000` |  |
| cassandra.runAsUser | int | `1000` |  |
| cassandra.securityOptional | bool | `false` | set to "true" to allow clients to connect without TLS and authentication |
| cassandra.snitch.extractCMD | string | `"echo rack1"` | Change to "awk \-\-field-separator='\-' '{print $NF}' /node-labels/topology.kubernetes.io/zone" for production to get proper zone awareness |
| cassandra.snitch.name | string | `"customGossipingPropertyFileSnitch"` | Default should work in most Kubernetes clusters. Use out-of-the-box snitches if preferred and leave exctactCMD empty. https://cassandra.apache.org/doc/latest/cassandra/architecture/snitch.html |
| cassandra.tolerations | object | `{}` | {key1: label1, key2: label2} |
| cassandra.updateStrategy | string | `"RollingUpdate"` |  |
| cassandra.upgradeToCassandra4 | bool | `false` | Set to true during upgrade from cassandra-3.x |
| global.captures.cassandra.storage | bool | `true` |  |
| global.cassandra.caSecretName | string | `"cassandra-ca-secret"` | This secret will be exported by cert-manager with the CA certificate |
| global.cassandra.datacenterName | string | `"DC1"` | This is ignored when an out-of-the-box snitch is configured |
| global.cassandra.endpoint | string | `"cassandra"` | set endpoint name |
| global.cassandra.external | bool | `false` | Configure cassandra cluster outside of Kubernetes |
| global.cassandra.password | string | `nil` | cassandra password, WARNING: if not explicitly provided it is randomly generated. When doing `helm template` to re-use the same value generated and deployed (so living in the secret in the live k8s cluster), you also need to provide the flag `--dry-run=server`. |
| global.cassandra.replicaCount | int | `1` | set number of Cassandra node replicas |
| global.cassandra.replicationStrategy | string | `"NetworkTopologyStrategy"` |  |
| global.cassandra.secure | bool | `true` | Enable cluster encryption. Please do not change this value |
| global.cassandra.ssl | bool | `true` | Enable cluster encryption |
| global.cassandra.sslCaCrt | string | `""` | Required: base64 encoded CA certificate for cassandra provided by the users; because by default cluster encryption enabled generate the certificate from the previously generated private key as follows: openssl req -new -x509 -days 3650 -extensions v3_ca -key private/cakey.pem -out certs/cacert.pem |
| global.cassandra.sslCaKey | string | `""` | Required: base64 encoded CA key for cassandra by the users; because by default cluster encryption enabled generate the private key as follows: openssl genrsa -out private/cakey.pem 4096 |
| global.cassandra.useCertManager | bool | `false` | whether to use certManager for generating certs |
| global.cassandra.user | string | `"sysdigcassandra"` |  |
| global.cassandra.workloadName | string | `"cassandra"` | Statefulset name |
| global.cloudProvider.isMultiAZ | bool | `false` | "true" spreads pods across AZs |
| global.helmDeploy | bool | `false` | Feature flag for helm installation |
| global.namespace | string | `"sysdig"` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.storageClassName | string | `"sysdig"` | name of the storage class cassandra would be using |
| global.storageClassProvisioner | string | `""` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# certman

![Version: 5.2.0-260217091115-main-v6973d25](https://img.shields.io/badge/Version-5.2.0--260217091115--main--v6973d25-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Certman

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| certman.audit.enabled | bool | `true` |  |
| certman.authorizationService.enabled | bool | `false` |  |
| certman.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| certman.enabled | bool | `true` |  |
| certman.enabledServices | string | `"EventsForwarder"` |  |
| certman.forceMigrations | bool | `false` |  |
| certman.grpc.tls.enabled | bool | `true` |  |
| certman.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-certman"` |  |
| certman.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-certman"` |  |
| certman.ingress[0].hosts[0].paths[0].path | string | `"/api/certman/v1"` |  |
| certman.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-certman"` |  |
| certman.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| certman.ingress[0].hosts[1].paths[0].apiGatewayRouteName | string | `"sysdigcloud-certman-generator"` |  |
| certman.ingress[0].hosts[1].paths[0].openshiftRouteName | string | `"sysdigcloud-certman-generator"` |  |
| certman.ingress[0].hosts[1].paths[0].path | string | `"/secure/certman/v1"` |  |
| certman.ingress[0].hosts[1].paths[0].serviceName | string | `"sysdigcloud-certman"` |  |
| certman.ingress[0].hosts[1].paths[0].servicePort | int | `7000` |  |
| certman.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| certman.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| certman.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| certman.ingress[0].labels.role | string | `"ingress-config"` |  |
| certman.ingress[0].labels.tier | string | `"infra"` |  |
| certman.ingress[0].name | string | `"sysdigcloud-certman-ingress"` |  |
| certman.janitor.cronjob | string | `"@daily"` |  |
| certman.janitor.dryRun | bool | `true` |  |
| certman.janitor.maxAllowedSolitaryDays | int | `15` |  |
| certman.password | string | `nil` |  |
| certman.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| certman.replicaCount | int | `1` |  |
| certman.repositoryPrefix | string | `"secure"` |  |
| certman.resources.certman.limits.cpu | int | `1` |  |
| certman.resources.certman.limits.memory | string | `"500Mi"` |  |
| certman.resources.certman.requests.cpu | string | `"250m"` |  |
| certman.resources.certman.requests.memory | string | `"50Mi"` |  |
| certman.resources.certmanJanitor.limits.cpu | string | `"250m"` |  |
| certman.resources.certmanJanitor.limits.memory | string | `"250Mi"` |  |
| certman.resources.certmanJanitor.requests.cpu | string | `"250m"` |  |
| certman.resources.certmanJanitor.requests.memory | string | `"250Mi"` |  |
| certman.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| certman.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| certman.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| certman.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| certman.serviceAccountName | string | `"sysdig"` |  |
| global.api.serviceTokens.certman.serviceToken | string | `""` |  |
| global.apps | string | `"secure"` |  |
| global.dnsName | string | `""` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.certman.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.certman.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.certman.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.certman.db | string | `"sysdig_db"` |  |
| global.legacyPostgres.postgresDatabases.certman.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.certman.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.certman.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.certman.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.certman.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.certman.username | string | `"sysdig_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.postgresImageName | string | `"postgresql-client"` |  |
| global.postgresVersion | string | `"0.0.50"` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# clickhouse-keeper

![Version: 1.5.0](https://img.shields.io/badge/Version-1.5.0-informational?style=flat-square) ![AppVersion: 26.2.4.23](https://img.shields.io/badge/AppVersion-26.2.4.23-informational?style=flat-square)

ClickHouse Keeper Helm Chart

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| DevOps | <devops@sysdig.com> |  |

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| clickhouseKeeper.clickhouseKeeperImage | string | `"clickhouse-keeper"` |  |
| clickhouseKeeper.clickhouseKeeperInstances | int | `3` |  |
| clickhouseKeeper.clickhouseKeeperVersion | string | `"1.2.14"` |  |
| clickhouseKeeper.clientPortEnabled | bool | `true` |  |
| clickhouseKeeper.clusterDNS | string | `"svc.cluster.local"` |  |
| clickhouseKeeper.containerSecurityContext.allowPrivilegeEscalation | bool | `false` |  |
| clickhouseKeeper.containerSecurityContext.capabilities.drop[0] | string | `"ALL"` |  |
| clickhouseKeeper.containerSecurityContext.readOnlyRootFilesystem | bool | `false` |  |
| clickhouseKeeper.coordinationSettings.compressLogs | bool | `false` |  |
| clickhouseKeeper.coordinationSettings.operationTimeoutMs | int | `10000` |  |
| clickhouseKeeper.coordinationSettings.sessionTimeoutMs | int | `100000` |  |
| clickhouseKeeper.enableReconfiguration | bool | `false` |  |
| clickhouseKeeper.extraAnnotations."cluster-autoscaler.kubernetes.io/safe-to-evict" | string | `"false"` |  |
| clickhouseKeeper.extraAnnotations."prometheus.io/path" | string | `"/metrics"` |  |
| clickhouseKeeper.extraAnnotations."prometheus.io/port" | string | `"7000"` |  |
| clickhouseKeeper.extraAnnotations."prometheus.io/scrape" | string | `"true"` |  |
| clickhouseKeeper.extraAntiAffinity | list | `[]` |  |
| clickhouseKeeper.fullname | string | `"clickhouse-keeper"` |  |
| clickhouseKeeper.hostpathInit.resources.limits.cpu | string | `"50m"` |  |
| clickhouseKeeper.hostpathInit.resources.limits.memory | string | `"100Mi"` |  |
| clickhouseKeeper.hostpathInit.resources.requests.cpu | string | `"50m"` |  |
| clickhouseKeeper.hostpathInit.resources.requests.memory | string | `"100Mi"` |  |
| clickhouseKeeper.labels.affinity | string | `"clickhouse-keeper"` |  |
| clickhouseKeeper.labels.app | string | `"sysdig"` |  |
| clickhouseKeeper.labels.role | string | `"clickhouse-keeper"` |  |
| clickhouseKeeper.livenessProbe.timeoutSeconds | int | `10` |  |
| clickhouseKeeper.multiCluster.enabled | bool | `false` |  |
| clickhouseKeeper.multiCluster.roles[0] | string | `"source"` |  |
| clickhouseKeeper.multiCluster.roles[1] | string | `"dest"` |  |
| clickhouseKeeper.multiCluster.side | string | `"source"` |  |
| clickhouseKeeper.multiCluster.stableDNSSvc | bool | `false` |  |
| clickhouseKeeper.name | string | `"clickhouse-keeper"` |  |
| clickhouseKeeper.offset | int | `0` |  |
| clickhouseKeeper.podSecurityContext.fsGroup | int | `1000` |  |
| clickhouseKeeper.podSecurityContext.runAsGroup | int | `1000` |  |
| clickhouseKeeper.podSecurityContext.runAsNonRoot | bool | `true` |  |
| clickhouseKeeper.podSecurityContext.runAsUser | int | `1000` |  |
| clickhouseKeeper.podSecurityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| clickhouseKeeper.ports.health | int | `7001` |  |
| clickhouseKeeper.ports.metrics | int | `7000` |  |
| clickhouseKeeper.ports.raft | int | `9234` |  |
| clickhouseKeeper.ports.secureTCP | int | `9281` |  |
| clickhouseKeeper.ports.tcp | int | `9181` |  |
| clickhouseKeeper.raftConfig.enabled | bool | `false` |  |
| clickhouseKeeper.readinessProbe.timeoutSeconds | int | `20` |  |
| clickhouseKeeper.resources.limits.cpu | string | `"500m"` |  |
| clickhouseKeeper.resources.limits.memory | string | `"1Gi"` |  |
| clickhouseKeeper.resources.requests.cpu | string | `"500m"` |  |
| clickhouseKeeper.resources.requests.memory | string | `"1Gi"` |  |
| clickhouseKeeper.service.name | string | `"clickhouse-keeper"` |  |
| clickhouseKeeper.storage.accessModes[0] | string | `"ReadWriteOnce"` |  |
| clickhouseKeeper.storage.hostPathCustomPath | string | `"/var/lib/clickhouse-keeper"` |  |
| clickhouseKeeper.storage.mountPath | string | `"/var/lib/clickhouse-keeper/"` |  |
| clickhouseKeeper.storage.size | string | `"20Gi"` |  |
| clickhouseKeeper.storage.storageClass | string | `""` |  |
| clickhouseKeeper.tls.certsMountPath | string | `"/etc/clickhouse-keeper/certs"` |  |
| clickhouseKeeper.tls.serverVerificationMode | string | `"relaxed"` |  |
| clickhouseKeeper.updateStrategy.rollingUpdate.partition | int | `0` |  |
| clickhouseKeeper.updateStrategy.type | string | `"RollingUpdate"` |  |
| global.certManager.enabled | bool | `false` |  |
| global.clickhouse.enabled | bool | `true` |  |
| global.clickhouse.keeper.instances | int | `3` |  |
| global.clickhouse.keeper.name | string | `"clickhouse-keeper"` |  |
| global.clickhouse.keeper.port | int | `9181` |  |
| global.clickhouse.keeper.securePort | int | `9281` |  |
| global.clickhouse.keeper.serviceName | string | `"clickhouse-keeper"` |  |
| global.clickhouse.tls.enabled | bool | `true` |  |
| global.clickhouse.tls.fips | bool | `false` |  |
| global.clickhouse.tls.useCertManager | bool | `true` |  |
| global.cloudProvider.isMultiAZ | bool | `true` |  |
| global.cloudProvider.name | string | `"aws"` |  |
| global.namespace | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# clickhouse-shards

![Version: 1.5.0](https://img.shields.io/badge/Version-1.5.0-informational?style=flat-square) ![AppVersion: 26.2.4.23](https://img.shields.io/badge/AppVersion-26.2.4.23-informational?style=flat-square)

ClickHouse Helm Chart

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| DevOps | <devops@sysdig.com> |  |

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| clickhouseShards.adminUsername | string | `"admin"` |  |
| clickhouseShards.clickhouseBackup.BACKUPS_TO_KEEP_LOCAL | int | `-1` |  |
| clickhouseShards.clickhouseBackup.BACKUPS_TO_KEEP_REMOTE | int | `0` |  |
| clickhouseShards.clickhouseBackup.CLICKHOUSE_HOST | string | `"localhost"` |  |
| clickhouseShards.clickhouseBackup.GCS_DAILY_BUCKET | string | `"daily-bucket"` |  |
| clickhouseShards.clickhouseBackup.GCS_MONTHLY_BUCKET | string | `"monthly-bucket"` |  |
| clickhouseShards.clickhouseBackup.GCS_WEEKLY_BUCKET | string | `"weekly-bucket"` |  |
| clickhouseShards.clickhouseBackup.IBM_DAILY_BUCKET | string | `"daily-bucket"` |  |
| clickhouseShards.clickhouseBackup.IBM_MONTHLY_BUCKET | string | `"monthly-bucket"` |  |
| clickhouseShards.clickhouseBackup.IBM_WEEKLY_BUCKET | string | `"weekly-bucket"` |  |
| clickhouseShards.clickhouseBackup.REMOTE_STORAGE | string | `"s3"` |  |
| clickhouseShards.clickhouseBackup.S3_ACCESS_KEY | string | `""` |  |
| clickhouseShards.clickhouseBackup.S3_ACL | string | `""` |  |
| clickhouseShards.clickhouseBackup.S3_BUCKET | string | `"backups-bucket"` |  |
| clickhouseShards.clickhouseBackup.S3_ENDPOINT | string | `""` |  |
| clickhouseShards.clickhouseBackup.S3_FORCE_PATH_STYLE | string | `"true"` |  |
| clickhouseShards.clickhouseBackup.S3_REGION | string | `"us-east-1"` |  |
| clickhouseShards.clickhouseBackup.S3_SECRET_KEY | string | `""` |  |
| clickhouseShards.clickhouseBackup.UPLOAD_MAX_BYTES_PER_SECOND | int | `262144000` |  |
| clickhouseShards.clickhouseBackup.crontab | string | `"30 1-23 * * * /clickhouse-backup-scripts/clickhouse-backup.sh hourly\n30 0 * * 0-5 /clickhouse-backup-scripts/clickhouse-backup.sh daily\n30 0 * * 6 /clickhouse-backup-scripts/clickhouse-backup.sh weekly\n30 0 5 * * /clickhouse-backup-scripts/clickhouse-backup.sh monthly\n"` |  |
| clickhouseShards.clickhouseBackup.enabled | bool | `true` |  |
| clickhouseShards.clickhouseBackupFIPSVersion | string | `"1.0.26-fips"` |  |
| clickhouseShards.clickhouseBackupIBMVersion | string | `"1.0.27-ibm"` |  |
| clickhouseShards.clickhouseBackupImage | string | `"clickhouse-backup"` |  |
| clickhouseShards.clickhouseBackupVersion | string | `"1.0.25"` |  |
| clickhouseShards.clickhouseImage | string | `"clickhouse-server"` |  |
| clickhouseShards.clickhouseKeeper.name | string | `"clickhouse-keeper"` |  |
| clickhouseShards.clickhouseKeeper.svcName | string | `"clickhouse-keeper"` |  |
| clickhouseShards.clickhouseVersion | string | `"1.2.14"` |  |
| clickhouseShards.clusterDNS | string | `"svc.cluster.local"` |  |
| clickhouseShards.config.additionalConfig | object | `{}` |  |
| clickhouseShards.config.quota.duration | int | `3600` |  |
| clickhouseShards.config.quota.errors | int | `0` |  |
| clickhouseShards.config.quota.executionTime | int | `0` |  |
| clickhouseShards.config.quota.queries | int | `0` |  |
| clickhouseShards.config.quota.readRows | int | `0` |  |
| clickhouseShards.config.quota.resultRows | int | `0` |  |
| clickhouseShards.config.systemLogTTL.enabled | bool | `true` |  |
| clickhouseShards.config.systemLogTTL.tables.asynchronous_metric_log.engine | string | `"ENGINE = MergeTree PARTITION BY event_date ORDER BY (metric, event_date, event_time) TTL event_date + INTERVAL 7 DAY DELETE"` |  |
| clickhouseShards.config.systemLogTTL.tables.asynchronous_metric_log.flush_interval_milliseconds | int | `7500` |  |
| clickhouseShards.config.systemLogTTL.tables.metric_log.engine | string | `"ENGINE = MergeTree PARTITION BY event_date ORDER BY (event_time) TTL event_date + INTERVAL 7 DAY DELETE"` |  |
| clickhouseShards.config.systemLogTTL.tables.metric_log.flush_interval_milliseconds | int | `7500` |  |
| clickhouseShards.config.systemLogTTL.tables.part_log.engine | string | `"ENGINE = MergeTree PARTITION BY event_date ORDER BY (event_time) TTL event_date + INTERVAL 14 DAY DELETE"` |  |
| clickhouseShards.config.systemLogTTL.tables.part_log.flush_interval_milliseconds | int | `7500` |  |
| clickhouseShards.config.systemLogTTL.tables.processors_profile_log.engine | string | `"ENGINE = MergeTree PARTITION BY event_date ORDER BY (event_time) TTL event_date + INTERVAL 3 DAY DELETE"` |  |
| clickhouseShards.config.systemLogTTL.tables.processors_profile_log.flush_interval_milliseconds | int | `7500` |  |
| clickhouseShards.config.systemLogTTL.tables.query_log.engine | string | `"ENGINE = MergeTree PARTITION BY event_date ORDER BY (event_time) TTL event_date + INTERVAL 14 DAY DELETE"` |  |
| clickhouseShards.config.systemLogTTL.tables.query_log.flush_interval_milliseconds | int | `7500` |  |
| clickhouseShards.config.systemLogTTL.tables.query_metric_log.engine | string | `"ENGINE = MergeTree PARTITION BY event_date ORDER BY (event_time) TTL event_date + INTERVAL 3 DAY DELETE"` |  |
| clickhouseShards.config.systemLogTTL.tables.query_metric_log.flush_interval_milliseconds | int | `7500` |  |
| clickhouseShards.config.systemLogTTL.tables.query_views_log.engine | string | `"ENGINE = MergeTree PARTITION BY event_date ORDER BY (event_time) TTL event_date + INTERVAL 14 DAY DELETE"` |  |
| clickhouseShards.config.systemLogTTL.tables.query_views_log.flush_interval_milliseconds | int | `7500` |  |
| clickhouseShards.config.systemLogTTL.tables.text_log.engine | string | `"ENGINE = MergeTree PARTITION BY event_date ORDER BY (event_time) TTL event_date + INTERVAL 7 DAY DELETE"` |  |
| clickhouseShards.config.systemLogTTL.tables.text_log.flush_interval_milliseconds | int | `7500` |  |
| clickhouseShards.config.systemLogTTL.tables.trace_log.engine | string | `"ENGINE = MergeTree PARTITION BY event_date ORDER BY (event_time) TTL event_date + INTERVAL 3 DAY DELETE"` |  |
| clickhouseShards.config.systemLogTTL.tables.trace_log.flush_interval_milliseconds | int | `7500` |  |
| clickhouseShards.config.userProfiles.admin.background_distributed_schedule_pool_size | int | `8` |  |
| clickhouseShards.config.userProfiles.admin.httpReceiveTimeout | int | `300` |  |
| clickhouseShards.config.userProfiles.admin.httpSendTimeout | int | `300` |  |
| clickhouseShards.config.userProfiles.admin.maxBytesBeforeExternalGroupBy | int | `6442450944` |  |
| clickhouseShards.config.userProfiles.admin.maxBytesBeforeExternalSort | int | `6442450944` |  |
| clickhouseShards.config.userProfiles.admin.maxMemUsage | int | `8589934592` |  |
| clickhouseShards.config.userProfiles.admin.receiveTimeout | int | `600` |  |
| clickhouseShards.config.userProfiles.admin.sendTimeout | int | `600` |  |
| clickhouseShards.config.userProfiles.reader.aggregationMemMergeThreads | int | `4` |  |
| clickhouseShards.config.userProfiles.reader.background_distributed_schedule_pool_size | int | `8` |  |
| clickhouseShards.config.userProfiles.reader.distributedProductMode | string | `"allow"` |  |
| clickhouseShards.config.userProfiles.reader.httpReceiveTimeout | int | `300` |  |
| clickhouseShards.config.userProfiles.reader.httpSendTimeout | int | `300` |  |
| clickhouseShards.config.userProfiles.reader.maxBlockSize | int | `32705` |  |
| clickhouseShards.config.userProfiles.reader.maxBytesBeforeExternalGroupBy | int | `6442450944` |  |
| clickhouseShards.config.userProfiles.reader.maxBytesBeforeExternalSort | int | `6442450944` |  |
| clickhouseShards.config.userProfiles.reader.maxMemUsage | int | `12884901888` |  |
| clickhouseShards.config.userProfiles.reader.readonly | int | `2` |  |
| clickhouseShards.config.userProfiles.reader.receiveTimeout | int | `600` |  |
| clickhouseShards.config.userProfiles.reader.sendTimeout | int | `600` |  |
| clickhouseShards.config.userProfiles.writer.asyncInsert | int | `1` |  |
| clickhouseShards.config.userProfiles.writer.asyncInsertBusyTimeout | int | `10000` |  |
| clickhouseShards.config.userProfiles.writer.asyncInsertMaxDataSize | int | `104857600` |  |
| clickhouseShards.config.userProfiles.writer.background_distributed_schedule_pool_size | int | `8` |  |
| clickhouseShards.config.userProfiles.writer.enableAsync | bool | `false` |  |
| clickhouseShards.config.userProfiles.writer.httpReceiveTimeout | int | `300` |  |
| clickhouseShards.config.userProfiles.writer.httpSendTimeout | int | `300` |  |
| clickhouseShards.config.userProfiles.writer.maxBlockSize | int | `32705` |  |
| clickhouseShards.config.userProfiles.writer.maxBytesBeforeExternalGroupBy | int | `6442450944` |  |
| clickhouseShards.config.userProfiles.writer.maxBytesBeforeExternalSort | int | `6442450944` |  |
| clickhouseShards.config.userProfiles.writer.maxInsertThreads | int | `4` |  |
| clickhouseShards.config.userProfiles.writer.maxMemUsage | int | `8589934592` |  |
| clickhouseShards.config.userProfiles.writer.minInsertBlockSizeBytes | int | `1342177280` |  |
| clickhouseShards.config.userProfiles.writer.minInsertBlockSizeRows | int | `0` |  |
| clickhouseShards.config.userProfiles.writer.receiveTimeout | int | `600` |  |
| clickhouseShards.config.userProfiles.writer.sendTimeout | int | `600` |  |
| clickhouseShards.config.userProfiles.writer.waitAsyncInsert | int | `0` |  |
| clickhouseShards.containerSecurityContext.allowPrivilegeEscalation | bool | `false` |  |
| clickhouseShards.containerSecurityContext.capabilities.drop[0] | string | `"ALL"` |  |
| clickhouseShards.containerSecurityContext.readOnlyRootFilesystem | bool | `false` |  |
| clickhouseShards.enablePostgresSupport | bool | `false` |  |
| clickhouseShards.extraAnnotations."cluster-autoscaler.kubernetes.io/safe-to-evict" | string | `"false"` |  |
| clickhouseShards.extraAnnotations."prometheus.io/path" | string | `"/metrics"` |  |
| clickhouseShards.extraAnnotations."prometheus.io/port" | string | `"9363"` |  |
| clickhouseShards.extraAnnotations."prometheus.io/scrape" | string | `"true"` |  |
| clickhouseShards.extraAntiAffinity | list | `[]` |  |
| clickhouseShards.fullname | string | `"clickhouse-shard"` |  |
| clickhouseShards.keeperConfigOverride.config | object | `{}` |  |
| clickhouseShards.keeperConfigOverride.enabled | bool | `false` |  |
| clickhouseShards.labels.affinity | string | `"clickhouse-shards"` |  |
| clickhouseShards.labels.app | string | `"sysdig"` |  |
| clickhouseShards.labels.role | string | `"clickhouse-shards"` |  |
| clickhouseShards.labels.type | string | `"multi-shard"` |  |
| clickhouseShards.livenessProbe.failureThreshold | int | `6` |  |
| clickhouseShards.livenessProbe.initialDelaySeconds | int | `60` |  |
| clickhouseShards.livenessProbe.periodSeconds | int | `15` |  |
| clickhouseShards.livenessProbe.timeoutSeconds | int | `10` |  |
| clickhouseShards.multiCluster.enabled | bool | `false` |  |
| clickhouseShards.multiCluster.roles[0] | string | `"source"` |  |
| clickhouseShards.multiCluster.roles[1] | string | `"dest"` |  |
| clickhouseShards.multiCluster.side | string | `"source"` |  |
| clickhouseShards.multiCluster.stableDNSSvc | bool | `false` |  |
| clickhouseShards.name | string | `"clickhouse"` |  |
| clickhouseShards.podSecurityContext.fsGroupChangePolicy | string | `"OnRootMismatch"` |  |
| clickhouseShards.podSecurityContext.runAsNonRoot | bool | `true` |  |
| clickhouseShards.podSecurityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| clickhouseShards.ports.http | int | `8123` |  |
| clickhouseShards.ports.https | int | `8443` |  |
| clickhouseShards.ports.interNodeTLS | int | `9010` |  |
| clickhouseShards.ports.interServer | int | `9009` |  |
| clickhouseShards.ports.metrics | int | `9363` |  |
| clickhouseShards.ports.postgres | int | `9005` |  |
| clickhouseShards.ports.secureTCP | int | `9440` |  |
| clickhouseShards.ports.tcp | int | `9000` |  |
| clickhouseShards.postStartHook.command | string | `"clickhouse-client --user=$CLICKHOUSE_ADMIN_USER --password=$CLICKHOUSE_ADMIN_PASSWORD --port=$CLICKHOUSE_PORT $CLICKHOUSE_SECURE_FLAG --query=\"\n  SELECT 'DROP TABLE IF EXISTS system.' || name || ';'\n  FROM system.tables\n  WHERE database = 'system'\n    AND engine = 'MergeTree'\n    AND name REGEXP '.*_log_[0-9]+$'\n\" | clickhouse-client --user=$CLICKHOUSE_ADMIN_USER --password=$CLICKHOUSE_ADMIN_PASSWORD --port=$CLICKHOUSE_PORT $CLICKHOUSE_SECURE_FLAG --multiquery\n"` |  |
| clickhouseShards.postStartHook.enabled | bool | `true` |  |
| clickhouseShards.readinessProbe.failureThreshold | int | `3` |  |
| clickhouseShards.readinessProbe.initialDelaySeconds | int | `15` |  |
| clickhouseShards.readinessProbe.periodSeconds | int | `10` |  |
| clickhouseShards.readinessProbe.timeoutSeconds | int | `20` |  |
| clickhouseShards.replicaCount | int | `3` |  |
| clickhouseShards.replicaOffsetOverride.enabled | bool | `false` |  |
| clickhouseShards.replicaOffsetOverride.offset | string | `"dest"` |  |
| clickhouseShards.resources.clickhouse.limits.cpu | int | `4` |  |
| clickhouseShards.resources.clickhouse.limits.memory | string | `"8Gi"` |  |
| clickhouseShards.resources.clickhouse.requests.cpu | int | `4` |  |
| clickhouseShards.resources.clickhouse.requests.memory | string | `"8Gi"` |  |
| clickhouseShards.resources.clickhouseBackup.limits.cpu | int | `1` |  |
| clickhouseShards.resources.clickhouseBackup.limits.memory | string | `"2Gi"` |  |
| clickhouseShards.resources.clickhouseBackup.requests.cpu | string | `"100m"` |  |
| clickhouseShards.resources.clickhouseBackup.requests.memory | string | `"100Mi"` |  |
| clickhouseShards.resources.hostpathInit.limits.cpu | string | `"50m"` |  |
| clickhouseShards.resources.hostpathInit.limits.memory | string | `"100Mi"` |  |
| clickhouseShards.resources.hostpathInit.requests.cpu | string | `"50m"` |  |
| clickhouseShards.resources.hostpathInit.requests.memory | string | `"100Mi"` |  |
| clickhouseShards.service.name | string | `"clickhouse-shards"` |  |
| clickhouseShards.shardConfigOverride.config | object | `{}` |  |
| clickhouseShards.shardConfigOverride.enabled | bool | `false` |  |
| clickhouseShards.shardCount | int | `3` |  |
| clickhouseShards.storage.extraLocalVolumes.enabled | bool | `false` |  |
| clickhouseShards.storage.extraLocalVolumes.moveFactor | float | `0.25` |  |
| clickhouseShards.storage.extraLocalVolumes.storageClass | string | `""` |  |
| clickhouseShards.storage.extraLocalVolumes.volumes[0].accessModes[0] | string | `"ReadWriteOnce"` |  |
| clickhouseShards.storage.extraLocalVolumes.volumes[0].mountPath | string | `"/var/lib/clickhouse-ext1/"` |  |
| clickhouseShards.storage.extraLocalVolumes.volumes[0].name | string | `"ch-data-ext1"` |  |
| clickhouseShards.storage.extraLocalVolumes.volumes[0].size | string | `"100Gi"` |  |
| clickhouseShards.storage.hostPathCustomPath | string | `"/var/lib/clickhouse"` |  |
| clickhouseShards.storage.hotcold.enabled | bool | `false` |  |
| clickhouseShards.storage.localVolume.accessModes[0] | string | `"ReadWriteOnce"` |  |
| clickhouseShards.storage.localVolume.enabled | bool | `true` |  |
| clickhouseShards.storage.localVolume.mountPath | string | `"/var/lib/clickhouse/"` |  |
| clickhouseShards.storage.localVolume.name | string | `"clickhouse-data"` |  |
| clickhouseShards.storage.localVolume.size | string | `"100Gi"` |  |
| clickhouseShards.storage.localVolume.storageClass | string | `""` |  |
| clickhouseShards.storage.queryVolume.accessModes[0] | string | `"ReadWriteOnce"` |  |
| clickhouseShards.storage.queryVolume.enabled | bool | `true` |  |
| clickhouseShards.storage.queryVolume.mountPath | string | `"/opt/clickhouse/"` |  |
| clickhouseShards.storage.queryVolume.name | string | `"clickhouse-query-data"` |  |
| clickhouseShards.storage.queryVolume.size | string | `"100Gi"` |  |
| clickhouseShards.storage.queryVolume.storageClass | string | `""` |  |
| clickhouseShards.storage.s3.enabled | bool | `false` |  |
| clickhouseShards.storage.shardOverrides | object | `{}` |  |
| clickhouseShards.tabix.enabled | bool | `false` |  |
| clickhouseShards.tls.certsMountPath | string | `"/etc/clickhouse-server/certs"` |  |
| clickhouseShards.tls.serverVerificationMode | string | `"relaxed"` |  |
| global.certManager.enabled | bool | `false` |  |
| global.clickhouse.adminPassword | string | `nil` |  |
| global.clickhouse.defaultDb | string | `"sysdig"` |  |
| global.clickhouse.enabled | bool | `true` |  |
| global.clickhouse.keeper.instances | int | `3` |  |
| global.clickhouse.keeper.name | string | `"clickhouse-keeper"` |  |
| global.clickhouse.keeper.port | int | `9181` |  |
| global.clickhouse.keeper.securePort | int | `9281` |  |
| global.clickhouse.keeper.serviceName | string | `"clickhouse-keeper"` |  |
| global.clickhouse.readerPassword | string | `nil` |  |
| global.clickhouse.tls.enabled | bool | `true` |  |
| global.clickhouse.tls.fips | bool | `false` |  |
| global.clickhouse.tls.useCertManager | bool | `true` |  |
| global.clickhouse.writerPassword | string | `nil` |  |
| global.cloudProvider.isMultiAZ | bool | `true` |  |
| global.cloudProvider.name | string | `"aws"` |  |
| global.namespace | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# cloudsec

![Version: 5.0.0-260312155045-main-v265bb33](https://img.shields.io/badge/Version-5.0.0--260312155045--main--v265bb33-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Cloud Security

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| cloudsec.api.logLevel | string | `"info"` |  |
| cloudsec.api.serviceAccountName | string | `"sysdig"` |  |
| cloudsec.audit.enabled | bool | `true` |  |
| cloudsec.collector.cloudauth.grpc.endpointAddress | string | `"sysdigcloud-cloudauth-api-grpc:6000"` |  |
| cloudsec.collector.cloudauth.grpc.gzipCompressorEnabled | bool | `true` |  |
| cloudsec.collector.cloudauth.grpc.maxReceiveMessageSize | string | `"33554432"` |  |
| cloudsec.collector.cloudauth.grpc.maxRetries | int | `7` |  |
| cloudsec.collector.cloudauth.grpc.maxRetryDelay | string | `"500ms"` |  |
| cloudsec.collector.cloudauth.identityEntitlement.accountsLister.pageSize | int | `500` |  |
| cloudsec.collector.cloudauth.identityEntitlement.accountsLister.type | string | `"paginated"` |  |
| cloudsec.collector.dryRunEnabled | string | `"true"` |  |
| cloudsec.collector.enabled | bool | `false` |  |
| cloudsec.collector.logLevel | string | `"info"` |  |
| cloudsec.collector.storage.bucketExpiration | string | `"10m"` |  |
| cloudsec.collector.storage.bucketMaxPoolSize | int | `8` |  |
| cloudsec.collector.storage.bucketType | string | `"durable"` |  |
| cloudsec.collector.storage.keyType | string | `"hash"` |  |
| cloudsec.collector.stream.dispatchAddress | string | `"sysdigcloud-events-dispatcher:8080"` |  |
| cloudsec.collector.stream.maxExporters | int | `1` |  |
| cloudsec.collector.stream.maxProcessors | int | `1` |  |
| cloudsec.collectorReplicaCount | int | `2` |  |
| cloudsec.enabled | bool | `true` |  |
| cloudsec.graph.enabled | bool | `true` |  |
| cloudsec.graph.nats.enabled | bool | `false` |  |
| cloudsec.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-cloudsec-api"` |  |
| cloudsec.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-cloudsec-api"` |  |
| cloudsec.ingress[0].hosts[0].paths[0].path | string | `"/api/cloud/v2"` |  |
| cloudsec.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-cloudsec-api"` |  |
| cloudsec.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| cloudsec.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| cloudsec.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| cloudsec.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| cloudsec.ingress[0].labels.role | string | `"ingress-config"` |  |
| cloudsec.ingress[0].labels.tier | string | `"infra"` |  |
| cloudsec.ingress[0].name | string | `"sysdigcloud-cloudsec-ingress"` |  |
| cloudsec.proxy.enable | bool | `false` |  |
| cloudsec.prwsToken | string | `""` |  |
| cloudsec.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| cloudsec.replicaCount | int | `4` |  |
| cloudsec.repositoryPrefix | string | `"secure"` |  |
| cloudsec.resources.cloudsecApi.limits.cpu | int | `4` |  |
| cloudsec.resources.cloudsecApi.limits.memory | string | `"8Gi"` |  |
| cloudsec.resources.cloudsecApi.requests.cpu | int | `2` |  |
| cloudsec.resources.cloudsecApi.requests.memory | string | `"4Gi"` |  |
| cloudsec.resources.cloudsecCollector.limits.cpu | int | `4` |  |
| cloudsec.resources.cloudsecCollector.limits.memory | string | `"2Gi"` |  |
| cloudsec.resources.cloudsecCollector.requests.cpu | int | `2` |  |
| cloudsec.resources.cloudsecCollector.requests.memory | string | `"1Gi"` |  |
| cloudsec.resources.cloudsecWorker.limits.cpu | int | `4` |  |
| cloudsec.resources.cloudsecWorker.limits.memory | string | `"2Gi"` |  |
| cloudsec.resources.cloudsecWorker.requests.cpu | int | `2` |  |
| cloudsec.resources.cloudsecWorker.requests.memory | string | `"1Gi"` |  |
| cloudsec.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| cloudsec.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| cloudsec.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| cloudsec.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| cloudsec.sysdigJiraAssignee | string | `"Aesha-Choksi"` |  |
| cloudsec.sysdigOwner | string | `"Sysdig-CIEM-team"` |  |
| cloudsec.sysql.api.rpcAuthEnabled | string | `"true"` |  |
| cloudsec.sysql.api.rpcEndpoint | string | `"secure-sysql-api:6000"` |  |
| cloudsec.sysql.grammarVersion | string | `"0.17.23"` |  |
| cloudsec.taskEnabled | bool | `true` |  |
| cloudsec.taskRateLimit | string | `"10000"` |  |
| cloudsec.taskRateLimitEnabled | bool | `true` |  |
| cloudsec.worker.logLevel | string | `"info"` |  |
| cloudsec.workerReplicaCount | int | `8` |  |
| global.api.serviceTokens.cloudsec.serviceToken | string | `""` |  |
| global.apps | string | `"secure"` |  |
| global.azurePrincipal.auth.clientId | string | `""` |  |
| global.azurePrincipal.auth.clientSecret | string | `""` |  |
| global.azurePrincipal.clientId | string | `""` |  |
| global.azurePrincipal.clientSecret | string | `""` |  |
| global.azurePrincipal.tenantId | string | `""` |  |
| global.cloudProvider.name | string | `""` |  |
| global.cloudProvider.region | string | `""` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.cloudsec.admindb | string | `"anchore"` |  |
| global.legacyPostgres.postgresDatabases.cloudsec.adminpassword | string | `""` |  |
| global.legacyPostgres.postgresDatabases.cloudsec.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.cloudsec.db | string | `"cloudsec"` |  |
| global.legacyPostgres.postgresDatabases.cloudsec.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.cloudsec.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.cloudsec.password | string | `""` |  |
| global.legacyPostgres.postgresDatabases.cloudsec.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.cloudsec.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.cloudsec.username | string | `"cloudsec_user"` |  |
| global.legacyRedis.redisClientsSecure.cloudsec.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `nil` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.namespace | string | `"sysdig"` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.secure.cloudOnboardingConfig.aws.gov.enabled | bool | `false` |  |
| global.secure.cloudsec.githubToken | string | `""` |  |
| global.secure.iamUser.accessKey | string | `""` |  |
| global.secure.iamUser.region | string | `""` |  |
| global.secure.iamUser.secretKey | string | `""` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.secure.sysqlApi | object | `{"enabled":true,"serviceToken":null}` | sysqlApi Token mounted from sysql-api chart secret |
| global.secure.trustedIdentity.aws | string | `""` |  |
| global.secure.trustedIdentity.azure | string | `""` |  |
| global.secure.trustedIdentity.gcp | string | `""` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# cloudwatch-metric-streams-converter

![Version: 1.1.20260304-v1a0ad09](https://img.shields.io/badge/Version-1.1.20260304--v1a0ad09-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Service to consume stream of Cloudwatch metrics, convert to Prometheus format and send to a Prometheus Remote Write

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| cloudwatchMetricStreamsConverter.enabled | bool | `true` |  |
| cloudwatchMetricStreamsConverter.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdig-cloudwatch-metric-streams-converter"` |  |
| cloudwatchMetricStreamsConverter.ingress[0].hosts[0].paths[0].path | string | `"/api/awsmetrics/v1/input"` |  |
| cloudwatchMetricStreamsConverter.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdig-cloudwatch-metric-streams-converter"` |  |
| cloudwatchMetricStreamsConverter.ingress[0].hosts[0].paths[0].servicePort | int | `10101` |  |
| cloudwatchMetricStreamsConverter.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| cloudwatchMetricStreamsConverter.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| cloudwatchMetricStreamsConverter.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| cloudwatchMetricStreamsConverter.ingress[0].labels.role | string | `"ingress-config"` |  |
| cloudwatchMetricStreamsConverter.ingress[0].labels.tier | string | `"infra"` |  |
| cloudwatchMetricStreamsConverter.ingress[0].name | string | `"sysdig-cloudwatch-metric-streams-converter"` |  |
| cloudwatchMetricStreamsConverter.port | int | `10101` |  |
| cloudwatchMetricStreamsConverter.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| cloudwatchMetricStreamsConverter.remoteWrite.insecureSkipVerify | bool | `false` |  |
| cloudwatchMetricStreamsConverter.replicaCount | int | `2` |  |
| cloudwatchMetricStreamsConverter.repositoryPrefix | string | `"monitor"` |  |
| cloudwatchMetricStreamsConverter.resources.cloudwatchMetricStreamsConverter.limits.cpu | int | `2` |  |
| cloudwatchMetricStreamsConverter.resources.cloudwatchMetricStreamsConverter.limits.memory | string | `"1Gi"` |  |
| cloudwatchMetricStreamsConverter.resources.cloudwatchMetricStreamsConverter.requests.cpu | string | `"500m"` |  |
| cloudwatchMetricStreamsConverter.resources.cloudwatchMetricStreamsConverter.requests.memory | string | `"512Mi"` |  |
| cloudwatchMetricStreamsConverter.serviceAccountName | string | `"sysdig"` |  |
| global.api.serviceTokens.cloudwatchMetricConverter.serviceToken | string | `nil` |  |
| global.kafka.broker.externalPort | int | `9093` |  |
| global.kafka.name | string | `"cp-kafka"` |  |
| global.kafka.namespace | string | `"sysdigcloud"` |  |
| global.kafka.secure.enabled | bool | `false` |  |
| global.namespace | string | `"sysdigcloud"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# collector

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig Collector

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| collector.certificate.externalSecretName | string | `"sysdigcloud-ssl-secret"` |  |
| collector.certificate.useExternalSecret | bool | `false` |  |
| collector.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| collector.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| collector.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| collector.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| collector.enabled | bool | `true` |  |
| collector.jvmOptions | string | `""` |  |
| collector.maxMessageUncompressedBytes | int | `100000000` |  |
| collector.nats.streams.activityAudit.maxBytes | int | `4294967296` |  |
| collector.nats.streams.fingerprints.maxBytes | int | `4294967296` |  |
| collector.nats.streams.policyEvents.maxBytes | int | `4294967296` |  |
| collector.nats.streams.previewPolicyEvents.maxBytes | int | `2147483648` |  |
| collector.podExtraEnv.MALLOC_ARENA_MAX | string | `"4"` |  |
| collector.policies.pusher.retryEnabled | bool | `false` |  |
| collector.protocolDumpFalcoEnabled | bool | `false` |  |
| collector.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| collector.replicaCount | int | `1` |  |
| collector.repositoryPrefix | string | `"monitor"` |  |
| collector.resources.collector.limits.cpu | int | `4` |  |
| collector.resources.collector.limits.memory | string | `"4Gi"` |  |
| collector.resources.collector.requests.cpu | int | `1` |  |
| collector.resources.collector.requests.memory | string | `"1Gi"` |  |
| collector.resources.collectorNginx.limits.cpu | string | `"200m"` |  |
| collector.resources.collectorNginx.limits.memory | string | `"200Mi"` |  |
| collector.resources.collectorNginx.requests.cpu | string | `"100m"` |  |
| collector.resources.collectorNginx.requests.memory | string | `"100Mi"` |  |
| collector.secureForwarderPool.auditStream | object | `{"kafkaPublishingEnabled":true}` | secureForwarderPool NATS / Kafka configuration for the different streams |
| collector.secureForwarderPool.policyStream.kafkaPublishingEnabled | bool | `true` |  |
| collector.secureForwarderPool.previewPolicyStream.kafkaPublishingEnabled | bool | `false` |  |
| collector.secureForwarderPool.profiling.kafkaPublishingEnabled | bool | `true` |  |
| collector.supportedCustomMetricsLimits[0] | string | `"DEFAULT"` |  |
| collector.supportedCustomMetricsLimits[1] | string | `"10k"` |  |
| collector.supportedCustomMetricsLimits[2] | string | `"20k"` |  |
| global.admin.password | string | `"test"` |  |
| global.admin.username | string | `"test@sysdig.com"` |  |
| global.api.serviceTokens.policies.serviceToken | string | `nil` |  |
| global.apps | string | `"monitor"` |  |
| global.captures.cassandra.storage | bool | `true` |  |
| global.cassandra | object | `{"datacenterName":"DC1","endpoint":"sysdigcloud-cassandra","port":9042,"replicaCount":3,"replicationStrategy":"SimpleStrategy","ssl":true,"sslVerify":false,"useCertManager":false}` | cassandra shared values |
| global.collectorPort | int | `6443` |  |
| global.deployment | string | `"kubernetes"` |  |
| global.dnsName | string | `"sysdigcloud-collector"` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","clientsConfigs":{"discovery":true,"signAWSRequests":false},"hostname":"sysdigcloud-elasticsearch","scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.kafka | object | `{"broker":{"externalPort":9093,"internalPort":9092},"name":"cp-kafka","namespace":"sysdigcloud","secure":{"enabled":false,"useCertManager":false}}` | kafka shared values |
| global.kafkaReplicaCount | int | `3` |  |
| global.legacyPostgres.postgresDatabases.quartz.db | string | `"quartz"` |  |
| global.legacyPostgres.postgresDatabases.quartz.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.quartz.password | string | `""` |  |
| global.legacyPostgres.postgresDatabases.quartz.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.quartz.username | string | `"quartz_user"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.db | string | `"sysdig"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.password | string | `""` |  |
| global.legacyPostgres.postgresDatabases.sysdig.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.sysdig.username | string | `"sysdig_user"` |  |
| global.legacyRedis | object | `{"redisClientsMonitor":{"agent":{"tls":true},"cache":{"tls":true},"common":{"tls":true},"policiesCache":{"tls":true}},"redisHa":false,"redisTls":{"enabled":true,"endpoint":"redistls","ha":false,"port":6379,"sentinel":{"port":26379},"useCertManager":false},"sysdigRedis":{"endpoint":"redis"},"useRedisTls":false}` | redis shared values |
| global.meerkat.defaultNumCustomerShards | int | `8` |  |
| global.meerkat.enabled | bool | `true` |  |
| global.metadataService.enabled | bool | `true` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.nats | object | `{"certManager":{"enabled":false}}` | nats shared values |
| global.nginxVersion | string | `"6.12.33"` |  |
| global.prometheus.enabled | bool | `true` |  |
| global.secure.sysqlApi.enabled | bool | `true` |  |
| global.secure.sysqlApi.serviceToken | string | `nil` | sysqlApi token mounted from sysql-api chart secret |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# compliance

![Version: 5.0.0-260303072402-main-v9652576](https://img.shields.io/badge/Version-5.0.0--260303072402--main--v9652576-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Compliance

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| compliance.apiReplicaCount | int | `1` |  |
| compliance.audit.enabled | bool | `false` |  |
| compliance.authorizationService.enabled | bool | `false` |  |
| compliance.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| compliance.benchmarks.readFromCompIndex | bool | `true` |  |
| compliance.benchmarks.writeToCompIndex | bool | `false` |  |
| compliance.cloudBenchmarksEnabled | bool | `false` |  |
| compliance.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| compliance.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| compliance.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| compliance.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| compliance.enableDispatchRateLimit | bool | `false` |  |
| compliance.enabled | bool | `true` |  |
| compliance.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-compliance-api-legacy"` |  |
| compliance.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-compliance-api-legacy"` |  |
| compliance.ingress[0].hosts[0].paths[0].path | string | `"/api/compliance/v1"` |  |
| compliance.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-compliance-api"` |  |
| compliance.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| compliance.ingress[0].hosts[1].paths[0].apiGatewayRouteName | string | `"sysdigcloud-compliance-api"` |  |
| compliance.ingress[0].hosts[1].paths[0].openshiftRouteName | string | `"sysdigcloud-compliance-api"` |  |
| compliance.ingress[0].hosts[1].paths[0].path | string | `"/api/compliance/v2"` |  |
| compliance.ingress[0].hosts[1].paths[0].serviceName | string | `"sysdigcloud-compliance-api"` |  |
| compliance.ingress[0].hosts[1].paths[0].servicePort | int | `7000` |  |
| compliance.ingress[0].hosts[2].paths[0].apiGatewayRouteName | string | `"sysdigcloud-benchmarks"` |  |
| compliance.ingress[0].hosts[2].paths[0].openshiftRouteName | string | `"sysdigcloud-benchmarks"` |  |
| compliance.ingress[0].hosts[2].paths[0].path | string | `"/api/benchmarks/v2"` |  |
| compliance.ingress[0].hosts[2].paths[0].serviceName | string | `"sysdigcloud-compliance-api"` |  |
| compliance.ingress[0].hosts[2].paths[0].servicePort | int | `7000` |  |
| compliance.ingress[0].hosts[3].paths[0].apiGatewayRouteName | string | `"sysdigcloud-cloud-api"` |  |
| compliance.ingress[0].hosts[3].paths[0].openshiftRouteName | string | `"sysdigcloud-cloud-api"` |  |
| compliance.ingress[0].hosts[3].paths[0].path | string | `"/api/cloud/v1"` |  |
| compliance.ingress[0].hosts[3].paths[0].serviceName | string | `"sysdigcloud-compliance-api"` |  |
| compliance.ingress[0].hosts[3].paths[0].servicePort | int | `7000` |  |
| compliance.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| compliance.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| compliance.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| compliance.ingress[0].labels.role | string | `"ingress-config"` |  |
| compliance.ingress[0].labels.tier | string | `"infra"` |  |
| compliance.ingress[0].name | string | `"sysdigcloud-compliance-ingress"` |  |
| compliance.maxDispatchPerSecond | int | `500` |  |
| compliance.maxParallelPolicies | int | `3` |  |
| compliance.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| compliance.repositoryPrefix | string | `"secure"` |  |
| compliance.resources.benchmarkTask.limits.cpu | string | `"500m"` |  |
| compliance.resources.benchmarkTask.limits.memory | string | `"500Mi"` |  |
| compliance.resources.benchmarkTask.requests.cpu | string | `"100m"` |  |
| compliance.resources.benchmarkTask.requests.memory | string | `"100Mi"` |  |
| compliance.resources.complianceApi.limits.cpu | int | `2` |  |
| compliance.resources.complianceApi.limits.memory | string | `"4Gi"` |  |
| compliance.resources.complianceApi.requests.cpu | string | `"1000m"` |  |
| compliance.resources.complianceApi.requests.memory | string | `"2Gi"` |  |
| compliance.resources.complianceWorker.limits.cpu | int | `8` |  |
| compliance.resources.complianceWorker.limits.memory | string | `"4Gi"` |  |
| compliance.resources.complianceWorker.requests.cpu | int | `4` |  |
| compliance.resources.complianceWorker.requests.memory | string | `"2Gi"` |  |
| compliance.segmentToken | string | `"change_me"` |  |
| compliance.serviceDisabledExemptions | string | `""` |  |
| compliance.workerReplicaCount | int | `3` |  |
| global.api.serviceTokens.compliance.serviceToken | string | `"change_me"` |  |
| global.apps | string | `"secure"` |  |
| global.dnsName | string | `"change-me.com"` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","hostname":"sysdigcloud-elasticsearch","scheme":"https"}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.legacyPostgres.postgresDatabases.compliance.admindb | string | `"anchore"` |  |
| global.legacyPostgres.postgresDatabases.compliance.adminpassword | string | `"change_me"` |  |
| global.legacyPostgres.postgresDatabases.compliance.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.compliance.db | string | `"compliance"` |  |
| global.legacyPostgres.postgresDatabases.compliance.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.compliance.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.compliance.password | string | `"change_me"` |  |
| global.legacyPostgres.postgresDatabases.compliance.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.compliance.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.compliance.username | string | `"compliance_user"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.db | string | `"sysdig"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.password | string | `"change_me"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.sysdig.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.username | string | `"sysdig_user"` |  |
| global.legacyRedis.redisClientsSecure.compliance.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `"change_me"` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.namespace | string | `"sysdig"` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.secure.azurePrincipal.clientId | string | `""` |  |
| global.secure.azurePrincipal.clientSecret | string | `""` |  |
| global.secure.compliance.audit.enabled | bool | `false` |  |
| global.secure.compliance.authorizationServiceEndpoint | string | `"sysdig-authorization-service:9602"` |  |
| global.secure.compliance.benchmarks.readFromCompIndex | bool | `true` |  |
| global.secure.compliance.benchmarks.writeToCompIndex | bool | `false` |  |
| global.secure.compliance.cloudBenchmarksEnabled | bool | `false` |  |
| global.secure.compliance.enableDispatchRateLimit | bool | `false` |  |
| global.secure.compliance.enabled | bool | `true` |  |
| global.secure.compliance.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-compliance-api-legacy"` |  |
| global.secure.compliance.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-compliance-api-legacy"` |  |
| global.secure.compliance.ingress[0].hosts[0].paths[0].path | string | `"/api/compliance/v1"` |  |
| global.secure.compliance.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-compliance-api"` |  |
| global.secure.compliance.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| global.secure.compliance.ingress[0].hosts[1].paths[0].apiGatewayRouteName | string | `"sysdigcloud-compliance-api"` |  |
| global.secure.compliance.ingress[0].hosts[1].paths[0].openshiftRouteName | string | `"sysdigcloud-compliance-api"` |  |
| global.secure.compliance.ingress[0].hosts[1].paths[0].path | string | `"/api/compliance/v2"` |  |
| global.secure.compliance.ingress[0].hosts[1].paths[0].serviceName | string | `"sysdigcloud-compliance-api"` |  |
| global.secure.compliance.ingress[0].hosts[1].paths[0].servicePort | int | `7000` |  |
| global.secure.compliance.ingress[0].hosts[2].paths[0].apiGatewayRouteName | string | `"sysdigcloud-benchmarks"` |  |
| global.secure.compliance.ingress[0].hosts[2].paths[0].openshiftRouteName | string | `"sysdigcloud-benchmarks"` |  |
| global.secure.compliance.ingress[0].hosts[2].paths[0].path | string | `"/api/benchmarks/v2"` |  |
| global.secure.compliance.ingress[0].hosts[2].paths[0].serviceName | string | `"sysdigcloud-compliance-api"` |  |
| global.secure.compliance.ingress[0].hosts[2].paths[0].servicePort | int | `7000` |  |
| global.secure.compliance.ingress[0].hosts[3].paths[0].apiGatewayRouteName | string | `"sysdigcloud-cloud-api"` |  |
| global.secure.compliance.ingress[0].hosts[3].paths[0].openshiftRouteName | string | `"sysdigcloud-cloud-api"` |  |
| global.secure.compliance.ingress[0].hosts[3].paths[0].path | string | `"/api/cloud/v1"` |  |
| global.secure.compliance.ingress[0].hosts[3].paths[0].serviceName | string | `"sysdigcloud-compliance-api"` |  |
| global.secure.compliance.ingress[0].hosts[3].paths[0].servicePort | int | `7000` |  |
| global.secure.compliance.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| global.secure.compliance.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| global.secure.compliance.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| global.secure.compliance.ingress[0].labels.role | string | `"ingress-config"` |  |
| global.secure.compliance.ingress[0].labels.tier | string | `"infra"` |  |
| global.secure.compliance.ingress[0].name | string | `"sysdigcloud-compliance-ingress"` |  |
| global.secure.compliance.maxDispatchPerSecond | int | `500` |  |
| global.secure.compliance.maxParallelPolicies | int | `3` |  |
| global.secure.compliance.segmentToken | string | `"change_me"` |  |
| global.secure.compliance.serviceDisabledExemptions | string | `""` |  |
| global.secure.compliance.serviceToken | string | `"change_me"` |  |
| global.secure.compliance.useAuthorizationService | bool | `false` |  |
| global.secure.iamUser.accessKey | string | `""` |  |
| global.secure.iamUser.region | string | `""` |  |
| global.secure.iamUser.secretKey | string | `""` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.secure.trustedIdentity.aws | string | `""` |  |
| global.secure.trustedIdentity.azure | string | `""` |  |
| global.secure.trustedIdentity.gcp | string | `""` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# elasticsearch-exporter

![Version: 0.5.2](https://img.shields.io/badge/Version-0.5.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.3.0](https://img.shields.io/badge/AppVersion-1.3.0-informational?style=flat-square)

This is owned and maintained by Sysdig Infra team. It conditionally installs elasticsearch-exporter

In this first version the `values.yaml` structure resembles the one used by the `installer` for compatibility reasons.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| elasticsearchExporter.authentication | object | `{"password":"","useExistingSecret":true,"username":""}` | Enable authentication to Opensearch cluster |
| elasticsearchExporter.authentication.password | string | `""` | Password for basic authentication (ignored if useExistingSecret is true) |
| elasticsearchExporter.authentication.useExistingSecret | bool | `true` | Use an existing secret from `elasticsearch` chart for authentication. `true` - use existing secret from elasticsearch chart. `false` - create new secret and stores username and password |
| elasticsearchExporter.authentication.username | string | `""` | Username for basic authentication (ignored if useExistingSecret is true) |
| elasticsearchExporter.enableMetrics | bool | `true` | DEPRECATED, look at elasticsearch.exporter.enabled |
| elasticsearchExporter.enabled | bool | `true` |  |
| elasticsearchExporter.extraArgs | list | `[]` | Additional arguments to pass to elasticsearch_exporter command |
| elasticsearchExporter.extraLabels | object | `{}` | extra labels for objects |
| elasticsearchExporter.image | string | `""` | if defined, will override the value built from airgapped_registry_name, airgapped_repository_prefix, infraRegistryName, infraRepositoryPrefix, elasticsearchExporterImageName, elasticsearchExporterVersion |
| elasticsearchExporter.imageName | string | `"elasticsearch-exporter"` | es exporter image name |
| elasticsearchExporter.imagePullSecrets | list | `["sysdigcloud-pull-secret"]` | image pull secret |
| elasticsearchExporter.imageTag | string | `"v1.3.35-ubi"` | es exporter image tag |
| elasticsearchExporter.nodeAffinity | list | `[]` | Add required nodeAffinity rules |
| elasticsearchExporter.registryName | string | `"quay.io"` | default registry name |
| elasticsearchExporter.repositoryPrefix | string | `"sysdig"` | default repository prefix |
| elasticsearchExporter.resources | object | `{"limits":{"cpu":"100m","memory":"128Mi"},"requests":{"cpu":"25m","memory":"64Mi"}}` | configure resources |
| elasticsearchExporter.servicePort | int | `9200` | the port used to connect to the service |
| elasticsearchExporter.tolerations | list | `[]` | setup tolerations |
| global.airgappedRegistryName | string | `nil` | registry name for airgapped environments |
| global.airgappedRepositoryPrefix | string | `nil` | repository prefix for airgapped environments |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.hostname | string | `"sysdigcloud-elasticsearch"` | the Elastcsearch endpoint to contact |
| global.elasticsearch.serviceAccount | string | `""` | name of ES serviceAccount to be used |
| global.elasticsearch.tlsencryption | object | `{"enabled":true,"useCertManager":false}` | for ES6, enable tlsencryption |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.elasticsearch.tlsencryption.useCertManager | bool | `false` | whether to use cert-manager to manage elasticsearch tls certificates |
| global.elasticsearch.workloadName | string | `""` | if used will override the name of ES statefulset |
| global.namespace | string | `"sysdig"` | namespace where to install elastic exporter |

# elasticsearch

![Version: 0.8.4](https://img.shields.io/badge/Version-0.8.4-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.19.2](https://img.shields.io/badge/AppVersion-2.19.2-informational?style=flat-square)

This is owned and maintained by Sysdig Infra team. It conditionally installs elasticsearch

In this first version the `values.yaml` structure resembles the one used by the `installer` for compatibility reasons.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| elasticsearch.clusterName | string | `"sysdigcloud"` | name of ES cluster |
| elasticsearch.dedicatedMasters | bool | `false` | if we want dedicated nodes for masters |
| elasticsearch.discoveryZenMinimumMasterNodes | string | `nil` | manually set DISCOVERY_ZEN_MINIMUM_MASTER_NODES, only useful for ES <= 6 |
| elasticsearch.discoveryZenPingUnicastHosts | string | `nil` | manually set elasticsearch masters endpoint |
| elasticsearch.esUid | int | `1000` | UID for process |
| elasticsearch.extraLabels | object | `{}` | extra labels for objects |
| elasticsearch.hostNetwork | bool | `false` | hostNetwork value |
| elasticsearch.javaHeapSizeToResourceMemoryRatio | float | `0.75` | javaHeapSizeToResourceMemoryRatio calculates java heap size based on value of memory resources of the pod. If javaHeapSizeToResourceMemoryRatio is 0.75 means java heap memory is set to 75% of memory limit of the pod |
| elasticsearch.jobExtraLabels | object | `{}` | extra job labels |
| elasticsearch.jobs | object | `{"checkIndicesCompatibility":true,"checkIndicesReplicas":true,"deleteIncompatibleIndices":true,"discardableIndices":".tasks,searchguard","persistentSettings":"cluster.max_shards_per_node=8000\nindices.recovery.max_bytes_per_sec=100mb\n","postJobBackoffLimit":0,"postJobTtlSecondsAfterFinished":3600,"preJobTtlSecondsAfterFinished":3600,"resetTransientSettings":"cluster.routing.allocation.node_concurrent_recoveries=","rollNodes":true,"setPersistentSettings":true,"toolsImageName":"elasticsearch-tools","toolsImagePullSecret":"sysdigcloud-pull-secret","toolsImageVersion":"0.0.143","transientSettings":"discovery.zen.minimum_master_nodes=,cluster.routing.allocation.node_concurrent_recoveries=10"}` | elasticsearch pre/post job configurations |
| elasticsearch.jobs.checkIndicesCompatibility | bool | `true` | whether to check if all indices are compatible with the cluster version that will be deployed, in pre job |
| elasticsearch.jobs.checkIndicesReplicas | bool | `true` | whether to check if all indices have at least a replica before rolling nodes, in post job |
| elasticsearch.jobs.deleteIncompatibleIndices | bool | `true` | whether to delete specific incompatible indices with the cluster version to be applied before rolling nodes, in post job |
| elasticsearch.jobs.discardableIndices | string | `".tasks,searchguard"` | comma separated list of indices that, if incompatible with the next version, will be deleted in post job. Will also ignore them in pre job indices compatibility check |
| elasticsearch.jobs.persistentSettings | string | `"cluster.max_shards_per_node=8000\nindices.recovery.max_bytes_per_sec=100mb\n"` | persistent settings to be applied to ES cluster with the _cluster/settings api, flat key=value, one per line, not quoted, no value on the right of = means null (i.e. revert to default). See example below |
| elasticsearch.jobs.postJobBackoffLimit | int | `0` | number of retries of post job in case of failures |
| elasticsearch.jobs.postJobTtlSecondsAfterFinished | int | `3600` | ttlSecondsAfterFinished will automatically clean up completed Jobs after a specified time period |
| elasticsearch.jobs.preJobTtlSecondsAfterFinished | int | `3600` | ttlSecondsAfterFinished will automatically clean up completed Jobs after a specified time period |
| elasticsearch.jobs.resetTransientSettings | string | `"cluster.routing.allocation.node_concurrent_recoveries="` | Transient cluster settings that you want to reset after the cluster restart is completed |
| elasticsearch.jobs.rollNodes | bool | `true` | whether to roll nodes in post job |
| elasticsearch.jobs.setPersistentSettings | bool | `true` | whether to set persistent settings, in post job |
| elasticsearch.jobs.transientSettings | string | `"discovery.zen.minimum_master_nodes=,cluster.routing.allocation.node_concurrent_recoveries=10"` | Transient cluster settings that you want to set on the cluster |
| elasticsearch.jvmOptions | string | `""` | jvmOptions, "-Dlog4j2.formatMsgNoLookups=true" is automatically added for log4shell vulnerability |
| elasticsearch.masterPersistentVolumeClaim.size | string | `"10Gi"` | elasticsearch data pvc size |
| elasticsearch.masterPersistentVolumeClaim.storageClassName | string | `"sysdig"` | elasticsearch data pvc storage class name |
| elasticsearch.mastersJvmOptions | string | `""` | jvmOptions for masters, "-Dlog4j2.formatMsgNoLookups=true" is automatically added for log4shell vulnerability |
| elasticsearch.mastersReplicaCount | string | `"3"` | set number of replicas for masters |
| elasticsearch.noComponentLabel | bool | `true` | add "component" label |
| elasticsearch.nodeAffinityMode | string | `"preferred"` | make nodeAffinity "required" or "preferred" |
| elasticsearch.nodeLabelsImageName | string | `"node-labels-to-files"` | NodeLabels image name |
| elasticsearch.nodeLabelsVersion | string | `"1.0.77"` | NodeLabels image tag |
| elasticsearch.nodeaffinityLabel | string | `nil` | label on which create nodeAffinity |
| elasticsearch.opensearchImageName | string | `"opensearch-2"` | opensearch image name |
| elasticsearch.opensearchVersion | string | `"0.5.9"` | opensearch image tag |
| elasticsearch.overrideOpensearchConfig | string | `""` | Custom opensearch.yml configuration to override the default opensearch.yml baked into the container image. When set, a ConfigMap will be created and mounted at /opensearch-security/opensearch.yml with subPath, overriding only that file while leaving other files in /opensearch-security/ intact. |
| elasticsearch.overrideRegistryPath | string | `""` | if defined, will use this as registry path |
| elasticsearch.persistentVolumeClaim | object | `{"size":"30Gi","storageClassName":"sysdig"}` | pvc configuration |
| elasticsearch.persistentVolumeClaim.size | string | `"30Gi"` | elasticsearch data pvc size |
| elasticsearch.persistentVolumeClaim.storageClassName | string | `"sysdig"` | elasticsearch data pvc storage class name |
| elasticsearch.podExtraAnnotations | object | `{}` | extra pod annotations |
| elasticsearch.podExtraEnv | list | `[]` | extra pod environment variables |
| elasticsearch.podExtraEnvFromConfigMapRefs | list | `[]` | list of configmaps from which to load extra environment variables for pods |
| elasticsearch.podExtraEnvFromSecretRefs | list | `[]` | list of secrets from which to load extra environment variables for pods |
| elasticsearch.podExtraLabels | object | `{}` | extra pod labels |
| elasticsearch.podExtraVolumeMounts | list | `[]` | extra pod volume mounts |
| elasticsearch.podExtraVolumesFromSecrets | list | `[]` | extra pod volumes from secrets. List of entries with "name", "defaultMode" and "secretName" |
| elasticsearch.readinessProbe | object | `{"initialDelaySeconds":30}` | Readiness probe initial delay configuration |
| elasticsearch.registryName | string | `"quay.io"` | default registry name |
| elasticsearch.repositoryPrefix | string | `"sysdig"` | default repository prefix |
| elasticsearch.resetOpenDistroSecurity | bool | `false` | resets opendistro security by running security-admin.sh (only available with useOpensearch: true) |
| elasticsearch.resources.elasticsearch | object | `{"limits":{"cpu":"4","memory":"8Gi"},"requests":{"cpu":"2","memory":"4Gi"}}` | ES pods resources |
| elasticsearch.resources.init | object | `{"limits":{"cpu":"100m","memory":"128Mi"},"requests":{"cpu":"25m","memory":"64Mi"}}` | elasticsearch-init pod resources |
| elasticsearch.resources.initVmmaxmapcount | object | `{"limits":{"cpu":"100m","memory":"128Mi"},"requests":{"cpu":"25m","memory":"64Mi"}}` | elasticsearch-init-vmmaxmapcount pod resources |
| elasticsearch.resources.masters | object | `{"limits":{"cpu":"2","memory":"4Gi"},"requests":{"cpu":"2","memory":"4Gi"}}` | ES pods resources |
| elasticsearch.resources.node-labels-to-files | object | `{"limits":{"cpu":"100m","memory":"128Mi"},"requests":{"cpu":"25m","memory":"64Mi"}}` | node-labels-to-files pod resources |
| elasticsearch.serviceName | string | `""` | if used will will override the name of ES service |
| elasticsearch.setVmMaxMapCount | bool | `false` | setup vm.max_map_count=262144 with an initContainer |
| elasticsearch.snitch | object | `{"extractCMD":"","hostnameFile":""}` | setup snitch |
| elasticsearch.tlsencryption.caCertExpiry | string | `"87660h"` | set ca cert expiry in hours |
| elasticsearch.tlsencryption.caCertRenewBefore | string | `"360h"` | renew before how many hours of cert expiration |
| elasticsearch.tlsencryption.certificateIssuer | string | `"sysdig-selfsigned-issuer"` | certificate issuer to use, keep this empty if creating an issuer |
| elasticsearch.tlsencryption.certificateIssuerKind | string | `"ClusterIssuer"` | certificate issuer kind to use, keep this empty if creating an issuer |
| elasticsearch.tlsencryption.createIssuer | bool | `false` | create a elasticsearch certificate issuer |
| elasticsearch.tlsencryption.privateKeyAlgorithm | string | `"RSA"` | private key algorithm to use |
| elasticsearch.tlsencryption.privateKeySize | int | `4096` | private key size to use |
| elasticsearch.tolerations | list | `[]` | setup tolerations |
| elasticsearch.updateStrategy | string | `"OnDelete"` | which update strategy to use "OnDelete" or "RollingRestart" |
| elasticsearch.useOpensearch | bool | `true` | wether to use Opensearch |
| global.airgappedRegistryName | string | `nil` | registry name for airgapped environments |
| global.airgappedRepositoryPrefix | string | `nil` | repository prefix for airgapped environments |
| global.apps | string | `"monitor secure"` | platform apps |
| global.cloudProvider.isMultiAZ | bool | `false` | "true" spreads pods across AZs |
| global.clusterDomain | string | `"cluster.local"` | domain of the k8s cluster |
| global.elasticsearch | object | `{"basename":"elasticsearch","external":false,"replicaCount":"3","serviceAccount":"","tlsencryption":{"adminUser":"sysdig","caCrts":[],"caCrtsExternalSecretName":"","elasticsearchCASecretName":"elasticsearch-ca-secret","enabled":true,"trtUser":"sysdig_trt","useCertManager":false},"workloadName":""}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.external | bool | `false` | if should be deployed |
| global.elasticsearch.replicaCount | string | `"3"` | ES replica count (sets both the number of the sts replicas and the conf ELASTICSEARCH_GOSSIP_NODES_NUM) |
| global.elasticsearch.serviceAccount | string | `""` | name of ES serviceAccount to be used |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","caCrts":[],"caCrtsExternalSecretName":"","elasticsearchCASecretName":"elasticsearch-ca-secret","enabled":true,"trtUser":"sysdig_trt","useCertManager":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.caCrts | list | `[]` | base64 encoded CA certificates for tls encryption. These certs can be generated with: ```openssl req -x509 -nodes -sha256 -days 7300 -newkey rsa:4096 -subj '/C=US/ST=CA/L=SanFrancisco/O=Sysdig' -addext "keyUsage= digitalSignature, keyEncipherment, keyCertSign" -addext "extendedKeyUsage= serverAuth, clientAuth" -keyout "ca.key" -out "ca.crt"``` |
| global.elasticsearch.tlsencryption.caCrtsExternalSecretName | string | `""` | external secret name used for tls |
| global.elasticsearch.tlsencryption.elasticsearchCASecretName | string | `"elasticsearch-ca-secret"` | this is the secret name exported by cert manager for the CA certificate |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.elasticsearch.tlsencryption.trtUser | string | `"sysdig_trt"` | name of the trt user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.useCertManager | bool | `false` | whether to use cert-manager to manage elasticsearch tls certificates |
| global.elasticsearch.workloadName | string | `""` | if used will override the name of ES statefulset |
| global.helmDeploy | bool | `false` | Feature Flag for Helm Deployment - set to true when deploying using pure helm |
| global.installationType | string | `"saas"` |  |
| global.namespace | string | `"sysdig"` | namespace where to install elasticsearch/opensearch |
| global.storageClassProvisioner | string | `"aws"` | storageclass provisioner to use |
| global.tlsencryption | object | `{"adminUser":{"password":null},"readonly":{"password":null},"trtUser":{"password":null}}` | ES >= 6 tlsencryption admin/readonly passwords |
| global.tolerations | list | `[]` | setup global tolerations |

# events-forwarder

![Version: 5.2.1-260312130820-main-v5bc2e92](https://img.shields.io/badge/Version-5.2.1--260312130820--main--v5bc2e92-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Events Forwarder

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| eventsForwarder.addressBlocklist | string | `"127.0.0.1/8,172.16.0.0/12,192.168.0.0/16,10.0.0.0/8,localhost"` |  |
| eventsForwarder.affinity | object | `{}` |  |
| eventsForwarder.api.serviceAccountName | string | `"sysdig"` |  |
| eventsForwarder.apiReplicaCount | int | `1` |  |
| eventsForwarder.async.execRoutines | int | `16` |  |
| eventsForwarder.async.timeout | string | `"25s"` |  |
| eventsForwarder.audit.enabled | bool | `true` |  |
| eventsForwarder.authorizationService.enabled | bool | `false` |  |
| eventsForwarder.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| eventsForwarder.certman.enabled | bool | `false` |  |
| eventsForwarder.certman.endpoint | string | `"sysdigcloud-certman:6000"` |  |
| eventsForwarder.customerAvailableChannels | string | `""` |  |
| eventsForwarder.customerUnavailableChannels | string | `""` |  |
| eventsForwarder.enabled | bool | `true` |  |
| eventsForwarder.errorHandler.cacheSize | int | `1000` |  |
| eventsForwarder.errorHandler.disabled | bool | `false` |  |
| eventsForwarder.errorHandler.expiration | string | `"24h"` |  |
| eventsForwarder.forceMigrations | bool | `false` |  |
| eventsForwarder.hiddenChannels | string | `"SECURE_VM_RUNTIME_SCANNING_RESULT,SECURE_VM_REGISTRY_SCANNING_RESULT,SECURE_VM_PIPELINE_SCANNING_RESULT,CLOUD_PLATFORM_EVENTS"` |  |
| eventsForwarder.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-events-forwarder-api"` |  |
| eventsForwarder.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-events-forwarder-api"` |  |
| eventsForwarder.ingress[0].hosts[0].paths[0].path | string | `"/api/v1/eventsForwarding"` |  |
| eventsForwarder.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-events-forwarder-api"` |  |
| eventsForwarder.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| eventsForwarder.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-events-forwarder-api-public"` |  |
| eventsForwarder.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-events-forwarder-api-public"` |  |
| eventsForwarder.ingress[0].hosts[0].paths[1].path | string | `"/secure/events-forwarder/v1"` |  |
| eventsForwarder.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-events-forwarder-api"` |  |
| eventsForwarder.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| eventsForwarder.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| eventsForwarder.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| eventsForwarder.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| eventsForwarder.ingress[0].labels.role | string | `"ingress-config"` |  |
| eventsForwarder.ingress[0].labels.tier | string | `"infra"` |  |
| eventsForwarder.ingress[0].name | string | `"sysdigcloud-events-forwarder-ingress"` |  |
| eventsForwarder.natsConsumers.auditTap.ackWait | string | `"30s"` |  |
| eventsForwarder.natsConsumers.auditTap.dlqHandleDelay | string | `"30s"` |  |
| eventsForwarder.natsConsumers.auditTap.dlqSubjectPrefix | string | `"efo.retry.1"` |  |
| eventsForwarder.natsConsumers.auditTap.durable | string | `"efo"` |  |
| eventsForwarder.natsConsumers.auditTap.maxInFlight | int | `10000` |  |
| eventsForwarder.natsConsumers.auditTap.name | string | `"efo-audit-tap"` |  |
| eventsForwarder.natsConsumers.auditTap.queue | string | `"efo"` |  |
| eventsForwarder.natsConsumers.auditTap.streamName | string | `"collector-audittap-1"` |  |
| eventsForwarder.natsConsumers.auditTap.subject | string | `"collector.audittap.>"` |  |
| eventsForwarder.natsConsumers.cloudPlatform.ackWait | string | `"30s"` |  |
| eventsForwarder.natsConsumers.cloudPlatform.dlqHandleDelay | string | `"30s"` |  |
| eventsForwarder.natsConsumers.cloudPlatform.dlqSubjectPrefix | string | `"efo.retry.1"` |  |
| eventsForwarder.natsConsumers.cloudPlatform.durable | string | `"efo"` |  |
| eventsForwarder.natsConsumers.cloudPlatform.maxInFlight | int | `10000` |  |
| eventsForwarder.natsConsumers.cloudPlatform.name | string | `"efo-cloud-platform"` |  |
| eventsForwarder.natsConsumers.cloudPlatform.queue | string | `"efo"` |  |
| eventsForwarder.natsConsumers.cloudPlatform.streamName | string | `"cloudauth-api-cloudaccount-activity-stream"` |  |
| eventsForwarder.natsConsumers.cloudPlatform.subject | string | `"cloudauth.cloudaccount.platformevents.elasticlog"` |  |
| eventsForwarder.natsConsumers.events.ackWait | string | `"30s"` |  |
| eventsForwarder.natsConsumers.events.dlqHandleDelay | string | `"30s"` |  |
| eventsForwarder.natsConsumers.events.dlqSubjectPrefix | string | `"efo.retry.1"` |  |
| eventsForwarder.natsConsumers.events.durable | string | `"efo-events"` |  |
| eventsForwarder.natsConsumers.events.maxInFlight | int | `10000` |  |
| eventsForwarder.natsConsumers.events.name | string | `"efo-events"` |  |
| eventsForwarder.natsConsumers.events.queue | string | `"efo-events"` |  |
| eventsForwarder.natsConsumers.events.streamName | string | `"events"` |  |
| eventsForwarder.natsConsumers.events.subject | string | `"events.>"` |  |
| eventsForwarder.natsConsumers.monitor.ackWait | string | `"30s"` |  |
| eventsForwarder.natsConsumers.monitor.dlqHandleDelay | string | `"30s"` |  |
| eventsForwarder.natsConsumers.monitor.dlqSubjectPrefix | string | `"efo.retry.1"` |  |
| eventsForwarder.natsConsumers.monitor.durable | string | `"efo"` |  |
| eventsForwarder.natsConsumers.monitor.maxInFlight | int | `10000` |  |
| eventsForwarder.natsConsumers.monitor.name | string | `"efo-monitor-events"` |  |
| eventsForwarder.natsConsumers.monitor.queue | string | `"efo"` |  |
| eventsForwarder.natsConsumers.monitor.streamName | string | `"monitor-events-1"` |  |
| eventsForwarder.natsConsumers.monitor.subject | string | `"monitor.>"` |  |
| eventsForwarder.natsConsumers.retry1.ackWait | string | `"30s"` |  |
| eventsForwarder.natsConsumers.retry1.disabled | bool | `false` |  |
| eventsForwarder.natsConsumers.retry1.dlqHandleDelay | string | `"60s"` |  |
| eventsForwarder.natsConsumers.retry1.dlqSubjectPrefix | string | `"efo.retry.2"` |  |
| eventsForwarder.natsConsumers.retry1.durable | string | `"efo"` |  |
| eventsForwarder.natsConsumers.retry1.maxInFlight | int | `10000` |  |
| eventsForwarder.natsConsumers.retry1.name | string | `"efo-retry-1"` |  |
| eventsForwarder.natsConsumers.retry1.queue | string | `"efo"` |  |
| eventsForwarder.natsConsumers.retry1.streamName | string | `"efo-retry-1"` |  |
| eventsForwarder.natsConsumers.retry1.subject | string | `"efo.retry.1.>"` |  |
| eventsForwarder.natsConsumers.retry2.ackWait | string | `"30s"` |  |
| eventsForwarder.natsConsumers.retry2.disabled | bool | `false` |  |
| eventsForwarder.natsConsumers.retry2.dlqHandleDelay | string | `"90s"` |  |
| eventsForwarder.natsConsumers.retry2.dlqSubjectPrefix | string | `"efo.retry.3"` |  |
| eventsForwarder.natsConsumers.retry2.durable | string | `"efo"` |  |
| eventsForwarder.natsConsumers.retry2.maxInFlight | int | `10000` |  |
| eventsForwarder.natsConsumers.retry2.name | string | `"efo-retry-2"` |  |
| eventsForwarder.natsConsumers.retry2.queue | string | `"efo"` |  |
| eventsForwarder.natsConsumers.retry2.streamName | string | `"efo-retry-2"` |  |
| eventsForwarder.natsConsumers.retry2.subject | string | `"efo.retry.2.>"` |  |
| eventsForwarder.natsConsumers.retry3.ackWait | string | `"30s"` |  |
| eventsForwarder.natsConsumers.retry3.disabled | bool | `false` |  |
| eventsForwarder.natsConsumers.retry3.durable | string | `"efo"` |  |
| eventsForwarder.natsConsumers.retry3.maxDeliver | int | `2` |  |
| eventsForwarder.natsConsumers.retry3.maxInFlight | int | `10000` |  |
| eventsForwarder.natsConsumers.retry3.name | string | `"efo-retry-3"` |  |
| eventsForwarder.natsConsumers.retry3.queue | string | `"efo"` |  |
| eventsForwarder.natsConsumers.retry3.streamName | string | `"efo-retry-3"` |  |
| eventsForwarder.natsConsumers.retry3.subject | string | `"efo.retry.3.>"` |  |
| eventsForwarder.natsConsumers.vm.ackWait | string | `"30s"` |  |
| eventsForwarder.natsConsumers.vm.disabled | bool | `true` |  |
| eventsForwarder.natsConsumers.vm.dlqHandleDelay | string | `"30s"` |  |
| eventsForwarder.natsConsumers.vm.dlqSubjectPrefix | string | `"efo.retry.1"` |  |
| eventsForwarder.natsConsumers.vm.durable | string | `"efo"` |  |
| eventsForwarder.natsConsumers.vm.maxInFlight | int | `10000` |  |
| eventsForwarder.natsConsumers.vm.name | string | `"efo-vm-scanner-scan-response"` |  |
| eventsForwarder.natsConsumers.vm.queue | string | `"efo"` |  |
| eventsForwarder.natsConsumers.vm.streamName | string | `"secure-vm-scanner-scan-response"` |  |
| eventsForwarder.natsConsumers.vm.subjects | string | `"secure.vm.scanner.scan.response.runtime.*.success,secure.vm.scanner.scan.response.registry.*.success,secure.vm.scanner.scan.response.pipeline.*.success"` |  |
| eventsForwarder.nodeSelector | object | `{}` |  |
| eventsForwarder.notifier.cronjob | string | `"00 9 * * *"` |  |
| eventsForwarder.notifier.notificationRoutingKey | string | `"notifier.notifications.1.generic.email"` |  |
| eventsForwarder.notifier.suspend | bool | `false` |  |
| eventsForwarder.proxy.enable | bool | `false` |  |
| eventsForwarder.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| eventsForwarder.remotebody.enabled | bool | `false` |  |
| eventsForwarder.remotebody.pullerBackends | string | `"s3"` |  |
| eventsForwarder.remotebody.s3.accessKeyId | string | `""` |  |
| eventsForwarder.remotebody.s3.bucket | string | `""` |  |
| eventsForwarder.remotebody.s3.cloudProvider | string | `""` |  |
| eventsForwarder.remotebody.s3.endpoint | string | `""` |  |
| eventsForwarder.remotebody.s3.region | string | `""` |  |
| eventsForwarder.remotebody.s3.secretAccessKey | string | `""` |  |
| eventsForwarder.replicaCount | int | `1` |  |
| eventsForwarder.repositoryPrefix | string | `"secure"` |  |
| eventsForwarder.resources.eventsForwarder.limits.cpu | int | `1` |  |
| eventsForwarder.resources.eventsForwarder.limits.memory | string | `"500Mi"` |  |
| eventsForwarder.resources.eventsForwarder.requests.cpu | string | `"250m"` |  |
| eventsForwarder.resources.eventsForwarder.requests.memory | string | `"50Mi"` |  |
| eventsForwarder.resources.eventsForwarderAPI.limits.cpu | int | `1` |  |
| eventsForwarder.resources.eventsForwarderAPI.limits.memory | string | `"500Mi"` |  |
| eventsForwarder.resources.eventsForwarderAPI.requests.cpu | string | `"250m"` |  |
| eventsForwarder.resources.eventsForwarderAPI.requests.memory | string | `"50Mi"` |  |
| eventsForwarder.resources.eventsForwarderNotifier.limits.cpu | int | `1` |  |
| eventsForwarder.resources.eventsForwarderNotifier.limits.memory | string | `"500Mi"` |  |
| eventsForwarder.resources.eventsForwarderNotifier.requests.cpu | string | `"250m"` |  |
| eventsForwarder.resources.eventsForwarderNotifier.requests.memory | string | `"50Mi"` |  |
| eventsForwarder.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| eventsForwarder.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| eventsForwarder.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| eventsForwarder.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| eventsForwarder.resources.postgresqlinitLinkerd.limits.cpu | string | `"500m"` |  |
| eventsForwarder.resources.postgresqlinitLinkerd.limits.memory | string | `"500Mi"` |  |
| eventsForwarder.resources.postgresqlinitLinkerd.requests.cpu | string | `"100m"` |  |
| eventsForwarder.resources.postgresqlinitLinkerd.requests.memory | string | `"100Mi"` |  |
| eventsForwarder.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| eventsForwarder.scaler.backlogThreshold | int | `7000` |  |
| eventsForwarder.scaler.clusterName | string | `""` |  |
| eventsForwarder.scaler.cpuThreshold | int | `100` |  |
| eventsForwarder.scaler.enabled | bool | `false` |  |
| eventsForwarder.scaler.maxReplicaCount | int | `10` |  |
| eventsForwarder.scaler.memoryThreshold | int | `90` |  |
| eventsForwarder.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| eventsForwarder.serviceAccountName | string | `"sysdig"` |  |
| eventsForwarder.statsPrintedLabels | string | `""` |  |
| eventsForwarder.tolerations | list | `[]` |  |
| eventsForwarder.useFipsImages | bool | `true` |  |
| eventsForwarder.useNatsJsPubSub | bool | `false` |  |
| global.api.serviceTokens.eventsForwarder.serviceToken | string | `""` |  |
| global.apps | string | `"secure"` |  |
| global.dnsName | string | `""` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.eventsForwarder.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.eventsForwarder.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.eventsForwarder.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.eventsForwarder.db | string | `"sysdig_db"` |  |
| global.legacyPostgres.postgresDatabases.eventsForwarder.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.eventsForwarder.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.eventsForwarder.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.eventsForwarder.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.eventsForwarder.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.eventsForwarder.username | string | `"sysdig_user"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.sysdig.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.db | string | `"sysdig_db"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.sysdig.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.sysdig.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.username | string | `"sysdig_user"` |  |
| global.legacyRedis.redisClientsSecure.eventsForwarder.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.platformAuditTrail.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgresql-client"` |  |
| global.postgresVersion | string | `"0.0.50"` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# events

![Version: 5.1.0-260310144013-main-vee66d73](https://img.shields.io/badge/Version-5.1.0--260310144013--main--vee66d73-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Events

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| events.api.geolocDB.enabled | bool | `true` |  |
| events.api.geolocDB.sizeLimit | string | `"2Gi"` |  |
| events.api.geolocDB.version | string | `"v0.0.5"` |  |
| events.api.serviceAccountName | string | `"sysdig"` |  |
| events.audit.config.store.ip | bool | `false` |  |
| events.audit.enabled | bool | `true` |  |
| events.authorizationService.enabled | bool | `false` |  |
| events.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| events.batching.activityAuditGatherer.opensearch.batchingEnabled | bool | `true` |  |
| events.batching.activityAuditGatherer.opensearch.flushPeriod | string | `"500ms"` |  |
| events.batching.activityAuditGatherer.opensearch.flushingRoutines | int | `24` |  |
| events.batching.activityAuditGatherer.opensearch.maxBatchSize | int | `150` |  |
| events.batching.activityAuditGatherer.opensearch.maxBufferSize | int | `150` |  |
| events.batching.api.opensearch.batchingEnabled | bool | `false` |  |
| events.batching.api.opensearch.flushPeriod | string | `"100ms"` |  |
| events.batching.api.opensearch.flushingRoutines | int | `2` |  |
| events.batching.api.opensearch.maxBatchSize | int | `5` |  |
| events.batching.api.opensearch.maxBufferSize | int | `5` |  |
| events.batching.dispatcher.flushPeriod | string | `"3s"` |  |
| events.batching.dispatcher.flushingRoutines | int | `2` |  |
| events.batching.dispatcher.maxAsyncCalls | int | `30` |  |
| events.batching.dispatcher.maxBatchByteSize | int | `10000` |  |
| events.batching.dispatcher.maxBatchSize | int | `10` |  |
| events.batching.dispatcher.maxBufferByteSize | int | `50000` |  |
| events.batching.dispatcher.maxBufferSize | int | `50` |  |
| events.batching.eventSource.flushPeriod | string | `"3s"` |  |
| events.batching.eventSource.flushingRoutines | int | `2` |  |
| events.batching.eventSource.maxAsyncCalls | int | `30` |  |
| events.batching.eventSource.maxBatchByteSize | int | `10000` |  |
| events.batching.eventSource.maxBatchSize | int | `5` |  |
| events.batching.eventSource.maxBufferByteSize | int | `50000` |  |
| events.batching.eventSource.maxBufferSize | int | `10` |  |
| events.batching.eventsGatherer.opensearch.batchingEnabled | bool | `true` |  |
| events.batching.eventsGatherer.opensearch.flushPeriod | string | `"500ms"` |  |
| events.batching.eventsGatherer.opensearch.flushingRoutines | int | `24` |  |
| events.batching.eventsGatherer.opensearch.maxBatchSize | int | `75` |  |
| events.batching.eventsGatherer.opensearch.maxBufferSize | int | `75` |  |
| events.batching.ingestion.flushPeriod | string | `"5s"` |  |
| events.batching.ingestion.flushingRoutines | int | `1` |  |
| events.batching.ingestion.maxAsyncCalls | int | `30` |  |
| events.batching.ingestion.maxBatchByteSize | int | `10000` |  |
| events.batching.ingestion.maxBatchSize | int | `10` |  |
| events.batching.ingestion.maxBufferByteSize | int | `50000` |  |
| events.batching.ingestion.maxBufferSize | int | `50` |  |
| events.dedup.activityAuditGatherer.enabled | bool | `false` |  |
| events.dedup.eventsGatherer.enabled | bool | `false` |  |
| events.dispatcher.ingestCustomerBlocklist | string | `""` |  |
| events.dispatcher.nats.streams.events-dispatcher.max_age | int | `86400000000000` |  |
| events.dispatcher.nats.streams.events-dispatcher.max_bytes | int | `2147483648` |  |
| events.dispatcher.nats.streams.events-dispatcher.metadata.version | string | `"2"` |  |
| events.dispatcher.nats.streams.events-dispatcher.name | string | `"events-dispatcher"` |  |
| events.dispatcher.nats.streams.events-dispatcher.num_replicas | int | `3` |  |
| events.dispatcher.nats.streams.events-dispatcher.storage | string | `"file"` |  |
| events.dispatcher.nats.streams.events-dispatcher.subjects[0] | string | `"dispatcher.>"` |  |
| events.dispatcher.serviceAccountName | string | `"sysdig"` |  |
| events.elasticsearch.compressedRequestBody | bool | `true` |  |
| events.elasticsearch.disableRetry | bool | `true` |  |
| events.elasticsearch.maxRetry | int | `5` |  |
| events.elasticsearch.nodeDiscoveryInterval | string | `"10m"` |  |
| events.elasticsearch.nodeDiscoveryOnStart | bool | `true` |  |
| events.elasticsearch.retryHTTPStatuses | string | `"429,500,502,503,504"` |  |
| events.elasticsearch.retryOnTimeout | bool | `true` |  |
| events.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| events.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| events.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| events.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| events.enableIngestion | bool | `true` |  |
| events.enabled | bool | `true` |  |
| events.eventsActivityAuditGatherer.envVars | object | `{}` |  |
| events.eventsActivityAuditGathererReplicaCount | int | `1` |  |
| events.eventsApiReplicaCount | int | `1` |  |
| events.eventsDispatcherReplicaCount | int | `1` |  |
| events.eventsGatherer.envVars | object | `{}` |  |
| events.eventsGatherer.nats.streams.events-dlq.max_age | int | `172800000000000` |  |
| events.eventsGatherer.nats.streams.events-dlq.max_bytes | int | `4294967296` |  |
| events.eventsGatherer.nats.streams.events-dlq.metadata.version | string | `"5"` |  |
| events.eventsGatherer.nats.streams.events-dlq.name | string | `"events-dlq"` |  |
| events.eventsGatherer.nats.streams.events-dlq.num_replicas | int | `3` |  |
| events.eventsGatherer.nats.streams.events-dlq.storage | string | `"file"` |  |
| events.eventsGatherer.nats.streams.events-dlq.subjects[0] | string | `"events.gatherer.dlq.>"` |  |
| events.eventsGatherer.nats.streams.events-dlq.subjects[1] | string | `"events.gatherer.quickwit.dlq.>"` |  |
| events.eventsGatherer.nats.streams.events-dlq.subjects[2] | string | `"events.activityaudit.gatherer.dlq.>"` |  |
| events.eventsGatherer.nats.streams.events-dlq.subjects[3] | string | `"events.activityaudit.gatherer.quickwit.dlq.>"` |  |
| events.eventsGatherer.nats.streams.events-notifications.max_age | int | `86400000000000` |  |
| events.eventsGatherer.nats.streams.events-notifications.metadata.version | string | `"2"` |  |
| events.eventsGatherer.nats.streams.events-notifications.name | string | `"events-notifications"` |  |
| events.eventsGatherer.nats.streams.events-notifications.num_replicas | int | `3` |  |
| events.eventsGatherer.nats.streams.events-notifications.retention | string | `"workqueue"` |  |
| events.eventsGatherer.nats.streams.events-notifications.storage | string | `"file"` |  |
| events.eventsGatherer.nats.streams.events-notifications.subjects[0] | string | `"events.notifications.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-1.max_age | int | `86400000000000` |  |
| events.eventsGatherer.nats.streams.events-retry-1.max_bytes | int | `1073741824` |  |
| events.eventsGatherer.nats.streams.events-retry-1.metadata.version | string | `"5"` |  |
| events.eventsGatherer.nats.streams.events-retry-1.name | string | `"events-retry-1"` |  |
| events.eventsGatherer.nats.streams.events-retry-1.num_replicas | int | `3` |  |
| events.eventsGatherer.nats.streams.events-retry-1.storage | string | `"file"` |  |
| events.eventsGatherer.nats.streams.events-retry-1.subjects[0] | string | `"events.gatherer.retry.1.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-1.subjects[1] | string | `"events.gatherer.quickwit.retry.1.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-1.subjects[2] | string | `"events.activityaudit.gatherer.retry.1.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-1.subjects[3] | string | `"events.activityaudit.gatherer.quickwit.retry.1.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-2.max_age | int | `86400000000000` |  |
| events.eventsGatherer.nats.streams.events-retry-2.max_bytes | int | `1073741824` |  |
| events.eventsGatherer.nats.streams.events-retry-2.metadata.version | string | `"5"` |  |
| events.eventsGatherer.nats.streams.events-retry-2.name | string | `"events-retry-2"` |  |
| events.eventsGatherer.nats.streams.events-retry-2.num_replicas | int | `3` |  |
| events.eventsGatherer.nats.streams.events-retry-2.storage | string | `"file"` |  |
| events.eventsGatherer.nats.streams.events-retry-2.subjects[0] | string | `"events.gatherer.retry.2.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-2.subjects[1] | string | `"events.gatherer.quickwit.retry.2.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-2.subjects[2] | string | `"events.activityaudit.gatherer.retry.2.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-2.subjects[3] | string | `"events.activityaudit.gatherer.quickwit.retry.2.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-3.max_age | int | `86400000000000` |  |
| events.eventsGatherer.nats.streams.events-retry-3.max_bytes | int | `1073741824` |  |
| events.eventsGatherer.nats.streams.events-retry-3.metadata.version | string | `"5"` |  |
| events.eventsGatherer.nats.streams.events-retry-3.name | string | `"events-retry-3"` |  |
| events.eventsGatherer.nats.streams.events-retry-3.num_replicas | int | `3` |  |
| events.eventsGatherer.nats.streams.events-retry-3.storage | string | `"file"` |  |
| events.eventsGatherer.nats.streams.events-retry-3.subjects[0] | string | `"events.gatherer.retry.3.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-3.subjects[1] | string | `"events.gatherer.quickwit.retry.3.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-3.subjects[2] | string | `"events.activityaudit.gatherer.retry.3.>"` |  |
| events.eventsGatherer.nats.streams.events-retry-3.subjects[3] | string | `"events.activityaudit.gatherer.quickwit.retry.3.>"` |  |
| events.eventsGatherer.nats.streams.events.max_age | int | `86400000000000` |  |
| events.eventsGatherer.nats.streams.events.max_bytes | int | `2147483648` |  |
| events.eventsGatherer.nats.streams.events.metadata.version | string | `"2"` |  |
| events.eventsGatherer.nats.streams.events.name | string | `"events"` |  |
| events.eventsGatherer.nats.streams.events.num_replicas | int | `3` |  |
| events.eventsGatherer.nats.streams.events.storage | string | `"file"` |  |
| events.eventsGatherer.nats.streams.events.subjects[0] | string | `"events.forwarder.>"` |  |
| events.eventsGatherer.nats.streams.events.subjects[1] | string | `"events.source.>"` |  |
| events.eventsGatherer.nats.streamsToDelete | string | `""` |  |
| events.eventsGathererReplicaCount | int | `1` |  |
| events.eventsIngestionReplicaCount | int | `3` |  |
| events.forceMigrations | bool | `false` |  |
| events.ingestion.ingestCustomerBlocklist | string | `""` |  |
| events.ingestion.nats.streams.platformaudit.max_age | int | `86400000000000` |  |
| events.ingestion.nats.streams.platformaudit.max_bytes | int | `1073741824` |  |
| events.ingestion.nats.streams.platformaudit.metadata.version | string | `"2"` |  |
| events.ingestion.nats.streams.platformaudit.name | string | `"platformaudit"` |  |
| events.ingestion.nats.streams.platformaudit.num_replicas | int | `3` |  |
| events.ingestion.nats.streams.platformaudit.storage | string | `"file"` |  |
| events.ingestion.nats.streams.platformaudit.subjects[0] | string | `"platformaudit.>"` |  |
| events.ingestion.serviceAccountName | string | `"sysdig"` |  |
| events.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-events-standard-api-http"` |  |
| events.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-events-standard-api-http"` |  |
| events.ingress[0].hosts[0].paths[0].path | string | `"/secure/events/v1"` |  |
| events.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-events-api-http"` |  |
| events.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| events.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-events-standard-api-v2-http"` |  |
| events.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-events-standard-api-v2-http"` |  |
| events.ingress[0].hosts[0].paths[1].path | string | `"/secure/events/v2"` |  |
| events.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-events-api-http"` |  |
| events.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| events.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-events-api-http"` |  |
| events.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-events-api-http"` |  |
| events.ingress[0].hosts[0].paths[2].path | string | `"/api/v1/secureEvents"` |  |
| events.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-events-api-http"` |  |
| events.ingress[0].hosts[0].paths[2].servicePort | int | `7000` |  |
| events.ingress[0].hosts[1].paths[0].apiGatewayRouteName | string | `"sysdigcloud-platform-audit-events-api-http"` |  |
| events.ingress[0].hosts[1].paths[0].openshiftRouteName | string | `"sysdigcloud-platform-audit-events-api-http"` |  |
| events.ingress[0].hosts[1].paths[0].path | string | `"/api/v1/platformAuditEvents"` |  |
| events.ingress[0].hosts[1].paths[0].serviceName | string | `"sysdigcloud-events-api-http"` |  |
| events.ingress[0].hosts[1].paths[0].servicePort | int | `7000` |  |
| events.ingress[0].hosts[2].paths[0].apiGatewayRouteName | string | `"sysdigcloud-platform-audit-events-public-api-http"` |  |
| events.ingress[0].hosts[2].paths[0].openshiftRouteName | string | `"sysdigcloud-platform-audit-events-public-api-http"` |  |
| events.ingress[0].hosts[2].paths[0].path | string | `"/platform/v1/platform-audit-events"` |  |
| events.ingress[0].hosts[2].paths[0].serviceName | string | `"sysdigcloud-events-api-http"` |  |
| events.ingress[0].hosts[2].paths[0].servicePort | int | `7000` |  |
| events.ingress[0].hosts[3].paths[0].apiGatewayRouteName | string | `"sysdigcloud-events-dispatcher-http"` |  |
| events.ingress[0].hosts[3].paths[0].openshiftRouteName | string | `"sysdigcloud-events-dispatcher-http"` |  |
| events.ingress[0].hosts[3].paths[0].path | string | `"/api/v1/eventsDispatch"` |  |
| events.ingress[0].hosts[3].paths[0].serviceName | string | `"sysdigcloud-events-dispatcher"` |  |
| events.ingress[0].hosts[3].paths[0].servicePort | int | `7000` |  |
| events.ingress[0].hosts[4].paths[0].apiGatewayRouteName | string | `"sysdigcloud-events-dispatcher-http-v2"` |  |
| events.ingress[0].hosts[4].paths[0].openshiftRouteName | string | `"sysdigcloud-events-dispatcher-http-v2"` |  |
| events.ingress[0].hosts[4].paths[0].path | string | `"/api/eventsDispatcher/v2"` |  |
| events.ingress[0].hosts[4].paths[0].serviceName | string | `"sysdigcloud-events-dispatcher"` |  |
| events.ingress[0].hosts[4].paths[0].servicePort | int | `7000` |  |
| events.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| events.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| events.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| events.ingress[0].labels.role | string | `"ingress-config"` |  |
| events.ingress[0].labels.tier | string | `"infra"` |  |
| events.ingress[0].name | string | `"sysdigcloud-events-ingress"` |  |
| events.janitor.cronjob | string | `"0 2 * * *"` |  |
| events.janitor.suspend | bool | `false` |  |
| events.natsConsumers.aaMde.ackWait | string | `"30s"` |  |
| events.natsConsumers.aaMde.disabled | bool | `false` |  |
| events.natsConsumers.aaMde.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.admissioncontroller.ackWait | string | `"30s"` |  |
| events.natsConsumers.admissioncontroller.disabled | bool | `false` |  |
| events.natsConsumers.admissioncontroller.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.dispatcher.ackWait | string | `"30s"` |  |
| events.natsConsumers.dispatcher.disabled | bool | `false` |  |
| events.natsConsumers.dispatcher.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.falcoCustom.ackWait | string | `"30s"` |  |
| events.natsConsumers.falcoCustom.disabled | bool | `false` |  |
| events.natsConsumers.falcoCustom.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.falcoManaged.ackWait | string | `"30s"` |  |
| events.natsConsumers.falcoManaged.disabled | bool | `false` |  |
| events.natsConsumers.falcoManaged.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.falcoPreview.ackWait | string | `"30s"` |  |
| events.natsConsumers.falcoPreview.disabled | bool | `false` |  |
| events.natsConsumers.falcoPreview.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.mdeCustom.ackWait | string | `"30s"` |  |
| events.natsConsumers.mdeCustom.disabled | bool | `false` |  |
| events.natsConsumers.mdeCustom.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.mdeManaged.ackWait | string | `"30s"` |  |
| events.natsConsumers.mdeManaged.disabled | bool | `false` |  |
| events.natsConsumers.mdeManaged.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.mdePreview.ackWait | string | `"30s"` |  |
| events.natsConsumers.mdePreview.disabled | bool | `false` |  |
| events.natsConsumers.mdePreview.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.mlCloud.ackWait | string | `"30s"` |  |
| events.natsConsumers.mlCloud.disabled | bool | `false` |  |
| events.natsConsumers.mlCloud.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.platformAudit.ackWait | string | `"30s"` |  |
| events.natsConsumers.platformAudit.disabled | bool | `false` |  |
| events.natsConsumers.platformAudit.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.preview.ackWait | string | `"30s"` |  |
| events.natsConsumers.preview.disabled | bool | `false` |  |
| events.natsConsumers.preview.maxInFlight | string | `"10000"` |  |
| events.natsConsumers.statefulDetections.ackWait | string | `"30s"` |  |
| events.natsConsumers.statefulDetections.disabled | bool | `true` |  |
| events.natsConsumers.statefulDetections.maxInFlight | string | `"10000"` |  |
| events.natsjs.tls.enabled | string | `"true"` |  |
| events.policies.grpc.enabled | bool | `true` |  |
| events.quickwit.eventsActivityAuditGatherer.enabled | bool | `false` |  |
| events.quickwit.eventsApi.cutoffTime | string | `""` |  |
| events.quickwit.eventsApi.enabled | bool | `false` |  |
| events.quickwit.eventsGatherer.enabled | bool | `false` |  |
| events.quickwit.eventsJanitor.debug | bool | `false` |  |
| events.quickwit.eventsJanitor.dryRun | bool | `true` |  |
| events.quickwit.eventsJanitor.enabled | bool | `false` |  |
| events.quickwit.verifySSL | bool | `false` |  |
| events.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| events.repositoryPrefix | string | `"secure"` |  |
| events.resources.eventsActivityAuditGatherer.limits.cpu | int | `2` |  |
| events.resources.eventsActivityAuditGatherer.limits.memory | string | `"1Gi"` |  |
| events.resources.eventsActivityAuditGatherer.requests.cpu | string | `"250m"` |  |
| events.resources.eventsActivityAuditGatherer.requests.memory | string | `"250Mi"` |  |
| events.resources.eventsApi.limits.cpu | int | `1` |  |
| events.resources.eventsApi.limits.memory | string | `"500Mi"` |  |
| events.resources.eventsApi.requests.cpu | string | `"250m"` |  |
| events.resources.eventsApi.requests.memory | string | `"50Mi"` |  |
| events.resources.eventsDispatcher.limits.cpu | int | `1` |  |
| events.resources.eventsDispatcher.limits.memory | string | `"250Mi"` |  |
| events.resources.eventsDispatcher.requests.cpu | string | `"250m"` |  |
| events.resources.eventsDispatcher.requests.memory | string | `"50Mi"` |  |
| events.resources.eventsGatherer.limits.cpu | int | `2` |  |
| events.resources.eventsGatherer.limits.memory | string | `"1Gi"` |  |
| events.resources.eventsGatherer.requests.cpu | string | `"250m"` |  |
| events.resources.eventsGatherer.requests.memory | string | `"250Mi"` |  |
| events.resources.eventsIngestion.limits.cpu | int | `1` |  |
| events.resources.eventsIngestion.limits.memory | string | `"250Mi"` |  |
| events.resources.eventsIngestion.requests.cpu | string | `"250m"` |  |
| events.resources.eventsIngestion.requests.memory | string | `"50Mi"` |  |
| events.resources.eventsJanitor.limits.cpu | string | `"250m"` |  |
| events.resources.eventsJanitor.limits.memory | string | `"250Mi"` |  |
| events.resources.eventsJanitor.requests.cpu | string | `"250m"` |  |
| events.resources.eventsJanitor.requests.memory | string | `"250Mi"` |  |
| events.resources.geolocDbLoader.limits.cpu | int | `1` |  |
| events.resources.geolocDbLoader.limits.memory | string | `"500Mi"` |  |
| events.resources.geolocDbLoader.requests.cpu | string | `"250m"` |  |
| events.resources.geolocDbLoader.requests.memory | string | `"50Mi"` |  |
| events.scaler.aaGatherer.backlogThreshold | int | `7000` |  |
| events.scaler.aaGatherer.cpuThreshold | int | `100` |  |
| events.scaler.aaGatherer.enabled | bool | `false` |  |
| events.scaler.aaGatherer.maxReplicaCount | int | `10` |  |
| events.scaler.aaGatherer.memoryThreshold | int | `90` |  |
| events.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| events.scaler.clusterName | string | `"provider-env-region-DD"` |  |
| events.scaler.gatherer.backlogThreshold | int | `7000` |  |
| events.scaler.gatherer.cpuThreshold | int | `100` |  |
| events.scaler.gatherer.enabled | bool | `false` |  |
| events.scaler.gatherer.maxReplicaCount | int | `10` |  |
| events.scaler.gatherer.memoryThreshold | int | `90` |  |
| events.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| events.sdauthCacheTTL | string | `"5m"` |  |
| events.skippedLabels | string | `""` |  |
| events.statsPrintedLabels | string | `""` |  |
| events.tier.apiBased | bool | `false` |  |
| events.tier.default.override | string | `"benchmark:365"` |  |
| events.tier.default.retentionDays | int | `90` |  |
| events.zones.enabled | bool | `true` |  |
| events.zones.v2 | bool | `true` |  |
| global.api.serviceTokens.events.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","hostname":"sysdigcloud-elasticsearch","port":9200,"scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyRedis.redisClientsSecure.events.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.platformAuditTrail.enabled | bool | `false` |  |
| global.quickwit.auth.basicAuth.password | string | `nil` |  |
| global.quickwit.auth.basicAuth.username | string | `nil` |  |
| global.quickwit.indexer.endpoint | string | `nil` |  |
| global.quickwit.searcher.endpoint | string | `nil` |  |
| global.secure.iac.policyService.endpoint | string | `"secure-iac-policy-service:8080"` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.secure.mds.endpoint | string | `"sysdigcloud-metadata-service-server:5300"` |  |
| global.secure.policies.grpcEndpoint | string | `"sysdigcloud-policies-api:9199"` |  |
| global.secure.policies.restEndpoint | string | `"http://sysdigcloud-policies-api:9137"` |  |
| global.zones.platformService.endpoint | string | `"sysdigcloud-platform-zones-service-grpc:8091"` |  |
| global.zones.platformService.tlsSkip | string | `"true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# falco-validator

![Version: 4.0.1-260309140914-main-v50f8079](https://img.shields.io/badge/Version-4.0.1--260309140914--main--v50f8079-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Falco Validator Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| falcovalidator.enabled | bool | `true` |  |
| falcovalidator.falcoValidatorReplicaCount | int | `5` |  |
| falcovalidator.hpa.cpuAverage | float | `1.5` |  |
| falcovalidator.hpa.enabled | bool | `true` |  |
| falcovalidator.hpa.maxReplicas | int | `25` |  |
| falcovalidator.hpa.memoryAverage | int | `50` |  |
| falcovalidator.hpa.minReplicas | int | `5` |  |
| falcovalidator.hpa.scaleDown.periodSeconds | int | `300` |  |
| falcovalidator.hpa.scaleDown.podValue | int | `1` |  |
| falcovalidator.hpa.scaleDown.stabilizationWindowSeconds | int | `120` |  |
| falcovalidator.hpa.scaleUp.periodSeconds | int | `15` |  |
| falcovalidator.hpa.scaleUp.podValue | int | `2` |  |
| falcovalidator.hpa.scaleUp.stabilizationWindowSeconds | int | `0` |  |
| falcovalidator.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| falcovalidator.repositoryPrefix | string | `"secure"` |  |
| falcovalidator.resources.falcoValidator.limits.cpu | string | `"5500m"` |  |
| falcovalidator.resources.falcoValidator.limits.memory | string | `"3Gi"` |  |
| falcovalidator.resources.falcoValidator.requests.cpu | string | `"1500m"` |  |
| falcovalidator.resources.falcoValidator.requests.memory | string | `"3Gi"` |  |
| global.api.serviceTokens.falcovalidator.serviceToken | string | `"change_me"` |  |
| global.apps | string | `"secure"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# fingerprints

![Version: 5.2.0-260212153214-main-v118f5b8](https://img.shields.io/badge/Version-5.2.0--260212153214--main--v118f5b8-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Fingerprints Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| fingerprints.allowAllCustomers | bool | `true` |  |
| fingerprints.allowedCustomers | string | `""` |  |
| fingerprints.api.store.osReadBatcher.execChanSize | int | `100` |  |
| fingerprints.api.store.osReadBatcher.flushPeriod | string | `"200ms"` |  |
| fingerprints.api.store.osReadBatcher.flushingRoutines | int | `20` |  |
| fingerprints.api.store.osReadBatcher.inputChanSize | int | `100` |  |
| fingerprints.api.store.osReadBatcher.maxBatchSize | int | `3` |  |
| fingerprints.api.store.osReadBatcher.maxBufferSize | int | `3` |  |
| fingerprints.api.store.osWriteBatcher.flushingRoutines | int | `1` |  |
| fingerprints.api.store.redisBatcher.execChanSize | int | `100` |  |
| fingerprints.api.store.redisBatcher.flushPeriod | string | `"200ms"` |  |
| fingerprints.api.store.redisBatcher.flushingRoutines | int | `20` |  |
| fingerprints.api.store.redisBatcher.inputChanSize | int | `100` |  |
| fingerprints.api.store.redisBatcher.maxBatchSize | int | `6` |  |
| fingerprints.api.store.redisBatcher.maxBufferSize | int | `6` |  |
| fingerprints.apiReplicaCount | int | `1` |  |
| fingerprints.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| fingerprints.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| fingerprints.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| fingerprints.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| fingerprints.enabled | bool | `true` |  |
| fingerprints.filesJanitor.retentionDays | string | `"3"` |  |
| fingerprints.filesJanitor.schedule | string | `"0 3 * * *"` |  |
| fingerprints.forceMigrations | bool | `false` |  |
| fingerprints.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-fingerprints-files-http"` |  |
| fingerprints.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-fingerprints-files-http"` |  |
| fingerprints.ingress[0].hosts[0].paths[0].path | string | `"/api/fingerprints"` |  |
| fingerprints.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-fingerprints-files-http"` |  |
| fingerprints.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| fingerprints.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-fingerprints-files-v1-http"` |  |
| fingerprints.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-fingerprints-files-v1-http"` |  |
| fingerprints.ingress[0].hosts[0].paths[1].path | string | `"/api/v1/profiling/runtime/kubernetes"` |  |
| fingerprints.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-fingerprints-files-http"` |  |
| fingerprints.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| fingerprints.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| fingerprints.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| fingerprints.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| fingerprints.ingress[0].labels.role | string | `"ingress-config"` |  |
| fingerprints.ingress[0].labels.tier | string | `"infra"` |  |
| fingerprints.ingress[0].name | string | `"sysdigcloud-fingerprints"` |  |
| fingerprints.nats.batching.retry.flushPeriod | string | `"5s"` |  |
| fingerprints.nats.batching.retry.flushingRoutines | int | `2` |  |
| fingerprints.nats.batching.retry.maxAsyncCalls | int | `30` |  |
| fingerprints.nats.batching.retry.maxBatchByteSize | int | `10000` |  |
| fingerprints.nats.batching.retry.maxBatchSize | int | `30` |  |
| fingerprints.nats.batching.retry.maxBufferByteSize | int | `50000` |  |
| fingerprints.nats.batching.retry.maxBufferSize | int | `90` |  |
| fingerprints.nats.consumers.mde.ackWait | string | `"180s"` |  |
| fingerprints.nats.consumers.mde.dlqHandleDelay | string | `"30s"` |  |
| fingerprints.nats.consumers.mde.dlqSubjectPrefix | string | `"fingerprints.files.dlq"` |  |
| fingerprints.nats.consumers.mde.durable | string | `"fingerprints-files"` |  |
| fingerprints.nats.consumers.mde.maxInFlight | int | `20000` |  |
| fingerprints.nats.consumers.mde.name | string | `"metadata-enricher-fingerprints-1"` |  |
| fingerprints.nats.consumers.mde.pullBatch | int | `32` |  |
| fingerprints.nats.consumers.mde.queue | string | `"fingerprints-files"` |  |
| fingerprints.nats.consumers.mde.streamName | string | `"metadata-enricher-fingerprints-1"` |  |
| fingerprints.nats.consumers.mde.subject | string | `"metadataenricher.fingerprints.1.>"` |  |
| fingerprints.nats.consumers.retry.ackWait | string | `"180s"` |  |
| fingerprints.nats.consumers.retry.dlqHandleDelay | string | `"30s"` |  |
| fingerprints.nats.consumers.retry.dlqSubjectPrefix | string | `"fingerprints.files.dlq"` |  |
| fingerprints.nats.consumers.retry.durable | string | `"fingerprints-files-retry"` |  |
| fingerprints.nats.consumers.retry.maxInFlight | int | `10000` |  |
| fingerprints.nats.consumers.retry.name | string | `"fingerprints-files-retry"` |  |
| fingerprints.nats.consumers.retry.pullBatch | int | `32` |  |
| fingerprints.nats.consumers.retry.queue | string | `"fingerprints-files-retry"` |  |
| fingerprints.nats.consumers.retry.streamName | string | `"fingerprints-files-internal"` |  |
| fingerprints.nats.consumers.retry.subject | string | `"fingerprints.files.retry"` |  |
| fingerprints.nats.streams.fingerprints-files-internal.max_age | int | `172800000000000` |  |
| fingerprints.nats.streams.fingerprints-files-internal.max_bytes | int | `4294967296` |  |
| fingerprints.nats.streams.fingerprints-files-internal.metadata.version | string | `"2"` |  |
| fingerprints.nats.streams.fingerprints-files-internal.name | string | `"fingerprints-files-internal"` |  |
| fingerprints.nats.streams.fingerprints-files-internal.num_replicas | int | `3` |  |
| fingerprints.nats.streams.fingerprints-files-internal.storage | string | `"file"` |  |
| fingerprints.nats.streams.fingerprints-files-internal.subjects[0] | string | `"fingerprints.files.dlq.>"` |  |
| fingerprints.nats.streams.fingerprints-files-internal.subjects[1] | string | `"fingerprints.files.retry"` |  |
| fingerprints.opensearch.host | string | `"opensearch:9200"` |  |
| fingerprints.opensearch.nodeDiscovery | bool | `true` |  |
| fingerprints.opensearch.nodeDiscoveryInterval | string | `"5m"` |  |
| fingerprints.opensearch.password | string | `""` |  |
| fingerprints.opensearch.tls.certs | list | `[]` |  |
| fingerprints.opensearch.tls.skipCheck | bool | `false` |  |
| fingerprints.opensearch.useDedicated | bool | `false` |  |
| fingerprints.opensearch.username | string | `""` |  |
| fingerprints.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| fingerprints.replicaCount | int | `1` |  |
| fingerprints.repositoryPrefix | string | `"secure"` |  |
| fingerprints.resources.fingerprintsFiles.limits.cpu | string | `"250m"` |  |
| fingerprints.resources.fingerprintsFiles.limits.memory | string | `"250Mi"` |  |
| fingerprints.resources.fingerprintsFiles.requests.cpu | string | `"250m"` |  |
| fingerprints.resources.fingerprintsFiles.requests.memory | string | `"250Mi"` |  |
| fingerprints.resources.fingerprintsFilesApi.limits.cpu | string | `"250m"` |  |
| fingerprints.resources.fingerprintsFilesApi.limits.memory | string | `"250Mi"` |  |
| fingerprints.resources.fingerprintsFilesApi.requests.cpu | string | `"250m"` |  |
| fingerprints.resources.fingerprintsFilesApi.requests.memory | string | `"250Mi"` |  |
| fingerprints.resources.fingerprintsFilesJanitor.limits.cpu | string | `"250m"` |  |
| fingerprints.resources.fingerprintsFilesJanitor.limits.memory | string | `"250Mi"` |  |
| fingerprints.resources.fingerprintsFilesJanitor.requests.cpu | string | `"250m"` |  |
| fingerprints.resources.fingerprintsFilesJanitor.requests.memory | string | `"250Mi"` |  |
| fingerprints.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| fingerprints.scaler.clusterName | string | `"provider-env-region-DD"` |  |
| fingerprints.scaler.files.backlogThreshold | int | `2500` |  |
| fingerprints.scaler.files.enabled | bool | `true` |  |
| fingerprints.scaler.files.maxReplicaCount | int | `15` |  |
| fingerprints.scaler.files.memoryThreshold | int | `90` |  |
| fingerprints.scaler.filesApi.cpuThreshold | int | `90` |  |
| fingerprints.scaler.filesApi.enabled | bool | `true` |  |
| fingerprints.scaler.filesApi.maxReplicaCount | int | `10` |  |
| fingerprints.scaler.filesApi.memoryThreshold | int | `90` |  |
| fingerprints.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| fingerprints.serviceAccountName | string | `"sysdig"` |  |
| fingerprints.skippedCustomers | string | `""` |  |
| fingerprints.store.cached.hardLimit | string | `"1500"` |  |
| fingerprints.store.cached.redisShortTTL | string | `"1h"` |  |
| fingerprints.store.cached.redisTTL | string | `"6h"` |  |
| fingerprints.store.cached.softLimit | string | `"1000"` |  |
| fingerprints.store.cached.useHash | bool | `false` |  |
| fingerprints.store.os.readBatcher.execChanSize | int | `100` |  |
| fingerprints.store.os.readBatcher.flushPeriod | string | `"200ms"` |  |
| fingerprints.store.os.readBatcher.flushingRoutines | int | `20` |  |
| fingerprints.store.os.readBatcher.inputChanSize | int | `100` |  |
| fingerprints.store.os.readBatcher.maxBatchSize | int | `15` |  |
| fingerprints.store.os.readBatcher.maxBufferSize | int | `15` |  |
| fingerprints.store.os.searchSize | string | `"1000"` |  |
| fingerprints.store.os.writeBatcher.execChanSize | int | `100` |  |
| fingerprints.store.os.writeBatcher.flushPeriod | string | `"1s"` |  |
| fingerprints.store.os.writeBatcher.flushingRoutines | int | `8` |  |
| fingerprints.store.os.writeBatcher.inputChanSize | int | `100` |  |
| fingerprints.store.os.writeBatcher.maxBatchSize | int | `150` |  |
| fingerprints.store.os.writeBatcher.maxBufferSize | int | `150` |  |
| fingerprints.store.redisBatched.execChanSize | int | `100` |  |
| fingerprints.store.redisBatched.flushPeriod | string | `"2s"` |  |
| fingerprints.store.redisBatched.flushingRoutines | int | `20` |  |
| fingerprints.store.redisBatched.inputChanSize | int | `100` |  |
| fingerprints.store.redisBatched.maxBatchSize | int | `10` |  |
| fingerprints.store.redisBatched.maxBufferSize | int | `10` |  |
| fingerprints.worker.handleTimeout | string | `"120s"` |  |
| fingerprints.worker.maxRetries | int | `1` |  |
| fingerprints.worker.natsConsumerRoutines | int | `0` |  |
| fingerprints.worker.retryConsumerRoutines | int | `0` |  |
| fingerprints.worker.retryDelay | string | `"1m"` |  |
| global.api.serviceTokens.fingerprints.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","hostname":"sysdigcloud-elasticsearch","port":9200,"scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.legacyRedis.redisClientsSecure.fingerprints.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.secure.mds.endpoint | string | `"sysdigcloud-metadata-service-server:5300"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# haproxy-ingress

![Version: 1.9.14](https://img.shields.io/badge/Version-1.9.14-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.0](https://img.shields.io/badge/AppVersion-1.0.0-informational?style=flat-square)

This is owned and maintained by Sysdig Infra team.

In this first version the `values.yaml` structure resembles the one used by the `installer` for compatibility reasons.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.airgappedRegistryName | string | `""` |  |
| global.airgappedRepositoryPrefix | string | `""` |  |
| global.apps | string | `"monitor"` |  |
| global.cloudProvider.create_loadbalancer | bool | `false` |  |
| global.deployment | string | `"kubernetes"` |  |
| global.haproxy.defaultBackendVersion | float | `1.5` |  |
| global.haproxy.enabled | bool | `true` |  |
| global.haproxy.forwardfor | string | `nil` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.ingressServiceExternalTrafficPolicy | string | `nil` |  |
| global.namespace | string | `"sysdig"` |  |
| global.tolerations | list | `[]` |  |
| haproxyIngress.IKSPerVLANReplicaCount | int | `2` |  |
| haproxyIngress.additionalTcpServices | list | `[]` |  |
| haproxyIngress.certificateSecret | string | `"sysdigcloud-collector-ssl-secret"` |  |
| haproxyIngress.collectorInternalPort | int | `6000` |  |
| haproxyIngress.defaultIngressClass | bool | `true` |  |
| haproxyIngress.haproxyVersion | string | `"1.8.15-v0.14-ubi"` |  |
| haproxyIngress.priorityClass.create | bool | `false` |  |
| haproxyIngress.priorityClass.value | int | `800000000` |  |
| haproxyIngress.registryName | string | `"quay.io"` |  |
| haproxyIngress.repositoryPrefix | string | `"sysdig"` |  |
| haproxyIngress.resources.ingressControllerHaProxy.limits.cpu | string | `"1"` |  |
| haproxyIngress.resources.ingressControllerHaProxy.limits.memory | string | `"500Mi"` |  |
| haproxyIngress.resources.ingressControllerHaProxy.requests.cpu | string | `"100m"` |  |
| haproxyIngress.resources.ingressControllerHaProxy.requests.memory | string | `"100Mi"` |  |
| haproxyIngress.resources.ingressControllerRsyslog.limits.cpu | string | `"250m"` |  |
| haproxyIngress.resources.ingressControllerRsyslog.limits.memory | string | `"100Mi"` |  |
| haproxyIngress.resources.ingressControllerRsyslog.requests.cpu | string | `"50m"` |  |
| haproxyIngress.resources.ingressControllerRsyslog.requests.memory | string | `"20Mi"` |  |
| haproxyIngress.rsyslogVersion | string | `"8.2506.0"` |  |
| haproxyIngress.watchAllNamespaces | bool | `false` |  |

# helm-renderer

![Version: 1.2.344](https://img.shields.io/badge/Version-1.2.344-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Helm Renderer

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor"` |  |
| global.helmRenderer.enabled | bool | `true` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nodeaffinityLabel | object | `{}` |  |
| helmRenderer.enableNetworkPolicy | bool | false | creates NetworkPolicy objects for the helmRenderer service. |
| helmRenderer.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| helmRenderer.replicaCount | int | `2` |  |
| helmRenderer.repositoryPrefix | string | `"monitor"` |  |
| helmRenderer.resources.helmRenderer.limits.cpu | int | `2` |  |
| helmRenderer.resources.helmRenderer.limits.memory | string | `"1Gi"` |  |
| helmRenderer.resources.helmRenderer.requests.cpu | string | `"500m"` |  |
| helmRenderer.resources.helmRenderer.requests.memory | string | `"512Mi"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# kafka-cruise-control

![Version: 2.4.13](https://img.shields.io/badge/Version-2.4.13-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.5.146](https://img.shields.io/badge/AppVersion-2.5.146-informational?style=flat-square)

This is owned and maintained by Sysdig Infra team. It conditionally installs Kafka CruiseControl

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.airgappedRegistryName | string | `nil` | registry name for airgapped environments |
| global.airgappedRepositoryPrefix | string | `nil` | repository prefix for airgapped environments |
| global.kafka.broker.internalPort | int | `9092` |  |
| global.kafka.name | string | `"cp-kafka"` |  |
| global.kafka.namespace | string | `"sysdig"` | namespace where to install cruise-control |
| global.kafka.secure.enabled | bool | `false` |  |
| global.kafka.secure.useCertManager | bool | `false` | whether to use cert-manager for certificate management |
| global.kafkaCASecretName | string | `"kafka-ca-secret"` | name of the secret exported by cert manager |
| global.kafkaCruiseControl.enabled | bool | `true` | if false, scales deployment to 0 replicas |
| global.zookeeper.clientPort | int | `2181` |  |
| global.zookeeper.name | string | `"zookeeper"` |  |
| global.zookeeper.secureClientPort | int | `2182` |  |
| kafkaCruiseControl.additionalConfiguration | object | `{"default.replication.throttle":"20971520","max.num.cluster.partition.movements":"10","max.replicas.per.broker":"10000","num.concurrent.leader.movements":"100","num.concurrent.leader.movements.per.broker":"50","num.concurrent.partition.movements.per.broker":"5","overprovisioned.max.replicas.per.broker":"1500","sample.store.topic.replication.factor":"3","self.healing.goal.violation.enabled":"false"}` | additional configurations, WARNING: values should be quoted! (reference https://github.com/linkedin/cruise-control/wiki/Configurations) |
| kafkaCruiseControl.capacity.cpuCores | int | `2` | set the brokers CPU target for the Capacity Goals |
| kafkaCruiseControl.capacity.diskMB | int | `1000` | set the brokers Storage MB target for the Capacity Goals |
| kafkaCruiseControl.capacity.networkInKBS | int | `20480` | set the brokers Network IN target for the Capacity Goals |
| kafkaCruiseControl.capacity.networkOutKBS | int | `20480` | set the brokers Network OUT target for the Capacity Goals |
| kafkaCruiseControl.goals.anomalyDetection | list | `["RackAwareGoal","CpuCapacityGoal","DiskCapacityGoal","NetworkInboundCapacityGoal","NetworkOutboundCapacityGoal"]` | anomalyDetection (enabled) goals are the ones that will trigger GOAL anomalies (useful if self.headling.goals.violation.enabled) (https://github.com/linkedin/cruise-control#goals) |
| kafkaCruiseControl.goals.default | list | `["RackAwareGoal","CpuCapacityGoal","DiskCapacityGoal","NetworkInboundCapacityGoal","NetworkOutboundCapacityGoal","LeaderBytesInDistributionGoal","NetworkInboundUsageDistributionGoal","NetworkOutboundUsageDistributionGoal","DiskUsageDistributionGoal","ReplicaDistributionGoal"]` | default (enabled) goals are the ones that will contribute to the overall rebalance plan/execution (https://github.com/linkedin/cruise-control#goals), the order of appearance in the list defines the goals priority!!! |
| kafkaCruiseControl.goals.hard | list | `["RackAwareGoal","CpuCapacityGoal","DiskCapacityGoal","NetworkInboundCapacityGoal","NetworkOutboundCapacityGoal"]` | hard (enabled) goals are the ones that have higher priority and are enforced for every rebalance plan/execution (https://github.com/linkedin/cruise-control#goals) |
| kafkaCruiseControl.goals.selfHealing | list | `["RackAwareGoal","CpuCapacityGoal","DiskCapacityGoal","NetworkInboundCapacityGoal","NetworkOutboundCapacityGoal","LeaderBytesInDistributionGoal","NetworkInboundUsageDistributionGoal","NetworkOutboundUsageDistributionGoal","DiskUsageDistributionGoal","ReplicaDistributionGoal"]` | selfHealing (enabled) goals are the ones used by the self healing rebalance after a goalAnomaly got triggered (useful if self.headling.goals.violation.enabled) |
| kafkaCruiseControl.image.name | string | `"cruise-control-2"` |  |
| kafkaCruiseControl.image.tag | string | `"2.4.12"` |  |
| kafkaCruiseControl.imagePullSecrets[0].name | string | `"sysdigcloud-pull-secret"` |  |
| kafkaCruiseControl.prometheus.autodiscovery | bool | `false` | adds Prometheus autodiscovery annotations to the pods |
| kafkaCruiseControl.prometheus.jmxExporterConfiguration | string | `"rules:\n- pattern: \".*\""` | prometheus jmx exporter minimal configuration (https://github.com/prometheus/jmx_exporter/blob/release-0.20.0/README.md) |
| kafkaCruiseControl.registryName | string | `"quay.io"` | default registry name |
| kafkaCruiseControl.repositoryPrefix | string | `"sysdig"` | default repository prefix |
| kafkaCruiseControl.resources.limits | object | `{"cpu":"1","memory":"2Gi"}` | resource limits |
| kafkaCruiseControl.resources.requests | object | `{"cpu":"1","memory":"2Gi"}` | resource requests |

# kafka

![Version: 3.6.17](https://img.shields.io/badge/Version-3.6.17-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 7.9.4](https://img.shields.io/badge/AppVersion-7.9.4-informational?style=flat-square)

This is owned and maintained by Sysdig Infra team. It conditionally installs kafka

In this first version the `values.yaml` structure resembles the one used by the `installer` for compatibility reasons.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.airgappedRegistryName | string | `nil` | registry name for airgapped environments |
| global.airgappedRepositoryPrefix | string | `nil` | repository prefix for airgapped environments |
| global.cloudProvider.isMultiAZ | bool | `false` | "true" spreads pods across AZs |
| global.cloudProvider.name | string | `""` |  |
| global.fastpathAggregator.enabled | bool | `false` |  |
| global.kafka.broker.internalPort | int | `9092` | kafka internal port |
| global.kafka.name | string | `"cp-kafka"` | used as base name to create kafka k8s objects |
| global.kafka.namespace | string | `"sysdig"` | namespace where to install kafka |
| global.kafka.secure.caCrt | string | `""` | base64 encoded CA certificate for kafka. These certs can be generated with: ```openssl req -x509 -nodes -sha256 -days 7300 -newkey rsa:4096 -subj '/C=US/ST=CA/L=SanFrancisco/O=Sysdig' -addext "keyUsage= digitalSignature, keyEncipherment, keyCertSign" -addext "extendedKeyUsage= serverAuth, clientAuth" -keyout "ca.key" -out "ca.crt"``` |
| global.kafka.secure.caKey | string | `""` | base64 encoded CA key for kafka |
| global.kafka.secure.enabled | bool | `false` | whether to enable TLS for kafka cluster |
| global.kafka.secure.fipsmode | bool | `false` | enable FIPS mode |
| global.kafka.secure.securityProtocol | string | `"SSL"` | define security protocol |
| global.kafka.secure.sslClientAuth | string | `"requested"` | set the encryption requirements for kafka clients. can be none, requested, or required |
| global.kafka.secure.useCertManager | bool | `false` | whether to use cert-manager for certificate management |
| global.kafka.serviceAccount | string | `""` | name of an already existing serviceAccount to be used for default workloads, if empty, will create a new one |
| global.kafkaCASecretName | string | `"kafka-ca-secret"` | name of the secret produced by cert manager for the CA certificate |
| global.kafkaCruiseControl.enabled | bool | `true` | if false, scales deployment to 0 replicas |
| global.kafkaOpts | string | `""` | used to fill KAFKA_OPTS. Could used be to enable debugging "-Djava.security.debug=sunpkcs11" |
| global.meerkat.enabled | bool | `false` |  |
| global.storageClassProvisioner | string | `""` |  |
| global.streamsnap.enabled | bool | `false` |  |
| global.zookeeper.clientPort | int | `2181` | zookeeper client port |
| global.zookeeper.name | string | `"zookeeper"` | used as base name to create zookeeper k8s resources |
| global.zookeeper.secureClientPort | int | `2182` | zookeeper secure client port |
| kafka.broker.externalPort | int | `9093` | kafka external port |
| kafka.broker.readinessProbe.periodSeconds | int | `10` | kafka readiness probe frequency of checks |
| kafka.broker.readinessProbe.timeoutSeconds | int | `30` | kafka readiness probe timeout |
| kafka.configurationOverrides | object | `{"auto.create.topics.enable":"false","default.replication.factor":"3","delete.topic.enable":"true","group.initial.rebalance.delay.ms":"15000","group.max.session.timeout.ms":"300000","message.max.bytes":"20971520","min.insync.replicas":"2","num.replica.fetchers":"3","offsets.topic.replication.factor":"3","replica.fetch.max.bytes":"20971520","replica.lag.time.max.ms":"29000","replica.selector.class":"org.apache.kafka.common.replica.RackAwareReplicaSelector","unclean.leader.election.enable":"true","zookeeper.connection.timeout.ms":"6000","zookeeper.session.timeout.ms":"6000"}` | additional env vars for the kafka pods |
| kafka.cruiseControl.metricsTopic.autoCreate | bool | `true` |  |
| kafka.cruiseControl.metricsTopic.partitions | int | `10` |  |
| kafka.cruiseControl.metricsTopic.replicationFactor | int | `3` |  |
| kafka.disableEviction | bool | `false` | disable pod eviction by cluster autoscaler |
| kafka.enableMetrics | bool | `false` | enable kafka jmx exporter metrics |
| kafka.exporter.livenessProbe.initialDelaySeconds | int | `90` | kafka exporter container initial delay seconds for liveness probe |
| kafka.exporter.livenessProbe.periodSeconds | int | `30` | kafka exporter liveness probe frequency of checks |
| kafka.exporter.livenessProbe.timeoutSeconds | int | `30` | kafka exporter liveness probe timeout |
| kafka.exporter.readinessProbe.initialDelaySeconds | int | `30` | kafka exporter container initial delay seconds for readiness probe |
| kafka.exporter.readinessProbe.periodSeconds | int | `10` | kafka exporter readiness probe frequency of checks |
| kafka.exporter.readinessProbe.timeoutSeconds | int | `30` | kafka exporter readiness probe timeout |
| kafka.extraLabels | object | `{"owners":"infra"}` | extra pod labels for kafka objects |
| kafka.imageName | string | `"cp-kafka-7"` | name of the kafka image |
| kafka.interBrokerProtocolVersion | string | `"3.9"` | protocol version for inter broker communication |
| kafka.jmxPort | int | `9010` | kafka jmx port |
| kafka.jvmOptions | string | `""` | used to fill KAFKA_HEAP_OPTS kafka pods env var |
| kafka.kafkaExporterVersion | string | `"v1.0.22-ubi"` | jmx exporter image name |
| kafka.livenessProbeInitialDelaySeconds | int | `600` | kafka broker container initial delay seconds for liveness probe, on slow disks the initial recovery can take a large amount of time, during this time the client port is not listening for connections |
| kafka.loggersConfig | string | `"kafka=INFO,kafka.controller=INFO,kafka.log.LogCleaner=INFO,state.change.logger=INFO,kafka.producer.async.DefaultEventHandler=INFO"` |  |
| kafka.minReadySeconds | int | `0` | how many seconds to wait after a pod is ready before rolling the next pod in a rolling update |
| kafka.multiAZServiceAccount | string | `""` | name of an already existing serviceAccount to be used for workloads that queries the api server (e.g. node-labels-to-files, when cloudProvider.isMultiAZ: true), if empty, will create a new one |
| kafka.multiCluster | object | `{"enabled":false,"roles":["source","target"],"side":"source","stableDNSSvc":false}` | kafka migration config (using linkerd multicluster) |
| kafka.nodeAffinityMode | string | `"preferred"` | make nodeAffinity "required" or "preferred" |
| kafka.nodeLabelsImageName | string | `"node-labels-to-files"` | NodeLabels image tag |
| kafka.nodeLabelsVersion | string | `"1.0.76"` |  |
| kafka.nodeaffinityLabel | string | `nil` | label on which create nodeAffinity |
| kafka.offset | int | `0` |  |
| kafka.persistentVolumeClaim.size | string | `"100Gi"` | kafka data pvc size |
| kafka.persistentVolumeClaim.storageClassName | string | `"sysdig"` | kafka data pvc storage class name |
| kafka.podManagementPolicy | string | `"Parallel"` | which pod management policy to use "Parallel" or "OrderedReady" for kafka |
| kafka.productCategory.enabled | bool | `false` |  |
| kafka.productCategory.label | string | `"monitor"` |  |
| kafka.registryName | string | `"quay.io"` | default registry name |
| kafka.replicaCount | int | `3` | kafka replica count |
| kafka.repositoryPrefix | string | `"sysdig"` | default repository prefix |
| kafka.resources.kafka | object | `{"limits":{"cpu":"4","memory":"8Gi"},"requests":{"cpu":"1","memory":"3Gi"}}` | kafka pods resources |
| kafka.resources.kafka_exporter.limits.cpu | string | `"1"` |  |
| kafka.resources.kafka_exporter.limits.memory | string | `"500Mi"` |  |
| kafka.resources.kafka_exporter.requests.cpu | string | `"300m"` |  |
| kafka.resources.kafka_exporter.requests.memory | string | `"100Mi"` |  |
| kafka.resources.kafka_hostpath_init.limits.cpu | string | `"50m"` |  |
| kafka.resources.kafka_hostpath_init.limits.memory | string | `"100Mi"` |  |
| kafka.resources.kafka_hostpath_init.requests.cpu | string | `"50m"` |  |
| kafka.resources.kafka_hostpath_init.requests.memory | string | `"100Mi"` |  |
| kafka.resources.kafka_init_vmmaxmapcount.limits.cpu | string | `"50m"` |  |
| kafka.resources.kafka_init_vmmaxmapcount.limits.memory | string | `"100Mi"` |  |
| kafka.resources.kafka_init_vmmaxmapcount.requests.cpu | string | `"50m"` |  |
| kafka.resources.kafka_init_vmmaxmapcount.requests.memory | string | `"100Mi"` |  |
| kafka.resources.node_labels_to_files.limits.cpu | string | `"50m"` |  |
| kafka.resources.node_labels_to_files.limits.memory | string | `"100Mi"` |  |
| kafka.resources.node_labels_to_files.requests.cpu | string | `"50m"` |  |
| kafka.resources.node_labels_to_files.requests.memory | string | `"100Mi"` |  |
| kafka.rootLogLevel | string | `"INFO"` | control kafka log level |
| kafka.secure.caCertExpiry | string | `"87660h"` | set ca cert expiry in hours |
| kafka.secure.caCertRenewBefore | string | `"360h"` | renew before how many hours of cert expiration |
| kafka.secure.certificateIssuer | string | `"sysdig-selfsigned-issuer"` | certificate issuer to use, keep this empty if creating an issuer |
| kafka.secure.certificateIssuerKind | string | `"ClusterIssuer"` | certificate issuer kind, this can be an Issuer or ClusterIssuer |
| kafka.secure.createIssuer | bool | `false` | create a kafka certificate issuer |
| kafka.secure.privateKeyAlgorithm | string | `"RSA"` | private key algorithm to use |
| kafka.secure.privateKeySize | int | `4096` | private key size to use |
| kafka.secure.securityProtocol | string | `"SSL"` |  |
| kafka.secure.sslClientAuth | string | `"requested"` |  |
| kafka.secure.sslProtocolVersion | string | `"TLSv1.3"` | define the SSL/TLS protocol version |
| kafka.setVmMaxMapCount | bool | `false` | setup vm.max_map_count=262144 with an initContainer |
| kafka.tolerations | list | `[]` | setup tolerations |
| kafka.topologySpreadConstraints.hostname | object | `{"whenUnsatisfiable":"DoNotSchedule"}` | Topology Spread toleration for hostname spread. Can be `DoNotSchedule` for a hard constraint or `ScheduleAnyway` for a soft constraint. |
| kafka.topologySpreadConstraints.multiAZ | object | `{"whenUnsatisfiable":"DoNotSchedule"}` | Topology Spread toleration for multiAZ spread. Can be `DoNotSchedule` for a hard constraint or `ScheduleAnyway` for a soft constraint. |
| kafka.updateStrategy | string | `"RollingUpdate"` | which update strategy to use "OnDelete" or "RollingRestart" for kafka |
| kafka.version | string | `"1.6.14"` | kafka image tag |

# linkerd

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: edge-24.10.5](https://img.shields.io/badge/AppVersion-edge-24.10.5-informational?style=flat-square)

Linkerd sysdig helm chart

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| airgapped_registry_name | string | `""` | registry name for airgapped environments |
| airgapped_repository_prefix | string | `""` | repository prefix for airgapped environments |
| networkEncryption.controlPlane.cniEnabled | bool | `false` |  |
| networkEncryption.controlPlane.identity.issuer.scheme | string | `"linkerd.io/tls"` |  |
| networkEncryption.controlPlane.identity.issuer.tls | object | `{"crtPEM":"","keyPEM":""}` | Which scheme is used for the identity issuer secret format |
| networkEncryption.controlPlane.identity.issuer.tls.crtPEM | string | `""` | Issuer certificate (ECDSA). It must be provided during install. |
| networkEncryption.controlPlane.identity.issuer.tls.keyPEM | string | `""` | Key for the issuer certificate (ECDSA). It must be provided during install |
| networkEncryption.controlPlane.identityTrustAnchorsPEM | string | `""` | Trust root certificate (ECDSA). It must be provided during install. |
| networkEncryption.controlPlane.imageVersions.cniPlugin | string | `"2.0.9"` |  |
| networkEncryption.controlPlane.imageVersions.controller | string | `"2.0.16"` |  |
| networkEncryption.controlPlane.imageVersions.debug | string | `"2.0.9"` |  |
| networkEncryption.controlPlane.imageVersions.policyController | string | `"2.0.17"` |  |
| networkEncryption.controlPlane.imageVersions.proxy | string | `"2.0.18"` |  |
| networkEncryption.controlPlane.imageVersions.proxyInit | string | `"2.0.18"` |  |
| networkEncryption.enabled | bool | `false` |  |
| registryName | string | `"quay.io"` | default registry name |
| repositoryPrefix | string | `"sysdig"` | default repository prefix |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# meerkat-aggregator

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig Meerkat Aggregator

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.meerkatAggregator.serviceToken | string | `nil` |  |
| global.apps | string | `"monitor"` |  |
| global.cassandra.datacenterName | string | `"DC1"` |  |
| global.cassandra.endpoint | string | `"sysdigcloud-cassandra"` |  |
| global.cassandra.port | int | `9042` |  |
| global.cassandra.replicaCount | int | `3` |  |
| global.cassandra.replicationStrategy | string | `"SimpleStrategy"` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.cassandra.sslVerify | bool | `false` |  |
| global.cassandra.useCertManager | bool | `false` |  |
| global.cassandra.workloadName | string | `"cassandra"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.grpc.auth.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.kafka.broker.externalPort | int | `9093` |  |
| global.kafka.name | string | `"cp-kafka"` |  |
| global.kafka.namespace | string | `"sysdigcloud"` |  |
| global.kafka.secure.enabled | bool | `false` |  |
| global.kafka.secure.useCertManager | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.common.tls | bool | `true` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `true` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.meerkat.enabled | bool | `true` |  |
| global.meerkat.objectStorage.accessKey | string | `""` |  |
| global.meerkat.objectStorage.endpoint | string | `""` |  |
| global.meerkat.objectStorage.region | string | `"us-east-1"` |  |
| global.meerkat.objectStorage.secretKey | string | `""` |  |
| global.meerkat.store.storageSource.primaryWriteSource | string | `"CASSANDRA"` |  |
| global.meerkat.store.storageSource.readSource | string | `"CASSANDRA"` |  |
| global.meerkat.store.storageSource.writeSource[0] | string | `"CASSANDRA"` |  |
| global.meerkat.store.useCassandraGPartTablePerSampling | bool | `true` |  |
| global.monitorRepositoryPrefix | string | `"monitor"` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.nodeLabelsVersion | string | `"1.0.74"` |  |
| global.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| meerkatAggregator.authorizationService.enabled | bool | `false` |  |
| meerkatAggregator.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| meerkatAggregator.consumer.maxBacklogSize | int | `5000` |  |
| meerkatAggregator.jvmOptions | string | `"-Dlogging.level.org.springframework.transaction.interceptor=TRACE -Dio.netty.leakDetection.level=advanced"` |  |
| meerkatAggregator.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| meerkatAggregator.replicaCount | int | `1` |  |
| meerkatAggregator.resources.meerkatAggregator.limits.cpu | int | `4` |  |
| meerkatAggregator.resources.meerkatAggregator.limits.memory | string | `"4Gi"` |  |
| meerkatAggregator.resources.meerkatAggregator.requests.cpu | int | `1` |  |
| meerkatAggregator.resources.meerkatAggregator.requests.memory | string | `"1Gi"` |  |
| meerkatAggregator.resources.meerkatAggregatorWorker.limits.cpu | int | `4` |  |
| meerkatAggregator.resources.meerkatAggregatorWorker.limits.memory | string | `"4Gi"` |  |
| meerkatAggregator.resources.meerkatAggregatorWorker.requests.cpu | int | `1` |  |
| meerkatAggregator.resources.meerkatAggregatorWorker.requests.memory | string | `"1Gi"` |  |
| meerkatAggregator.resources.nodeLabelsToFiles.limits.cpu | string | `"50m"` |  |
| meerkatAggregator.resources.nodeLabelsToFiles.limits.memory | string | `"64Mi"` |  |
| meerkatAggregator.resources.nodeLabelsToFiles.requests.cpu | string | `"50m"` |  |
| meerkatAggregator.resources.nodeLabelsToFiles.requests.memory | string | `"64Mi"` |  |
| meerkatAggregator.worker.cardinalityCountingEnabled | bool | `false` |  |
| meerkatAggregator.worker.hpa.enabled | bool | `false` |  |
| meerkatAggregator.workerReplicaCount | int | `1` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# meerkat-api

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig Meerkat API

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.meerkatApi.serviceToken | string | `nil` |  |
| global.apps | string | `"monitor"` |  |
| global.beacon.enabled | bool | `false` |  |
| global.beacon.platformMetricsEnabled | bool | `false` |  |
| global.beacon.promEnabled | bool | `false` |  |
| global.beacon.prwsInternalIngestionEnabled | bool | `false` |  |
| global.cassandra.datacenterName | string | `"DC1"` |  |
| global.cassandra.endpoint | string | `"sysdigcloud-cassandra"` |  |
| global.cassandra.port | int | `9042` |  |
| global.cassandra.replicaCount | int | `3` |  |
| global.cassandra.replicationStrategy | string | `"SimpleStrategy"` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.cassandra.sslVerify | bool | `false` |  |
| global.cassandra.useCertManager | bool | `false` |  |
| global.cassandra.workloadName | string | `"cassandra"` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","hostname":"sysdigcloud-elasticsearch","port":9200,"scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.grpc.auth.enabled | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.common.tls | bool | `true` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `true` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.meerkat.collectorDeployments | int | `1` |  |
| global.meerkat.enabled | bool | `true` |  |
| global.meerkat.objectStorage.accessKey | string | `""` |  |
| global.meerkat.objectStorage.endpoint | string | `""` |  |
| global.meerkat.objectStorage.region | string | `"us-east-1"` |  |
| global.meerkat.objectStorage.secretKey | string | `""` |  |
| global.meerkat.queryThrottling.enabled | bool | `false` |  |
| global.meerkat.store.storageSource.primaryWriteSource | string | `"CASSANDRA"` |  |
| global.meerkat.store.storageSource.readSource | string | `"CASSANDRA"` |  |
| global.meerkat.store.storageSource.writeSource[0] | string | `"CASSANDRA"` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.tlsencryption.adminUser.password | string | `"changeme"` |  |
| meerkatApi.authorizationService.enabled | bool | `false` |  |
| meerkatApi.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| meerkatApi.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| meerkatApi.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| meerkatApi.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| meerkatApi.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| meerkatApi.jvmOptions | string | `"-Dlogging.level.org.springframework.transaction.interceptor=TRACE -Dio.netty.leakDetection.level=advanced -Dlogging.level.com.sysdig.meerkat.api.server.adapter.TimeSeriesGAdapter=DEBUG -Dlogging.level.com.sysdig.meerkat.api.server.service.realtime.RealTimeQueryServiceImpl=DEBUG -Dlogging.level.com.sysdig.meerkat.api.server.service.realtime.MeerkatClientDNSGrpcResolver=DEBUG -Dsysdig.meerkat.cassandra.features.queryAllMetricDescriptorsEnabled=true"` |  |
| meerkatApi.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| meerkatApi.replicaCount | int | `1` |  |
| meerkatApi.repositoryPrefix | string | `"monitor"` |  |
| meerkatApi.resources.meerkatApi.limits.cpu | int | `4` |  |
| meerkatApi.resources.meerkatApi.limits.memory | string | `"4Gi"` |  |
| meerkatApi.resources.meerkatApi.requests.cpu | int | `1` |  |
| meerkatApi.resources.meerkatApi.requests.memory | string | `"1Gi"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# meerkat-collector

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig Meerkat Collector

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor"` |  |
| global.beacon.enabled | bool | `false` |  |
| global.beacon.platformMetricsEnabled | bool | `false` |  |
| global.beacon.promEnabled | bool | `false` |  |
| global.beacon.prwsInternalIngestionEnabled | bool | `false` |  |
| global.cassandra.datacenterName | string | `"DC1"` |  |
| global.cassandra.endpoint | string | `"sysdigcloud-cassandra"` |  |
| global.cassandra.port | int | `9042` |  |
| global.cassandra.replicaCount | int | `3` |  |
| global.cassandra.replicationStrategy | string | `"SimpleStrategy"` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.cassandra.sslVerify | bool | `false` |  |
| global.cassandra.useCertManager | bool | `false` |  |
| global.cassandra.workloadName | string | `"cassandra"` |  |
| global.certificate.customCerts | list | `[]` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","hostname":"sysdigcloud-elasticsearch","scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.grpc.auth.enabled | bool | `false` |  |
| global.kafka.broker.externalPort | int | `9093` |  |
| global.kafka.name | string | `"cp-kafka"` |  |
| global.kafka.namespace | string | `"sysdigcloud"` |  |
| global.kafka.secure.enabled | bool | `false` |  |
| global.kafka.secure.useCertManager | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.common.tls | bool | `true` |  |
| global.legacyRedis.redisClientsMonitor.metering.tls | bool | `true` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `true` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.meerkat.collector.deploymentStrategy.rollingUpdate.maxSurge | int | `0` |  |
| global.meerkat.collector.deploymentStrategy.rollingUpdate.maxUnavailable | string | `"25%"` |  |
| global.meerkat.collector.deploymentStrategy.type | string | `"Recreate"` |  |
| global.meerkat.collectorDeployments | int | `2` |  |
| global.meerkat.collectorProgressDeadline | int | `3600` |  |
| global.meerkat.enabled | bool | `true` |  |
| global.meerkat.objectStorage.accessKey | string | `""` |  |
| global.meerkat.objectStorage.endpoint | string | `""` |  |
| global.meerkat.objectStorage.region | string | `"us-east-1"` |  |
| global.meerkat.objectStorage.secretKey | string | `""` |  |
| global.meerkat.store.storageSource.primaryWriteSource | string | `"CASSANDRA"` |  |
| global.meerkat.store.storageSource.readSource | string | `"CASSANDRA"` |  |
| global.meerkat.store.storageSource.writeSource[0] | string | `"CASSANDRA"` |  |
| global.meerkat.store.useCassandraGPartTablePerSampling | bool | `true` |  |
| global.monitorRepositoryPrefix | string | `"monitor"` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.nodeLabelsVersion | string | `"1.0.74"` |  |
| global.tlsencryption.adminUser.password | string | `"changeme"` |  |
| meerkatCollector.CollectorDeploymentIndex | int | `0` |  |
| meerkatCollector.authorizationService.enabled | bool | `false` |  |
| meerkatCollector.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| meerkatCollector.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| meerkatCollector.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| meerkatCollector.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| meerkatCollector.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| meerkatCollector.jvmOptions | string | `"-Dsysdig.cassandra.auto-schema=true -Dlogging.level.org.springframework.transaction.interceptor=TRACE -Dio.netty.leakDetection.level=advanced -Dlogging.level.com.sysdig.meerkat.collector.kafka.epochstate.ShardEpochState=DEBUG -Dlogging.level.com.sysdig.meerkat.collector.service.GPartBuilderImpl=DEBUG -Dlogging.level.com.sysdig.meerkat.collector.service.MeerkatIndexer=DEBUG -Dlogging.level.com.sysdig.meerkat.collector.kafka.MeerkatWorker=DEBUG -Dlogging.level.com.sysdig.meerkat.collector.grpc.GPartsQueryServiceGrpcImpl=DEBUG"` |  |
| meerkatCollector.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| meerkatCollector.replicaCount | int | `1` |  |
| meerkatCollector.resources.meerkatCollector.limits.cpu | int | `4` |  |
| meerkatCollector.resources.meerkatCollector.limits.memory | string | `"4Gi"` |  |
| meerkatCollector.resources.meerkatCollector.requests.cpu | int | `1` |  |
| meerkatCollector.resources.meerkatCollector.requests.memory | string | `"1Gi"` |  |
| meerkatCollector.resources.nodeLabelsToFiles.limits.cpu | string | `"50m"` |  |
| meerkatCollector.resources.nodeLabelsToFiles.limits.memory | string | `"64Mi"` |  |
| meerkatCollector.resources.nodeLabelsToFiles.requests.cpu | string | `"50m"` |  |
| meerkatCollector.resources.nodeLabelsToFiles.requests.memory | string | `"64Mi"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# meerkat-datastream

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig Meerkat Datastream

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor"` |  |
| global.cassandra.datacenterName | string | `"DC1"` |  |
| global.cassandra.endpoint | string | `"sysdigcloud-cassandra"` |  |
| global.cassandra.port | int | `9042` |  |
| global.cassandra.replicaCount | int | `3` |  |
| global.cassandra.replicationStrategy | string | `"SimpleStrategy"` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.cassandra.sslVerify | bool | `false` |  |
| global.cassandra.useCertManager | bool | `false` |  |
| global.cassandra.workloadName | string | `"cassandra"` |  |
| global.certificate.customCA | string | `""` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.kafka.broker.externalPort | int | `9093` |  |
| global.kafka.name | string | `"cp-kafka"` |  |
| global.kafka.namespace | string | `"sysdigcloud"` |  |
| global.kafka.secure.enabled | bool | `false` |  |
| global.kafka.secure.useCertManager | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.common.tls | bool | `true` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `true` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.meerkat.datastreamEnabled | bool | `true` |  |
| global.meerkat.enabled | bool | `true` |  |
| global.monitorRepositoryPrefix | string | `"monitor"` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.nodeLabelsVersion | string | `"1.0.74"` |  |
| global.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| meerkatDatastream.authorizationService.enabled | bool | `false` |  |
| meerkatDatastream.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| meerkatDatastream.hpa.enabled | bool | `false` |  |
| meerkatDatastream.jvmOptions | string | `"-Xms1g -Xmx1g"` |  |
| meerkatDatastream.nodeSelector | object | `{}` |  |
| meerkatDatastream.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| meerkatDatastream.replicaCount | int | `1` |  |
| meerkatDatastream.resources.meerkatDatastream.limits.cpu | int | `4` |  |
| meerkatDatastream.resources.meerkatDatastream.limits.memory | string | `"4Gi"` |  |
| meerkatDatastream.resources.meerkatDatastream.requests.cpu | int | `1` |  |
| meerkatDatastream.resources.meerkatDatastream.requests.memory | string | `"1Gi"` |  |
| meerkatDatastream.serviceAccount.annotations | object | `{}` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# metadata-enricher

![Version: 0.2.0-260303084344-main-v0665ae2](https://img.shields.io/badge/Version-0.2.0--260303084344--main--v0665ae2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Metadata Enricher Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.metadataEnricher.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.kafka.broker.externalPort | int | `9092` |  |
| global.kafka.name | string | `"cp-kafka"` |  |
| global.kafka.namespace | string | `"sysdigcloud"` |  |
| global.kafka.secure.enabled | bool | `false` |  |
| global.kafka.secure.useCertManager | bool | `false` |  |
| global.legacyRedis.redisClientsSecure.metadataEnricher.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.secure.policies.endpoint | string | `"sysdigcloud-policies-api:9199"` |  |
| metadataEnricher.consumers.activityAudit.ackWait | string | `"30s"` |  |
| metadataEnricher.consumers.activityAudit.disabled | bool | `false` |  |
| metadataEnricher.consumers.activityAudit.maxInFlight | string | `"10000"` |  |
| metadataEnricher.consumers.dispatcher.ackWait | string | `"30s"` |  |
| metadataEnricher.consumers.dispatcher.disabled | bool | `false` |  |
| metadataEnricher.consumers.dispatcher.maxInFlight | string | `"10000"` |  |
| metadataEnricher.consumers.fingerprints.ackWait | string | `"30s"` |  |
| metadataEnricher.consumers.fingerprints.disabled | bool | `false` |  |
| metadataEnricher.consumers.fingerprints.maxInFlight | string | `"10000"` |  |
| metadataEnricher.consumers.policyEvents.ackWait | string | `"30s"` |  |
| metadataEnricher.consumers.policyEvents.disabled | bool | `false` |  |
| metadataEnricher.consumers.policyEvents.maxInFlight | string | `"10000"` |  |
| metadataEnricher.consumers.retry.ackWait | string | `"30s"` |  |
| metadataEnricher.consumers.retry.maxInFlight | string | `"10000"` |  |
| metadataEnricher.enabled | bool | `true` |  |
| metadataEnricher.forceMigrations | bool | `false` |  |
| metadataEnricher.kafka.asyncRoutines | int | `0` |  |
| metadataEnricher.kafka.azAwareness | bool | `false` |  |
| metadataEnricher.kafka.enabled | bool | `true` |  |
| metadataEnricher.kafka.partitionLevelMetricsEnabled | bool | `true` |  |
| metadataEnricher.kafka.timeoutRetryMaxWait | string | `"30s"` |  |
| metadataEnricher.kafka.timeoutRetryMinWait | string | `"1s"` |  |
| metadataEnricher.mdsEndpoint | string | `"sysdigcloud-metadata-service-server:5300"` |  |
| metadataEnricher.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| metadataEnricher.replicaCount | int | `1` |  |
| metadataEnricher.repositoryPrefix | string | `"secure"` |  |
| metadataEnricher.resources.metadataEnricher.limits.cpu | int | `1` |  |
| metadataEnricher.resources.metadataEnricher.limits.memory | string | `"2Gi"` |  |
| metadataEnricher.resources.metadataEnricher.requests.cpu | int | `1` |  |
| metadataEnricher.resources.metadataEnricher.requests.memory | string | `"2Gi"` |  |
| metadataEnricher.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| metadataEnricher.scaler.clusterName | string | `"provider-env-region-DD"` |  |
| metadataEnricher.scaler.enabled | bool | `true` |  |
| metadataEnricher.scaler.maxReplicaCount | int | `10` |  |
| metadataEnricher.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| metadataEnricher.scaler.thresholds.activityAuditBacklog | int | `7000` |  |
| metadataEnricher.scaler.thresholds.dispatcherBacklog | int | `7000` |  |
| metadataEnricher.scaler.thresholds.fingerprintsBacklog | int | `2500` |  |
| metadataEnricher.scaler.thresholds.kafkaActivityAuditBacklog | int | `7000` |  |
| metadataEnricher.scaler.thresholds.kafkaFingerprintsBacklog | int | `2500` |  |
| metadataEnricher.scaler.thresholds.kafkaPolicyBacklog | int | `7000` |  |
| metadataEnricher.scaler.thresholds.kafkaRetryBacklog | int | `5000` |  |
| metadataEnricher.scaler.thresholds.memoryUsage | int | `90` |  |
| metadataEnricher.scaler.thresholds.policyBacklog | int | `7000` |  |
| metadataEnricher.streams.metadata-enricher-activity-audit-1.max_age | int | `86400000000000` |  |
| metadataEnricher.streams.metadata-enricher-activity-audit-1.max_bytes | int | `12884901888` |  |
| metadataEnricher.streams.metadata-enricher-activity-audit-1.metadata.version | string | `"4"` |  |
| metadataEnricher.streams.metadata-enricher-activity-audit-1.name | string | `"metadata-enricher-activity-audit-1"` |  |
| metadataEnricher.streams.metadata-enricher-activity-audit-1.num_replicas | int | `3` |  |
| metadataEnricher.streams.metadata-enricher-activity-audit-1.storage | string | `"file"` |  |
| metadataEnricher.streams.metadata-enricher-activity-audit-1.subjects[0] | string | `"metadataenricher.activityaudit.1.>"` |  |
| metadataEnricher.streams.metadata-enricher-dlq.max_age | int | `172800000000000` |  |
| metadataEnricher.streams.metadata-enricher-dlq.max_bytes | int | `4294967296` |  |
| metadataEnricher.streams.metadata-enricher-dlq.metadata.version | string | `"4"` |  |
| metadataEnricher.streams.metadata-enricher-dlq.name | string | `"metadata-enricher-dlq"` |  |
| metadataEnricher.streams.metadata-enricher-dlq.num_replicas | int | `3` |  |
| metadataEnricher.streams.metadata-enricher-dlq.storage | string | `"file"` |  |
| metadataEnricher.streams.metadata-enricher-dlq.subjects[0] | string | `"metadataenricher.dlq.>"` |  |
| metadataEnricher.streams.metadata-enricher-fingerprints-1.max_age | int | `86400000000000` |  |
| metadataEnricher.streams.metadata-enricher-fingerprints-1.max_bytes | int | `12884901888` |  |
| metadataEnricher.streams.metadata-enricher-fingerprints-1.metadata.version | string | `"4"` |  |
| metadataEnricher.streams.metadata-enricher-fingerprints-1.name | string | `"metadata-enricher-fingerprints-1"` |  |
| metadataEnricher.streams.metadata-enricher-fingerprints-1.num_replicas | int | `3` |  |
| metadataEnricher.streams.metadata-enricher-fingerprints-1.storage | string | `"file"` |  |
| metadataEnricher.streams.metadata-enricher-fingerprints-1.subjects[0] | string | `"metadataenricher.fingerprints.1.>"` |  |
| metadataEnricher.streams.metadata-enricher-policy-custom-events-1.max_age | int | `86400000000000` |  |
| metadataEnricher.streams.metadata-enricher-policy-custom-events-1.max_bytes | int | `8589934592` |  |
| metadataEnricher.streams.metadata-enricher-policy-custom-events-1.metadata.version | string | `"4"` |  |
| metadataEnricher.streams.metadata-enricher-policy-custom-events-1.name | string | `"metadata-enricher-policy-custom-events-1"` |  |
| metadataEnricher.streams.metadata-enricher-policy-custom-events-1.num_replicas | int | `3` |  |
| metadataEnricher.streams.metadata-enricher-policy-custom-events-1.storage | string | `"file"` |  |
| metadataEnricher.streams.metadata-enricher-policy-custom-events-1.subjects[0] | string | `"metadataenricher.policy.custom.1.>"` |  |
| metadataEnricher.streams.metadata-enricher-policy-managed-events-1.max_age | int | `86400000000000` |  |
| metadataEnricher.streams.metadata-enricher-policy-managed-events-1.max_bytes | int | `8589934592` |  |
| metadataEnricher.streams.metadata-enricher-policy-managed-events-1.metadata.version | string | `"4"` |  |
| metadataEnricher.streams.metadata-enricher-policy-managed-events-1.name | string | `"metadata-enricher-policy-managed-events-1"` |  |
| metadataEnricher.streams.metadata-enricher-policy-managed-events-1.num_replicas | int | `3` |  |
| metadataEnricher.streams.metadata-enricher-policy-managed-events-1.storage | string | `"file"` |  |
| metadataEnricher.streams.metadata-enricher-policy-managed-events-1.subjects[0] | string | `"metadataenricher.policy.managed.1.>"` |  |
| metadataEnricher.streams.metadata-enricher-policy-preview-events-1.max_age | int | `14400000000000` |  |
| metadataEnricher.streams.metadata-enricher-policy-preview-events-1.max_bytes | int | `1073741824` |  |
| metadataEnricher.streams.metadata-enricher-policy-preview-events-1.metadata.version | string | `"1"` |  |
| metadataEnricher.streams.metadata-enricher-policy-preview-events-1.name | string | `"metadata-enricher-policy-preview-events-1"` |  |
| metadataEnricher.streams.metadata-enricher-policy-preview-events-1.num_replicas | int | `1` |  |
| metadataEnricher.streams.metadata-enricher-policy-preview-events-1.storage | string | `"file"` |  |
| metadataEnricher.streams.metadata-enricher-policy-preview-events-1.subjects[0] | string | `"metadataenricher.policy.preview.1.>"` |  |
| metadataEnricher.streams.metadata-enricher-retry-1.max_age | int | `86400000000000` |  |
| metadataEnricher.streams.metadata-enricher-retry-1.max_bytes | int | `4294967296` |  |
| metadataEnricher.streams.metadata-enricher-retry-1.metadata.version | string | `"4"` |  |
| metadataEnricher.streams.metadata-enricher-retry-1.name | string | `"metadata-enricher-retry-1"` |  |
| metadataEnricher.streams.metadata-enricher-retry-1.num_replicas | int | `3` |  |
| metadataEnricher.streams.metadata-enricher-retry-1.storage | string | `"file"` |  |
| metadataEnricher.streams.metadata-enricher-retry-1.subjects[0] | string | `"metadataenricher.retry.1.>"` |  |
| metadataEnricher.streams.metadata-enricher-retry-2.max_age | int | `86400000000000` |  |
| metadataEnricher.streams.metadata-enricher-retry-2.max_bytes | int | `4294967296` |  |
| metadataEnricher.streams.metadata-enricher-retry-2.metadata.version | string | `"4"` |  |
| metadataEnricher.streams.metadata-enricher-retry-2.name | string | `"metadata-enricher-retry-2"` |  |
| metadataEnricher.streams.metadata-enricher-retry-2.num_replicas | int | `3` |  |
| metadataEnricher.streams.metadata-enricher-retry-2.storage | string | `"file"` |  |
| metadataEnricher.streams.metadata-enricher-retry-2.subjects[0] | string | `"metadataenricher.retry.2.>"` |  |
| metadataEnricher.streams.metadata-enricher-retry-3.max_age | int | `86400000000000` |  |
| metadataEnricher.streams.metadata-enricher-retry-3.max_bytes | int | `4294967296` |  |
| metadataEnricher.streams.metadata-enricher-retry-3.metadata.version | string | `"4"` |  |
| metadataEnricher.streams.metadata-enricher-retry-3.name | string | `"metadata-enricher-retry-3"` |  |
| metadataEnricher.streams.metadata-enricher-retry-3.num_replicas | int | `3` |  |
| metadataEnricher.streams.metadata-enricher-retry-3.storage | string | `"file"` |  |
| metadataEnricher.streams.metadata-enricher-retry-3.subjects[0] | string | `"metadataenricher.retry.3.>"` |  |
| metadataEnricher.vm.consumers.collector.ackWait | string | `"30s"` |  |
| metadataEnricher.vm.consumers.collector.disabled | bool | `false` |  |
| metadataEnricher.vm.consumers.collector.maxInFlight | int | `10000` |  |
| metadataEnricher.vm.consumers.retry.ackWait | string | `"30s"` |  |
| metadataEnricher.vm.consumers.retry.maxInFlight | int | `10000` |  |
| metadataEnricher.vm.enabled | bool | `true` |  |
| metadataEnricher.vm.forceMigrations | bool | `false` |  |
| metadataEnricher.vm.loggingLevel | string | `"INFO"` |  |
| metadataEnricher.vm.mdsEndpoint | string | `"sysdigcloud-metadata-service-server:5300"` |  |
| metadataEnricher.vm.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| metadataEnricher.vm.replicaCount | int | `1` |  |
| metadataEnricher.vm.repositoryPrefix | string | `"secure"` |  |
| metadataEnricher.vm.resources.metadataEnricherVm.limits.cpu | int | `1` |  |
| metadataEnricher.vm.resources.metadataEnricherVm.limits.memory | string | `"2Gi"` |  |
| metadataEnricher.vm.resources.metadataEnricherVm.requests.cpu | int | `1` |  |
| metadataEnricher.vm.resources.metadataEnricherVm.requests.memory | string | `"2Gi"` |  |
| metadataEnricher.vm.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| metadataEnricher.vm.scaler.clusterName | string | `"provider-env-region-DD"` |  |
| metadataEnricher.vm.scaler.enabled | bool | `true` |  |
| metadataEnricher.vm.scaler.maxReplicaCount | int | `10` |  |
| metadataEnricher.vm.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| metadataEnricher.vm.scaler.thresholds.memoryUsage | int | `90` |  |
| metadataEnricher.vm.scaler.thresholds.messagesInQueueThreshold | int | `10000` |  |
| metadataEnricher.vm.sparkBatching | bool | `true` |  |
| metadataEnricher.vm.streams.vm-metadata-enricher-retry-1.max_age | int | `86400000000000` |  |
| metadataEnricher.vm.streams.vm-metadata-enricher-retry-1.max_bytes | int | `4294967296` |  |
| metadataEnricher.vm.streams.vm-metadata-enricher-retry-1.metadata.version | string | `"1"` |  |
| metadataEnricher.vm.streams.vm-metadata-enricher-retry-1.name | string | `"vm-metadata-enricher-retry-1"` |  |
| metadataEnricher.vm.streams.vm-metadata-enricher-retry-1.num_replicas | int | `3` |  |
| metadataEnricher.vm.streams.vm-metadata-enricher-retry-1.storage | string | `"file"` |  |
| metadataEnricher.vm.streams.vm-metadata-enricher-retry-1.subjects[0] | string | `"vm.metadataenricher.retry.1.>"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# metadata-service

![Version: 2.2.0-260306120218-main-v0a2a54d](https://img.shields.io/badge/Version-2.2.0--260306120218--main--v0a2a54d-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Metadata Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| azureMetricsConverter.cloudauth.token | string | `nil` |  |
| global.api.serviceTokens.metadataService.serviceToken | string | `"qwerty"` |  |
| global.apps | string | `"monitor"` |  |
| global.clusterDomain | string | `"cluster.local"` |  |
| global.graphServicesEnabled | bool | `false` |  |
| global.kafka.broker.externalPort | int | `9092` |  |
| global.kafka.name | string | `"cp-kafka"` |  |
| global.kafka.namespace | string | `"sysdigcloud"` |  |
| global.kafka.secure.enabled | bool | `false` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.scanningv2Scanresults.nats.js.streamName | string | `"secure-vm-scanner-scan-response"` |  |
| global.scanningv2Scanresults.nats.js.subjectFilter | string | `"secure.vm.scanner.scan.response.*.*.success"` |  |
| global.scanningv2Scanresults.nats.js.tlsEnabled | bool | `true` |  |
| global.scanningv2Scanresults.nats.js.url | string | `"nats"` |  |
| global.secure.cloudauth.enabled | bool | `true` |  |
| global.secure.cloudauth.tls.enabled | bool | `false` |  |
| metadataService.awsEnabled | bool | `true` |  |
| metadataService.awsKafkaConsumerThreads | int | `1` |  |
| metadataService.captureRawData | bool | `false` |  |
| metadataService.cloudDataCacheEnabled | bool | `true` |  |
| metadataService.cloudauth.maxReceiveSizeBytes | string | `"8388608"` |  |
| metadataService.enableEntitiesInBatch | bool | `false` |  |
| metadataService.enableIpIndex | bool | `false` |  |
| metadataService.enableNetworkPolicy | bool | `false` |  |
| metadataService.enableNodesInBatch | bool | `false` |  |
| metadataService.enabled | bool | `true` |  |
| metadataService.enabledNodeUpdates | bool | `false` |  |
| metadataService.heartbeatDelayThresholdSec | int | `30` |  |
| metadataService.inventoryBatchSize | int | `100` |  |
| metadataService.inventoryConsumers | int | `3` |  |
| metadataService.inventoryDeleteSubject | string | `"graph.ingestionLimits.delete"` |  |
| metadataService.inventoryDeleteSubjectLegacy | string | `"graph.ingestion.delete.metadata.service"` |  |
| metadataService.inventoryEnabled | bool | `false` |  |
| metadataService.inventoryStaleDeleteSubject | string | `"graph.ingestion.staledata.deleted"` |  |
| metadataService.inventoryStreamName | string | `"graph-ingestionLimits"` |  |
| metadataService.inventoryStreamNameLegacy | string | `"graph-ingestion"` |  |
| metadataService.inventorySubject | string | `"graph.ingestionLimits.resources"` |  |
| metadataService.jobAgentlessCleanCron | string | `"@every 2h"` |  |
| metadataService.jobCleanCron | string | `"@every 1h"` |  |
| metadataService.jobCleanThreshold | int | `3600` |  |
| metadataService.jobDNSUpdate | string | `"@every 30s"` |  |
| metadataService.jobInventoryCleanCron | string | `"@every 6h"` |  |
| metadataService.kafkaAdditionalConfigs.aws | string | `""` |  |
| metadataService.kafkaAdditionalConfigs.metrics | string | `""` |  |
| metadataService.kafkaAdditionalConfigs.secure | string | `""` |  |
| metadataService.kafkaConsumerThreads | int | `8` |  |
| metadataService.kafkaMessageTimeoutMs | string | `"60000"` |  |
| metadataService.kafkaNodeAzAwareness | bool | `false` |  |
| metadataService.mdsCollectorReplicaCount | int | `2` |  |
| metadataService.mdsDeploymentReplicaCount | int | `2` |  |
| metadataService.mdsOperatorReplicaCount | int | `1` |  |
| metadataService.mdsOperatorVersion | string | `"1.5.105-vc32e84e"` |  |
| metadataService.operatorEnabled | bool | `true` |  |
| metadataService.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| metadataService.remotebody.pullerBackends | string | `"s3"` |  |
| metadataService.remotebody.s3.accessKeyId | string | `""` |  |
| metadataService.remotebody.s3.bucket | string | `""` |  |
| metadataService.remotebody.s3.cloudProvider | string | `""` |  |
| metadataService.remotebody.s3.endpoint | string | `""` |  |
| metadataService.remotebody.s3.region | string | `""` |  |
| metadataService.replicaCount | int | `2` |  |
| metadataService.repositoryPrefix | string | `"monitor"` |  |
| metadataService.resources.metadataService.limits.cpu | int | `2` |  |
| metadataService.resources.metadataService.limits.memory | string | `"2Gi"` |  |
| metadataService.resources.metadataService.requests.cpu | int | `1` |  |
| metadataService.resources.metadataService.requests.memory | string | `"1Gi"` |  |
| metadataService.resources.metadataServiceCollector.limits.cpu | int | `2` |  |
| metadataService.resources.metadataServiceCollector.limits.memory | string | `"1Gi"` |  |
| metadataService.resources.metadataServiceCollector.requests.cpu | int | `1` |  |
| metadataService.resources.metadataServiceCollector.requests.memory | string | `"500Mi"` |  |
| metadataService.secureCleanupCron | string | `"@every 6h"` |  |
| metadataService.secureCleanupEnabled | bool | `true` |  |
| metadataService.secureKafkaConsumerThreads | int | `2` |  |
| metadataService.shardsPerResourceTypeMap | int | `6` |  |
| metadataService.useManagedCertificate | bool | `false` |  |
| metadataService.vmBatchSize | int | `40` |  |
| metadataService.vmConsumerName | string | `"mds-collector-vm"` |  |
| metadataService.vmConsumers | int | `2` |  |
| metadataService.vmEnabled | bool | `true` |  |
| metadataService.vmIgnorePackageInfo | bool | `true` |  |
| metadataService.vmLifecycleConsumerName | string | `"mds-collector-vm"` |  |
| metadataService.vmLifecycleConsumers | int | `2` |  |
| metadataService.vmLifecycleEnabled | bool | `true` |  |
| secureGraphIngestion.remotebody.s3.secretAccessKey | string | `""` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# nats

![Version: 0.1.68](https://img.shields.io/badge/Version-0.1.68-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2.11.4](https://img.shields.io/badge/AppVersion-2.11.4-informational?style=flat-square)

A Helm chart for Nats, the Sysdig way

**Homepage:** <https://github.com/draios/datastore-nats-js>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| devops-team | <devops@sysdig.com> |  |

## Source Code

* <https://github.com/draios/datastore-nats-js>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
|  | nats(nats) | 0.18.2 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.airgappedRegistryName | string | `"quay.io"` |  |
| global.airgappedRepositoryPrefix | string | `"sysdig"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.enableNetworkPolicy | bool | `false` |  |
| global.nats.certManager.certs[0].additionalSubjectAltNames.dns | list | `[]` |  |
| global.nats.certManager.certs[0].additionalSubjectAltNames.uris | list | `[]` |  |
| global.nats.certManager.certs[0].name | string | `"client-tls"` |  |
| global.nats.certManager.certs[1].additionalSubjectAltNames.dns | list | `[]` |  |
| global.nats.certManager.certs[1].additionalSubjectAltNames.uris | list | `[]` |  |
| global.nats.certManager.certs[1].name | string | `"server-tls"` |  |
| global.nats.certManager.enabled | bool | `true` |  |
| global.natsBoxVersion | string | `"0.17.0-0.0.46"` |  |
| global.natsExporterVersion | string | `"0.17.2-0.1.33"` |  |
| global.natsReloaderVersion | string | `"0.14.3-0.1.34"` |  |
| global.natsServerVersion | string | `"2.10.14-0.1.37"` |  |
| global.storageClassName | string | `"sysdig"` |  |
| nats.auth.enabled | bool | `false` |  |
| nats.auth.systemAccount | string | `"SYS"` |  |
| nats.bootconfig.securityContext.allowPrivilegeEscalation | bool | `false` |  |
| nats.bootconfig.securityContext.capabilities.drop[0] | string | `"ALL"` |  |
| nats.bootconfig.securityContext.readOnlyRootFilesystem | bool | `true` |  |
| nats.cluster.enabled | bool | `true` |  |
| nats.cluster.name | string | `"nats"` |  |
| nats.cluster.replicas | int | `3` |  |
| nats.cluster.tls.ca | string | `"ca.crt"` |  |
| nats.cluster.tls.cert | string | `"tls.crt"` |  |
| nats.cluster.tls.key | string | `"tls.key"` |  |
| nats.cluster.tls.secret.name | string | `"server-tls"` |  |
| nats.cluster.tls.timeout | int | `5` |  |
| nats.commonLabels.app | string | `"sysdigcloud"` |  |
| nats.commonLabels.owners | string | `"infra"` |  |
| nats.commonLabels.productCategory | string | `"cdr_cspm_cwpp"` |  |
| nats.commonLabels.role | string | `"nats-cluster"` |  |
| nats.exporter.enabled | bool | `true` |  |
| nats.exporter.image | string | `"natsio/prometheus-nats-exporter:latest"` |  |
| nats.exporter.pullPolicy | string | `"IfNotPresent"` |  |
| nats.exporter.resources.limits.cpu | string | `"200m"` |  |
| nats.exporter.resources.limits.memory | string | `"256Mi"` |  |
| nats.exporter.resources.requests.cpu | string | `"200m"` |  |
| nats.exporter.resources.requests.memory | string | `"256Mi"` |  |
| nats.exporter.securityContext.allowPrivilegeEscalation | bool | `false` |  |
| nats.exporter.securityContext.capabilities.drop[0] | string | `"ALL"` |  |
| nats.exporter.securityContext.readOnlyRootFilesystem | bool | `true` |  |
| nats.imagePullSecrets[0].name | string | `"sysdigcloud-pull-secret"` |  |
| nats.k8sClusterDomain | string | `"cluster.local"` |  |
| nats.multiCluster.enabled | bool | `false` |  |
| nats.multiCluster.onlyLocalRoutes | bool | `false` |  |
| nats.multiCluster.roles[0] | string | `"source"` |  |
| nats.multiCluster.setClusterAdvertise | bool | `false` |  |
| nats.multiCluster.side | string | `"source"` |  |
| nats.nats.automountServiceAccountToken | bool | `true` |  |
| nats.nats.connectRetries | int | `30` |  |
| nats.nats.gomemlimit | string | `"1600MiB"` |  |
| nats.nats.image | string | `"nats:2.9.0-alpine"` |  |
| nats.nats.jetstream.enabled | bool | `true` |  |
| nats.nats.jetstream.fileStorage.enabled | bool | `true` |  |
| nats.nats.jetstream.fileStorage.size | string | `"10Gi"` |  |
| nats.nats.jetstream.memStorage.enabled | bool | `false` |  |
| nats.nats.jetstream.memStorage.size | string | `"2Gi"` |  |
| nats.nats.limits.lameDuckDuration | string | `nil` |  |
| nats.nats.limits.maxConnections | string | `nil` |  |
| nats.nats.limits.maxControlLine | string | `nil` |  |
| nats.nats.limits.maxPayload | string | `"8MB"` |  |
| nats.nats.limits.maxPending | string | `nil` |  |
| nats.nats.limits.maxPings | string | `nil` |  |
| nats.nats.limits.maxSubscriptions | string | `nil` |  |
| nats.nats.limits.writeDeadline | string | `nil` |  |
| nats.nats.logging.authViolationErrorReports | bool | `false` |  |
| nats.nats.logging.connectErrorReports | bool | `false` |  |
| nats.nats.logging.debug | bool | `false` |  |
| nats.nats.logging.disconnectErrorReports | bool | `false` |  |
| nats.nats.logging.logtime | bool | `true` |  |
| nats.nats.logging.pedantic | bool | `false` |  |
| nats.nats.logging.reconnectErrorReports | bool | `false` |  |
| nats.nats.logging.slowConsumerErrorReports | bool | `false` |  |
| nats.nats.logging.staleConnectionErrorReports | bool | `false` |  |
| nats.nats.logging.tlsTimeout | string | `"60"` |  |
| nats.nats.logging.trace | bool | `false` |  |
| nats.nats.logging.verbose | bool | `false` |  |
| nats.nats.pingInterval | int | `2` |  |
| nats.nats.pullPolicy | string | `"IfNotPresent"` |  |
| nats.nats.resources.limits.cpu | string | `"1000m"` |  |
| nats.nats.resources.limits.memory | string | `"2Gi"` |  |
| nats.nats.resources.requests.cpu | string | `"1000m"` |  |
| nats.nats.resources.requests.memory | string | `"2Gi"` |  |
| nats.nats.securityContext.allowPrivilegeEscalation | bool | `false` |  |
| nats.nats.securityContext.capabilities.drop[0] | string | `"ALL"` |  |
| nats.nats.securityContext.readOnlyRootFilesystem | bool | `true` |  |
| nats.nats.securityContext.runAsGroup | int | `1000` |  |
| nats.nats.securityContext.runAsUser | int | `1000` |  |
| nats.nats.serviceAccount.create | bool | `true` |  |
| nats.nats.terminationGracePeriodSeconds | string | `"10"` |  |
| nats.nats.tls.ca | string | `"ca.crt"` |  |
| nats.nats.tls.cert | string | `"tls.crt"` |  |
| nats.nats.tls.key | string | `"tls.key"` |  |
| nats.nats.tls.secret.name | string | `"client-tls"` |  |
| nats.nats.tls.timeout | int | `60` |  |
| nats.natsbox.additionalLabels.owners | string | `"infra"` |  |
| nats.natsbox.additionalLabels.productCategory | string | `"infrastructure"` |  |
| nats.natsbox.enabled | bool | `false` |  |
| nats.natsbox.image | string | `"natsio/nats-box:latest"` |  |
| nats.natsbox.podLabels.owners | string | `"infra"` |  |
| nats.natsbox.podLabels.productCategory | string | `"infrastructure"` |  |
| nats.natsbox.securityContext.allowPrivilegeEscalation | bool | `false` |  |
| nats.natsbox.securityContext.capabilities.drop[0] | string | `"ALL"` |  |
| nats.natsbox.securityContext.readOnlyRootFilesystem | bool | `false` |  |
| nats.natsbox.securityContext.runAsGroup | int | `1000` |  |
| nats.natsbox.securityContext.runAsUser | int | `1000` |  |
| nats.reloader.enabled | bool | `true` |  |
| nats.reloader.image | string | `"natsio/nats-server-config-reloader:latest"` |  |
| nats.reloader.pullPolicy | string | `"IfNotPresent"` |  |
| nats.reloader.resources.limits.cpu | string | `"100m"` |  |
| nats.reloader.resources.limits.memory | string | `"128Mi"` |  |
| nats.reloader.resources.requests.cpu | string | `"100m"` |  |
| nats.reloader.resources.requests.memory | string | `"128Mi"` |  |
| nats.reloader.securityContext.allowPrivilegeEscalation | bool | `false` |  |
| nats.reloader.securityContext.capabilities.drop[0] | string | `"ALL"` |  |
| nats.reloader.securityContext.readOnlyRootFilesystem | bool | `true` |  |
| nats.securityContext.fsGroup | int | `1000` |  |
| nats.securityContext.runAsGroup | int | `1000` |  |
| nats.securityContext.runAsNonRoot | bool | `true` |  |
| nats.securityContext.runAsUser | int | `1000` |  |
| nats.securityContext.seccompProfile.type | string | `"RuntimeDefault"` |  |
| nats.statefulSetAnnotations."prometheus.io/port" | string | `"7777"` |  |
| nats.statefulSetAnnotations."prometheus.io/scrape" | string | `"true"` |  |
| nats.statefulSetPodLabels.app | string | `"sysdigcloud"` |  |
| nats.statefulSetPodLabels.owners | string | `"infra"` |  |
| nats.statefulSetPodLabels.productCategory | string | `"cdr_cspm_cwpp"` |  |
| nats.statefulSetPodLabels.role | string | `"nats-cluster"` |  |
| nats.updateStrategy.type | string | `"RollingUpdate"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# neo4j

![Version: 0.2.38](https://img.shields.io/badge/Version-0.2.38-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 2025.12.1-enterprise-ubi9](https://img.shields.io/badge/AppVersion-2025.12.1--enterprise--ubi9-informational?style=flat-square)

A Helm chart for Neo4j, the Sysdig way

**Homepage:** <https://github.com/draios/infra-datastore-neo4j>

## Maintainers

| Name | Email | Url |
| ---- | ------ | --- |
| devops-team | <devops@sysdig.com> |  |

## Source Code

* <https://github.com/draios/infra-datastore-neo4j>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
|  | neo4j(neo4j) | 5.19.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.airgappedRegistryName | string | `nil` |  |
| global.airgappedRepositoryPrefix | string | `nil` |  |
| global.neo4j.certManager.enabled | bool | `false` |  |
| global.neo4jDatabases.graphingestion | object | `{}` |  |
| global.neo4jDatabases.graphquery | object | `{}` |  |
| global.neo4jDatabases.risk | object | `{}` |  |
| global.neo4jDatabases.riskengine | object | `{}` |  |
| neo4j.additionalVolumeMounts | list | `[]` |  |
| neo4j.additionalVolumes | list | `[]` |  |
| neo4j.apoc_config."apoc.export.file.enabled" | string | `"true"` |  |
| neo4j.apoc_config."apoc.import.file.enabled" | string | `"true"` |  |
| neo4j.apoc_config."apoc.trigger.enabled" | string | `"true"` |  |
| neo4j.bloom.enabled | bool | `false` |  |
| neo4j.clusterDomain | string | `"cluster.local"` |  |
| neo4j.config."dbms.cluster.minimum_initial_system_primaries_count" | string | `"3"` |  |
| neo4j.config."dbms.security.procedures.allowlist" | string | `"apoc.*"` |  |
| neo4j.config."dbms.security.procedures.unrestricted" | string | `"apoc.*"` |  |
| neo4j.config."dbms.ssl.policy.backup.verify_hostname" | string | `"false"` |  |
| neo4j.config."dbms.ssl.policy.bolt.verify_hostname" | string | `"false"` |  |
| neo4j.config."dbms.ssl.policy.cluster.verify_hostname" | string | `"false"` |  |
| neo4j.config."dbms.ssl.policy.https.verify_hostname" | string | `"false"` |  |
| neo4j.config."initial.dbms.automatically_enable_free_servers" | string | `"true"` |  |
| neo4j.config."server.cluster.advertised_address" | string | `"$(bash -c 'echo ${POD_ADDRESS}')"` |  |
| neo4j.config."server.cluster.raft.advertised_address" | string | `"$(bash -c 'echo ${POD_ADDRESS}')"` |  |
| neo4j.config."server.config.strict_validation.enabled" | string | `"false"` |  |
| neo4j.config."server.directories.plugins" | string | `"/plugins/"` |  |
| neo4j.config."server.discovery.advertised_address" | string | `"$(bash -c 'echo ${POD_ADDRESS}')"` |  |
| neo4j.config."server.http.enabled" | string | `"false"` |  |
| neo4j.config."server.https.enabled" | string | `"true"` |  |
| neo4j.config."server.memory.heap.initial_size" | string | `"4g"` |  |
| neo4j.config."server.memory.heap.max_size" | string | `"4g"` |  |
| neo4j.config."server.memory.pagecache.size" | string | `"6g"` |  |
| neo4j.config."server.metrics.filter" | string | `"*bolt.connections*,*bolt.messages_received*,*bolt.messages_started*,*dbms.pool.bolt.free,*dbms.pool.bolt.total_size,*dbms.pool.bolt.total_used,*dbms.pool.bolt.used_heap,*cluster.raft.is_leader,*cluster.raft.last_leader_message,*cluster.raft.replication_attempt,*cluster.raft.replication_fail,*cluster.raft.last_applied,*cluster.raft.last_appended,*cluster.raft.append_index,*cluster.raft.commit_index,*cluster.raft.applied_index,*check_point.*,*cypher.replan_events,*cypher.cache*,*ids_in_use*,*.neo4j.count.*,*pool.transaction.*.total_used,*pool.transaction.*.used_heap,*pool.transaction.*.used_native,*store.size*,*transaction.active_read,*transaction.active_write,*transaction.committed*,*transaction.last_committed_tx_id,*transaction.peak_concurrent,*transaction.rollbacks*,*page_cache.hit*,*page_cache.page_faults,*page_cache.usage_ratio,*vm.file.descriptors.count,*vm.gc.time.*,*vm.heap.used,*vm.memory.buffer.direct.used,*vm.memory.pool.g1_eden_space,*vm.memory.pool.g1_old_gen,*vm.pause_time,*vm.thread*,*db.query.execution*,*protocol*,*db.state.count.*,*cluster.store_copy.*"` |  |
| neo4j.config."server.metrics.prometheus.enabled" | string | `"true"` |  |
| neo4j.config."server.metrics.prometheus.endpoint" | string | `"0.0.0.0:2004"` |  |
| neo4j.config."server.routing.advertised_address" | string | `"$(bash -c 'echo ${POD_ADDRESS}')"` |  |
| neo4j.containerSecurityContext.runAsGroup | int | `1000` |  |
| neo4j.containerSecurityContext.runAsNonRoot | bool | `true` |  |
| neo4j.containerSecurityContext.runAsUser | int | `1000` |  |
| neo4j.customCert.caCrt | string | `nil` |  |
| neo4j.customCert.enabled | bool | `false` |  |
| neo4j.customCert.tlsCrt | string | `nil` |  |
| neo4j.customCert.tlsKey | string | `nil` |  |
| neo4j.disableLookups | bool | `true` |  |
| neo4j.env.NEO4J_PLUGINS | string | `"[\"apoc\"]"` |  |
| neo4j.fips.enabled | bool | `false` |  |
| neo4j.fullnameOverride | string | `"neo4j"` |  |
| neo4j.hostPath.resources.limits.cpu | string | `"2"` |  |
| neo4j.hostPath.resources.limits.memory | string | `"2Gi"` |  |
| neo4j.hostPath.resources.requests.cpu | string | `"2"` |  |
| neo4j.hostPath.resources.requests.memory | string | `"2Gi"` |  |
| neo4j.image.imagePullPolicy | string | `"IfNotPresent"` |  |
| neo4j.image.imagePullSecrets[0] | string | `"sysdigcloud-pull-secret"` |  |
| neo4j.jvm.additionalJvmArguments | list | `[]` |  |
| neo4j.jvm.useNeo4jDefaultJvmArguments | bool | `true` |  |
| neo4j.livenessProbe.failureThreshold | int | `40` |  |
| neo4j.livenessProbe.periodSeconds | int | `30` |  |
| neo4j.livenessProbe.timeoutSeconds | int | `10` |  |
| neo4j.logInitialPassword | bool | `true` |  |
| neo4j.logging.serverLogsXml | string | `"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Example JSON logging configuration -->\n<Configuration status=\"ERROR\" monitorInterval=\"30\" packages=\"org.neo4j.logging.log4j\">\n    <Appenders>\n        <!-- Default debug.log, please keep -->\n        <RollingRandomAccessFile name=\"DebugLog\" fileName=\"${config:server.directories.logs}/debug.log\"\n                                 filePattern=\"$${config:server.directories.logs}/debug.log.%02i\">\n            <JsonTemplateLayout eventTemplateUri=\"classpath:org/neo4j/logging/StructuredLayoutWithMessage.json\"/>\n            <Policies>\n                <SizeBasedTriggeringPolicy size=\"80 MB\"/>\n            </Policies>\n            <DefaultRolloverStrategy fileIndex=\"min\" max=\"10\"/>\n        </RollingRandomAccessFile>\n\n        <RollingRandomAccessFile name=\"HttpLog\" fileName=\"${config:server.directories.logs}/http.log\"\n                                 filePattern=\"$${config:server.directories.logs}/http.log.%02i\">\n            <JsonTemplateLayout eventTemplateUri=\"classpath:org/neo4j/logging/StructuredLayoutWithMessage.json\"/>\n            <Policies>\n                <SizeBasedTriggeringPolicy size=\"20 MB\"/>\n            </Policies>\n            <DefaultRolloverStrategy fileIndex=\"min\" max=\"10\"/>\n        </RollingRandomAccessFile>\n\n        <RollingRandomAccessFile name=\"QueryLog\" fileName=\"${config:server.directories.logs}/query.log\"\n                                 filePattern=\"$${config:server.directories.logs}/query.log.%02i\">\n            <JsonTemplateLayout eventTemplateUri=\"classpath:org/neo4j/logging/QueryLogJsonLayout.json\"/>\n            <Policies>\n                <SizeBasedTriggeringPolicy size=\"100 MB\"/>\n            </Policies>\n            <DefaultRolloverStrategy fileIndex=\"min\" max=\"20\"/>\n        </RollingRandomAccessFile>\n\n        <RollingRandomAccessFile name=\"SecurityLog\" fileName=\"${config:server.directories.logs}/security.log\"\n                                 filePattern=\"$${config:server.directories.logs}/security.log.%02i\">\n            <JsonTemplateLayout eventTemplateUri=\"classpath:org/neo4j/logging/StructuredLayoutWithMessage.json\"/>\n            <Policies>\n                <SizeBasedTriggeringPolicy size=\"40 MB\"/>\n            </Policies>\n            <DefaultRolloverStrategy fileIndex=\"min\" max=\"10\"/>\n        </RollingRandomAccessFile>\n    </Appenders>\n\n    <Loggers>\n        <!-- Log levels. One of DEBUG, INFO, WARN, ERROR or OFF -->\n\n        <!-- The debug log is used as the root logger to catch everything -->\n        <Root level=\"INFO\">\n            <AppenderRef ref=\"DebugLog\"/> <!-- Keep this -->\n        </Root>\n        <!-- The query log, must be named \"QueryLogger\" -->\n        <Logger name=\"QueryLogger\" level=\"INFO\" additivity=\"false\">\n            <AppenderRef ref=\"QueryLog\"/>\n        </Logger>\n        <!-- The http request log, must be named \"HttpLogger\" -->\n        <Logger name=\"HttpLogger\" level=\"INFO\" additivity=\"false\">\n            <AppenderRef ref=\"HttpLog\"/>\n        </Logger>\n        <!-- The security log, must be named \"SecurityLogger\" -->\n        <Logger name=\"SecurityLogger\" level=\"INFO\" additivity=\"false\">\n            <AppenderRef ref=\"SecurityLog\"/>\n        </Logger>\n    </Loggers>\n</Configuration>"` |  |
| neo4j.logging.userLogsXml | string | `"<?xml version=\"1.0\" encoding=\"UTF-8\"?>\n<!-- Example JSON logging configuration -->\n<Configuration status=\"ERROR\" monitorInterval=\"30\" packages=\"org.neo4j.logging.log4j\">\n<Appenders>\n    <RollingRandomAccessFile name=\"Neo4jLog\" fileName=\"${config:server.directories.logs}/neo4j.log\"\n                             filePattern=\"$${config:server.directories.logs}/neo4j.log.%02i\">\n        <JsonTemplateLayout eventTemplateUri=\"classpath:org/neo4j/logging/StructuredLayoutWithMessage.json\"/>\n        <Policies>\n            <SizeBasedTriggeringPolicy size=\"100 MB\"/>\n        </Policies>\n        <DefaultRolloverStrategy fileIndex=\"min\" max=\"10\"/>\n    </RollingRandomAccessFile>\n    <!-- Only used by \"neo4j console\", will be ignored otherwise -->\n    <Console name=\"ConsoleAppender\" target=\"SYSTEM_OUT\">\n        <PatternLayout pattern=\"%d{yyyy-MM-dd HH:mm:ss.SSSZ}{GMT+0} %-5p %m%n\"/>\n    </Console>\n</Appenders>\n<Loggers>\n    <!-- Log level for the neo4j log. One of DEBUG, INFO, WARN, ERROR or OFF -->\n    <Root level=\"INFO\">\n        <AppenderRef ref=\"Neo4jLog\"/>\n        <AppenderRef ref=\"ConsoleAppender\"/>\n    </Root>\n</Loggers>\n</Configuration>"` |  |
| neo4j.multiCluster.enabled | bool | `false` |  |
| neo4j.multiCluster.roles[0] | string | `"source"` |  |
| neo4j.multiCluster.roles[1] | string | `"target"` |  |
| neo4j.multiCluster.side | string | `"source"` |  |
| neo4j.name | string | `"neo4j-cluster"` |  |
| neo4j.neo4j.acceptLicenseAgreement | string | `"yes"` |  |
| neo4j.neo4j.edition | string | `"enterprise"` |  |
| neo4j.neo4j.endpoint | string | `"neo4j-internals.sysdigcloud.svc.cluster.local"` |  |
| neo4j.neo4j.labels.productCategory | string | `"cdr_cspm_cwpp"` |  |
| neo4j.neo4j.minimumClusterSize | int | `3` |  |
| neo4j.neo4j.name | string | `"neo4j-cluster"` |  |
| neo4j.neo4j.offlineMaintenanceModeEnabled | bool | `false` |  |
| neo4j.neo4j.resources.cpu | string | `"2"` |  |
| neo4j.neo4j.resources.memory | string | `"15Gi"` |  |
| neo4j.neo4jServerVersion | string | `"2025.12.1-0.4.31"` |  |
| neo4j.nodeSelector | object | `{}` |  |
| neo4j.podDisruptionBudget.enabled | bool | `true` |  |
| neo4j.podDisruptionBudget.maxUnavailable | string | `"1"` |  |
| neo4j.podDisruptionBudget.minAvailable | string | `""` |  |
| neo4j.podSpec.annotations."prometheus.io/path" | string | `"/metrics"` |  |
| neo4j.podSpec.annotations."prometheus.io/port" | string | `"2004"` |  |
| neo4j.podSpec.annotations."prometheus.io/scrape" | string | `"true"` |  |
| neo4j.podSpec.containers | list | `[]` |  |
| neo4j.podSpec.initContainers | list | `[]` |  |
| neo4j.podSpec.loadbalancer | string | `"include"` |  |
| neo4j.podSpec.podAntiAffinity | bool | `true` |  |
| neo4j.podSpec.priorityClassName | string | `""` |  |
| neo4j.podSpec.serviceAccountName | string | `""` |  |
| neo4j.podSpec.terminationGracePeriodSeconds | int | `3600` |  |
| neo4j.podSpec.tolerations | list | `[]` |  |
| neo4j.podSpec.topologySpreadConstraints[0].maxSkew | int | `1` |  |
| neo4j.podSpec.topologySpreadConstraints[0].topologyKey | string | `"topology.kubernetes.io/zone"` |  |
| neo4j.podSpec.topologySpreadConstraints[0].whenUnsatisfiable | string | `"DoNotSchedule"` |  |
| neo4j.readinessProbe.failureThreshold | int | `20` |  |
| neo4j.readinessProbe.initialDelaySeconds | int | `60` |  |
| neo4j.readinessProbe.neo4jTimeoutSeconds | int | `60` |  |
| neo4j.readinessProbe.periodSeconds | int | `30` |  |
| neo4j.readinessProbe.timeoutSeconds | int | `10` |  |
| neo4j.securityContext.fsGroup | int | `1000` |  |
| neo4j.securityContext.fsGroupChangePolicy | string | `"Always"` |  |
| neo4j.securityContext.runAsGroup | int | `1000` |  |
| neo4j.securityContext.runAsNonRoot | bool | `true` |  |
| neo4j.securityContext.runAsUser | int | `1000` |  |
| neo4j.services.admin.annotations | object | `{}` |  |
| neo4j.services.admin.enabled | bool | `true` |  |
| neo4j.services.admin.spec.type | string | `"ClusterIP"` |  |
| neo4j.services.default.annotations | object | `{}` |  |
| neo4j.services.internals.annotations | object | `{}` |  |
| neo4j.services.internals.enabled | bool | `true` |  |
| neo4j.services.neo4j.enabled | bool | `false` |  |
| neo4j.ssl.bolt.privateKey.secretName | string | `"neo4j-bolt-https-tls"` |  |
| neo4j.ssl.bolt.privateKey.subPath | string | `"tls.key"` |  |
| neo4j.ssl.bolt.publicCertificate.secretName | string | `"neo4j-bolt-https-tls"` |  |
| neo4j.ssl.bolt.publicCertificate.subPath | string | `"tls.crt"` |  |
| neo4j.ssl.cluster.privateKey.secretName | string | `"neo4j-cluster-tls"` |  |
| neo4j.ssl.cluster.privateKey.subPath | string | `"tls.key"` |  |
| neo4j.ssl.cluster.publicCertificate.secretName | string | `"neo4j-cluster-tls"` |  |
| neo4j.ssl.cluster.publicCertificate.subPath | string | `"tls.crt"` |  |
| neo4j.ssl.cluster.trustedCerts.sources[0].secret.items[0].key | string | `"ca.crt"` |  |
| neo4j.ssl.cluster.trustedCerts.sources[0].secret.items[0].path | string | `"public.crt"` |  |
| neo4j.ssl.cluster.trustedCerts.sources[0].secret.name | string | `"neo4j-cluster-tls"` |  |
| neo4j.ssl.https.privateKey.secretName | string | `"neo4j-bolt-https-tls"` |  |
| neo4j.ssl.https.privateKey.subPath | string | `"tls.key"` |  |
| neo4j.ssl.https.publicCertificate.secretName | string | `"neo4j-bolt-https-tls"` |  |
| neo4j.ssl.https.publicCertificate.subPath | string | `"tls.crt"` |  |
| neo4j.ssl.https.trustedCerts.sources[0].secret.items[0].key | string | `"ca.crt"` |  |
| neo4j.ssl.https.trustedCerts.sources[0].secret.items[0].path | string | `"public.crt"` |  |
| neo4j.ssl.https.trustedCerts.sources[0].secret.name | string | `"neo4j-bolt-https-tls"` |  |
| neo4j.startupProbe.failureThreshold | int | `1000` |  |
| neo4j.startupProbe.periodSeconds | int | `5` |  |
| neo4j.statefulset.metadata.annotations | string | `nil` |  |
| neo4j.usingInstaller | bool | `true` |  |
| neo4j.volumes.backups.disableSubPathExpr | bool | `false` |  |
| neo4j.volumes.backups.mode | string | `"share"` |  |
| neo4j.volumes.backups.share.name | string | `"data"` |  |
| neo4j.volumes.data.disableSubPathExpr | bool | `false` |  |
| neo4j.volumes.data.dynamic.accessModes[0] | string | `"ReadWriteOnce"` |  |
| neo4j.volumes.data.dynamic.requests.storage | string | `"50Gi"` |  |
| neo4j.volumes.data.mode | string | `"dynamic"` |  |
| neo4j.volumes.import.disableSubPathExpr | bool | `false` |  |
| neo4j.volumes.import.mode | string | `"share"` |  |
| neo4j.volumes.import.share.name | string | `"data"` |  |
| neo4j.volumes.licenses.disableSubPathExpr | bool | `false` |  |
| neo4j.volumes.licenses.mode | string | `"share"` |  |
| neo4j.volumes.licenses.share.name | string | `"data"` |  |
| neo4j.volumes.logs.disableSubPathExpr | bool | `false` |  |
| neo4j.volumes.logs.mode | string | `"share"` |  |
| neo4j.volumes.logs.share.name | string | `"data"` |  |
| neo4j.volumes.metrics.disableSubPathExpr | bool | `false` |  |
| neo4j.volumes.metrics.mode | string | `"share"` |  |
| neo4j.volumes.metrics.share.name | string | `"data"` |  |
| neo4j.volumes.plugins.disableSubPathExpr | bool | `false` |  |
| neo4j.volumes.plugins.mode | string | `"share"` |  |
| neo4j.volumes.plugins.share.name | string | `"data"` |  |
| neo4jBox.enabled | bool | `true` |  |
| neo4jBox.podSecurityContext.fsGroup | int | `1000` |  |
| neo4jBox.ports.bolt | int | `7687` |  |
| neo4jBox.ports.https | int | `7473` |  |
| neo4jBox.replicas | int | `1` |  |
| neo4jBox.resources.limits.cpu | string | `"200m"` |  |
| neo4jBox.resources.limits.memory | string | `"256Mi"` |  |
| neo4jBox.resources.requests.cpu | string | `"100m"` |  |
| neo4jBox.resources.requests.memory | string | `"128Mi"` |  |
| neo4jBox.securityContext.allowPrivilegeEscalation | bool | `false` |  |
| neo4jBox.securityContext.capabilities.drop[0] | string | `"ALL"` |  |
| neo4jBox.securityContext.readOnlyRootFilesystem | bool | `false` |  |
| neo4jBox.securityContext.runAsGroup | int | `1000` |  |
| neo4jBox.securityContext.runAsNonRoot | bool | `true` |  |
| neo4jBox.securityContext.runAsUser | int | `1000` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# netsec

![Version: 5.0.1-260212195530-main-va1ed589](https://img.shields.io/badge/Version-5.0.1--260212195530--main--va1ed589-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Network Security

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.netsec.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","hostname":"sysdigcloud-elasticsearch","port":9200,"scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.netsec.admindb | string | `"anchore"` |  |
| global.legacyPostgres.postgresDatabases.netsec.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.netsec.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.netsec.db | string | `"netsec"` |  |
| global.legacyPostgres.postgresDatabases.netsec.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.netsec.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.netsec.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.netsec.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.netsec.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.netsec.username | string | `"netsec_user"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.password | string | `""` |  |
| global.legacyRedis.redisClientsSecure.netsec.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| netsec.api.deleteJanitorRedisKey | string | `"false"` |  |
| netsec.apiReplicaCount | int | `1` |  |
| netsec.audit.enabled | bool | `true` |  |
| netsec.communicationShards | int | `3` |  |
| netsec.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| netsec.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| netsec.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| netsec.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| netsec.enabled | bool | `true` |  |
| netsec.ingest.natsMaxInFlightMapper | int | `1024` |  |
| netsec.ingest.natsMaxInFlightReducer | int | `1024` |  |
| netsec.ingestReplicaCount | int | `1` |  |
| netsec.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-netsec-api"` |  |
| netsec.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-netsec-api"` |  |
| netsec.ingress[0].hosts[0].paths[0].path | string | `"/api/v1/networkSecurity"` |  |
| netsec.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-netsec-api"` |  |
| netsec.ingress[0].hosts[0].paths[0].servicePort | int | `9135` |  |
| netsec.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-netsec-topology-api"` |  |
| netsec.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-netsec-topology-api"` |  |
| netsec.ingress[0].hosts[0].paths[1].path | string | `"/api/v1/networkTopology"` |  |
| netsec.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-netsec-api"` |  |
| netsec.ingress[0].hosts[0].paths[1].servicePort | int | `9135` |  |
| netsec.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-netsec-threat-center-api"` |  |
| netsec.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-netsec-threat-center-api"` |  |
| netsec.ingress[0].hosts[0].paths[2].path | string | `"/api/secure/threat-center/v1"` |  |
| netsec.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-netsec-api"` |  |
| netsec.ingress[0].hosts[0].paths[2].servicePort | int | `9135` |  |
| netsec.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| netsec.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| netsec.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| netsec.ingress[0].labels.role | string | `"ingress-config"` |  |
| netsec.ingress[0].labels.tier | string | `"infra"` |  |
| netsec.ingress[0].name | string | `"sysdigcloud-netsec-ingress"` |  |
| netsec.janitor.cronjob | string | `"*/10 * * * *"` |  |
| netsec.janitor.updateKnpMappings | string | `"true"` |  |
| netsec.natsjs.enabled | bool | `false` |  |
| netsec.natsjs.endpoint | string | `"nats"` |  |
| netsec.rateLimit | int | `200` |  |
| netsec.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| netsec.repositoryPrefix | string | `"secure"` |  |
| netsec.resources.netsecAPI.limits.cpu | int | `1` |  |
| netsec.resources.netsecAPI.limits.memory | string | `"1Gi"` |  |
| netsec.resources.netsecAPI.requests.cpu | string | `"300m"` |  |
| netsec.resources.netsecAPI.requests.memory | string | `"1Gi"` |  |
| netsec.resources.netsecIngest.limits.cpu | int | `1` |  |
| netsec.resources.netsecIngest.limits.memory | string | `"4Gi"` |  |
| netsec.resources.netsecIngest.requests.cpu | string | `"500m"` |  |
| netsec.resources.netsecIngest.requests.memory | string | `"1Gi"` |  |
| netsec.resources.netsecJanitor.limits.cpu | string | `"300m"` |  |
| netsec.resources.netsecJanitor.limits.memory | string | `"4Gi"` |  |
| netsec.resources.netsecJanitor.requests.cpu | string | `"100m"` |  |
| netsec.resources.netsecJanitor.requests.memory | string | `"2Gi"` |  |
| netsec.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| netsec.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| netsec.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| netsec.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| netsec.serviceAccountName | string | `"sysdig"` |  |
| netsec.skipESAdditionalCerts | bool | `true` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# network-policies

![Version: 4.0.2](https://img.shields.io/badge/Version-4.0.2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.0](https://img.shields.io/badge/AppVersion-1.0.0-informational?style=flat-square)

This chart is owned and maintained by Sysdig Infra team.

It takes care of deploying Network Policies; different level of enforcement are set in the values for both ingress and egress. Please refer to the Runbooks

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| namespace | string | `"sysdig"` |  |
| networkPolicies.allowedNetworks | list | `[]` | Used for workloads that need to be accessed by things that are exposed through the host network (haproxy,kube-apiserver...), the CIDR is needed to authorize every node to connect to every authorized pod. This can be the `podNetwork`, the `hostNetwork` or a mix of the two if [cross-subnet selective encapsulation](https://projectcalico.docs.tigera.io/networking/vxlan-ipip#cross-subnet) is enabled |
| networkPolicies.enabled | bool | `true` | Use this flag to enable or disable the generated rules entirely |
| networkPolicies.falcocloudWorkerScaler.allowAll | bool | `false` | enabling this ignores allowedNetworks and allows all traffic to the falcocloud worker scaler this is needed to allow access from master nodes in GKE, since they are not part of our VPC and we don't know their IPs |
| networkPolicies.ingress.alb.selector | map | `{}` | A list of "app" label values to match ALB deployments to permit traffic from; make it `null` to exclude ALBs from generated rules |
| networkPolicies.ingress.allowedPodsLabel | map | `{}` | If a pod has this label, it will be permitted incoming traffic from Ingress pods. If not set or `null`, the value will be defaulted to `np-allow-ingress: "true"` |
| networkPolicies.ingress.allowedRolesSelector | object | `{}` | Roles that will be permitted incoming traffic, regardless of the presence of the label |
| networkPolicies.ingress.default | string | `"allow"` | Policies that block ingress traffic are created only when default is set to "deny" |
| networkPolicies.ingress.haproxy.selector | map | `{"matchExpressions":[{"key":"run","operator":"In","values":["haproxy-ingress"]}]}` | A list of "app" label values to match ALB deployments to permit traffic from; make it `null` to exclude HAproxy from generated rules |

# onboarding

![Version: 5.0.0-260212125638-main-v5f9bce1](https://img.shields.io/badge/Version-5.0.0--260212125638--main--v5f9bce1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Onboarding

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.onboarding.serviceToken | string | `"change_me"` |  |
| global.apps | string | `"secure"` |  |
| global.cloudProvider.name | string | `""` |  |
| global.cloudProvider.region | string | `""` |  |
| global.dnsName | string | `"change-me.com"` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.onboarding.admindb | string | `"anchore"` |  |
| global.legacyPostgres.postgresDatabases.onboarding.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.onboarding.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.onboarding.db | string | `"onboarding"` |  |
| global.legacyPostgres.postgresDatabases.onboarding.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.onboarding.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.onboarding.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.onboarding.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.onboarding.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.onboarding.username | string | `"onboarding_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.secure.azurePrincipal.auth.clientId | string | `""` |  |
| global.secure.azurePrincipal.auth.clientSecret | string | `""` |  |
| global.secure.backend.isEuRegion | bool | `false` |  |
| global.secure.cloudOnboardingConfig.aws.cdr.ebEnabled | bool | `true` |  |
| global.secure.cloudOnboardingConfig.aws.cdr.s3Enabled | bool | `true` |  |
| global.secure.cloudOnboardingConfig.aws.gov.cdr.ebEnabled | bool | `false` |  |
| global.secure.cloudOnboardingConfig.aws.gov.cdr.s3Enabled | bool | `true` |  |
| global.secure.cloudOnboardingConfig.aws.gov.enabled | bool | `false` |  |
| global.secure.oracleCloud.auth.configPosture.groupOcid | string | `""` |  |
| global.secure.oracleCloud.auth.configPosture.tenancyOcid | string | `""` |  |
| global.secure.oracleCloud.auth.configPosture.userOcid | string | `""` |  |
| global.secure.oracleCloud.auth.onboarding.groupOcid | string | `""` |  |
| global.secure.oracleCloud.auth.onboarding.tenancyOcid | string | `""` |  |
| global.secure.oracleCloud.auth.onboarding.userOcid | string | `""` |  |
| global.secure.trustedIdentity.aws | string | `""` |  |
| global.secure.trustedIdentity.awsGov | string | `""` |  |
| global.secure.trustedIdentity.azure | string | `""` |  |
| global.secure.trustedIdentity.azureApp.agentless.applicationId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.agentless.servicePrincipalId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.agentless.tenantId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.configPosture.applicationId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.configPosture.servicePrincipalId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.configPosture.tenantId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.onboarding.applicationId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.onboarding.servicePrincipalId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.onboarding.tenantId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.threatDetection.applicationId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.threatDetection.servicePrincipalId | string | `""` |  |
| global.secure.trustedIdentity.azureApp.threatDetection.tenantId | string | `""` |  |
| global.secure.trustedIdentity.gcp | string | `""` |  |
| onboarding.agentlessScanning.aws.accountId | string | `"878070807337"` |  |
| onboarding.agentlessScanning.azure.servicePrincipalId | string | `""` |  |
| onboarding.agentlessScanning.azure.tenantId | string | `"dd49593d-f413-4a73-937b-03e42293e446"` |  |
| onboarding.agentlessScanning.backend.cloudId | string | `""` |  |
| onboarding.agentlessScanning.backend.type | string | `"aws"` |  |
| onboarding.agentlessScanning.gcp.workerIdentity | string | `"agentless-worker-sa@prod-sysdig-agentless.iam.gserviceaccount.com"` |  |
| onboarding.authorizationService.enabled | bool | `false` |  |
| onboarding.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| onboarding.cloudsec.enabled | bool | `true` |  |
| onboarding.enabled | bool | `true` |  |
| onboarding.falcoCloud.eventBusArn | string | `"arn:aws:events:::event-bus/falco"` |  |
| onboarding.falcoCloud.eventBusArnGov | string | `""` |  |
| onboarding.firstTimeOnboarding.enabled | bool | `false` |  |
| onboarding.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-onboarding-api-v2"` |  |
| onboarding.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-onboarding-api-v2"` |  |
| onboarding.ingress[0].hosts[0].paths[0].path | string | `"/api/secure/onboarding/v2"` |  |
| onboarding.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-onboarding-api"` |  |
| onboarding.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| onboarding.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-onboarding-api-v3"` |  |
| onboarding.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-onboarding-api-v3"` |  |
| onboarding.ingress[0].hosts[0].paths[1].path | string | `"/api/secure/onboarding/v3"` |  |
| onboarding.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-onboarding-api"` |  |
| onboarding.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| onboarding.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| onboarding.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| onboarding.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| onboarding.ingress[0].labels.role | string | `"ingress-config"` |  |
| onboarding.ingress[0].labels.tier | string | `"infra"` |  |
| onboarding.ingress[0].name | string | `"sysdigcloud-onboarding-ingress"` |  |
| onboarding.isTest | bool | `false` |  |
| onboarding.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| onboarding.replicaCount | int | `1` |  |
| onboarding.repositoryPrefix | string | `"secure"` |  |
| onboarding.resources.onboardingApi.limits.cpu | int | `1` |  |
| onboarding.resources.onboardingApi.limits.memory | string | `"512Mi"` |  |
| onboarding.resources.onboardingApi.requests.cpu | string | `"500m"` |  |
| onboarding.resources.onboardingApi.requests.memory | string | `"128Mi"` |  |
| onboarding.serviceAccountName | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# onprem-docs

![Version: 0.0.1-main.2025-04-23T06-20-00Z.79053ad](https://img.shields.io/badge/Version-0.0.1--main.2025--04--23T06--20--00Z.79053ad-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.0.1-main.2025-04-23T06-20-00Z.79053ad](https://img.shields.io/badge/AppVersion-0.0.1--main.2025--04--23T06--20--00Z.79053ad-informational?style=flat-square)

Onprem docs

## Source Code

* <https://github.com/draios/docs>

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.ingressSpec.enabled | bool | `false` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.useIngressV2 | bool | `true` |  |
| onpremDocs.enabled | bool | `false` |  |
| onpremDocs.ingress[0].hosts[0].host | string | `""` |  |
| onpremDocs.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-docs"` |  |
| onpremDocs.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-docs"` |  |
| onpremDocs.ingress[0].hosts[0].paths[0].path | string | `"/docs"` |  |
| onpremDocs.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-docs"` |  |
| onpremDocs.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| onpremDocs.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| onpremDocs.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| onpremDocs.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| onpremDocs.ingress[0].labels.role | string | `"ingress-config"` |  |
| onpremDocs.ingress[0].labels.tier | string | `"infra"` |  |
| onpremDocs.ingress[0].name | string | `"sysdigcloud-docs-ingress"` |  |
| onpremDocs.namespace | string | `"sysdigcloud"` |  |
| onpremDocs.replicaCount | int | `1` |  |
| onpremDocs.resources.limits.cpu | string | `"500m"` |  |
| onpremDocs.resources.limits.memory | string | `"512Mi"` |  |
| onpremDocs.resources.requests.cpu | string | `"100m"` |  |
| onpremDocs.resources.requests.memory | string | `"200Mi"` |  |
| onpremDocs.serviceAccountName | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# platform-service

![Version: 0.0.1-260312095512-main-v86956af](https://img.shields.io/badge/Version-0.0.1--260312095512--main--v86956af-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.0.1-260312095512-main-v86956af](https://img.shields.io/badge/AppVersion-0.0.1--260312095512--main--v86956af-informational?style=flat-square)

Platform Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.platformService.alerts.serviceToken | string | `nil` |  |
| global.api.serviceTokens.platformService.zones.serviceToken | string | `nil` |  |
| global.apps | string | `"monitor"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.appname | string | `"platform_alerts"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.connectMaxRetries | int | `10` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.connectMaxRetryDelay | string | `"30s"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.connectRetryDelay | string | `"1s"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.db | string | `"platform_alerts"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.forceSkipDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.migrationdir | string | `"/platform-service/alerts/postgres/migrations"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.poolMaxConns | int | `16` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.poolMinConns | int | `0` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.platformAlerts.username | string | `"platform_alerts_user"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.platformZones.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.appname | string | `"platform_zones"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.connectMaxRetries | int | `10` |  |
| global.legacyPostgres.postgresDatabases.platformZones.connectMaxRetryDelay | string | `"30s"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.connectRetryDelay | string | `"1s"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.db | string | `"platform_zones"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.forceSkipDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.platformZones.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.migrationEnabled | bool | `true` |  |
| global.legacyPostgres.postgresDatabases.platformZones.migrationdir | string | `"/platform-service/zones/postgres/migrations"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.platformZones.poolMaxConnectionsLife | string | `"3600s"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.poolMaxIdleConnections | int | `20` |  |
| global.legacyPostgres.postgresDatabases.platformZones.poolMaxOpenConnections | int | `20` |  |
| global.legacyPostgres.postgresDatabases.platformZones.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.platformZones.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.platformZones.username | string | `"platform_zones_user"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.appname | string | `"platform_zones_monitor"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.connectMaxRetries | int | `10` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.connectMaxRetryDelay | string | `"30s"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.connectRetryDelay | string | `"1s"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.migrationEnabled | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.poolMaxConnectionsLife | string | `"3600s"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.poolMaxIdleConnections | int | `1` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.poolMaxOpenConnections | int | `1` |  |
| global.legacyPostgres.postgresDatabases.platformZonesMonitorDB.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.appname | string | `"platform_zones"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.connectMaxRetries | int | `10` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.connectMaxRetryDelay | string | `"30s"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.connectRetryDelay | string | `"1s"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.db | string | `"policy"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.forceSkipDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.migrationEnabled | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.poolMaxConnectionsLife | string | `"3600s"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.poolMaxIdleConnections | int | `20` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.poolMaxOpenConnections | int | `20` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.platformZonesPolicyDB.username | string | `"policydbuser"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.db | string | `"sysdig"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.sysdig.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.sysdig.username | string | `"sysdig_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| platformService.alerts.analytics.enabled | bool | `true` |  |
| platformService.alerts.analytics.schedule | string | `"0 23 * * *"` |  |
| platformService.alerts.audit.enabled | bool | `true` |  |
| platformService.alerts.audit.ingestionEndpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| platformService.alerts.automation.automationByIDCache.cleanup | string | `"5m"` |  |
| platformService.alerts.automation.automationByIDCache.enabled | bool | `true` |  |
| platformService.alerts.automation.automationByIDCache.expiration | string | `"5s"` |  |
| platformService.alerts.automation.automationExecutionTracker.batchSize | int | `100` |  |
| platformService.alerts.automation.automationExecutionTracker.dbInterval | string | `"1m"` |  |
| platformService.alerts.automation.automationExecutionTracker.enabled | bool | `true` |  |
| platformService.alerts.automation.automationRateLimitStats.updateInterval | string | `"1m"` |  |
| platformService.alerts.automation.automationsToTriggerCache.cleanup | string | `"5m"` |  |
| platformService.alerts.automation.automationsToTriggerCache.enabled | bool | `true` |  |
| platformService.alerts.automation.automationsToTriggerCache.expiration | string | `"5s"` |  |
| platformService.alerts.automation.cleanup.batchSize | int | `1000` |  |
| platformService.alerts.automation.cleanup.cutoffDays | int | `14` |  |
| platformService.alerts.automation.cleanup.enabled | bool | `true` |  |
| platformService.alerts.automation.cleanup.schedule | string | `"0 0 * * *"` |  |
| platformService.alerts.automation.customerSettingsCache.cleanup | string | `"5m"` |  |
| platformService.alerts.automation.customerSettingsCache.enabled | bool | `true` |  |
| platformService.alerts.automation.customerSettingsCache.expiration | string | `"1m"` |  |
| platformService.alerts.automation.downloadLink.jwt.expiration | string | `"336h"` |  |
| platformService.alerts.automation.executionRateLimit.runtime.cache.cleanup | string | `"1m"` |  |
| platformService.alerts.automation.executionRateLimit.runtime.cache.expiration | string | `"1s"` |  |
| platformService.alerts.automation.executionRateLimit.runtime.value | int | `10` |  |
| platformService.alerts.automation.logging.eventsEnabled | bool | `true` |  |
| platformService.alerts.automation.natsExecutor.asyncActionsTimeout | string | `"10m"` |  |
| platformService.alerts.automation.natsExecutor.asyncActionsTimeoutJira | string | `"2h"` |  |
| platformService.alerts.automation.natsExecutor.consumer.enabled | bool | `true` |  |
| platformService.alerts.automation.natsExecutor.consumer.fetchTimeout | string | `"1s"` |  |
| platformService.alerts.automation.natsExecutor.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.automation.natsExecutor.consumer.name | string | `"platform-automations-consumer"` |  |
| platformService.alerts.automation.natsExecutor.consumer.pullBatch | int | `100` |  |
| platformService.alerts.automation.natsExecutor.consumer.queuedNodeWorkers | int | `100` |  |
| platformService.alerts.automation.natsExecutor.consumer.stream | string | `"platform-automations"` |  |
| platformService.alerts.automation.natsExecutor.consumer.subjects | string | `"platform_automations.nodes.>"` |  |
| platformService.alerts.automation.natsExecutor.consumer.timeoutRetryMaxWait | string | `"1s"` |  |
| platformService.alerts.automation.natsExecutor.enabled | bool | `true` |  |
| platformService.alerts.automation.natsExecutor.poller.finishProcessedExecutionsInterval | string | `"1s"` |  |
| platformService.alerts.automation.natsExecutor.poller.finishProcessedExecutionsPullSize | int | `10000` |  |
| platformService.alerts.automation.natsExecutor.poller.interval | string | `"3s"` |  |
| platformService.alerts.automation.natsExecutor.poller.processExpiredNodesInterval | string | `"1m"` |  |
| platformService.alerts.automation.natsExecutor.poller.processExpiredNodesPullSize | int | `10000` |  |
| platformService.alerts.automation.natsExecutor.poller.pullSize | int | `10000` |  |
| platformService.alerts.automation.natsExecutor.poller.queuedNodes.backoff.factor | int | `2` |  |
| platformService.alerts.automation.natsExecutor.poller.queuedNodes.backoff.max | string | `"3s"` |  |
| platformService.alerts.automation.natsExecutor.poller.queuedNodes.backoff.min | string | `"10ms"` |  |
| platformService.alerts.automation.natsExecutor.poller.queuedNodes.subject | string | `"platform_automations.nodes.queued.v1"` |  |
| platformService.alerts.automation.natsExecutor.poller.queuedNodes.workers | int | `100` |  |
| platformService.alerts.automation.natsExecutor.workers | int | `1` |  |
| platformService.alerts.automation.queryParser.cache.size | int | `1000` |  |
| platformService.alerts.automation.status.componentHealthEnabled | bool | `false` |  |
| platformService.alerts.automation.status.monitorAlertsEnabled | bool | `false` |  |
| platformService.alerts.automation.status.riskEnabled | bool | `true` |  |
| platformService.alerts.automation.status.runtimeEnabled | bool | `true` |  |
| platformService.alerts.automation.status.threatsEnabled | bool | `true` |  |
| platformService.alerts.automation.status.vmExceptionEnabled | bool | `true` |  |
| platformService.alerts.automation.status.vmNewFindingsEnabled | bool | `true` |  |
| platformService.alerts.automation.translatedZoneFilter.cache.expiration | string | `"1m"` |  |
| platformService.alerts.automation.translatedZoneFilter.cache.size | int | `1000` |  |
| platformService.alerts.automation.validator.batchSize | int | `100` |  |
| platformService.alerts.automation.validator.enabled | bool | `true` |  |
| platformService.alerts.automation.validator.schedule | string | `"0 * * * *"` |  |
| platformService.alerts.enabled | bool | `true` |  |
| platformService.alerts.monitor.cache.cleanup | string | `"10m"` |  |
| platformService.alerts.monitor.cache.expiration | string | `"5m"` |  |
| platformService.alerts.monitor.team.cache.cleanup | string | `"2m"` |  |
| platformService.alerts.monitor.team.cache.expiration | string | `"30s"` |  |
| platformService.alerts.monitor.url | string | `"http://sysdigcloud-api:8080"` |  |
| platformService.alerts.nats.js.automations.events.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.automations.events.consumer.fetchTimeout | string | `"1s"` |  |
| platformService.alerts.nats.js.automations.events.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.automations.events.consumer.name | string | `"platform-automations-events-consumer"` |  |
| platformService.alerts.nats.js.automations.events.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.automations.events.consumer.stream | string | `"platform-automations-events"` |  |
| platformService.alerts.nats.js.automations.events.consumer.subjects | string | `"platform.automations.events.v1.>"` |  |
| platformService.alerts.nats.js.automations.events.consumer.timeoutRetryMaxWait | string | `"1s"` |  |
| platformService.alerts.nats.js.automations.events.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.automations.events.stream.maxAge | string | `"86400000000000"` |  |
| platformService.alerts.nats.js.automations.events.stream.maxBytes | string | `"4294967296"` |  |
| platformService.alerts.nats.js.automations.events.stream.numReplicas | int | `3` |  |
| platformService.alerts.nats.js.automations.nodesQueued.stream.maxAge | string | `"86400000000000"` |  |
| platformService.alerts.nats.js.automations.nodesQueued.stream.maxBytes | string | `"4294967296"` |  |
| platformService.alerts.nats.js.automations.nodesQueued.stream.numReplicas | int | `3` |  |
| platformService.alerts.nats.js.clientName | string | `"sysdigcloud-platform-alerts-api"` |  |
| platformService.alerts.nats.js.componentHealth.shieldStatusChange.notifier.subject | string | `"notifier.notifications.1.component.health"` |  |
| platformService.alerts.nats.js.enabled | bool | `true` |  |
| platformService.alerts.nats.js.migrationFile | string | `"/platform-service/alerts/nats/migrations/streams.json"` |  |
| platformService.alerts.nats.js.monitorAlerts.notifier.enabled | bool | `true` |  |
| platformService.alerts.nats.js.monitorAlerts.notifier.subject | string | `"notifier.notifications.1.monitor.alerts.occurrences"` |  |
| platformService.alerts.nats.js.notifier.genericEmail.notifier.subject | string | `"notifier.notifications.1.generic.email"` |  |
| platformService.alerts.nats.js.notifier.responses.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.notifier.responses.consumer.fetchTimeout | string | `"1s"` |  |
| platformService.alerts.nats.js.notifier.responses.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.notifier.responses.consumer.name | string | `"platform-automation-responses-consumer"` |  |
| platformService.alerts.nats.js.notifier.responses.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.notifier.responses.consumer.stream | string | `"notifier-responses-1"` |  |
| platformService.alerts.nats.js.notifier.responses.consumer.subjects | string | `"notifier.responses.1.automations"` |  |
| platformService.alerts.nats.js.notifier.responses.consumer.timeoutRetryMaxWait | string | `"10s"` |  |
| platformService.alerts.nats.js.notifier.responses.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.responseActions.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.responseActions.consumer.fetchTimeout | string | `"10s"` |  |
| platformService.alerts.nats.js.responseActions.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.responseActions.consumer.name | string | `"platform-automations-consumer"` |  |
| platformService.alerts.nats.js.responseActions.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.responseActions.consumer.stream | string | `"response-actions-executions-1"` |  |
| platformService.alerts.nats.js.responseActions.consumer.subjects | string | `"response-actions.execution.action.v1.>"` |  |
| platformService.alerts.nats.js.responseActions.consumer.timeoutRetryMaxWait | string | `"10s"` |  |
| platformService.alerts.nats.js.responseActions.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.risk.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.risk.consumer.fetchTimeout | string | `"10s"` |  |
| platformService.alerts.nats.js.risk.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.risk.consumer.name | string | `"platform-alerts-consumer"` |  |
| platformService.alerts.nats.js.risk.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.risk.consumer.stream | string | `"risks-alerts"` |  |
| platformService.alerts.nats.js.risk.consumer.subjects | string | `"risks-alerts.*"` |  |
| platformService.alerts.nats.js.risk.consumer.timeoutRetryMaxWait | string | `"10s"` |  |
| platformService.alerts.nats.js.risk.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.risk.notifier.enabled | bool | `true` |  |
| platformService.alerts.nats.js.risk.notifier.subject | string | `"notifier.notifications.1.risk"` |  |
| platformService.alerts.nats.js.runtime.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.runtime.consumer.fetchTimeout | string | `"1s"` |  |
| platformService.alerts.nats.js.runtime.consumer.listenAllRuntimeEvents | bool | `true` |  |
| platformService.alerts.nats.js.runtime.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.runtime.consumer.name | string | `"platform-automations-consumer"` |  |
| platformService.alerts.nats.js.runtime.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.runtime.consumer.stream | string | `"events"` |  |
| platformService.alerts.nats.js.runtime.consumer.subjects | string | `"events.source.events.policy.>"` |  |
| platformService.alerts.nats.js.runtime.consumer.timeoutRetryMaxWait | string | `"1s"` |  |
| platformService.alerts.nats.js.runtime.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.runtime.notifier.commonContentEnabled | bool | `true` |  |
| platformService.alerts.nats.js.runtime.notifier.enabled | bool | `true` |  |
| platformService.alerts.nats.js.runtime.notifier.subject | string | `"notifier.notifications.1.runtime"` |  |
| platformService.alerts.nats.js.threat.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.threat.consumer.fetchTimeout | string | `"10s"` |  |
| platformService.alerts.nats.js.threat.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.threat.consumer.name | string | `"platform-automations-consumer"` |  |
| platformService.alerts.nats.js.threat.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.threat.consumer.stream | string | `"threats-engine"` |  |
| platformService.alerts.nats.js.threat.consumer.subjects | string | `"threats.engine.activity.created"` |  |
| platformService.alerts.nats.js.threat.consumer.timeoutRetryMaxWait | string | `"10s"` |  |
| platformService.alerts.nats.js.threat.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.threat.notifier.enabled | bool | `true` |  |
| platformService.alerts.nats.js.threat.notifier.subject | string | `"notifier.notifications.1.threat"` |  |
| platformService.alerts.nats.js.ticketing.issues.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.ticketing.issues.consumer.fetchTimeout | string | `"10s"` |  |
| platformService.alerts.nats.js.ticketing.issues.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.ticketing.issues.consumer.name | string | `"platform-automation-jira-issues-consumer"` |  |
| platformService.alerts.nats.js.ticketing.issues.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.ticketing.issues.consumer.stream | string | `"jira_issues"` |  |
| platformService.alerts.nats.js.ticketing.issues.consumer.subjects | string | `"jira_issues.>"` |  |
| platformService.alerts.nats.js.ticketing.issues.consumer.timeoutRetryMaxWait | string | `"10s"` |  |
| platformService.alerts.nats.js.ticketing.issues.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.tls.cert | string | `"/opt/certs/nats-js-tls-certs/ca.crt"` |  |
| platformService.alerts.nats.js.tls.enabled | bool | `true` |  |
| platformService.alerts.nats.js.url | string | `"nats"` |  |
| platformService.alerts.nats.js.vm.exception.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.vm.exception.consumer.fetchTimeout | string | `"10s"` |  |
| platformService.alerts.nats.js.vm.exception.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.vm.exception.consumer.name | string | `"platform-automations-exceptions-consumer"` |  |
| platformService.alerts.nats.js.vm.exception.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.vm.exception.consumer.stream | string | `"secure-vm-notifier-integrations"` |  |
| platformService.alerts.nats.js.vm.exception.consumer.subjects | string | `"secure.vm.notifier.integrations.exceptions"` |  |
| platformService.alerts.nats.js.vm.exception.consumer.timeoutRetryMaxWait | string | `"10s"` |  |
| platformService.alerts.nats.js.vm.exception.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.vm.exception.notifier.enabled | bool | `true` |  |
| platformService.alerts.nats.js.vm.exception.notifier.subject | string | `"notifier.notifications.1.vm"` |  |
| platformService.alerts.nats.js.vm.imageHasVulns.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.vm.imageHasVulns.consumer.name | string | `"platform-alerts-consumer"` |  |
| platformService.alerts.nats.js.vm.imageHasVulns.consumer.stream | string | `"secure-vm-notifier-integrations"` |  |
| platformService.alerts.nats.js.vm.imageHasVulns.consumer.subjects | string | `"secure.vm.notifier.integrations.jira"` |  |
| platformService.alerts.nats.js.vm.imageHasVulns.consumer.timeoutRetryMaxWait | string | `"10s"` |  |
| platformService.alerts.nats.js.vm.imageHasVulns.notifier.enabled | bool | `true` |  |
| platformService.alerts.nats.js.vm.imageHasVulns.notifier.subject | string | `"notifier.notifications.1.vm"` |  |
| platformService.alerts.nats.js.vm.newFindings.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.vm.newFindings.consumer.fetchTimeout | string | `"10s"` |  |
| platformService.alerts.nats.js.vm.newFindings.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.vm.newFindings.consumer.name | string | `"platform-automations-consumer"` |  |
| platformService.alerts.nats.js.vm.newFindings.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.vm.newFindings.consumer.stream | string | `"secure-vm-notifier-integrations"` |  |
| platformService.alerts.nats.js.vm.newFindings.consumer.subjects | string | `"secure.vm.notifier.integrations.resourcefindings"` |  |
| platformService.alerts.nats.js.vm.newFindings.consumer.timeoutRetryMaxWait | string | `"10s"` |  |
| platformService.alerts.nats.js.vm.newFindings.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.vm.newFindings.notifier.enabled | bool | `true` |  |
| platformService.alerts.nats.js.vm.newFindings.notifier.subject | string | `"notifier.notifications.1.vm"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByImage.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByImage.consumer.fetchTimeout | string | `"10s"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByImage.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByImage.consumer.name | string | `"platform-automations-new-findings-grouped-by-image-consumer"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByImage.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByImage.consumer.stream | string | `"secure-vm-notifier-integrations"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByImage.consumer.subjects | string | `"secure.vm.notifier.integrations.findings-grouped-by-image"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByImage.consumer.timeoutRetryMaxWait | string | `"10s"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByImage.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByImage.notifier.subject | string | `"notifier.notifications.1.vm"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByResource.consumer.enabled | bool | `true` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByResource.consumer.fetchTimeout | string | `"10s"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByResource.consumer.maxInFlight | int | `10000` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByResource.consumer.name | string | `"platform-automations-new-findings-grouped-by-resource-consumer"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByResource.consumer.pullBatch | int | `100` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByResource.consumer.stream | string | `"secure-vm-notifier-integrations"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByResource.consumer.subjects | string | `"secure.vm.notifier.integrations.findings-grouped-by-resource"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByResource.consumer.timeoutRetryMaxWait | string | `"10s"` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByResource.consumer.workers | int | `100` |  |
| platformService.alerts.nats.js.vm.newFindingsGroupedByResource.notifier.subject | string | `"notifier.notifications.1.vm"` |  |
| platformService.alerts.responseActions.url | string | `"sysdigcloud-response-actions-controller-grpc:50051"` |  |
| platformService.alerts.server.enableEventsEndpoints | bool | `false` |  |
| platformService.alerts.server.port.grpc | int | `5052` |  |
| platformService.alerts.server.port.rest | int | `7004` |  |
| platformService.alerts.ticketing.url | string | `"http://sysdigcloud-ticketing-api:7001"` |  |
| platformService.alerts.zones.cache.cleanup | string | `"2m"` |  |
| platformService.alerts.zones.cache.expiration | string | `"30s"` |  |
| platformService.alerts.zones.url | string | `"sysdigcloud-platform-zones-service-grpc:8091"` |  |
| platformService.api.serviceAccountName | string | `"sysdig"` |  |
| platformService.audit.enabled | bool | `true` |  |
| platformService.enabled | bool | `true` |  |
| platformService.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| platformService.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-platform-service-api"` |  |
| platformService.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-platform-service-api"` |  |
| platformService.ingress[0].hosts[0].paths[0].path | string | `"/api/platform-service/v1"` |  |
| platformService.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-platform-service-api"` |  |
| platformService.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| platformService.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-platform-automations-api"` |  |
| platformService.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-platform-automations-api"` |  |
| platformService.ingress[0].hosts[0].paths[1].path | string | `"/api/platform-automations/v1"` |  |
| platformService.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-platform-alerts-api"` |  |
| platformService.ingress[0].hosts[0].paths[1].servicePort | int | `7004` |  |
| platformService.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| platformService.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| platformService.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| platformService.ingress[0].labels.role | string | `"ingress-config"` |  |
| platformService.ingress[0].labels.tier | string | `"infra"` |  |
| platformService.ingress[0].name | string | `"sysdigcloud-platform-service-ingress"` |  |
| platformService.logLevel.debug.enabled | bool | `false` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-platform-zones-public-api"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[0].apiGatewayStickySessions | bool | `true` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-platform-zones-public-api"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[0].path | string | `"/platform/v1/zones"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-platform-zones-service-rest"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[0].servicePort | int | `8090` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-platform-zones-private-api"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[1].apiGatewayStickySessions | bool | `true` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-platform-zones-private-api"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[1].path | string | `"/api/v1/zones"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[1].pathType | string | `"ImplementationSpecific"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-platform-zones-service-rest"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[1].servicePort | int | `8090` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-platform-zones-v2-private-api"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[2].apiGatewayStickySessions | bool | `true` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-platform-zones-v2-private-api"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[2].path | string | `"/api/v2/zones"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[2].pathType | string | `"ImplementationSpecific"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-platform-zones-service-rest"` |  |
| platformService.platformZones.ingress[0].hosts[0].paths[2].servicePort | int | `8090` |  |
| platformService.platformZones.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| platformService.platformZones.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| platformService.platformZones.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| platformService.platformZones.ingress[0].labels.role | string | `"ingress-config"` |  |
| platformService.platformZones.ingress[0].labels.tier | string | `"infra"` |  |
| platformService.platformZones.ingress[0].name | string | `"sysdigcloud-platform-zones-ingress"` |  |
| platformService.postJob.ttlSecondsAfterFinished | int | `60` |  |
| platformService.preJob.ttlSecondsAfterFinished | int | `60` |  |
| platformService.profiler.enabled | bool | `false` |  |
| platformService.profiler.port | int | `6060` |  |
| platformService.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| platformService.replicaCount | int | `2` |  |
| platformService.repositoryPrefix | string | `"monitor"` |  |
| platformService.resources.platformAlertsAnalytics.limits.cpu | string | `"500m"` |  |
| platformService.resources.platformAlertsAnalytics.limits.memory | string | `"150Mi"` |  |
| platformService.resources.platformAlertsAnalytics.requests.cpu | string | `"100m"` |  |
| platformService.resources.platformAlertsAnalytics.requests.memory | string | `"100Mi"` |  |
| platformService.resources.platformAlertsAutomationValidator.limits.cpu | string | `"500m"` |  |
| platformService.resources.platformAlertsAutomationValidator.limits.memory | string | `"150Mi"` |  |
| platformService.resources.platformAlertsAutomationValidator.requests.cpu | string | `"100m"` |  |
| platformService.resources.platformAlertsAutomationValidator.requests.memory | string | `"100Mi"` |  |
| platformService.resources.platformAlertsCleanup.limits.cpu | string | `"500m"` |  |
| platformService.resources.platformAlertsCleanup.limits.memory | string | `"150Mi"` |  |
| platformService.resources.platformAlertsCleanup.requests.cpu | string | `"100m"` |  |
| platformService.resources.platformAlertsCleanup.requests.memory | string | `"100Mi"` |  |
| platformService.resources.platformService.limits.cpu | int | `2` |  |
| platformService.resources.platformService.limits.memory | string | `"1Gi"` |  |
| platformService.resources.platformService.requests.cpu | string | `"500m"` |  |
| platformService.resources.platformService.requests.memory | string | `"200Mi"` |  |
| platformService.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| platformService.resources.postgresqlinit.limits.memory | string | `"150Mi"` |  |
| platformService.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| platformService.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| platformService.server.port.health | int | `8083` |  |
| platformService.server.port.metric | int | `25000` |  |
| platformService.zones.cloudauth.enabled | bool | `false` |  |
| platformService.zones.cloudauth.failureTtlCacheExpiration | string | `"5m"` |  |
| platformService.zones.cloudauth.internalCacheExpiration | string | `"5s"` |  |
| platformService.zones.cloudauth.maxReceiveSizeBytes | string | `"33554432"` |  |
| platformService.zones.cloudauth.tls.cert | string | `""` |  |
| platformService.zones.cloudauth.tls.enabled | bool | `false` |  |
| platformService.zones.cloudauth.ttlCacheExpiration | string | `"2h"` |  |
| platformService.zones.cloudauth.url | string | `"sysdigcloud-cloudauth-api-grpc:6000"` |  |
| platformService.zones.command[0] | string | `"/bin/sh"` |  |
| platformService.zones.command[1] | string | `"-c"` |  |
| platformService.zones.command[2] | string | `"source /workdir/env-vars.sh && /usr/bin/platform-service-api"` |  |
| platformService.zones.devmode | bool | `false` |  |
| platformService.zones.enabled | bool | `false` |  |
| platformService.zones.ibm | bool | `false` |  |
| platformService.zones.ingressEnabled | bool | `false` |  |
| platformService.zones.loggingLevel | string | `"info"` |  |
| platformService.zones.mds.endpoint | string | `"sysdigcloud-metadata-service-server:5300"` |  |
| platformService.zones.mds.failureTtlCacheExpiration | string | `"5m"` |  |
| platformService.zones.mds.ttlCacheExpiration | string | `"2h"` |  |
| platformService.zones.monitor.authCache.expiration | string | `"5m"` |  |
| platformService.zones.monitor.skipTLS | bool | `false` |  |
| platformService.zones.monitor.url | string | `"http://sysdigcloud-api:8080"` |  |
| platformService.zones.nats.js.clientName | string | `"sysdigcloud-platform-zones-service"` |  |
| platformService.zones.nats.js.enabled | bool | `true` |  |
| platformService.zones.nats.js.migrationFile | string | `"/platform-service/zones/nats/migrations/streams.json"` |  |
| platformService.zones.nats.js.tls.cert | string | `"/opt/certs/nats-js-tls-certs/ca.crt"` |  |
| platformService.zones.nats.js.tls.enabled | bool | `true` |  |
| platformService.zones.nats.js.url | string | `"nats"` |  |
| platformService.zones.nats.js.zones.stream.maxAge | string | `"0"` |  |
| platformService.zones.nats.js.zones.stream.maxBytes | string | `"2147483648"` |  |
| platformService.zones.nats.js.zones.stream.numReplicas | int | `3` |  |
| platformService.zones.onprem | bool | `false` |  |
| platformService.zones.readOnly | bool | `false` |  |
| platformService.zones.server.port.grpc | int | `8091` |  |
| platformService.zones.server.port.rest | int | `8090` |  |
| platformService.zones.useOldDatabase | bool | `false` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# plotter

![Version: 0.0.1-main.2026-03-11T12-03-56Z.d67b9fe](https://img.shields.io/badge/Version-0.0.1--main.2026--03--11T12--03--56Z.d67b9fe-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig Monitor Plotter

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.alertingSystem.enabled | bool | `true` |  |
| global.api.serviceTokens.plotter.serviceToken | string | `""` |  |
| global.apps | string | `"monitor"` |  |
| global.cloudProvider | object | `{}` |  |
| global.clusterDomain | string | `"cluster.local"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdig"` |  |
| plotter.blockingThreads | int | `1` |  |
| plotter.cpu_threads | int | `1` |  |
| plotter.enabled | bool | `true` |  |
| plotter.logLevel | string | `"info"` |  |
| plotter.port | int | `8000` |  |
| plotter.prometheusExporter.port | int | `8000` |  |
| plotter.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| plotter.replicaCount | int | `2` |  |
| plotter.repositoryPrefix | string | `"monitor"` |  |
| plotter.resources.plotter.limits.cpu | string | `"500m"` |  |
| plotter.resources.plotter.limits.memory | string | `"300Mi"` |  |
| plotter.resources.plotter.requests.cpu | string | `"100m"` |  |
| plotter.resources.plotter.requests.memory | string | `"50Mi"` |  |
| plotter.workerThreads | int | `2` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# policies

![Version: 4.3.3-260312190648-main-v8cd847a](https://img.shields.io/badge/Version-4.3.3--260312190648--main--v8cd847a-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Policies

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.policies.serviceToken | string | `nil` |  |
| global.api.serviceTokens.rulesDeployer.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.dnsName | string | `""` |  |
| global.elasticsearch.tlsencryption.useCertManager | bool | `false` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.policies.admindb | string | `"anchore"` |  |
| global.legacyPostgres.postgresDatabases.policies.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.policies.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.policies.db | string | `"policies"` |  |
| global.legacyPostgres.postgresDatabases.policies.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.policies.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.policies.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.policies.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.policies.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.policies.username | string | `"policies_user"` |  |
| global.legacyRedis.redisClientsMonitor.agent.tls | bool | `false` |  |
| global.legacyRedis.redisClientsSecure.policies.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.secure.artifactDeployer.artifacts | string | `"malware_content_0 malware_content_1 malware_content_2 malware_content_3 malware_content_4 malware_content_5 malware_content_6 malware_content_7 malware_content_8 malware_content_9 yara_rules_0"` |  |
| global.secure.artifactDeployer.enabled | bool | `false` |  |
| global.secure.artifactDeployer.schedule | string | `"0 12 * * *"` |  |
| global.secure.backend.url | string | `"http://sysdigcloud-api:8080"` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.secure.rulesDeployer.createNewPolicies | string | `"no"` |  |
| global.secure.rulesDeployer.deployRules | string | `"yes"` |  |
| global.secure.rulesDeployer.enabled | bool | `false` |  |
| global.secure.rulesDeployer.schedule | string | `"0 0 * * *"` |  |
| global.secure.rulesDeployer.sdcSslVerify | bool | `false` |  |
| global.secure.rulesDeployer.serviceToken | string | `"from_the_default_values"` |  |
| global.secure.rulesDeployer.skip.entraContents | string | `"yes"` |  |
| global.secure.rulesDeployer.skip.falcoCloudContents | string | `"no"` |  |
| global.secure.rulesDeployer.skip.falcoVersion0 | string | `"yes"` |  |
| global.secure.rulesDeployer.skip.githubContents | string | `"no"` |  |
| global.secure.rulesDeployer.skip.guarddutyContents | string | `"yes"` |  |
| global.secure.rulesDeployer.skip.k8sVersion2 | string | `"yes"` |  |
| global.secure.rulesDeployer.skip.oktaContents | string | `"no"` |  |
| global.secure.rulesDeployer.skip.windowsContents | string | `"no"` |  |
| global.secure.rulesDeployer.validateRules | string | `"yes"` |  |
| policies.api.hpa.cpuAverage | float | `1.5` |  |
| policies.api.hpa.enabled | bool | `false` |  |
| policies.api.hpa.maxReplicas | int | `5` |  |
| policies.api.hpa.minReplicas | int | `2` |  |
| policies.api.hpa.scaleDown.periodSeconds | int | `60` |  |
| policies.api.hpa.scaleDown.podValue | int | `1` |  |
| policies.api.hpa.scaleDown.stabilizationWindowSeconds | int | `120` |  |
| policies.api.hpa.scaleUp.periodSeconds | int | `15` |  |
| policies.api.hpa.scaleUp.podValue | int | `2` |  |
| policies.api.hpa.scaleUp.stabilizationWindowSeconds | int | `0` |  |
| policies.api.serviceAccountName | string | `"sysdig"` |  |
| policies.apiReplicaCount | int | `1` |  |
| policies.audit.enabled | bool | `true` |  |
| policies.cloudauth.grpcMaxMsgSizeBytes | string | `"4194304"` |  |
| policies.enable.loadManifestFromValidatorService | bool | `true` |  |
| policies.enable.newValidatorsPaths | bool | `true` |  |
| policies.enable.rcValidation | bool | `false` |  |
| policies.enable.validationService | bool | `true` |  |
| policies.enabled | bool | `true` |  |
| policies.falcoCloud.CAPolicyTypes | string | `"awscloudtrail okta github azure_entra guardduty ibm_activitytracker"` |  |
| policies.falcoCloud.maximumCloudtrailRequiredPluginVersion | string | `""` |  |
| policies.falcoCloud.maximumJsonRequiredPluginVersion | string | `""` |  |
| policies.falcoCloud.unsupportedCloudauthPolicyTypes | string | `"okta github azure_entra guardduty"` |  |
| policies.forwardall.workerSendDelay | string | `"0s"` |  |
| policies.forwardall.workerThreads | int | `5` |  |
| policies.grpc.maxConnectionAge | string | `"1m"` |  |
| policies.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-policies-tuner-api"` |  |
| policies.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-policies-tuner-api"` |  |
| policies.ingress[0].hosts[0].paths[0].path | string | `"/api/v1/secure/policyTuner"` |  |
| policies.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[0].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[10].apiGatewayRouteName | string | `"sysdigcloud-policies-internal-falco-api"` |  |
| policies.ingress[0].hosts[0].paths[10].openshiftRouteName | string | `"sysdigcloud-policies-internal-falco-api"` |  |
| policies.ingress[0].hosts[0].paths[10].path | string | `"/api/internal/settings/falco"` |  |
| policies.ingress[0].hosts[0].paths[10].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[10].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[11].apiGatewayRouteName | string | `"sysdigcloud-policies-v4-api"` |  |
| policies.ingress[0].hosts[0].paths[11].openshiftRouteName | string | `"sysdigcloud-policies-v4-api"` |  |
| policies.ingress[0].hosts[0].paths[11].path | string | `"/secure/policies/v4/"` |  |
| policies.ingress[0].hosts[0].paths[11].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[11].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[1].path | string | `"/api/policies/v3"` |  |
| policies.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[1].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-policies-descriptors-api"` |  |
| policies.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-policies-descriptors-api"` |  |
| policies.ingress[0].hosts[0].paths[2].path | string | `"/api/v2/policyDescriptors"` |  |
| policies.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[2].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[3].apiGatewayRouteName | string | `"sysdigcloud-policies-actions-api"` |  |
| policies.ingress[0].hosts[0].paths[3].openshiftRouteName | string | `"sysdigcloud-policies-actions-api"` |  |
| policies.ingress[0].hosts[0].paths[3].path | string | `"/api/v2/policyActions"` |  |
| policies.ingress[0].hosts[0].paths[3].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[3].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[4].apiGatewayRouteName | string | `"sysdigcloud-policies-v2-api"` |  |
| policies.ingress[0].hosts[0].paths[4].openshiftRouteName | string | `"sysdigcloud-policies-v2-api"` |  |
| policies.ingress[0].hosts[0].paths[4].path | string | `"/api/v2/policies"` |  |
| policies.ingress[0].hosts[0].paths[4].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[4].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[5].apiGatewayRouteName | string | `"sysdigcloud-policies-settings-falco-api"` |  |
| policies.ingress[0].hosts[0].paths[5].openshiftRouteName | string | `"sysdigcloud-policies-settings-falco-api"` |  |
| policies.ingress[0].hosts[0].paths[5].path | string | `"/api/settings/falco"` |  |
| policies.ingress[0].hosts[0].paths[5].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[5].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[6].apiGatewayRouteName | string | `"sysdigcloud-policies-rules-api"` |  |
| policies.ingress[0].hosts[0].paths[6].openshiftRouteName | string | `"sysdigcloud-policies-rules-api"` |  |
| policies.ingress[0].hosts[0].paths[6].path | string | `"/api/secure/rules"` |  |
| policies.ingress[0].hosts[0].paths[6].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[6].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[7].apiGatewayRouteName | string | `"sysdigcloud-policies-falco-api"` |  |
| policies.ingress[0].hosts[0].paths[7].openshiftRouteName | string | `"sysdigcloud-policies-falco-api"` |  |
| policies.ingress[0].hosts[0].paths[7].path | string | `"/api/secure/falco"` |  |
| policies.ingress[0].hosts[0].paths[7].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[7].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[8].apiGatewayRouteName | string | `"sysdigcloud-secure-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[8].openshiftRouteName | string | `"sysdigcloud-secure-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[8].path | string | `"/api/secure/policies"` |  |
| policies.ingress[0].hosts[0].paths[8].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[8].servicePort | int | `9137` |  |
| policies.ingress[0].hosts[0].paths[9].apiGatewayRouteName | string | `"sysdigcloud-policies-internal-api"` |  |
| policies.ingress[0].hosts[0].paths[9].openshiftRouteName | string | `"sysdigcloud-policies-internal-api"` |  |
| policies.ingress[0].hosts[0].paths[9].path | string | `"/api/v2/internal/policies"` |  |
| policies.ingress[0].hosts[0].paths[9].serviceName | string | `"sysdigcloud-policies-api"` |  |
| policies.ingress[0].hosts[0].paths[9].servicePort | int | `9137` |  |
| policies.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| policies.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| policies.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| policies.ingress[0].labels.role | string | `"ingress-config"` |  |
| policies.ingress[0].labels.tier | string | `"infra"` |  |
| policies.ingress[0].name | string | `"sysdigcloud-policies-ingress"` |  |
| policies.janitor.cronjobSchedule | string | `"0 0 * * *"` |  |
| policies.janitor.enabled | bool | `true` |  |
| policies.listVersionsJanitor.cronjobSchedule | string | `"0 2 * * *"` |  |
| policies.listVersionsJanitor.enabled | bool | `true` |  |
| policies.listVersionsJanitor.retentionDays | int | `90` |  |
| policies.lists.v2.enabled | bool | `false` |  |
| policies.managedRules.cronjobSchedule | string | `"0 */4 * * *"` |  |
| policies.managedRules.enabled | bool | `false` |  |
| policies.manifestPath | string | `"/agent-manifest.yaml"` |  |
| policies.migration.checkStatus | string | `"false"` |  |
| policies.natsjs.enabled | bool | `false` |  |
| policies.natsjs.endpoint | string | `"nats"` |  |
| policies.policyV2Msg.perAgentEnabled | bool | `true` |  |
| policies.policyV2Msg.perAgentLockingEnabled | bool | `true` |  |
| policies.policyV2Msg.skipGenericMessage | bool | `true` |  |
| policies.policytypes.disabled[0] | string | `"machine_learning"` |  |
| policies.policytypes.disabled[1] | string | `"awscloudtrail"` |  |
| policies.policytypes.disabled[2] | string | `"okta"` |  |
| policies.policytypes.disabled[3] | string | `"github"` |  |
| policies.policytypes.disabled[4] | string | `"aws_machine_learning"` |  |
| policies.policytypes.disabled[5] | string | `"okta_machine_learning"` |  |
| policies.policytypes.disabled[6] | string | `"azure_entra"` |  |
| policies.policytypes.disabled[7] | string | `"guardduty"` |  |
| policies.policytypes.disabled[8] | string | `"awscloudtrail_stateful"` |  |
| policies.postJobEnabled | bool | `false` |  |
| policies.previewRules.cronjobSchedule | string | `"0 * * * *"` |  |
| policies.previewRules.enabled | bool | `false` |  |
| policies.previewRules.minimumAgentVersion | string | `"12.14.0"` |  |
| policies.previewRules.v2Enabled | bool | `false` |  |
| policies.proxy.defaultNoProxy | string | `"localhost,127.0.0.1,kubernetes.default.svc,*.svc.cluster.local,172.21.0.0/16,172.17.0.0/16,192.168.0.0/16"` |  |
| policies.proxy.enable | bool | `false` |  |
| policies.proxy.host | string | `"workload-egress-http-proxy.egress-proxy"` |  |
| policies.proxy.noProxy | string | `""` |  |
| policies.proxy.port | int | `3128` |  |
| policies.proxy.protocol | string | `"http"` |  |
| policies.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| policies.repositoryPrefix | string | `"secure"` |  |
| policies.requestOrigin.cronjobSchedule | string | `"0 0 * * 0"` |  |
| policies.requestOrigin.enabled | bool | `false` |  |
| policies.resources.policiesAPI.limits.cpu | float | `1.5` |  |
| policies.resources.policiesAPI.limits.memory | string | `"1Gi"` |  |
| policies.resources.policiesAPI.requests.cpu | string | `"300m"` |  |
| policies.resources.policiesAPI.requests.memory | string | `"256Mi"` |  |
| policies.resources.policiesJanitorCronJob.limits.cpu | string | `"200m"` |  |
| policies.resources.policiesJanitorCronJob.limits.memory | string | `"256Mi"` |  |
| policies.resources.policiesJanitorCronJob.requests.cpu | string | `"100m"` |  |
| policies.resources.policiesJanitorCronJob.requests.memory | string | `"128Mi"` |  |
| policies.resources.policiesListVersionsJanitorCronJob.limits.cpu | string | `"200m"` |  |
| policies.resources.policiesListVersionsJanitorCronJob.limits.memory | string | `"256Mi"` |  |
| policies.resources.policiesListVersionsJanitorCronJob.requests.cpu | string | `"100m"` |  |
| policies.resources.policiesListVersionsJanitorCronJob.requests.memory | string | `"128Mi"` |  |
| policies.resources.policiesMigrationPostJob.limits.cpu | string | `"200m"` |  |
| policies.resources.policiesMigrationPostJob.limits.memory | string | `"256Mi"` |  |
| policies.resources.policiesMigrationPostJob.requests.cpu | string | `"100m"` |  |
| policies.resources.policiesMigrationPostJob.requests.memory | string | `"128Mi"` |  |
| policies.resources.policiesRequestOriginCronJob.limits.cpu | string | `"200m"` |  |
| policies.resources.policiesRequestOriginCronJob.limits.memory | string | `"256Mi"` |  |
| policies.resources.policiesRequestOriginCronJob.requests.cpu | string | `"100m"` |  |
| policies.resources.policiesRequestOriginCronJob.requests.memory | string | `"128Mi"` |  |
| policies.resources.policiesValidationCronJob.limits.cpu | float | `1.5` |  |
| policies.resources.policiesValidationCronJob.limits.memory | string | `"1Gi"` |  |
| policies.resources.policiesValidationCronJob.requests.cpu | float | `1.5` |  |
| policies.resources.policiesValidationCronJob.requests.memory | string | `"1Gi"` |  |
| policies.resources.policiesWorker.limits.cpu | int | `1` |  |
| policies.resources.policiesWorker.limits.memory | string | `"1Gi"` |  |
| policies.resources.policiesWorker.requests.cpu | string | `"300m"` |  |
| policies.resources.policiesWorker.requests.memory | string | `"1Gi"` |  |
| policies.resources.postgresqlinit.limits.cpu | string | `"200m"` |  |
| policies.resources.postgresqlinit.limits.memory | string | `"256Mi"` |  |
| policies.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| policies.resources.postgresqlinit.requests.memory | string | `"128Mi"` |  |
| policies.rules.implicitlyAddMinimumEngineVersion.enabled | bool | `true` |  |
| policies.rules.windowsValidation | bool | `true` |  |
| policies.sentry.enabled | bool | `false` |  |
| policies.sentry.ingestUrl | string | `"ingest.us.sentry.io"` |  |
| policies.validation.cronjobSchedule | string | `"0 */12 * * *"` |  |
| policies.validation.enabled | bool | `false` |  |
| policies.workerReplicaCount | int | `1` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# postgres-ha

![Version: 0.5.17](https://img.shields.io/badge/Version-0.5.17-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.16.0](https://img.shields.io/badge/AppVersion-1.16.0-informational?style=flat-square)

## How to upgrade the zalando operator version and helm chart

### Helm chart changes

**NB**: This repo has been created before we started using the patch system for the upsteam helm charts (see minio, linkerd or neo4j)
and modifying it now will be complex. The good news is that is not necessary: we have very few lines that we changed from upstream helm chart.

### Change the upstream

run `task test:clone-upstream-operator-repository`, this will clone the upstream-operator repo and checkout the current sysdig version:

```bash
$ task test:clone-upstream-operator-repository
task: [test:clone-upstream-operator-repository] if [ ! -d 'upstream-operator' ]; then
  git clone https://github.com/zalando/postgres-operator.git -b $UPSTREAM_OPERATOR_VERSION upstream-operator
  patch -d upstream-operator/ -p1 < containers/zalando/postgres-operator/Dockerfile.patch
  patch -d upstream-operator/ -p1 < containers/zalando/postgres-operator/Makefile.patch
  make -C upstream-operator linux
fi

Cloning into 'upstream-operator'...
remote: Enumerating objects: 28783, done.
remote: Counting objects: 100% (574/574), done.
remote: Compressing objects: 100% (333/333), done.
remote: Total 28783 (delta 365), reused 395 (delta 240), pack-reused 28209
Receiving objects: 100% (28783/28783), 33.49 MiB | 35.17 MiB/s, done.
Resolving deltas: 100% (20844/20844), done.
Note: switching to '552bd26c0f8fc90feb8168ad78c732ecb23d290c'.
[...]
```

now let's go to the inside the upstream directory and let's checkout the latest upstrem version (or the one we want to use):

```bash
$ cd upstream-operator/
$ git stash
$ git checkout v1.13.0
Previous HEAD position was 552bd26c bump to v1.10.1 (#2410)
HEAD is now at cc9074c1 Bump operator to v1.13.0 (#2729)
```

(in this example we are upgrading the version from `v1.10.1` to `v1.13.0`

### Check the upstream differences

Now let's go back to the git root repo and check the differences:

```bash
vimdiff <(helm template k8s/postgres-ha/) <(helm template sysdigcloud-postgres-operator --set controllerID.create=true --set controllerID.name=sysdigcloud --set podPriorityClassName.create=false upstream-operator/charts/postgres-operator/)
```

Usually there are very few differences.

**You can safely ignore**:

* Namespace diffs

* The `app.kubernetes.io/instance` metadata.labels label

* The exporter configmap with additional queries that is present only on our own version

* Image diffs, we have our own images and naming convention

* In `OperatorConfiguration`:
    * `super_username` must be `root` due to historical reasons around anchore (the `postgres` user with `anchore` db will be created by the init job)
    * `pod_service_account_definition` we need it like that since we need to pass the imagepullpolicy to the postgres sts that will be created by the operator
    * `spilo_allow_privilege_escalation` it must be `false` for security reasons.
    * `watched_namespace`: must be the sysdig one (set in the values)
    * `default_*_request/limits`

* the `sysdigcloud-postgres-cluster` `postgresql` crd resource unless there are any breaking changes for that

**You should instead pay attention to**:

* Any verbs update in cluster/role that needs to be adjusted from upstream to our version

* Any other change in `OperatorConfiguration`

* Check the release note and see if there is any breaking change or change of logic

* The `helm.sh/chart` label needs to be updated to the target upstream version

Make all the changes we need in [k8s](./templates/)

### Update the CRDs

Based on the new upstream version (in this case 1.13.0) let's copy the 3 crds from the [`crds`](https://github.com/zalando/postgres-operator/tree/v1.13.0/charts/postgres-operator/crds) directory from zalando chart into our own [`crds`](./crds/) directory.

Be aware that for "installer reasons" all the crds manifests filename needs to have the `crd` suffix, so let's rename the downloaded crds:

```bash
mv operatorconfigurations.yaml operatorconfigurations-crd.yaml
mv postgresqls.yaml postgresqls-crd.yaml
mv postgresteams.yaml postgresteams-crd.yaml
```

### Helm lint

Try to run an helm lint to avoid any mistake/typo:

```bash
$helm lint k8s/postgres-ha
==> Linting k8s/postgres-ha
[INFO] Chart.yaml: icon is recommended

1 chart(s) linted, 0 chart(s) failed
```

### Move the operator build to the new upstream version

- In test [taskfile](./../../tests/Taskfile.yml) change the `UPSTREAM_OPERATOR_VERSION` to the new upstream version, for instance:

```bash
env:
  UPSTREAM_SPILO_VERSION: 3.0-p1
  UPSTREAM_OPERATOR_VERSION: v1.13.0
```

- It may be necessary to revisit the dockerfile or make patch if the upstream repo made complex change to those files. To double check that remove the `upstream-operator` directory and run

```bash
$ rm -rf upstream-operator/
$ task test:clone-upstream-operator-repository
task: [test:clone-upstream-operator-repository] if [ ! -d 'upstream-operator' ]; then
  git clone https://github.com/zalando/postgres-operator.git -b $UPSTREAM_OPERATOR_VERSION upstream-operator
  patch -d upstream-operator/ -p1 < containers/zalando/postgres-operator/Dockerfile.patch
  patch -d upstream-operator/ -p1 < containers/zalando/postgres-operator/Makefile.patch
  make -C upstream-operator linux
fi

Cloning into 'upstream-operator'...
remote: Enumerating objects: 28813, done.
remote: Counting objects: 100% (610/610), done.
remote: Compressing objects: 100% (419/419), done.
remote: Total 28813 (delta 381), reused 323 (delta 189), pack-reused 28203 (from 1)
Receiving objects: 100% (28813/28813), 33.71 MiB | 22.43 MiB/s, done.
Resolving deltas: 100% (20863/20863), done.
Note: switching to 'cc9074c18403d41594878518a3751971e65640ab'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by switching back to a branch.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -c with the switch command. Example:

  git switch -c <new-branch-name>

Or undo this operation with:

  git switch -

Turn off this advice by setting config variable advice.detachedHead to false

patching file docker/Dockerfile
patching file Makefile
make: Entering directory '/home/player1/repo/infra-datastore-postgres-ha/upstream-operator'
GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o docker/postgres-operator -v -ldflags "-X=main.version=v1.13.0-dirty" cmd/main.go
make: Leaving directory '/home/player1/repo/infra-datastore-postgres-ha/upstream-operator'
```

If you see these 2 patching lines without any issue:

```bash
patching file docker/Dockerfile
patching file Makefile
```

means that we don't need to modify the operator patches. If instead you got any error you need to change the [Dockerfile](../../containers/zalando/postgres-operator/Dockerfile.patch) or the [Makefile](../../containers/zalando/postgres-operator/Makefile.patch) one similar on what we did for the helm chart part.

- Change the golang version in github actions workflows files if it's necessary due to a go bump in the upstream new version

### Modify the upgrade test

In the zalando bats upgrade [scenario](../../tests/scenarios/zalando/1-helm-operator-upgrade.bats) we need to modify the `0.1 UPGRADE TEST` test by changing the helm install values with the latest sysdig chart and containers version before the our target upgrade.

### Run tests

Now you can run the bats tests locally or via github actions and check if everything is working correctly. To run everything local you can:

```bash
task test:zalando
```

and check the output

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.airgappedRegistryName | string | `"quay.io"` |  |
| global.airgappedRepositoryPrefix | string | `"sysdig"` |  |
| global.apps | string | `"monitor secure"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.deployment | string | `"kubernetes"` |  |
| global.helmDeploy | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.postgresImageName | string | `"postgres-15"` |  |
| global.postgresVersion | string | `"0.1.5"` |  |
| global.postgresql.ha.enabled | bool | `true` |  |
| global.postgresql.ha.networkPolicy.enabled | bool | `false` |  |
| global.postgresql.ha.networkPolicy.ingresses | list | `[]` |  |
| global.postgresql.ha.replicas | int | `3` |  |
| global.postgresql.ha.tls.enabled | bool | `false` |  |
| global.postgresql.ha.tls.secretAnnotations | object | `{}` |  |
| global.storageClassName | string | `"sysdig"` |  |
| global.storageClassProvisioner | string | `""` |  |
| postgresql.aws.awsAccessKeyID | string | `""` |  |
| postgresql.aws.awsSecretAccessKey | string | `""` |  |
| postgresql.aws.deploymentEnvironment | string | `""` |  |
| postgresql.aws.incrementalBackupS3Bucket | string | `""` |  |
| postgresql.aws.incrementalBackupS3Region | string | `"us-east-1"` |  |
| postgresql.aws.logicalBackupPath | string | `""` |  |
| postgresql.aws.logicalBackupProvider | string | `""` |  |
| postgresql.aws.logicalBackupS3Bucket | string | `""` |  |
| postgresql.aws.logicalBackupS3Region | string | `""` |  |
| postgresql.aws.logicalBackupS3RetentionTime | string | `""` |  |
| postgresql.backups.enabled | bool | `false` |  |
| postgresql.backups.imagePullSecret | string | `"sysdigcloud-pull-secret"` |  |
| postgresql.backups.incrementalBackup.enabled | bool | `false` |  |
| postgresql.backups.incrementalBackup.retentionDays | int | `30` |  |
| postgresql.backups.incrementalBackup.schedule | string | `"00 01 * * *"` |  |
| postgresql.backups.pointInTimeRecovery.timestamp | string | `"2023-10-24T12:40:33+01:00"` |  |
| postgresql.backups.pointInTimeRecovery.uid | string | `"e7f87600-e1ef-4f2d-81c8-85cfb05f966f"` |  |
| postgresql.backups.schedule | string | `"* */6 * * *"` |  |
| postgresql.backups.version | string | `"0.4.2"` |  |
| postgresql.external | bool | `false` |  |
| postgresql.ha.checkCRD | bool | `true` |  |
| postgresql.ha.customTls.caSecretName | string | `""` |  |
| postgresql.ha.customTls.crtSecretName | string | `""` |  |
| postgresql.ha.customTls.enabled | bool | `false` |  |
| postgresql.ha.enableExporter | bool | `true` |  |
| postgresql.ha.exporterVersion | string | `"v0.11.11-ubi"` |  |
| postgresql.ha.operatorVersion | string | `"0.4.2"` |  |
| postgresql.ha.pgMajorVersion | int | `15` |  |
| postgresql.ha.spiloVersion | string | `"0.3.5"` |  |
| postgresql.patroni.initdb.auth-host | string | `"scram-sha-256"` |  |
| postgresql.patroni.initdb.auth-local | string | `"trust"` |  |
| postgresql.patroni.pg_hba[0] | string | `"local   all,replication             all                                     trust"` |  |
| postgresql.patroni.pg_hba[10] | string | `"host    replication                 all             ::/0                    scram-sha-256"` |  |
| postgresql.patroni.pg_hba[1] | string | `"local   all,replication             all                                     md5"` |  |
| postgresql.patroni.pg_hba[2] | string | `"local   all,replication             all                                     scram-sha-256"` |  |
| postgresql.patroni.pg_hba[3] | string | `"host    all                         all             0.0.0.0/0               md5"` |  |
| postgresql.patroni.pg_hba[4] | string | `"host    all                         all             0.0.0.0/0               scram-sha-256"` |  |
| postgresql.patroni.pg_hba[5] | string | `"host    all                         all             ::/0                    md5"` |  |
| postgresql.patroni.pg_hba[6] | string | `"host    all                         all             ::/0                    scram-sha-256"` |  |
| postgresql.patroni.pg_hba[7] | string | `"host    replication                 all             0.0.0.0/0               md5"` |  |
| postgresql.patroni.pg_hba[8] | string | `"host    replication                 all             0.0.0.0/0               scram-sha-256"` |  |
| postgresql.patroni.pg_hba[9] | string | `"host    replication                 all             ::/0                    md5"` |  |
| postgresql.pgParameters.max_connections | string | `"1024"` |  |
| postgresql.pvStorageSize.medium.postgresql | string | `"6Gi"` |  |
| postgresql.reEncryptPasswords | bool | `false` |  |
| postgresql.resources.postgresql.limits.cpu | int | `4` |  |
| postgresql.resources.postgresql.limits.memory | string | `"4Gi"` |  |
| postgresql.resources.postgresql.requests.cpu | int | `1` |  |
| postgresql.resources.postgresql.requests.memory | string | `"1Gi"` |  |
| postgresql.size | string | `"medium"` |  |

# pgdumppostgresql-dump-job

![Version: 0.0.1](https://img.shields.io/badge/Version-0.0.1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

the Sysdig PostgreSQL Datastore helm chart

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor"` |  |
| global.namespace | string | `"7fd048f-123"` |  |
| global.postgresImageName | string | `"postgres-15"` |  |
| global.postgresVersion | string | `"0.0.4"` |  |
| global.secure.db.password | string | `"sysdigpa$$"` |  |
| postgresql.external | bool | `false` |  |
| postgresql.ha.enabled | bool | `false` |  |
| postgresql.hostName | string | `"sysdigcloud-postgresql"` |  |
| postgresql.pgParameters.max_connections | string | `"512"` |  |
| postgresql.pgParameters.shared_buffers | string | `"110MB"` |  |
| postgresql.preUpgradeJob.enabled | bool | `true` |  |
| postgresql.preUpgradeJob.name | string | `"sysdigcloud-postgresql-pre-upgrade-backup-job"` |  |
| postgresql.pvStorageSize.medium.postgresql | string | `"60Gi"` |  |
| postgresql.resources.postgresql.limits.cpu | int | `4` |  |
| postgresql.resources.postgresql.limits.memory | string | `"4Gi"` |  |
| postgresql.resources.postgresql.requests.cpu | int | `1` |  |
| postgresql.resources.postgresql.requests.memory | string | `"1Gi"` |  |
| postgresql.rootDb | string | `"anchore"` |  |
| postgresql.rootUser | string | `"postgres"` |  |
| postgresql.size | string | `"medium"` |  |
| postgresql.storageClassName | string | `"standard"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.11.3](https://github.com/norwoodj/helm-docs/releases/v1.11.3)

# postgresql

![Version: 0.1.9](https://img.shields.io/badge/Version-0.1.9-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

the Sysdig PostgreSQL Datastore helm chart

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.postgresImageName | string | `"postgres-15"` |  |
| global.postgresMigrationImageName | string | `"onprem_migration"` |  |
| global.postgresVersion | string | `"0.1.4"` |  |
| global.secure.db.password | string | `"sysdigpa$$"` |  |
| postgresql.external | bool | `false` |  |
| postgresql.ha.enabled | bool | `false` |  |
| postgresql.pgParameters.max_connections | string | `"512"` |  |
| postgresql.pgParameters.max_wal_size | string | `"8GB"` |  |
| postgresql.pgParameters.shared_buffers | string | `"110MB"` |  |
| postgresql.pgParameters.wal_compression | string | `"lz4"` |  |
| postgresql.pgsqlBackups.aws.awsAccessKeyID | string | `""` |  |
| postgresql.pgsqlBackups.aws.awsSecretAccessKey | string | `""` |  |
| postgresql.pgsqlBackups.aws.deploymentEnvironment | string | `""` |  |
| postgresql.pgsqlBackups.aws.incrementalBackupS3Bucket | string | `""` |  |
| postgresql.pgsqlBackups.aws.incrementalBackupS3Region | string | `"us-east-1"` |  |
| postgresql.pgsqlBackups.aws.logicalBackupPath | string | `""` |  |
| postgresql.pgsqlBackups.aws.logicalBackupProvider | string | `""` |  |
| postgresql.pgsqlBackups.aws.logicalBackupS3Bucket | string | `""` |  |
| postgresql.pgsqlBackups.aws.logicalBackupS3Region | string | `""` |  |
| postgresql.pgsqlBackups.aws.logicalBackupS3RetentionTime | string | `""` |  |
| postgresql.pgsqlBackups.enabled | bool | `false` |  |
| postgresql.pgsqlBackups.imagePullSecret | string | `"sysdigcloud-pull-secret"` |  |
| postgresql.pgsqlBackups.schedule | string | `"0 */6 * * *"` |  |
| postgresql.pgsqlBackups.version | string | `"0.1.3"` |  |
| postgresql.pvStorageSize.medium.postgresql | string | `"60Gi"` |  |
| postgresql.reEncryptPasswords | bool | `false` |  |
| postgresql.resources.postgresql.limits.cpu | int | `4` |  |
| postgresql.resources.postgresql.limits.memory | string | `"4Gi"` |  |
| postgresql.resources.postgresql.requests.cpu | int | `1` |  |
| postgresql.resources.postgresql.requests.memory | string | `"1Gi"` |  |
| postgresql.resources.postgresqlinit.limits.cpu | string | `"300m"` |  |
| postgresql.resources.postgresqlinit.limits.memory | string | `"200Mi"` |  |
| postgresql.resources.postgresqlinit.requests.cpu | string | `"50m"` |  |
| postgresql.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| postgresql.resources.postgresqlupgradeinit.limits.cpu | int | `4` |  |
| postgresql.resources.postgresqlupgradeinit.limits.memory | string | `"4Gi"` |  |
| postgresql.resources.postgresqlupgradeinit.requests.cpu | int | `1` |  |
| postgresql.resources.postgresqlupgradeinit.requests.memory | string | `"1Gi"` |  |
| postgresql.rootDb | string | `"anchore"` |  |
| postgresql.rootUser | string | `"postgres"` |  |
| postgresql.size | string | `"medium"` |  |
| postgresql.storageClassName | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# process-tree

![Version: 1.2.1-260303141055-main-vdaba289](https://img.shields.io/badge/Version-1.2.1--260303141055--main--vdaba289-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Runtime Security

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.processTree.serviceToken | string | `""` |  |
| global.apps | string | `"secure"` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","hostname":"sysdigcloud-elasticsearch","port":9200,"scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.secure.events.tiers.default | string | `"basic"` |  |
| global.secure.events.tiers.definitions[0].defaultRetention | int | `90` |  |
| global.secure.events.tiers.definitions[0].name | string | `"basic"` |  |
| global.secure.events.tiers.definitions[0].retentionDays.admissionController | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.auditTrail | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.awsMlConsoleLogin | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.benchmarks | int | `366` |  |
| global.secure.events.tiers.definitions[0].retentionDays.cloudsec | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.cloudtrail | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.compliance | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.github | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.hostScanning | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.okta | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.policies | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.profilingDetection | int | `90` |  |
| global.secure.events.tiers.definitions[0].retentionDays.scanning | int | `90` |  |
| global.secure.events.tiers.definitions[1].defaultRetention | int | `366` |  |
| global.secure.events.tiers.definitions[1].name | string | `"yearly"` |  |
| global.secure.events.tiers.definitions[1].retentionDays.admissionController | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.auditTrail | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.awsMlConsoleLogin | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.benchmarks | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.cloudsec | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.cloudtrail | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.compliance | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.github | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.hostScanning | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.okta | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.policies | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.profilingDetection | int | `366` |  |
| global.secure.events.tiers.definitions[1].retentionDays.scanning | int | `366` |  |
| processTree.aaEndpoint | string | `"http://sysdigcloud-activity-audit-api:7000"` |  |
| processTree.apiReplicaCount | int | `2` |  |
| processTree.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| processTree.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| processTree.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| processTree.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| processTree.enabled | bool | `true` |  |
| processTree.gathererReplicaCount | int | `2` |  |
| processTree.grpc | object | `{"port":9000}` | gRPC server configuration |
| processTree.grpc.port | int | `9000` | port for the gRPC server |
| processTree.ingestion.runtime.enabled | bool | `true` |  |
| processTree.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-process-tree-api"` |  |
| processTree.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-process-tree-api"` |  |
| processTree.ingress[0].hosts[0].paths[0].path | string | `"/api/process-tree/v1"` |  |
| processTree.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-process-tree-api"` |  |
| processTree.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| processTree.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| processTree.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| processTree.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| processTree.ingress[0].labels.role | string | `"ingress-config"` |  |
| processTree.ingress[0].labels.tier | string | `"infra"` |  |
| processTree.ingress[0].name | string | `"sysdigcloud-process-tree-ingress"` |  |
| processTree.janitor.schedule | string | `"30 3 * * *"` |  |
| processTree.natsjs.runtime.policy.durable | string | `"process-tree-gatherer"` |  |
| processTree.natsjs.runtime.policy.name | string | `"runtime-policy-events"` |  |
| processTree.natsjs.runtime.policy.queue | string | `"process-tree-gatherer"` |  |
| processTree.natsjs.runtime.policy.streamname | string | `"events"` |  |
| processTree.natsjs.runtime.policy.subject | string | `"events.source.events.policy.policies"` |  |
| processTree.natsjs.tls.enabled | bool | `true` |  |
| processTree.natsjs.url | string | `"nats"` |  |
| processTree.natsjs.workersPoolSize | int | `8` |  |
| processTree.opensearch | object | `{"nodeDiscovery":true,"nodeDiscoveryInterval":"10m","password":null}` | configuration for the opensearch instance |
| processTree.opensearch.password | string | `nil` | password of the opensearch instance, if set we will refer to opensearch instance instead of looking up for the elasticsearch chart managed secrets. |
| processTree.osWriteEnable | bool | `true` |  |
| processTree.proxy.defaultNoProxy | string | `"localhost,127.0.0.1,kubernetes.default.svc,*.svc.cluster.local,172.21.0.0/16,172.17.0.0/16,192.168.0.0/16"` |  |
| processTree.proxy.enable | bool | `false` |  |
| processTree.proxy.host | string | `"workload-egress-http-proxy.egress-proxy"` |  |
| processTree.proxy.noProxy | string | `""` |  |
| processTree.proxy.port | int | `3128` |  |
| processTree.proxy.protocol | string | `"http"` |  |
| processTree.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| processTree.repositoryPrefix | string | `"secure"` |  |
| processTree.resources.processTreeAPI.limits.cpu | int | `4` |  |
| processTree.resources.processTreeAPI.limits.memory | string | `"2Gi"` |  |
| processTree.resources.processTreeAPI.requests.cpu | int | `2` |  |
| processTree.resources.processTreeAPI.requests.memory | string | `"1Gi"` |  |
| processTree.resources.processTreeGatherer.limits.cpu | int | `4` |  |
| processTree.resources.processTreeGatherer.limits.memory | string | `"2Gi"` |  |
| processTree.resources.processTreeGatherer.requests.cpu | int | `2` |  |
| processTree.resources.processTreeGatherer.requests.memory | string | `"1Gi"` |  |
| processTree.resources.processTreeJanitor.limits.cpu | string | `"250m"` |  |
| processTree.resources.processTreeJanitor.limits.memory | string | `"250Mi"` |  |
| processTree.resources.processTreeJanitor.requests.cpu | string | `"250m"` |  |
| processTree.resources.processTreeJanitor.requests.memory | string | `"250Mi"` |  |
| processTree.sdauthCacheTTL | string | `"5m"` |  |
| processTree.serviceAccountName | string | `"sysdig"` |  |
| processTree.skippedLabels | string | `""` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# profiling

![Version: 5.3.0-250526141242-main-vfe39ed3](https://img.shields.io/badge/Version-5.3.0--250526141242--main--vfe39ed3-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Profiling

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.kubernetesServerVersion | string | `"1.18.1"` |  |
| global.legacyPostgres.postgresDatabases.profiling.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.profiling.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.profiling.adminusername | string | `"root"` |  |
| global.legacyPostgres.postgresDatabases.profiling.db | string | `"profiling_db"` |  |
| global.legacyPostgres.postgresDatabases.profiling.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.profiling.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.profiling.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.profiling.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.profiling.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.profiling.username | string | `"profiling_user"` |  |
| global.legacyRedis.redisClientsSecure.profiling.endpoint | string | `""` |  |
| global.legacyRedis.redisClientsSecure.profiling.port | int | `6379` |  |
| global.legacyRedis.redisClientsSecure.profiling.sentinel.enabled | bool | `false` |  |
| global.legacyRedis.redisClientsSecure.profiling.tls | bool | `false` |  |
| global.legacyRedis.redisClientsSecure.profiling.user | string | `""` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| profiling.allowAllCustomer | bool | `false` |  |
| profiling.collector.ackWait | string | `"60s"` |  |
| profiling.collector.disabled | bool | `false` |  |
| profiling.collector.dlqHandleDelay | string | `"30s"` |  |
| profiling.collector.dlqSubjectPrefix | string | `"profiling.dlq"` |  |
| profiling.collector.durable | string | `"profiling-worker"` |  |
| profiling.collector.maxInFlight | int | `10000` |  |
| profiling.collector.name | string | `"profiling-collector-1"` |  |
| profiling.collector.queue | string | `"profiling-worker"` |  |
| profiling.collector.streamName | string | `"collector-fingerprints-1"` |  |
| profiling.collector.subject | string | `"collector.fingerprints.>"` |  |
| profiling.enabled | bool | `true` |  |
| profiling.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-profiling-api"` |  |
| profiling.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-profiling-api"` |  |
| profiling.ingress[0].hosts[0].paths[0].path | string | `"/api/v1/profiling"` |  |
| profiling.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-profiling-api"` |  |
| profiling.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| profiling.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| profiling.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| profiling.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| profiling.ingress[0].labels.role | string | `"ingress-config"` |  |
| profiling.ingress[0].labels.tier | string | `"infra"` |  |
| profiling.ingress[0].name | string | `"sysdigcloud-profiling-ingress"` |  |
| profiling.janitor.cronjob | string | `"@daily"` |  |
| profiling.janitor.dryRun | bool | `false` |  |
| profiling.janitor.durationLimit | string | `"720h"` |  |
| profiling.janitor.learningDurationLimit | string | `"168h"` |  |
| profiling.janitor.maxAttempts | int | `3` |  |
| profiling.mde.ackWait | string | `"30s"` |  |
| profiling.mde.disabled | bool | `true` |  |
| profiling.mde.dlqHandleDelay | string | `"30s"` |  |
| profiling.mde.dlqSubjectPrefix | string | `"fingerprints.files.dlq"` |  |
| profiling.mde.durable | string | `"fingerprints-files"` |  |
| profiling.mde.maxInFlight | int | `10000` |  |
| profiling.mde.name | string | `"metadata-enricher-fingerprints-1"` |  |
| profiling.mde.queue | string | `"fingerprints-files"` |  |
| profiling.mde.streamName | string | `"metadata-enricher-fingerprints-1"` |  |
| profiling.mde.subject | string | `"metadataenricher.fingerprints.1.>"` |  |
| profiling.mds.alwaysEnrich | bool | `false` |  |
| profiling.mds.cacheSize | string | `"104857600"` |  |
| profiling.mds.cacheTTL | string | `"1h"` |  |
| profiling.mds.enabled | bool | `true` |  |
| profiling.mds.endpoint | string | `"sysdigcloud-metadata-service-server:5300"` |  |
| profiling.mds.meerkatEnabled | bool | `true` |  |
| profiling.profilingApiReplicaCount | int | `1` |  |
| profiling.profilingWorkerReplicaCount | int | `1` |  |
| profiling.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| profiling.repositoryPrefix | string | `"secure"` |  |
| profiling.resources.profilingApi.limits.cpu | int | `1` |  |
| profiling.resources.profilingApi.limits.memory | string | `"400Mi"` |  |
| profiling.resources.profilingApi.requests.cpu | int | `1` |  |
| profiling.resources.profilingApi.requests.memory | string | `"100Mi"` |  |
| profiling.resources.profilingJanitor.limits.cpu | int | `1` |  |
| profiling.resources.profilingJanitor.limits.memory | string | `"500Mi"` |  |
| profiling.resources.profilingJanitor.requests.cpu | int | `1` |  |
| profiling.resources.profilingJanitor.requests.memory | string | `"100Mi"` |  |
| profiling.resources.profilingPreJob.limits.cpu | string | `"500m"` |  |
| profiling.resources.profilingPreJob.limits.memory | string | `"150Mi"` |  |
| profiling.resources.profilingPreJob.requests.cpu | string | `"100m"` |  |
| profiling.resources.profilingPreJob.requests.memory | string | `"100Mi"` |  |
| profiling.resources.profilingWorker.limits.cpu | int | `1` |  |
| profiling.resources.profilingWorker.limits.memory | string | `"500Mi"` |  |
| profiling.resources.profilingWorker.requests.cpu | int | `1` |  |
| profiling.resources.profilingWorker.requests.memory | string | `"100Mi"` |  |
| profiling.serviceAccountName | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# promchap

![Version: 1.19.0-main.2026-03-10T10-46-07Z.3f1b68e](https://img.shields.io/badge/Version-1.19.0--main.2026--03--10T10--46--07Z.3f1b68e-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Promchap query service for Sysdig

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.common.endpoint | string | `""` |  |
| global.legacyRedis.redisClientsMonitor.common.port | int | `6379` |  |
| global.legacyRedis.redisClientsMonitor.common.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.enabled | bool | `false` |  |
| global.legacyRedis.redisTls.sentinel.masterSet | string | `"primary"` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.tls | bool | `true` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.prometheus.enabled | bool | `true` |  |
| promchap.auth.cacheIdentityTTL | string | `"1m"` |  |
| promchap.auth.cachePermissionsTTL | string | `"5m"` |  |
| promchap.auth.cacheTeamSettingsTTL | string | `"5m"` |  |
| promchap.auth.maxRetries | int | `3` |  |
| promchap.cacheResults | bool | `true` |  |
| promchap.clickhouse.addresses[0] | string | `"clickhouse-monitor-shards:8443"` |  |
| promchap.clickhouse.batchSize | int | `100` |  |
| promchap.clickhouse.channelBufferSize | int | `10000` |  |
| promchap.clickhouse.database | string | `"sysdig"` |  |
| promchap.clickhouse.debug | bool | `false` |  |
| promchap.clickhouse.enabled | bool | `false` |  |
| promchap.clickhouse.flushTimeout | string | `"5s"` |  |
| promchap.clickhouse.maxIdleConns | int | `5` |  |
| promchap.clickhouse.maxOpenConns | int | `10` |  |
| promchap.clickhouse.region | string | `"dev"` |  |
| promchap.clickhouse.retryBatchesPerInterval | int | `10` |  |
| promchap.clickhouse.retryBufferSize | int | `100` |  |
| promchap.clickhouse.tls.enabled | bool | `true` |  |
| promchap.clickhouse.tls.insecureSkipVerify | bool | `true` |  |
| promchap.clickhouse.username | string | `"writer"` |  |
| promchap.downstreamResponseCompression | bool | `false` |  |
| promchap.dynCacheFreshness | bool | `false` |  |
| promchap.enabled | bool | `true` |  |
| promchap.env.GOGC | string | `"50"` |  |
| promchap.excludeBoolBinExprFromLimiting | bool | `false` |  |
| promchap.fifocache_enabled | bool | `false` |  |
| promchap.fifocache_size | int | `0` |  |
| promchap.ingressNetworking | string | `"hostnetwork"` | redis definition for promchap for lookup function |
| promchap.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-prometheus-rules"` |  |
| promchap.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-prometheus-rules"` |  |
| promchap.ingress[0].hosts[0].paths[0].path | string | `"/prometheus/api/v1/rules"` |  |
| promchap.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-api"` |  |
| promchap.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| promchap.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-prometheus-alerts"` |  |
| promchap.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-prometheus-alerts"` |  |
| promchap.ingress[0].hosts[0].paths[1].path | string | `"/prometheus/api/v1/alerts"` |  |
| promchap.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-api"` |  |
| promchap.ingress[0].hosts[0].paths[1].servicePort | int | `8080` |  |
| promchap.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-prometheus-api"` |  |
| promchap.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-prometheus-api"` |  |
| promchap.ingress[0].hosts[0].paths[2].openshiftTargetPort | int | `9090` |  |
| promchap.ingress[0].hosts[0].paths[2].path | string | `"/prometheus/api"` |  |
| promchap.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-promchap"` |  |
| promchap.ingress[0].hosts[0].paths[2].servicePort | int | `80` |  |
| promchap.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| promchap.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| promchap.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| promchap.ingress[0].labels.role | string | `"ingress-config"` |  |
| promchap.ingress[0].labels.tier | string | `"infra"` |  |
| promchap.ingress[0].name | string | `"sysdigcloud-promchap"` |  |
| promchap.logFormat | string | `"json"` |  |
| promchap.maxCacheFreshness | string | `"6m"` |  |
| promchap.nonAggregatedQueryTsLimit | int | `0` |  |
| promchap.queryInfo.maxRetries | int | `1` |  |
| promchap.queryIssuer | string | `"customer"` |  |
| promchap.redis.promchap.name | string | `"promchap"` |  |
| promchap.redis.promchap.redisCaCrtMountPath | string | `"/opt/kubernetes_secrets/redis_certs"` |  |
| promchap.redis.promchap.redisCaPath | string | `"/opt/kubernetes_secrets/redis_certs/ca.crt"` |  |
| promchap.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| promchap.rejectQueryDryRun | bool | `true` |  |
| promchap.rejectQueryOnlyExternal | bool | `true` |  |
| promchap.rejectQueryTsLimit | int | `0` |  |
| promchap.replicaCount | int | `1` |  |
| promchap.repositoryPrefix | string | `"monitor"` |  |
| promchap.resources.promchap.limits.cpu | string | `"1"` |  |
| promchap.resources.promchap.limits.memory | string | `"1Gi"` |  |
| promchap.resources.promchap.requests.cpu | string | `"250m"` |  |
| promchap.resources.promchap.requests.memory | string | `"300Mi"` |  |
| promchap.serviceAccountName | string | `"sysdig"` |  |
| promchap.splitQueriesByInterval10 | string | `"4h"` |  |
| promchap.splitQueriesByInterval3600 | string | `"192h"` |  |
| promchap.splitQueriesByInterval60 | string | `"12h"` |  |
| promchap.splitQueriesByInterval600 | string | `"48h"` |  |
| promchap.splitQueriesByInterval86400 | string | `"720h"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# promqlator

![Version: 3.3.1-main.2026-03-09T08-54-55Z.v7a55ef7](https://img.shields.io/badge/Version-3.3.1--main.2026--03--09T08--54--55Z.v7a55ef7-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Prometheus service for Sysdig

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.prometheus.enabled | bool | `true` |  |
| promqlator.enableNetworkPolicy | bool | `false` |  |
| promqlator.enabled | bool | `true` |  |
| promqlator.engineConfig.parallelSelectsEnabled | bool | `true` |  |
| promqlator.engineConfig.parallelSelectsMaxConcurrent | int | `4` |  |
| promqlator.engineConfig.valueFilteringPushdownEnabled | bool | `false` |  |
| promqlator.features.labelInterning | bool | `false` |  |
| promqlator.features.labelInterningOnGrouping | bool | `false` |  |
| promqlator.features.labelTransferOptimization | bool | `false` |  |
| promqlator.maxWebConnections | string | `nil` |  |
| promqlator.meerkatResponseSizeLimit | string | `"5Gi"` |  |
| promqlator.prometheusReplicaCount | int | `0` |  |
| promqlator.queryMaxConcurrency | string | `nil` |  |
| promqlator.querySemaphore.enabled | bool | `false` |  |
| promqlator.querySemaphore.maxConcurrencyRatio | float | `0.5` |  |
| promqlator.querySemaphore.timeout | string | `"1m"` |  |
| promqlator.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| promqlator.replicaCount | int | `1` |  |
| promqlator.repositoryPrefix | string | `"monitor"` |  |
| promqlator.resources.promqlator.limits.cpu | string | `"2"` |  |
| promqlator.resources.promqlator.limits.memory | string | `"8Gi"` |  |
| promqlator.resources.promqlator.requests.cpu | string | `"500m"` |  |
| promqlator.resources.promqlator.requests.memory | string | `"1Gi"` |  |
| promqlator.slowQueryThreshold | string | `"5s"` |  |
| promqlator.zoneAwareRouting.enabled | bool | `false` |  |
| promqlator.zoneAwareRouting.minimumAddressesInZone | int | `1` |  |
| promqlator.zoneAwareRouting.minimumAddressesInZonePercentage | int | `25` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# prws-internal-ingestion

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

PRWS Internal Ingestion Application

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.promRemoteWrite.serviceToken | string | `nil` |  |
| global.apps | string | `"monitor"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.kafka.broker.externalPort | int | `9093` |  |
| global.kafka.name | string | `"cp-kafka"` |  |
| global.kafka.namespace | string | `"sysdigcloud"` |  |
| global.kafka.secure.enabled | bool | `false` |  |
| global.kafka.secure.useCertManager | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.prwsInternalIngestion.admindb | string | `"sysdig"` |  |
| global.legacyPostgres.postgresDatabases.prwsInternalIngestion.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.prwsInternalIngestion.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.prwsInternalIngestion.db | string | `"prws_internal_ingestion"` |  |
| global.legacyPostgres.postgresDatabases.prwsInternalIngestion.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.prwsInternalIngestion.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.prwsInternalIngestion.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.prwsInternalIngestion.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.prwsInternalIngestion.username | string | `"prws_internal_ingestion_user"` |  |
| global.legacyRedis.redisClientsMonitor.cache.tls | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.common.tls | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.ibmCache.tls | bool | `false` |  |
| global.legacyRedis.redisClientsMonitor.prws.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.secretsManagement.generate | bool | `true` |  |
| prwsInternalIngestion.enabled | bool | `true` |  |
| prwsInternalIngestion.hpa.enabled | bool | `false` |  |
| prwsInternalIngestion.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-prws-internal-ingestion"` |  |
| prwsInternalIngestion.ingress[0].hosts[0].paths[0].apiGatewayStickySession | bool | `false` |  |
| prwsInternalIngestion.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-prws-internal-ingestion"` |  |
| prwsInternalIngestion.ingress[0].hosts[0].paths[0].path | string | `"/api/admin/inject"` |  |
| prwsInternalIngestion.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-prws-internal-ingestion"` |  |
| prwsInternalIngestion.ingress[0].hosts[0].paths[0].servicePort | int | `9510` |  |
| prwsInternalIngestion.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| prwsInternalIngestion.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| prwsInternalIngestion.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| prwsInternalIngestion.ingress[0].labels.role | string | `"ingress-config"` |  |
| prwsInternalIngestion.ingress[0].labels.tier | string | `"infra"` |  |
| prwsInternalIngestion.ingress[0].name | string | `"sysdigcloud-prws-internal-ingestion"` |  |
| prwsInternalIngestion.jvmOptions | string | `"-Xmx8G"` |  |
| prwsInternalIngestion.privateEndpointCommunicationEnforcement | bool | `false` |  |
| prwsInternalIngestion.redis.timeout | int | `10000` |  |
| prwsInternalIngestion.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| prwsInternalIngestion.replicaCount | int | `1` |  |
| prwsInternalIngestion.repositoryPrefix | string | `"monitor"` |  |
| prwsInternalIngestion.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| prwsInternalIngestion.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| prwsInternalIngestion.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| prwsInternalIngestion.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| prwsInternalIngestion.resources.prwsInternalIngestion.limits.cpu | string | `"2"` |  |
| prwsInternalIngestion.resources.prwsInternalIngestion.limits.memory | string | `"8Gi"` |  |
| prwsInternalIngestion.resources.prwsInternalIngestion.requests.cpu | string | `"1"` |  |
| prwsInternalIngestion.resources.prwsInternalIngestion.requests.memory | string | `"3Gi"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# rapid-response

![Version: 5.3.0-260309105845-main-vc673dd2](https://img.shields.io/badge/Version-5.3.0--260309105845--main--vc673dd2-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Rapid Response

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.rapidResponse.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.rapidResponse.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.rapidResponse.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.rapidResponse.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.rapidResponse.db | string | `"rapid_response_db"` |  |
| global.legacyPostgres.postgresDatabases.rapidResponse.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.rapidResponse.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.rapidResponse.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.rapidResponse.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.rapidResponse.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.rapidResponse.username | string | `"rapidresponse_user"` |  |
| global.legacyRedis.redisClientsSecure.rapidResponse.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| rapidResponse.approvalEmailTemplate | string | `"rapid-response-3fa"` |  |
| rapidResponse.approvalQuorum | int | `0` |  |
| rapidResponse.approvalSecondsTimeout | int | `300` |  |
| rapidResponse.approvalSingleDeny | bool | `true` |  |
| rapidResponse.audit.enabled | bool | `true` |  |
| rapidResponse.authorizationService.enabled | bool | `false` |  |
| rapidResponse.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| rapidResponse.enabled | bool | `true` |  |
| rapidResponse.featureFlags.remoteStorageEnabledCustomers | string | `""` |  |
| rapidResponse.generallyAvailable | bool | `true` |  |
| rapidResponse.hostInactiveSecondsCutoff | int | `45` |  |
| rapidResponse.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-rapid-response-connector"` |  |
| rapidResponse.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-rapid-response-connector"` |  |
| rapidResponse.ingress[0].hosts[0].paths[0].path | string | `"/api/rapidresponse/v1"` |  |
| rapidResponse.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-rapid-response-connector"` |  |
| rapidResponse.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| rapidResponse.ingress[0].hosts[0].paths[1].apiGatewayAuthEnabled | bool | `false` |  |
| rapidResponse.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-rapid-response-connector-ws"` |  |
| rapidResponse.ingress[0].hosts[0].paths[1].apiGatewayUseWebSocket | bool | `true` |  |
| rapidResponse.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-rapid-response-connector-ws"` |  |
| rapidResponse.ingress[0].hosts[0].paths[1].path | string | `"/api/rapidresponse/v1/session/ws"` |  |
| rapidResponse.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-rapid-response-connector"` |  |
| rapidResponse.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| rapidResponse.ingress[0].hosts[0].paths[2].apiGatewayAuthEnabled | bool | `false` |  |
| rapidResponse.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-rapid-response-connector-status"` |  |
| rapidResponse.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-rapid-response-connector-status"` |  |
| rapidResponse.ingress[0].hosts[0].paths[2].path | string | `"/api/rapidresponse/v1/status"` |  |
| rapidResponse.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-rapid-response-connector"` |  |
| rapidResponse.ingress[0].hosts[0].paths[2].servicePort | int | `7000` |  |
| rapidResponse.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| rapidResponse.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| rapidResponse.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| rapidResponse.ingress[0].labels.role | string | `"ingress-config"` |  |
| rapidResponse.ingress[0].labels.tier | string | `"infra"` |  |
| rapidResponse.ingress[0].name | string | `"sysdigcloud-rapid-response-ingress"` |  |
| rapidResponse.janitor.cronjob | string | `"0 3 * * *"` |  |
| rapidResponse.janitor.dryRun | bool | `false` |  |
| rapidResponse.janitor.retentionDays | int | `90` |  |
| rapidResponse.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| rapidResponse.remoteStorage.endpoint | string | `"sysdigcloud-remote-storage-grpc:6000"` |  |
| rapidResponse.replicaCount | int | `1` |  |
| rapidResponse.repositoryPrefix | string | `"secure"` |  |
| rapidResponse.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| rapidResponse.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| rapidResponse.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| rapidResponse.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| rapidResponse.resources.rapidResponseConnector.limits.cpu | int | `1` |  |
| rapidResponse.resources.rapidResponseConnector.limits.memory | string | `"500Mi"` |  |
| rapidResponse.resources.rapidResponseConnector.requests.cpu | int | `1` |  |
| rapidResponse.resources.rapidResponseConnector.requests.memory | string | `"500Mi"` |  |
| rapidResponse.resources.rapidResponseJanitor.limits.cpu | string | `"250m"` |  |
| rapidResponse.resources.rapidResponseJanitor.limits.memory | string | `"250Mi"` |  |
| rapidResponse.resources.rapidResponseJanitor.requests.cpu | string | `"250m"` |  |
| rapidResponse.resources.rapidResponseJanitor.requests.memory | string | `"250Mi"` |  |
| rapidResponse.sdauthCacheTTL | string | `"5m"` |  |
| rapidResponse.serviceAccountName | string | `"sysdig"` |  |
| rapidResponse.sessionHostTokenSecondsTTL | int | `45` |  |
| rapidResponse.sessionIdleSecondsTTL | int | `300` |  |
| rapidResponse.sessionOppositeSecondsTimeout | int | `45` |  |
| rapidResponse.sessionTotalSecondsTTL | int | `7200` |  |
| rapidResponse.sessionUserTokenSecondsTTL | int | `180` |  |
| rapidResponse.validationCodeEmailTemplate | string | `"rapid-response"` |  |
| rapidResponse.validationCodeLength | int | `6` |  |
| rapidResponse.validationCodeSecondsDuration | int | `180` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# redis-exporter

![Version: 1.1.27](https://img.shields.io/badge/Version-1.1.27-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.16.3](https://img.shields.io/badge/AppVersion-1.16.3-informational?style=flat-square)

This is owned and maintained by Sysdig Infra team. It can install multiple Redis exporters

## Example

example with external password/cert

```
redisExporter:
  redisExporters:
    # `example` will be the suffix of the deployment name
    example:
      # redis user. If Cloud Provider or Redis implementation provides one, for example, `admin` is the default value in IBM Cloud
      redisUser: "myusername"
      # redis password. Expect `password` key as a default
      redisPasswordExistingSecret: redis-saas-secret
      redisAddr: "rediss://127.0.0.1:6379"
      # by default a ca.crt is expected
      redisCertificateExistingSecret: "redis-saas-ca-pub-certs"
      imagePullSecrets:
        - name: sysdigcloud-pull-secret
```

example with provided password/cert

```
redisExporter:
  redisExporters:
    # `example` will be the suffix of the deployment name
    example:
      # redis user. If Cloud Provider or Redis implementation provides one, for example, `admin` is the default value in IBM Cloud
      redisUser: "myusername"
      # redis password
      redisPassword: "mypassword"
      redisAddr: "rediss://127.0.0.1:6379"
      # redis ca.crt certificate
      redisCertificate: |
        -----BEGIN CERTIFICATE-----
        MIIC4TCCAcmgAwIBAgIUGcdNvwX9zBzlwprqYOF/qUyHYJ8wDQYJKoZIhvcNAQEL
        BQAwADAeFw0yMjAyMjYxNzU0NTFaFw0yMjAyMjcxNzU0NTFaMAAwggEiMA0GCSqG
        SIb3DQEBAQUAA4IBDwAwggEKAoIBAQDF+GZf4hG5GzOu5PyudfNxVnroWIuhTXzn
        /HT38KbrT7eAxrJ4rLp5qjJuVWr/nQkXqoA4UULau3iSQYzX+OjDCroHY9lIoKce
        1sbmYhBF7knDnzui6drh5I2xEEQG0qnDx6CvE1WhUqWSgLwpGWfCPUlzAnsWVfHs
        ZF45WXBCWrYOLONZcXXgwcRdkaan38jgVTbem/2xelvkW9z0g6HDO7pD5mL6Kxa3
        qs8u3gmkrrvgMm3MjztA28jFPQaSS/mnFkefjjnRoxSM1QDGuTXCCzL1PikSbG/h
        7VARMbGngxLsNl2noaTg6KedrCGBwAaXseFcS/VBQUm8bvieojEpAgMBAAGjUzBR
        MB0GA1UdDgQWBBS0Rj5Bxxt45qdFo7rHcW8m/OdwcTAfBgNVHSMEGDAWgBS0Rj5B
        xxt45qdFo7rHcW8m/OdwcTAPBgNVHRMBAf8EBTADAQH/MA0GCSqGSIb3DQEBCwUA
        A4IBAQCBUH6WFQEzltyzYW+IiaFtbVs57c1R2ttRmZALh6Gu9XOncIYwEG3GgdqP
        tJWpzvY3pngpbcwifORDRojeuaEqpNROHNAkT2bqK+V8Cx3P7WHHW7KVLrYl31kX
        eLQrX+k9wx/lHnxe2hS5FPv3301WoLWii5e76blWo5xWemMmkAc61bWfSO0JYBDR
        JMfpAbsqbKAXsH0VETIfzRgR68x7/DKvfF93xGgv++qR20DLzgPrux3rjnQ3TeOK
        nBTDIid+34tzxL2pmujWdyhKFj/tlp++mP/QbHawZbinOIkPFzjPIzzXnLB16VRy
        vOQYxuCGORvPRcLAuq1cHXnzj25p
        -----END CERTIFICATE-----
      imagePullSecrets:
        - name: sysdigcloud-pull-secret
```

if both `redisPasswordExistingSecret` and `redisPassword` are specified, `redisPasswordExistingSecret` takes the priority over `redisPassword`

if both `redisCertificateExistingSecret` and `redisCertificate` are specified, `redisCertificateExistingSecret` takes the priority over `redisCertificate`

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.airgappedRegistryName | string | `nil` | registry name for airgapped environments |
| global.airgappedRepositoryPrefix | string | `nil` | repository prefix for airgapped environments |
| global.cloudProvider.isMultiAZ | bool | `false` | "true" spreads redis pods across AZs |
| global.cloudProvider.name | string | `""` | it can be empty, "ibm", "aws" or "gcp" |
| global.legacyRedis.redisTls.useCertManager | bool | `false` | whether redis is using cert manager created certs. |
| global.namespace | string | `"sysdig"` | where to install redis-exporter |
| global.redistlsCASecretName | string | `"redistls-ca-secret"` | this is the secret name where the redisTls cert is exported by cert manager |
| redisExporter.affinity | object | `{}` |  |
| redisExporter.env | list | `[]` | append additional env |
| redisExporter.extraLabels | object | `{}` | extra labels for objects |
| redisExporter.fullnameOverride | string | `""` |  |
| redisExporter.image.pullPolicy | string | `"IfNotPresent"` |  |
| redisExporter.image.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/monitor/exporters/redis-exporter"` |  |
| redisExporter.image.tag | string | `"v1.43.21-ubi"` |  |
| redisExporter.imagePullSecret | string | `"sysdigcloud-pull-secret"` | image pull secret |
| redisExporter.labels.productCategory | string | `"infrastructure"` |  |
| redisExporter.nameOverride | string | `""` |  |
| redisExporter.namePrefix | string | `"redis-exporter"` | prefix name to use in redisExporters.<name> |
| redisExporter.nodeSelector | object | `{}` |  |
| redisExporter.podAnnotations."prometheus.io/port" | string | `"9121"` | prometheus scraping port |
| redisExporter.podAnnotations."prometheus.io/scrape" | string | `"true"` | prometheus scraping switch |
| redisExporter.redisAddr | string | `""` | redis target uri redis://127.1:6379 |
| redisExporter.redisCertificate | string | `""` | redis ca.crt certificate |
| redisExporter.redisCertificateExistingSecret | string | `""` | secret name where public ca.crt is located. Do not user together with redisCertificate |
| redisExporter.redisExporterSetClientName | bool | `false` | redis exporter client name used |
| redisExporter.redisExporterTlsCaCertFile | string | `"/opt/redis/certs/ca.crt"` | redis public ca.crt file path |
| redisExporter.redisPassword | string | `""` | redis password |
| redisExporter.redisPasswordExistingSecret | string | `""` | redis password secret |
| redisExporter.redisPasswordSecretKey | string | `"password"` | redis password secret key |
| redisExporter.redisUser | string | `""` | redis user |
| redisExporter.registryName | string | `"quay.io"` | default registry name |
| redisExporter.replicaCount | int | `1` |  |
| redisExporter.repositoryPrefix | string | `"sysdig"` | default repository prefix |
| redisExporter.resources.limits.cpu | string | `"100m"` |  |
| redisExporter.resources.limits.memory | string | `"128Mi"` |  |
| redisExporter.resources.requests.cpu | string | `"100m"` |  |
| redisExporter.resources.requests.memory | string | `"128Mi"` |  |
| redisExporter.tolerations | list | `[]` |  |

# redis

![Version: 2.1.45](https://img.shields.io/badge/Version-2.1.45-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.16.5](https://img.shields.io/badge/AppVersion-1.16.5-informational?style=flat-square)

This is owned and maintained by Sysdig Infra team. It conditionally installs
- redis6-ha statefulset
- redisTls(-ha) statefulset

In this first version the `values.yaml` structure resembles the one used by the `installer` for compatibility reasons.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.airgappedRegistryName | string | `nil` | registry name for airgapped environments |
| global.airgappedRepositoryPrefix | string | `nil` | repository prefix for airgapped environments |
| global.cloudProvider.isMultiAZ | bool | `false` | "true" spreads redis pods across AZs |
| global.cloudProvider.name | string | `""` | it can be empty, "ibm", "aws" or "gcp" |
| global.enableRedisTlsUpgrade | bool | `true` | enable redistls upgrade |
| global.legacyRedis.redisTls.caCertExpiry | string | `"87660h"` | set ca cert expiry in hours |
| global.legacyRedis.redisTls.caCertRenewBefore | string | `"360h"` | renew before how many hours of cert expiration |
| global.legacyRedis.redisTls.caCrts | list | `[]` | reditTls private certs encoded with b64 |
| global.legacyRedis.redisTls.caCrtsExternalSecretName | string | `""` | reditTls private certs external secret name |
| global.legacyRedis.redisTls.certificateIssuer | string | `"sysdig-selfsigned-issuer"` | certificate issuer to use, keep this empty if creating an issuer |
| global.legacyRedis.redisTls.certificateIssuerKind | string | `"ClusterIssuer"` | certificate issuer kind |
| global.legacyRedis.redisTls.createIssuer | bool | `false` | create a redis certificate issuer |
| global.legacyRedis.redisTls.deploy | bool | `true` | deploy redisTls, parameter coming from installer |
| global.legacyRedis.redisTls.enabled | bool | `false` | installs redisTls |
| global.legacyRedis.redisTls.exporter.imageName | string | `"redis-exporter"` | Docker registry for this image: artifactory |
| global.legacyRedis.redisTls.exporter.version | string | `"v1.43.15-ubi"` | redisTls exporter docker image tag |
| global.legacyRedis.redisTls.ha | bool | `false` | enables ha on redisTls |
| global.legacyRedis.redisTls.imageName | string | `"redis-7"` | redisTls docker image name |
| global.legacyRedis.redisTls.imagePullSecret | string | `"sysdigcloud-pull-secret"` | redistls image pull secret |
| global.legacyRedis.redisTls.nodeaffinityLabel | string | `""` |  |
| global.legacyRedis.redisTls.password | string | `""` | redisTls password (takes precedence on passwordExternalSecretKeyRef) |
| global.legacyRedis.redisTls.passwordExternalSecretKeyRef | object | `{}` | redisTls password from external secret |
| global.legacyRedis.redisTls.persistentVolumeClaim | object | `{"size":"100Gi","storageClassName":"sysdig"}` | redistls PV size for upgrade |
| global.legacyRedis.redisTls.podAnnotations | object | `{"cluster-autoscaler.kubernetes.io/safe-to-evict":"false"}` | redisTls extra annotations to add on to redis pods |
| global.legacyRedis.redisTls.port | int | `6379` | port where to expose redisTls |
| global.legacyRedis.redisTls.privateKeyAlgorithm | string | `"RSA"` | private key algorithm to use |
| global.legacyRedis.redisTls.privateKeySize | int | `4096` | private key size to use |
| global.legacyRedis.redisTls.pubCaCrts | list | `[]` | reditTls public Certs encoded with b64 |
| global.legacyRedis.redisTls.pubCaCrtsExternalSecretName | string | `""` | reditTls public certificates external secret name |
| global.legacyRedis.redisTls.registryName | string | `"quay.io"` | default registry name |
| global.legacyRedis.redisTls.repositoryPrefix | string | `"sysdig"` | default repository prefix |
| global.legacyRedis.redisTls.resources.redis | object | `{"limits":{"cpu":2,"memory":"2Gi"},"requests":{"cpu":"100m","memory":"2Gi"}}` | redisTls resources |
| global.legacyRedis.redisTls.resources.redis-init | object | `{"limits":{"cpu":"300m","memory":"200Mi"},"requests":{"cpu":"50m","memory":"100Mi"}}` | redisTLS initContainer resources: |
| global.legacyRedis.redisTls.resources.redis-metrics | object | `{"limits":{"cpu":"100m","memory":"128Mi"},"requests":{"cpu":"50m","memory":"64Mi"}}` | redisTLS metrics and check-version resources |
| global.legacyRedis.redisTls.resources.redis-sentinel | object | `{"limits":{"cpu":"300m","memory":"100Mi"},"requests":{"cpu":"50m","memory":"100Mi"}}` | redisTls sentinel resources |
| global.legacyRedis.redisTls.resources.redistls_upgrade | object | `{"limits":{"cpu":2,"memory":"2Gi"},"requests":{"cpu":"200m","memory":"2Gi"}}` | redisTLS upgrade resources |
| global.legacyRedis.redisTls.sentinel.imageName | string | `"redis-sentinel-7"` | redisTls docker image name |
| global.legacyRedis.redisTls.sentinel.masterSet | string | `"primary"` | redisTls sentinel masterSet |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` | port where to expose redisTls sentinel |
| global.legacyRedis.redisTls.sentinel.version | string | `"0.0.8"` | redisTls sentinel docker image tag |
| global.legacyRedis.redisTls.serviceAccountName | string | `"redis"` | service account to use into redistls pod |
| global.legacyRedis.redisTls.tls | bool | `true` | enables tls on redisTls (:troll) |
| global.legacyRedis.redisTls.updateStrategy | string | `"RollingUpdate"` | redisTls update strategy to use for redistls |
| global.legacyRedis.redisTls.upgrade.imageName | string | `"kubectl-fips"` |  |
| global.legacyRedis.redisTls.upgrade.imagePullPolicy | string | `"IfNotPresent"` |  |
| global.legacyRedis.redisTls.upgrade.version | string | `"1.34.3-1.4.9"` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` | whether to use cert-manager to create certs |
| global.legacyRedis.redisTls.version | string | `"0.0.9"` | redisTls docker image tag |
| global.namespace | string | `"sysdig"` | where to install redis |
| global.redistlsCASecretName | string | `"redistls-ca-secret"` | this is the secret name where the redisTls password is exported by cert manager |

# response-actions

![Version: 0.1.0-260312162947-main-v66aa223](https://img.shields.io/badge/Version-0.1.0--260312162947--main--v66aa223-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Response Actions

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.cloudProvider.name | string | `"change-me"` |  |
| global.cloudProvider.region | string | `"change-me"` |  |
| global.cloudauth.grpcEndpoint | string | `"sysdigcloud-cloudauth-api-grpc:6000"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.iamUser.accessKey | string | `"change-me"` |  |
| global.iamUser.region | string | `"us-east-1"` |  |
| global.iamUser.secretKey | string | `"change-me"` |  |
| global.iamUserGov.accessKey | string | `"change-me"` |  |
| global.iamUserGov.region | string | `"us-gov-west-1"` |  |
| global.iamUserGov.secretKey | string | `"change-me"` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.responseActions.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.responseActions.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.responseActions.db | string | `"response_actions_db"` |  |
| global.legacyPostgres.postgresDatabases.responseActions.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.responseActions.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.responseActions.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.responseActions.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.responseActions.username | string | `"responseactions_user"` |  |
| global.legacyRedis.redisClientsSecure.responseActions.tls | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgresql-client"` |  |
| global.postgresVersion | string | `"0.0.50"` |  |
| global.scaler.clusterName | string | `"provider-env-region-DD"` |  |
| global.trustedIdentity.aws | string | `"change-me"` |  |
| global.trustedIdentity.awsGov | string | `"change-me"` |  |
| responseActions.authorizationService.enabled | bool | `false` |  |
| responseActions.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| responseActions.cleanup.expiredResponderCleanupInterval | string | `"10m"` |  |
| responseActions.cleanup.terminatedActionsCleanupInterval | string | `"1h"` |  |
| responseActions.cleanup.terminatedActionsRetentionPeriod | string | `"2160h"` |  |
| responseActions.cloudActions.jwt.expiresIn | string | `"1h"` |  |
| responseActions.cloudActions.jwt.issuer | string | `"sysdig-response-actions"` |  |
| responseActions.cloudActions.jwt.secret | string | `"change-me"` |  |
| responseActions.enabled | bool | `true` |  |
| responseActions.featureFlags.enableFileQuarantine | bool | `false` |  |
| responseActions.featureFlags.remoteStorageEnabledCustomers | string | `""` |  |
| responseActions.ingestion.enabled | bool | `true` |  |
| responseActions.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-response-actions-controller"` |  |
| responseActions.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-response-actions-controller"` |  |
| responseActions.ingress[0].hosts[0].paths[0].path | string | `"/api/responseActions"` |  |
| responseActions.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-response-actions-controller"` |  |
| responseActions.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| responseActions.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-response-actions-controller-websocket"` |  |
| responseActions.ingress[0].hosts[0].paths[1].apiGatewayUseWebSocket | bool | `true` |  |
| responseActions.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-response-actions-controller-websocket"` |  |
| responseActions.ingress[0].hosts[0].paths[1].path | string | `"/api/responseActions/v1/responder/registration"` |  |
| responseActions.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-response-actions-controller"` |  |
| responseActions.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| responseActions.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-response-actions-controller-websocket-2"` |  |
| responseActions.ingress[0].hosts[0].paths[2].apiGatewayUseRegex | bool | `true` |  |
| responseActions.ingress[0].hosts[0].paths[2].apiGatewayUseWebSocket | bool | `true` |  |
| responseActions.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-response-actions-controller-websocket-2"` |  |
| responseActions.ingress[0].hosts[0].paths[2].path | string | `"/api/responseActions/v1/action/([a-f0-9-]+)/watch"` |  |
| responseActions.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-response-actions-controller"` |  |
| responseActions.ingress[0].hosts[0].paths[2].servicePort | int | `7000` |  |
| responseActions.ingress[0].hosts[0].paths[3].apiGatewayRouteName | string | `"secure-response-actions-controller-public-oas"` |  |
| responseActions.ingress[0].hosts[0].paths[3].openshiftRouteName | string | `"secure-response-actions-controller-public-oas"` |  |
| responseActions.ingress[0].hosts[0].paths[3].path | string | `"/secure/response-actions"` |  |
| responseActions.ingress[0].hosts[0].paths[3].serviceName | string | `"sysdigcloud-response-actions-controller"` |  |
| responseActions.ingress[0].hosts[0].paths[3].servicePort | int | `7000` |  |
| responseActions.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| responseActions.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| responseActions.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| responseActions.ingress[0].labels.role | string | `"ingress-config"` |  |
| responseActions.ingress[0].labels.tier | string | `"infra"` |  |
| responseActions.ingress[0].name | string | `"sysdigcloud-response-actions-ingress"` |  |
| responseActions.maxRespondersPerPod | int | `6000` |  |
| responseActions.metadataService.cacheExpiration | string | `"2m"` |  |
| responseActions.metadataService.cacheSizeBytes | string | `"10485760"` |  |
| responseActions.metadataService.endpoint | string | `"sysdigcloud-metadata-service-server:5300"` |  |
| responseActions.natsConsumers.cloudauth.ackWait | string | `"30s"` |  |
| responseActions.natsConsumers.cloudauth.maxInFlight | string | `"1000"` |  |
| responseActions.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| responseActions.remoteStorage.endpoint | string | `"sysdigcloud-remote-storage-grpc:6000"` |  |
| responseActions.replicaCount | int | `1` |  |
| responseActions.repositoryPrefix | string | `"secure"` |  |
| responseActions.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| responseActions.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| responseActions.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| responseActions.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| responseActions.resources.responseActionsController.limits.cpu | int | `1` |  |
| responseActions.resources.responseActionsController.limits.memory | string | `"500Mi"` |  |
| responseActions.resources.responseActionsController.requests.cpu | int | `1` |  |
| responseActions.resources.responseActionsController.requests.memory | string | `"500Mi"` |  |
| responseActions.responder.pingInterval | string | `"1m"` |  |
| responseActions.retry.maxRetries | int | `2` |  |
| responseActions.retry.retryDelay | string | `"15s"` |  |
| responseActions.retry.stuckInResponderExpiration | string | `"1m"` |  |
| responseActions.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| responseActions.scaler.responseActionsController.cpuThreshold | int | `70` |  |
| responseActions.scaler.responseActionsController.enabled | bool | `true` |  |
| responseActions.scaler.responseActionsController.maxReplicaCount | int | `10` |  |
| responseActions.scaler.responseActionsController.memoryThreshold | int | `70` |  |
| responseActions.scaler.responseActionsController.minReplicaCount | int | `1` |  |
| responseActions.scaler.responseActionsController.respondersThreshold | float | `0.5` |  |
| responseActions.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| responseActions.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 200\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-acvalidationengine

![Version: 2.0.0-260303144345-main-vc90ee56](https://img.shields.io/badge/Version-2.0.0--260303144345--main--vc90ee56-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

VM Admission Controller Validation Engine

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.deployment | string | `"kubernetes"` |  |
| global.dnsName | string | `""` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.scanningv2.enabled | bool | `true` |  |
| scanningv2AcvalidationEngine.customerMetricsEnabled | string | `"false"` |  |
| scanningv2AcvalidationEngine.enabled | bool | `true` |  |
| scanningv2AcvalidationEngine.engine.asyncRoutines | int | `4` |  |
| scanningv2AcvalidationEngine.enginesEnabled | string | `"VM,KSPM"` |  |
| scanningv2AcvalidationEngine.externalNats.enabled | bool | `true` |  |
| scanningv2AcvalidationEngine.externalNats.tlsSkip | bool | `true` |  |
| scanningv2AcvalidationEngine.externalNats.url | string | `"nats-external:4222"` |  |
| scanningv2AcvalidationEngine.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-acvalidationengine"` |  |
| scanningv2AcvalidationEngine.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-acvalidationengine"` |  |
| scanningv2AcvalidationEngine.ingress[0].hosts[0].paths[0].path | string | `"/api/posture/acve"` |  |
| scanningv2AcvalidationEngine.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-acvalidationengine-api-http"` |  |
| scanningv2AcvalidationEngine.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2AcvalidationEngine.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2AcvalidationEngine.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2AcvalidationEngine.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2AcvalidationEngine.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2AcvalidationEngine.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2AcvalidationEngine.ingress[0].name | string | `"sysdigcloud-scanningv2-acvalidationengine-ingress"` |  |
| scanningv2AcvalidationEngine.loggingLevel | string | `"DEBUG"` |  |
| scanningv2AcvalidationEngine.nats.sub | string | `nil` |  |
| scanningv2AcvalidationEngine.nats.tlsEnabled | bool | `true` |  |
| scanningv2AcvalidationEngine.nats.tlsSkip | bool | `false` |  |
| scanningv2AcvalidationEngine.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2AcvalidationEngine.replicaCount | int | `2` |  |
| scanningv2AcvalidationEngine.repositoryPrefix | string | `"secure"` |  |
| scanningv2AcvalidationEngine.resources.scanningv2AcvalidationEngine.limits.cpu | int | `1` |  |
| scanningv2AcvalidationEngine.resources.scanningv2AcvalidationEngine.limits.memory | string | `"2Gi"` |  |
| scanningv2AcvalidationEngine.resources.scanningv2AcvalidationEngine.requests.cpu | int | `1` |  |
| scanningv2AcvalidationEngine.resources.scanningv2AcvalidationEngine.requests.memory | string | `"2Gi"` |  |
| scanningv2AcvalidationEngine.scaler.api.cpuThreshold | int | `80` |  |
| scanningv2AcvalidationEngine.scaler.api.maxReplicaCount | int | `6` |  |
| scanningv2AcvalidationEngine.scaler.api.memoryThreshold | int | `80` |  |
| scanningv2AcvalidationEngine.scaler.api.minReplicaCount | int | `2` |  |
| scanningv2AcvalidationEngine.scaler.enabled | bool | `true` |  |
| scanningv2AcvalidationEngine.serviceDependencies.scanningv2Policies.grpc.endpoint | string | `"sysdigcloud-scanningv2-policies-api-grpc-headless:6000"` |  |
| scanningv2AcvalidationEngine.serviceDependencies.scanningv2Policies.grpc.maxMessageSizeBytes | int | `167772167` |  |
| scanningv2AcvalidationEngine.serviceDependencies.scanningv2Policies.grpc.tlsSkip | string | `"true"` |  |
| scanningv2AcvalidationEngine.serviceDependencies.scanningv2Scanrequestor.grpc.endpoint | string | `"sysdigcloud-scanningv2-scanrequestor-grpc-headless:6000"` |  |
| scanningv2AcvalidationEngine.serviceDependencies.scanningv2Scanrequestor.grpc.tlsSkip | string | `"true"` |  |
| scanningv2AcvalidationEngine.serviceDependencies.secureIacWorkload.grpc.endpoint | string | `"secure-iac-workload-service-headless:8080"` |  |
| scanningv2AcvalidationEngine.serviceDependencies.secureIacWorkload.grpc.tlsSkip | string | `"true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-agents-conf

![Version: 2.0.0-260219112623-main-vf3cc377](https://img.shields.io/badge/Version-2.0.0--260219112623--main--vf3cc377-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning Agents Conf

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.agentsConf.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.agentsConf.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.agentsConf.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.agentsConf.db | string | `"agents_conf"` |  |
| global.legacyPostgres.postgresDatabases.agentsConf.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.agentsConf.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.agentsConf.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.agentsConf.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.agentsConf.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.agentsConf.username | string | `"agents_conf_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.scanningv2.telemetry.clusterName | string | `""` |  |
| global.scanningv2.telemetry.segmentToken | string | `""` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| scanningv2AgentsConf.analytics.enabled | bool | `false` |  |
| scanningv2AgentsConf.audit.enabled | bool | `true` |  |
| scanningv2AgentsConf.configOverrides | string | `nil` |  |
| scanningv2AgentsConf.eventBatching | string | `nil` |  |
| scanningv2AgentsConf.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-agents-conf"` |  |
| scanningv2AgentsConf.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-agents-conf"` |  |
| scanningv2AgentsConf.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/agents"` |  |
| scanningv2AgentsConf.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-agents-conf-http"` |  |
| scanningv2AgentsConf.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2AgentsConf.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2AgentsConf.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2AgentsConf.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2AgentsConf.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2AgentsConf.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2AgentsConf.ingress[0].name | string | `"sysdigcloud-scanningv2-agents-conf-ingress"` |  |
| scanningv2AgentsConf.isBackendScanningEnabled | bool | `false` |  |
| scanningv2AgentsConf.isLocalScanningEnabled | bool | `false` |  |
| scanningv2AgentsConf.loggingLevel | string | `"INFO"` |  |
| scanningv2AgentsConf.natsJS.secure.enabled | string | `"true"` |  |
| scanningv2AgentsConf.natsJS.url | string | `"nats"` |  |
| scanningv2AgentsConf.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2AgentsConf.replicaCount | int | `3` |  |
| scanningv2AgentsConf.repositoryPrefix | string | `"secure"` |  |
| scanningv2AgentsConf.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2AgentsConf.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2AgentsConf.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2AgentsConf.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2AgentsConf.resources.scanningv2AgentsConf.limits.cpu | int | `1` |  |
| scanningv2AgentsConf.resources.scanningv2AgentsConf.limits.memory | string | `"1Gi"` |  |
| scanningv2AgentsConf.resources.scanningv2AgentsConf.requests.cpu | string | `"150m"` |  |
| scanningv2AgentsConf.resources.scanningv2AgentsConf.requests.memory | string | `"500Mi"` |  |
| scanningv2AgentsConf.runtimeScanner.fullScanInterval | string | `"12h"` |  |
| scanningv2AgentsConf.runtimeScanner.incrementalScanInterval | string | `"15m"` |  |
| scanningv2AgentsConf.runtimeScanner.keepaliveInterval | string | `"10m"` |  |
| scanningv2AgentsConf.runtimeScanner.minimumAccettableDatabaseTimestamp | string | `""` |  |
| scanningv2AgentsConf.scaler.api.cpuThreshold | int | `70` |  |
| scanningv2AgentsConf.scaler.api.maxReplicaCount | int | `5` |  |
| scanningv2AgentsConf.scaler.api.memoryThreshold | int | `70` |  |
| scanningv2AgentsConf.scaler.enabled | bool | `false` |  |
| scanningv2AgentsConf.serviceAccountName | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-airgap-vuln-feeds

![Version: 0.2.0-ve9fb6edf](https://img.shields.io/badge/Version-0.2.0--ve9fb6edf-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.2.0-ve9fb6edf](https://img.shields.io/badge/AppVersion-0.2.0--ve9fb6edf-informational?style=flat-square)

Secure Scanning Airgap Vuln Feeds

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.dnsName | string | `"change-me.com"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.scanningv2.airgappedFeeds | bool | `true` |  |
| global.scanningv2.enabled | bool | `true` |  |
| scanningv2AirgapVulnFeeds.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-airgap-vuln-feeds-http"` |  |
| scanningv2AirgapVulnFeeds.ingress[0].hosts[0].paths[0].path | string | `"/scanningv2-vuln-feeds"` |  |
| scanningv2AirgapVulnFeeds.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-airgap-vuln-feeds-http"` |  |
| scanningv2AirgapVulnFeeds.ingress[0].hosts[0].paths[0].servicePort | int | `9000` |  |
| scanningv2AirgapVulnFeeds.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2AirgapVulnFeeds.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2AirgapVulnFeeds.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2AirgapVulnFeeds.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2AirgapVulnFeeds.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2AirgapVulnFeeds.ingress[0].name | string | `"sysdigcloud-scanningv2-airgap-vuln-feeds-ingress"` |  |
| scanningv2AirgapVulnFeeds.password | string | `nil` |  |
| scanningv2AirgapVulnFeeds.registryName | string | `"quay.io"` |  |
| scanningv2AirgapVulnFeeds.replicaCount | int | `1` |  |
| scanningv2AirgapVulnFeeds.repositoryPrefix | string | `"sysdig"` |  |
| scanningv2AirgapVulnFeeds.resources.scanningv2AirgapVulnFeeds.limits.cpu | string | `"200m"` |  |
| scanningv2AirgapVulnFeeds.resources.scanningv2AirgapVulnFeeds.limits.ephemeralStorage | string | `"2Gi"` |  |
| scanningv2AirgapVulnFeeds.resources.scanningv2AirgapVulnFeeds.limits.memory | string | `"512Mi"` |  |
| scanningv2AirgapVulnFeeds.resources.scanningv2AirgapVulnFeeds.requests.cpu | string | `"100m"` |  |
| scanningv2AirgapVulnFeeds.resources.scanningv2AirgapVulnFeeds.requests.ephemeralStorage | string | `"2Gi"` |  |
| scanningv2AirgapVulnFeeds.resources.scanningv2AirgapVulnFeeds.requests.memory | string | `"512Mi"` |  |
| scanningv2AirgapVulnFeeds.user | string | `nil` |  |
| scanningv2AirgapVulnFeeds.version | string | `"dev"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-collector

![Version: 2.0.0-260310114936-main-vab463b1](https://img.shields.io/badge/Version-2.0.0--260310114936--main--vab463b1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning Collector

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.dnsName | string | `"change-me.com"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Collector.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Collector.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Collector.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Collector.db | string | `"scanningv2_collector"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Collector.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Collector.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Collector.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Collector.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Collector.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Collector.username | string | `"scanningv2_collector_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.secureRepositoryPrefix | string | `"secure"` |  |
| scanningv2Collector.agentsConf.grpc.endpoint | string | `"sysdigcloud-scanningv2-agents-conf-grpc:6000"` |  |
| scanningv2Collector.agentsConf.grpc.tlsSkip | string | `"true"` |  |
| scanningv2Collector.audit.enabled | bool | `true` |  |
| scanningv2Collector.authorizationService.enabled | bool | `false` |  |
| scanningv2Collector.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| scanningv2Collector.dbTimeout | string | `"10s"` |  |
| scanningv2Collector.enableCustomerLevelMetrics | bool | `true` |  |
| scanningv2Collector.ingressV2.defaultServiceName | string | `"sysdigcloud-scanningv2-collector-http"` |  |
| scanningv2Collector.ingressV2.defaultServicePort | int | `7000` |  |
| scanningv2Collector.ingressV2.name | string | `"sysdigcloud-scanningv2-collector-ingress"` |  |
| scanningv2Collector.ingressV2.paths.sysdigcloudScanningv2Collector.isPrivate | bool | `true` |  |
| scanningv2Collector.ingressV2.paths.sysdigcloudScanningv2Collector.isPublic | bool | `true` |  |
| scanningv2Collector.ingressV2.paths.sysdigcloudScanningv2Collector.path | string | `"/api/scanning/collector"` |  |
| scanningv2Collector.ingressV2.paths.sysdigcloudScanningv2CollectorRuntime.isPrivate | bool | `true` |  |
| scanningv2Collector.ingressV2.paths.sysdigcloudScanningv2CollectorRuntime.isPublic | bool | `true` |  |
| scanningv2Collector.ingressV2.paths.sysdigcloudScanningv2CollectorRuntime.path | string | `"/api/scanning/runtime"` |  |
| scanningv2Collector.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-collector-runtime"` |  |
| scanningv2Collector.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-collector-runtime"` |  |
| scanningv2Collector.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/runtime"` |  |
| scanningv2Collector.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-collector-http"` |  |
| scanningv2Collector.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Collector.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-collector"` |  |
| scanningv2Collector.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-scanningv2-collector"` |  |
| scanningv2Collector.ingress[0].hosts[0].paths[1].path | string | `"/api/scanning/collector"` |  |
| scanningv2Collector.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-scanningv2-collector-http"` |  |
| scanningv2Collector.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| scanningv2Collector.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Collector.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Collector.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Collector.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Collector.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Collector.ingress[0].name | string | `"sysdigcloud-scanningv2-collector-ingress"` |  |
| scanningv2Collector.loggingLevel | string | `"INFO"` |  |
| scanningv2Collector.nats.js.tlsEnabled | bool | `true` |  |
| scanningv2Collector.nats.js.url | string | `"nats"` |  |
| scanningv2Collector.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Collector.remotebody.enabled | bool | `false` |  |
| scanningv2Collector.remotebody.publishers | string | `"sbom"` |  |
| scanningv2Collector.remotebody.pusherBackend | string | `"s3"` |  |
| scanningv2Collector.remotebody.s3.accessKeyId | string | `""` |  |
| scanningv2Collector.remotebody.s3.bucket | string | `""` |  |
| scanningv2Collector.remotebody.s3.cloudProvider | string | `""` |  |
| scanningv2Collector.remotebody.s3.endpoint | string | `""` |  |
| scanningv2Collector.remotebody.s3.presignedUrlTtl | string | `"3h"` |  |
| scanningv2Collector.remotebody.s3.region | string | `""` |  |
| scanningv2Collector.remotebody.s3.secretAccessKey | string | `""` |  |
| scanningv2Collector.remotebody.s3.serviceAccountName | string | `"nats-remotebody"` |  |
| scanningv2Collector.remotebody.s3.usePresignedUrl | bool | `false` |  |
| scanningv2Collector.remotebody.thresholdBytes | string | `"8388608"` |  |
| scanningv2Collector.removeContainerID | bool | `true` |  |
| scanningv2Collector.replicaCount | int | `2` |  |
| scanningv2Collector.repositoryPrefix | string | `"secure"` |  |
| scanningv2Collector.resources.scanningv2Collector.limits.cpu | int | `2` |  |
| scanningv2Collector.resources.scanningv2Collector.limits.memory | string | `"4Gi"` |  |
| scanningv2Collector.resources.scanningv2Collector.requests.cpu | int | `2` |  |
| scanningv2Collector.resources.scanningv2Collector.requests.memory | string | `"4Gi"` |  |
| scanningv2Collector.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Collector.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 60\n    endpointOverrides:\n      forward_ingestion: 200\n      runtime_scanner_write: 120\n      registry_scanner_write: 10\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |
| scanningv2Collector.vmMDEenabled | bool | `true` |  |
| scanningv2Collector.vmMDEenabledHostContainer | bool | `true` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-credentialstore

![Version: 2.0.0-260203094633-main-vbfe6809](https://img.shields.io/badge/Version-2.0.0--260203094633--main--vbfe6809-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning Credential Store

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.deployment | string | `"kubernetes"` |  |
| global.dnsName | string | `""` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Credentialstore.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Credentialstore.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Credentialstore.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Credentialstore.db | string | `"scanningv2_credentialstore"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Credentialstore.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Credentialstore.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Credentialstore.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Credentialstore.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Credentialstore.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Credentialstore.username | string | `"scanningv2_credentialstore_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| scanningv2Credentialstore.enabled | bool | `true` |  |
| scanningv2Credentialstore.encryptionKey | string | `nil` |  |
| scanningv2Credentialstore.ingressV2.defaultServiceName | string | `"sysdigcloud-scanningv2-credentialstore-api-http"` |  |
| scanningv2Credentialstore.ingressV2.defaultServicePort | int | `7000` |  |
| scanningv2Credentialstore.ingressV2.name | string | `"sysdigcloud-scanningv2-credentialstore-ingress"` |  |
| scanningv2Credentialstore.ingressV2.paths.sysdigcloudScanningv2CredentialstoreV2.isPrivate | bool | `true` |  |
| scanningv2Credentialstore.ingressV2.paths.sysdigcloudScanningv2CredentialstoreV2.isPublic | bool | `true` |  |
| scanningv2Credentialstore.ingressV2.paths.sysdigcloudScanningv2CredentialstoreV2.path | string | `"/api/scanning/registries/v2"` |  |
| scanningv2Credentialstore.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-credentialstore-v2"` |  |
| scanningv2Credentialstore.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-credentialstore-v2"` |  |
| scanningv2Credentialstore.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/registries/v2"` |  |
| scanningv2Credentialstore.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-credentialstore-api-http"` |  |
| scanningv2Credentialstore.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Credentialstore.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Credentialstore.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Credentialstore.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Credentialstore.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Credentialstore.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Credentialstore.ingress[0].name | string | `"sysdigcloud-scanningv2-credentialstore-ingress"` |  |
| scanningv2Credentialstore.loggingLevel | string | `"INFO"` |  |
| scanningv2Credentialstore.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Credentialstore.replicaCount | int | `1` |  |
| scanningv2Credentialstore.repositoryPrefix | string | `"secure"` |  |
| scanningv2Credentialstore.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2Credentialstore.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2Credentialstore.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2Credentialstore.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2Credentialstore.resources.scanningv2Credentialstore.limits.cpu | int | `1` |  |
| scanningv2Credentialstore.resources.scanningv2Credentialstore.limits.memory | string | `"1Gi"` |  |
| scanningv2Credentialstore.resources.scanningv2Credentialstore.requests.cpu | int | `1` |  |
| scanningv2Credentialstore.resources.scanningv2Credentialstore.requests.memory | string | `"1Gi"` |  |
| scanningv2Credentialstore.scaler.api.cpuThreshold | int | `70` |  |
| scanningv2Credentialstore.scaler.api.maxReplicaCount | int | `5` |  |
| scanningv2Credentialstore.scaler.api.memoryThreshold | int | `70` |  |
| scanningv2Credentialstore.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| scanningv2Credentialstore.scaler.clusterName | string | `""` |  |
| scanningv2Credentialstore.scaler.enabled | bool | `false` |  |
| scanningv2Credentialstore.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| scanningv2Credentialstore.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Credentialstore.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 10\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-imagesbomextractor

![Version: 2.0.1-260219154831-main-v009c1a4](https://img.shields.io/badge/Version-2.0.1--260219154831--main--v009c1a4-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Image SBOM Extractor

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.9.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.azurePrincipal.auth.agentless.clientId | string | `""` |  |
| global.azurePrincipal.auth.agentless.clientSecret | string | `""` |  |
| global.azurePrincipal.tenantId | string | `""` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.iamUser.accessKey | string | `""` |  |
| global.iamUser.secretKey | string | `""` |  |
| global.legacyRedis.redisClientsSecure.scanning.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.proxy.enable | bool | `false` |  |
| global.scaler.authenticationRef | string | `""` |  |
| global.scaler.clusterName | string | `""` |  |
| global.scaler.serverAddress | string | `""` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.scanningv2.proxy.enable | bool | `false` |  |
| scanningv2Imagesbomextractor.accessKey | string | `"change-me"` |  |
| scanningv2Imagesbomextractor.accessKeySecretName | string | `""` |  |
| scanningv2Imagesbomextractor.analyzer.cache.local.maxElementSizeBytes | string | `"102400"` |  |
| scanningv2Imagesbomextractor.analyzer.cache.local.maxSizeBytes | string | `"36700160"` |  |
| scanningv2Imagesbomextractor.analyzer.cache.local.ttl | string | `"168h"` |  |
| scanningv2Imagesbomextractor.analyzer.cache.type | string | `"distributed,local[lru]"` |  |
| scanningv2Imagesbomextractor.apiEndpoint | string | `"https://secure.sysdig.com"` |  |
| scanningv2Imagesbomextractor.cloudAuth.cloudProviders.azure.auth.agentless.clientSecret | string | `""` |  |
| scanningv2Imagesbomextractor.cloudAuth.configurationDirectory | string | `"/var/image-sbom-extractor"` |  |
| scanningv2Imagesbomextractor.cloudAuth.configurationFileName | string | `"config.yaml"` |  |
| scanningv2Imagesbomextractor.cloudAuth.enabled | bool | `false` |  |
| scanningv2Imagesbomextractor.cloudAuth.environmentId | string | `"dev"` |  |
| scanningv2Imagesbomextractor.customerMetrics.enabled | bool | `false` |  |
| scanningv2Imagesbomextractor.defaultRegistryName | string | `"quay.io"` |  |
| scanningv2Imagesbomextractor.defaultRegistryRepositoryPrefix | string | `"sysdig"` |  |
| scanningv2Imagesbomextractor.livenessProbe.httpGet.path | string | `"/probes/liveness"` |  |
| scanningv2Imagesbomextractor.livenessProbe.httpGet.port | int | `7000` |  |
| scanningv2Imagesbomextractor.livenessProbe.initialDelaySeconds | int | `10` |  |
| scanningv2Imagesbomextractor.livenessProbe.periodSeconds | int | `10` |  |
| scanningv2Imagesbomextractor.loggingLevel | string | `"INFO"` |  |
| scanningv2Imagesbomextractor.mirrors.dockerdEnabled | bool | `false` |  |
| scanningv2Imagesbomextractor.mirrors.mirror | string | `"registry-1.docker.io"` |  |
| scanningv2Imagesbomextractor.mode | string | `"cluster"` |  |
| scanningv2Imagesbomextractor.natsJS.auth.password | string | `"change-me"` |  |
| scanningv2Imagesbomextractor.natsJS.auth.username | string | `"rsi-ise-user"` |  |
| scanningv2Imagesbomextractor.natsJS.consumer.ackWait | string | `"5m"` |  |
| scanningv2Imagesbomextractor.natsJS.consumer.deliverPolicyAll | bool | `true` |  |
| scanningv2Imagesbomextractor.natsJS.consumer.durable | string | `"ise-durable"` |  |
| scanningv2Imagesbomextractor.natsJS.consumer.maxDeliver | int | `3` |  |
| scanningv2Imagesbomextractor.natsJS.consumer.maxInFlight | int | `2048` |  |
| scanningv2Imagesbomextractor.natsJS.consumer.name | string | `"ise"` |  |
| scanningv2Imagesbomextractor.natsJS.consumer.pull | bool | `true` |  |
| scanningv2Imagesbomextractor.natsJS.consumer.pullBatch | int | `25` |  |
| scanningv2Imagesbomextractor.natsJS.consumer.stream | string | `"analysis-requests"` |  |
| scanningv2Imagesbomextractor.natsJS.consumer.subject | string | `"analysis.requests.>"` |  |
| scanningv2Imagesbomextractor.natsJS.messenger.fetchTimeout | string | `"5m"` |  |
| scanningv2Imagesbomextractor.natsJS.messenger.handleTimeout | string | `"5m"` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.ackWait | string | `"1m"` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.deliverPolicyAll | bool | `true` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.durable | string | `"vm-platform-imagesbomextractor-durable"` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.enabled | bool | `false` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.maxDeliver | int | `3` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.maxInFlight | int | `2048` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.name | string | `"vm-platform-imagesbomextractor"` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.pull | bool | `true` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.pullBatch | int | `25` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.stream | string | `"secure-vm-sbomapi-persist-sbom-response"` |  |
| scanningv2Imagesbomextractor.natsJS.persistSbomConsumer.subject | string | `"secure.vm.sbomapi.persist-sbom.response.*.ise.>"` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.ackWait | string | `"5m"` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.deliverPolicyAll | bool | `true` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.durable | string | `"ise-priority-durable"` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.enabled | bool | `true` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.maxDeliver | int | `3` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.maxInFlight | int | `2048` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.name | string | `"ise-priority"` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.pull | bool | `true` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.pullBatch | int | `25` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.stream | string | `"analysis-requests"` |  |
| scanningv2Imagesbomextractor.natsJS.priorityConsumer.subject | string | `"analysis.priority.requests.>"` |  |
| scanningv2Imagesbomextractor.natsJS.tls.enabled | bool | `true` |  |
| scanningv2Imagesbomextractor.natsJS.tls.secretName | string | `"sysdigcloud-scanningv2-rsi-nats-js-tls"` |  |
| scanningv2Imagesbomextractor.natsJS.tls.skipVerify | bool | `false` |  |
| scanningv2Imagesbomextractor.natsJS.url | string | `"nats://sysdigcloud-scanningv2-rsi-service:4222"` |  |
| scanningv2Imagesbomextractor.platformEnabled | bool | `true` |  |
| scanningv2Imagesbomextractor.readinessProbe.httpGet.path | string | `"/probes/readiness"` |  |
| scanningv2Imagesbomextractor.readinessProbe.httpGet.port | int | `7000` |  |
| scanningv2Imagesbomextractor.readinessProbe.initialDelaySeconds | int | `10` |  |
| scanningv2Imagesbomextractor.readinessProbe.periodSeconds | int | `10` |  |
| scanningv2Imagesbomextractor.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Imagesbomextractor.remotebody.enabled | bool | `false` |  |
| scanningv2Imagesbomextractor.remotebody.pusherBackend | string | `"s3"` |  |
| scanningv2Imagesbomextractor.remotebody.s3.accessKeyId | string | `""` |  |
| scanningv2Imagesbomextractor.remotebody.s3.bucket | string | `""` |  |
| scanningv2Imagesbomextractor.remotebody.s3.cloudProvider | string | `""` |  |
| scanningv2Imagesbomextractor.remotebody.s3.endpoint | string | `""` |  |
| scanningv2Imagesbomextractor.remotebody.s3.region | string | `""` |  |
| scanningv2Imagesbomextractor.remotebody.s3.secretAccessKey | string | `""` |  |
| scanningv2Imagesbomextractor.remotebody.s3.serviceAccountName | string | `"nats-remotebody"` |  |
| scanningv2Imagesbomextractor.remotebody.s3.usePresignedUrl | bool | `false` |  |
| scanningv2Imagesbomextractor.remotebody.thresholdBytes | string | `"8388608"` |  |
| scanningv2Imagesbomextractor.replicaCount | int | `2` |  |
| scanningv2Imagesbomextractor.repositoryPrefix | string | `"secure"` |  |
| scanningv2Imagesbomextractor.resources.scanningv2Imagesbomextractor.limits.cpu | string | `"1"` |  |
| scanningv2Imagesbomextractor.resources.scanningv2Imagesbomextractor.limits.memory | string | `"1Gi"` |  |
| scanningv2Imagesbomextractor.resources.scanningv2Imagesbomextractor.requests.cpu | string | `"1"` |  |
| scanningv2Imagesbomextractor.resources.scanningv2Imagesbomextractor.requests.memory | string | `"1Gi"` |  |
| scanningv2Imagesbomextractor.scaler.enabled | bool | `false` |  |
| scanningv2Imagesbomextractor.scaler.ise.cpuThreshold | int | `80` |  |
| scanningv2Imagesbomextractor.scaler.ise.extractRequestInQueueThreshold | int | `10000` |  |
| scanningv2Imagesbomextractor.scaler.ise.maxReplicaCount | int | `40` |  |
| scanningv2Imagesbomextractor.scaler.ise.memoryThreshold | int | `80` |  |
| scanningv2Imagesbomextractor.scaler.ise.minReplicaCount | int | `2` |  |
| scanningv2Imagesbomextractor.serviceAccount | string | `"sysdigcloud-scanningv2-imagesbomextractor"` |  |
| scanningv2Imagesbomextractor.serviceDependencies.scanningv2Credentialstore.enabled | bool | `false` |  |
| scanningv2Imagesbomextractor.serviceDependencies.scanningv2Credentialstore.grpc.endpoint | string | `"sysdigcloud-scanningv2-credentialstore-api-grpc-headless:6000"` |  |
| scanningv2Imagesbomextractor.serviceDependencies.scanningv2Credentialstore.grpc.tlsSkip | bool | `true` |  |
| scanningv2Imagesbomextractor.serviceDependencies.scanningv2Sbom.enabled | bool | `true` |  |
| scanningv2Imagesbomextractor.serviceDependencies.scanningv2Sbom.grpc.endpoint | string | `"sysdigcloud-scanningv2-sbom-api-grpc-headless:6000"` |  |
| scanningv2Imagesbomextractor.serviceDependencies.scanningv2Sbom.grpc.tlsSkip | bool | `true` |  |
| scanningv2Imagesbomextractor.sslVerifyCertificate | bool | `true` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-notifier

![Version: 2.0.0-260306163300-main-v010109d](https://img.shields.io/badge/Version-2.0.0--260306163300--main--v010109d-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning V2 Notifier Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.scanningv2Notifier.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.clickhouse.enabled | bool | `true` |  |
| global.clickhouse.readerPassword | string | `"password"` |  |
| global.dnsName | string | `""` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Notifier.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Notifier.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Notifier.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Notifier.db | string | `"scanningv2_notifier"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Notifier.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Notifier.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Notifier.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Notifier.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Notifier.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Notifier.username | string | `"scanningv2_notifier_user"` |  |
| global.legacyRedis.redisClientsSecure.scanning.password | string | `nil` |  |
| global.legacyRedis.redisClientsSecure.scanning.pubCaCrt | string | `nil` |  |
| global.legacyRedis.redisClientsSecure.scanning.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.8"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| scanningv2Notifier.authorizationService.enabled | bool | `false` |  |
| scanningv2Notifier.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| scanningv2Notifier.automationScheduler.interval | string | `"3m"` |  |
| scanningv2Notifier.automationScheduler.startDelay | string | `"10s"` |  |
| scanningv2Notifier.automations.config.notificationMaxQueryTimeRange | string | `"15m"` |  |
| scanningv2Notifier.automations.http.endpoint | string | `"http://sysdigcloud-platform-alerts-api:7004"` |  |
| scanningv2Notifier.clickhouse.database | string | `"sysdig"` |  |
| scanningv2Notifier.clickhouse.enabled | bool | `false` |  |
| scanningv2Notifier.clickhouse.endpoint | string | `"clickhouse-shards.sysdig.svc.cluster.local:9440"` |  |
| scanningv2Notifier.clickhouse.password | string | `"change-me"` |  |
| scanningv2Notifier.clickhouse.query.debounceTime | string | `"0"` |  |
| scanningv2Notifier.clickhouse.query.maxPageSize | int | `10000` |  |
| scanningv2Notifier.clickhouse.tlsSkip | bool | `true` |  |
| scanningv2Notifier.clickhouse.username | string | `"reader"` |  |
| scanningv2Notifier.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-notifier-notification"` |  |
| scanningv2Notifier.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-notifier-notification"` |  |
| scanningv2Notifier.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/notifier"` |  |
| scanningv2Notifier.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-notifier-http"` |  |
| scanningv2Notifier.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Notifier.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Notifier.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Notifier.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Notifier.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Notifier.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Notifier.ingress[0].name | string | `"sysdigcloud-scanningv2-notifier-ingress"` |  |
| scanningv2Notifier.loggingLevel | string | `"INFO"` |  |
| scanningv2Notifier.nats.connection.tlsEnabled | bool | `true` |  |
| scanningv2Notifier.nats.connection.url | string | `"nats"` |  |
| scanningv2Notifier.nats.riskacceptance.durable | string | `"notifier-riskacceptance"` |  |
| scanningv2Notifier.nats.riskacceptance.name | string | `"vm-secure-notifier-riskacceptance"` |  |
| scanningv2Notifier.nats.riskacceptance.stream | string | `"secure-vm-riskmanager-events"` |  |
| scanningv2Notifier.nats.riskacceptance.subject | string | `"secure.vm.riskmanager.events.>"` |  |
| scanningv2Notifier.nats.scanresponse.durable | string | `"notifier-scanresponse"` |  |
| scanningv2Notifier.nats.scanresponse.name | string | `"vm-secure-notifier-scanresponse"` |  |
| scanningv2Notifier.nats.scanresponse.stream | string | `"secure-vm-scanner-scan-response"` |  |
| scanningv2Notifier.nats.scanresponse.subject | string | `"secure.vm.scanner.scan.response.*.*.*"` |  |
| scanningv2Notifier.notificationScheduler.interval | string | `"15m"` |  |
| scanningv2Notifier.notificationScheduler.startDelay | string | `"10s"` |  |
| scanningv2Notifier.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Notifier.remotebody.enabled | bool | `false` |  |
| scanningv2Notifier.remotebody.pullerBackends | string | `"s3"` |  |
| scanningv2Notifier.remotebody.s3.cloudProvider | string | `""` |  |
| scanningv2Notifier.remotebody.s3.region | string | `""` |  |
| scanningv2Notifier.replicaCount | int | `3` |  |
| scanningv2Notifier.repositoryPrefix | string | `"secure"` |  |
| scanningv2Notifier.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2Notifier.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2Notifier.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2Notifier.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2Notifier.resources.scanningv2Notifier.limits.cpu | int | `2` |  |
| scanningv2Notifier.resources.scanningv2Notifier.limits.memory | string | `"1Gi"` |  |
| scanningv2Notifier.resources.scanningv2Notifier.requests.cpu | int | `2` |  |
| scanningv2Notifier.resources.scanningv2Notifier.requests.memory | string | `"1Gi"` |  |
| scanningv2Notifier.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| scanningv2Notifier.scaler.clusterName | string | `""` |  |
| scanningv2Notifier.scaler.enabled | bool | `false` |  |
| scanningv2Notifier.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| scanningv2Notifier.scaler.worker.maxReplicaCount | int | `10` |  |
| scanningv2Notifier.scaler.worker.messagesInQueueThreshold | int | `1000` |  |
| scanningv2Notifier.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Notifier.sysql.enabled | bool | `true` |  |
| scanningv2Notifier.sysql.grpc.endpoint | string | `"secure-sysql-api:6000"` |  |
| scanningv2Notifier.sysql.grpc.maxResponseSize | string | `"134217728"` |  |
| scanningv2Notifier.sysql.grpc.tlsSkip | string | `"true"` |  |
| scanningv2Notifier.sysql.query.debounceTime | string | `"0"` |  |
| scanningv2Notifier.sysql.version | string | `"0.17.7"` |  |
| scanningv2Notifier.ticketing.maxConcurrency | int | `50` |  |
| scanningv2Notifier.ticketing.publishBatchSize | int | `100` |  |
| scanningv2Notifier.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 60\n    endpointOverrides:\n      notifier_write: 60\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-pkgmeta

![Version: 2.0.1-260219001929-main-v2ad4c15](https://img.shields.io/badge/Version-2.0.1--260219001929--main--v2ad4c15-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning pkgmeta API

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.scanningv2Pkgmeta.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.pkgMeta.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.pkgMeta.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.pkgMeta.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.pkgMeta.db | string | `"pkgmeta"` |  |
| global.legacyPostgres.postgresDatabases.pkgMeta.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.pkgMeta.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.pkgMeta.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.pkgMeta.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.pkgMeta.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.pkgMeta.username | string | `"pkgmeta_user"` |  |
| global.legacyS3.s3.pkgMetaApi.bucket | string | `"change-me-bucket-name"` |  |
| global.legacyS3.s3.pkgMetaApi.bucketPrefix | string | `"etl/pkgmeta"` |  |
| global.legacyS3.s3.pkgMetaApi.cloudProvider | string | `"aws"` |  |
| global.legacyS3.s3.pkgMetaApi.region | string | `"change-me-region-name"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scanningv2.airgappedFeeds | bool | `false` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.scanningv2.proxy.enable | bool | `false` |  |
| global.secretsManagement.generate | bool | `true` |  |
| scanningv2Pkgmeta.audit.enabled | bool | `true` |  |
| scanningv2Pkgmeta.debug | string | `"false"` |  |
| scanningv2Pkgmeta.ingressV2.defaultServiceName | string | `"sysdigcloud-scanningv2-pkgmeta-api-http"` |  |
| scanningv2Pkgmeta.ingressV2.defaultServicePort | int | `7000` |  |
| scanningv2Pkgmeta.ingressV2.name | string | `"sysdigcloud-scanningv2-pkgmeta-ingress"` |  |
| scanningv2Pkgmeta.ingressV2.paths.sysdigcloudScanningv2PkgmetaApi.isPrivate | bool | `true` |  |
| scanningv2Pkgmeta.ingressV2.paths.sysdigcloudScanningv2PkgmetaApi.isPublic | bool | `true` |  |
| scanningv2Pkgmeta.ingressV2.paths.sysdigcloudScanningv2PkgmetaApi.path | string | `"/api/scanning/pkgmeta/v2"` |  |
| scanningv2Pkgmeta.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-pkgmeta-api"` |  |
| scanningv2Pkgmeta.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-pkgmeta-api"` |  |
| scanningv2Pkgmeta.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/pkgmeta/v2"` |  |
| scanningv2Pkgmeta.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-pkgmeta-api-http"` |  |
| scanningv2Pkgmeta.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Pkgmeta.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Pkgmeta.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Pkgmeta.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Pkgmeta.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Pkgmeta.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Pkgmeta.ingress[0].name | string | `"sysdigcloud-scanningv2-pkgmeta-ingress"` |  |
| scanningv2Pkgmeta.installationType | string | `"saas"` |  |
| scanningv2Pkgmeta.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Pkgmeta.replaceDbTimeout | string | `"60m"` |  |
| scanningv2Pkgmeta.replicaCount | int | `2` |  |
| scanningv2Pkgmeta.repositoryPrefix | string | `"secure"` |  |
| scanningv2Pkgmeta.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2Pkgmeta.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2Pkgmeta.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2Pkgmeta.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2Pkgmeta.resources.scanningv2Pkgmeta.limits.cpu | string | `"500m"` |  |
| scanningv2Pkgmeta.resources.scanningv2Pkgmeta.limits.memory | string | `"2Gi"` |  |
| scanningv2Pkgmeta.resources.scanningv2Pkgmeta.requests.cpu | string | `"500m"` |  |
| scanningv2Pkgmeta.resources.scanningv2Pkgmeta.requests.memory | string | `"2Gi"` |  |
| scanningv2Pkgmeta.scaler.api.cpuThreshold | int | `70` |  |
| scanningv2Pkgmeta.scaler.api.maxReplicaCount | int | `8` |  |
| scanningv2Pkgmeta.scaler.api.memoryThreshold | int | `70` |  |
| scanningv2Pkgmeta.scaler.api.minReplicaCount | int | `2` |  |
| scanningv2Pkgmeta.scaler.enabled | bool | `false` |  |
| scanningv2Pkgmeta.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Pkgmeta.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 3000\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |
| scanningv2Pkgmeta.tpa.indexload.enabled | string | `"false"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-policies

![Version: 2.0.0-260219001929-main-v2ad4c15](https://img.shields.io/badge/Version-2.0.0--260219001929--main--v2ad4c15-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning Policies API

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.scanningv2Policies.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.dnsName | string | `""` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Policies.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Policies.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Policies.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Policies.db | string | `"policies"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Policies.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Policies.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Policies.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Policies.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Policies.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Policies.username | string | `"policies"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| scanningv2Policies.audit.enabled | string | `"true"` |  |
| scanningv2Policies.authorizationService.enabled | bool | `false` |  |
| scanningv2Policies.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| scanningv2Policies.ingressV2.defaultServiceName | string | `"sysdigcloud-scanningv2-policies-api-http"` |  |
| scanningv2Policies.ingressV2.defaultServicePort | int | `7000` |  |
| scanningv2Policies.ingressV2.name | string | `"sysdigcloud-scanningv2-policies-api-ingress"` |  |
| scanningv2Policies.ingressV2.paths.sysdigcloudScanningv2PoliciesApi.isPrivate | bool | `true` |  |
| scanningv2Policies.ingressV2.paths.sysdigcloudScanningv2PoliciesApi.isPublic | bool | `true` |  |
| scanningv2Policies.ingressV2.paths.sysdigcloudScanningv2PoliciesApi.path | string | `"/api/scanning/policies/v2"` |  |
| scanningv2Policies.ingressV2.paths.sysdigcloudScanningv2PoliciesApiV3.isPrivate | bool | `true` |  |
| scanningv2Policies.ingressV2.paths.sysdigcloudScanningv2PoliciesApiV3.isPublic | bool | `true` |  |
| scanningv2Policies.ingressV2.paths.sysdigcloudScanningv2PoliciesApiV3.path | string | `"/api/scanning/policies/v3"` |  |
| scanningv2Policies.ingressV2.paths.sysdigcloudScanningv2PoliciesSupplyChain.isPrivate | bool | `true` |  |
| scanningv2Policies.ingressV2.paths.sysdigcloudScanningv2PoliciesSupplyChain.isPublic | bool | `true` |  |
| scanningv2Policies.ingressV2.paths.sysdigcloudScanningv2PoliciesSupplyChain.path | string | `"/api/supplychain/v1"` |  |
| scanningv2Policies.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-policies-api"` |  |
| scanningv2Policies.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-policies-api"` |  |
| scanningv2Policies.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/policies/v2"` |  |
| scanningv2Policies.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-policies-api-http"` |  |
| scanningv2Policies.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Policies.ingress[0].hosts[1].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-policies-v3-api"` |  |
| scanningv2Policies.ingress[0].hosts[1].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-policies-v3-api"` |  |
| scanningv2Policies.ingress[0].hosts[1].paths[0].path | string | `"/api/scanning/policies/v3"` |  |
| scanningv2Policies.ingress[0].hosts[1].paths[0].serviceName | string | `"sysdigcloud-scanningv2-policies-api-http"` |  |
| scanningv2Policies.ingress[0].hosts[1].paths[0].servicePort | int | `7000` |  |
| scanningv2Policies.ingress[0].hosts[2].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-supplychain-v1-api"` |  |
| scanningv2Policies.ingress[0].hosts[2].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-supplychain-v1-api"` |  |
| scanningv2Policies.ingress[0].hosts[2].paths[0].path | string | `"/api/supplychain/v1"` |  |
| scanningv2Policies.ingress[0].hosts[2].paths[0].serviceName | string | `"sysdigcloud-scanningv2-policies-api-http"` |  |
| scanningv2Policies.ingress[0].hosts[2].paths[0].servicePort | int | `7000` |  |
| scanningv2Policies.ingress[0].hosts[3].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-policies-public-api-v1"` |  |
| scanningv2Policies.ingress[0].hosts[3].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-policies-public-api-v1"` |  |
| scanningv2Policies.ingress[0].hosts[3].paths[0].path | string | `"/secure/vulnerability/v1/policies"` |  |
| scanningv2Policies.ingress[0].hosts[3].paths[0].serviceName | string | `"sysdigcloud-scanningv2-policies-api-http"` |  |
| scanningv2Policies.ingress[0].hosts[3].paths[0].servicePort | int | `7000` |  |
| scanningv2Policies.ingress[0].hosts[3].paths[1].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-bundles-public-api-v1"` |  |
| scanningv2Policies.ingress[0].hosts[3].paths[1].openshiftRouteName | string | `"sysdigcloud-scanningv2-bundles-public-api-v1"` |  |
| scanningv2Policies.ingress[0].hosts[3].paths[1].path | string | `"/secure/vulnerability/v1/bundles"` |  |
| scanningv2Policies.ingress[0].hosts[3].paths[1].serviceName | string | `"sysdigcloud-scanningv2-policies-api-http"` |  |
| scanningv2Policies.ingress[0].hosts[3].paths[1].servicePort | int | `7000` |  |
| scanningv2Policies.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Policies.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Policies.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Policies.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Policies.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Policies.ingress[0].name | string | `"sysdigcloud-scanningv2-policies-api-ingress"` |  |
| scanningv2Policies.loggingLevel | string | `"INFO"` |  |
| scanningv2Policies.nats.secure.enabled | string | `"true"` |  |
| scanningv2Policies.nats.url | string | `"nats"` |  |
| scanningv2Policies.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Policies.replicaCount | int | `3` |  |
| scanningv2Policies.repositoryPrefix | string | `"secure"` |  |
| scanningv2Policies.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2Policies.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2Policies.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2Policies.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2Policies.resources.scanningv2PoliciesApi.limits.cpu | int | `1` |  |
| scanningv2Policies.resources.scanningv2PoliciesApi.limits.memory | string | `"512Mi"` |  |
| scanningv2Policies.resources.scanningv2PoliciesApi.requests.cpu | int | `1` |  |
| scanningv2Policies.resources.scanningv2PoliciesApi.requests.memory | string | `"512Mi"` |  |
| scanningv2Policies.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Policies.store.timeout | string | `"15s"` |  |
| scanningv2Policies.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 60\n    endpointOverrides:\n      runtime_scanner_policies_read: 1000\n      public_api_read: 100\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-registry-scanner

![Version: 2.1.1-260310143434-main-v7bac9c1](https://img.shields.io/badge/Version-2.1.1--260310143434--main--v7bac9c1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure VM Registry API View

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.scanningv2RegistryScanner.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.authorizationService.enabled | bool | `false` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2RegistryScanner.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2RegistryScanner.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2RegistryScanner.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2RegistryScanner.db | string | `"scanningv2_registryscanner"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2RegistryScanner.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2RegistryScanner.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2RegistryScanner.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2RegistryScanner.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2RegistryScanner.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2RegistryScanner.username | string | `"scanningv2_registryscanner_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.8"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.zones.platformService.endpoint | string | `"sysdigcloud-platform-zones-service-grpc:8091"` |  |
| global.zones.platformService.tlsSkip | string | `"true"` |  |
| scanningv2RegistryScanner.analyticsEnabled | bool | `false` |  |
| scanningv2RegistryScanner.authorizationService.enabled | bool | `false` |  |
| scanningv2RegistryScanner.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| scanningv2RegistryScanner.ingressV2.defaultServiceName | string | `"sysdigcloud-scanningv2-registry-scanner-api-http"` |  |
| scanningv2RegistryScanner.ingressV2.defaultServicePort | int | `8080` |  |
| scanningv2RegistryScanner.ingressV2.name | string | `"sysdigcloud-scanningv2-registry-scanner-api-ingress"` |  |
| scanningv2RegistryScanner.ingressV2.paths.sysdigcloudRegistryscannerApi.isPrivate | bool | `true` |  |
| scanningv2RegistryScanner.ingressV2.paths.sysdigcloudRegistryscannerApi.isPublic | bool | `true` |  |
| scanningv2RegistryScanner.ingressV2.paths.sysdigcloudRegistryscannerApi.path | string | `"/api/registryscanner/v1"` |  |
| scanningv2RegistryScanner.ingressV2.paths.sysdigcloudRegistryscannerApiRegistryResults.isPrivate | bool | `true` |  |
| scanningv2RegistryScanner.ingressV2.paths.sysdigcloudRegistryscannerApiRegistryResults.isPublic | bool | `true` |  |
| scanningv2RegistryScanner.ingressV2.paths.sysdigcloudRegistryscannerApiRegistryResults.path | string | `"/secure/vulnerability/v1beta1/registry-results"` |  |
| scanningv2RegistryScanner.ingressV2.paths.sysdigcloudRegistryscannerApiRegistryResultsV1.isPrivate | bool | `true` |  |
| scanningv2RegistryScanner.ingressV2.paths.sysdigcloudRegistryscannerApiRegistryResultsV1.isPublic | bool | `true` |  |
| scanningv2RegistryScanner.ingressV2.paths.sysdigcloudRegistryscannerApiRegistryResultsV1.path | string | `"/secure/vulnerability/v1/registry-results"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-registryscanner-api"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-registryscanner-api"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[0].path | string | `"/api/registryscanner/v1"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-registry-scanner-api-http"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-registryscanner-api-registry-results"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-registryscanner-api-registry-results"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[1].path | string | `"/secure/vulnerability/v1beta1/registry-results"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-scanningv2-registry-scanner-api-http"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[1].servicePort | int | `8080` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-registryscanner-api-registry-results-v1"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-registryscanner-api-registry-results-v1"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[2].path | string | `"/secure/vulnerability/v1/registry-results"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-scanningv2-registry-scanner-api-http"` |  |
| scanningv2RegistryScanner.ingress[0].hosts[0].paths[2].servicePort | int | `8080` |  |
| scanningv2RegistryScanner.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2RegistryScanner.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2RegistryScanner.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2RegistryScanner.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2RegistryScanner.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2RegistryScanner.ingress[0].name | string | `"sysdigcloud-scanningv2-registry-scanner-api-ingress"` |  |
| scanningv2RegistryScanner.loggingLevel | string | `"INFO"` |  |
| scanningv2RegistryScanner.nats.connection.tlsEnabled | bool | `true` |  |
| scanningv2RegistryScanner.nats.connection.url | string | `"nats"` |  |
| scanningv2RegistryScanner.nats.scanresponse.name | string | `"registry-worker"` |  |
| scanningv2RegistryScanner.nats.scanresponse.stream | string | `"secure-vm-scanner-scan-response"` |  |
| scanningv2RegistryScanner.nats.scanresponse.subject | string | `"secure.vm.scanner.scan.response.registry.*.success"` |  |
| scanningv2RegistryScanner.progressDeadlineSeconds | int | `1200` |  |
| scanningv2RegistryScanner.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2RegistryScanner.remotebody.enabled | bool | `false` |  |
| scanningv2RegistryScanner.remotebody.pullerBackends | string | `"s3"` |  |
| scanningv2RegistryScanner.remotebody.s3.cloudProvider | string | `""` |  |
| scanningv2RegistryScanner.remotebody.s3.region | string | `""` |  |
| scanningv2RegistryScanner.replicaCount | int | `2` |  |
| scanningv2RegistryScanner.repositoryPrefix | string | `"secure"` |  |
| scanningv2RegistryScanner.resources.scanningv2RegistryScanner.limits.cpu | int | `1` |  |
| scanningv2RegistryScanner.resources.scanningv2RegistryScanner.limits.memory | string | `"512Mi"` |  |
| scanningv2RegistryScanner.resources.scanningv2RegistryScanner.requests.cpu | int | `1` |  |
| scanningv2RegistryScanner.resources.scanningv2RegistryScanner.requests.memory | string | `"512Mi"` |  |
| scanningv2RegistryScanner.serviceAccountName | string | `"sysdig"` |  |
| scanningv2RegistryScanner.serviceDependencies.zonesApi.grpc.endpoint | string | `"secure-iac-policy-service:8080"` |  |
| scanningv2RegistryScanner.serviceDependencies.zonesApi.grpc.tlsSkip | string | `"true"` |  |
| scanningv2RegistryScanner.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 60\n    endpointOverrides:\n      public_api_read: 60\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-reporting

![Version: 2.0.0-260310140744-main-v03747ea](https://img.shields.io/badge/Version-2.0.0--260310140744--main--v03747ea-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Reporting

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.scanningv2Reporting.serviceToken | string | `""` |  |
| global.apps | string | `"secure"` |  |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch"}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` | defines the kind of installation possible values are: "local", "onprem", "saas". |
| global.legacyPostgres.postgresDatabases.scanningv2Reporting.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Reporting.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Reporting.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Reporting.db | string | `"scanningv2_reporting"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Reporting.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Reporting.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Reporting.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Reporting.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Reporting.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Reporting.username | string | `"scanningv2_reporting_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| scanningv2Reporting.aws.bucket | string | `""` |  |
| scanningv2Reporting.aws.endpoint | string | `""` |  |
| scanningv2Reporting.aws.region | string | `""` |  |
| scanningv2Reporting.aws.writeEndpoint | string | `""` |  |
| scanningv2Reporting.cloudstorage.bucket | string | `""` |  |
| scanningv2Reporting.customLabels | string | `"[]"` |  |
| scanningv2Reporting.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| scanningv2Reporting.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| scanningv2Reporting.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| scanningv2Reporting.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| scanningv2Reporting.enabled | bool | `true` |  |
| scanningv2Reporting.loggingLevel | string | `"INFO"` |  |
| scanningv2Reporting.nats.connection.tlsEnabled | bool | `true` |  |
| scanningv2Reporting.nats.connection.url | string | `"nats"` |  |
| scanningv2Reporting.nats.scanresponse.ackWait | string | `"5m"` |  |
| scanningv2Reporting.nats.scanresponse.maxInFlight | int | `1024` |  |
| scanningv2Reporting.nats.scanresponse.name | string | `"secure-vm-reporting-worker-scanresponse"` |  |
| scanningv2Reporting.nats.scanresponse.pullBatchSize | int | `2` |  |
| scanningv2Reporting.nats.scanresponse.stream | string | `"secure-vm-scanner-scan-response"` |  |
| scanningv2Reporting.nats.scanresponse.subject | string | `"secure.vm.scanner.scan.response.*.*.success"` |  |
| scanningv2Reporting.opensearch | object | `{"host":"localhost:9200","nodeDiscoveryInterval":0,"nodeDiscoveryOnStart":false,"password":null,"tlsskipverify":false,"username":"admin"}` | configuration for the service dedicated openserach instance. |
| scanningv2Reporting.opensearch.password | string | `nil` | opensearch instance password, if not explicitly set it will be randomly generated by helm. |
| scanningv2Reporting.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Reporting.remotebody.enabled | bool | `false` |  |
| scanningv2Reporting.remotebody.pullerBackends | string | `"s3"` |  |
| scanningv2Reporting.remotebody.s3.cloudProvider | string | `""` |  |
| scanningv2Reporting.remotebody.s3.region | string | `""` |  |
| scanningv2Reporting.reportingApi.audit.enabled | bool | `true` |  |
| scanningv2Reporting.reportingApi.authorizationService.enabled | bool | `false` |  |
| scanningv2Reporting.reportingApi.authorizationService.endpoint | string | `"sysdig-authorization-service:9602"` |  |
| scanningv2Reporting.reportingApi.grpcReportingScheduleUrl | string | `"sysdigcloud-scanningv2-reporting-scheduler-grpc:8080"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-reporting-api"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-reporting-api"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/reporting/v2"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-reporting-api-http"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[1].apiGatewayAuthEnabled | bool | `false` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-reporting-api-schedules"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[1].apiGatewayUseRegex | bool | `true` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-scanningv2-reporting-api-schedules"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[1].path | string | `"/api/scanning/reporting/v2/schedules/([a-zA-Z0-9]+)/reports/([a-zA-Z0-9]+)/download"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-scanningv2-reporting-api-http"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-servicenow-api"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-scanningv2-servicenow-api"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[2].path | string | `"/api/scanning/servicenow/v2"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-scanningv2-reporting-api-http"` |  |
| scanningv2Reporting.reportingApi.ingress[0].hosts[0].paths[2].servicePort | int | `7000` |  |
| scanningv2Reporting.reportingApi.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Reporting.reportingApi.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Reporting.reportingApi.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Reporting.reportingApi.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Reporting.reportingApi.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Reporting.reportingApi.ingress[0].name | string | `"sysdigcloud-scanningv2-reporting-ingress"` |  |
| scanningv2Reporting.reportingApi.replicaCount | int | `1` |  |
| scanningv2Reporting.reportingApi.resources.scanningv2ReportingApi.limits.cpu | string | `"500m"` |  |
| scanningv2Reporting.reportingApi.resources.scanningv2ReportingApi.limits.memory | string | `"512Mi"` |  |
| scanningv2Reporting.reportingApi.resources.scanningv2ReportingApi.requests.cpu | string | `"500m"` |  |
| scanningv2Reporting.reportingApi.resources.scanningv2ReportingApi.requests.memory | string | `"512Mi"` |  |
| scanningv2Reporting.reportingGenerator.poolSize | int | `4` |  |
| scanningv2Reporting.reportingGenerator.replicaCount | int | `1` |  |
| scanningv2Reporting.reportingGenerator.resources.scanningv2ReportingGenerator.limits.cpu | int | `2` |  |
| scanningv2Reporting.reportingGenerator.resources.scanningv2ReportingGenerator.limits.memory | string | `"1Gi"` |  |
| scanningv2Reporting.reportingGenerator.resources.scanningv2ReportingGenerator.requests.cpu | int | `2` |  |
| scanningv2Reporting.reportingGenerator.resources.scanningv2ReportingGenerator.requests.memory | string | `"1Gi"` |  |
| scanningv2Reporting.reportingGenerator.searchRoutines | int | `4` |  |
| scanningv2Reporting.reportingGenerator.searchSize | int | `1000` |  |
| scanningv2Reporting.reportingJanitor.resources.scanningv2ReportingJanitor.limits.cpu | string | `"250m"` |  |
| scanningv2Reporting.reportingJanitor.resources.scanningv2ReportingJanitor.limits.memory | string | `"250Mi"` |  |
| scanningv2Reporting.reportingJanitor.resources.scanningv2ReportingJanitor.requests.cpu | string | `"250m"` |  |
| scanningv2Reporting.reportingJanitor.resources.scanningv2ReportingJanitor.requests.memory | string | `"250Mi"` |  |
| scanningv2Reporting.reportingJanitor.retentionCoefficient | int | `1` |  |
| scanningv2Reporting.reportingJanitor.schedule | string | `"0 * * * *"` |  |
| scanningv2Reporting.reportingScheduler.jobRetention | string | `"336h"` |  |
| scanningv2Reporting.reportingScheduler.jobTimeout | string | `"3h"` |  |
| scanningv2Reporting.reportingScheduler.maxRetry | int | `3` |  |
| scanningv2Reporting.reportingScheduler.reloadTimeout | string | `"6h"` |  |
| scanningv2Reporting.reportingScheduler.replicaCount | int | `1` |  |
| scanningv2Reporting.reportingScheduler.resources.scanningv2ReportingScheduler.limits.cpu | string | `"500m"` |  |
| scanningv2Reporting.reportingScheduler.resources.scanningv2ReportingScheduler.limits.memory | string | `"512Mi"` |  |
| scanningv2Reporting.reportingScheduler.resources.scanningv2ReportingScheduler.requests.cpu | string | `"500m"` |  |
| scanningv2Reporting.reportingScheduler.resources.scanningv2ReportingScheduler.requests.memory | string | `"512Mi"` |  |
| scanningv2Reporting.reportingWorker.autoscaler.enabled | bool | `true` |  |
| scanningv2Reporting.reportingWorker.autoscaler.maxReplicaCount | int | `12` |  |
| scanningv2Reporting.reportingWorker.autoscaler.minReplicaCount | int | `2` |  |
| scanningv2Reporting.reportingWorker.autoscaler.percentOfUnreadMessagesThreshold | int | `5` |  |
| scanningv2Reporting.reportingWorker.containerScopeNumberOfShards | int | `3` | Number of shards for container scope index |
| scanningv2Reporting.reportingWorker.containerVulnNumberOfShards | int | `12` | Number of shards for container vulnerability index |
| scanningv2Reporting.reportingWorker.forceElasticsearchMigrations | bool | `false` | Fail if elasticsearch has more updated migrations than the service |
| scanningv2Reporting.reportingWorker.hostScopeNumberOfShards | int | `3` | Number of shards for host scope index |
| scanningv2Reporting.reportingWorker.hostVulnNumberOfShards | int | `12` | Number of shards for host vulnerability index |
| scanningv2Reporting.reportingWorker.k8sScopeNumberOfShards | int | `3` | Number of shards for k8s scope index |
| scanningv2Reporting.reportingWorker.k8sVulnNumberOfShards | int | `12` | Number of shards for k8s vulnerability index |
| scanningv2Reporting.reportingWorker.osBatchSize | int | `10000` | Max number of documents in each insertion request to elasticsearch |
| scanningv2Reporting.reportingWorker.pipelineScopeNumberOfShards | int | `3` | Number of shards for pipeline scope index |
| scanningv2Reporting.reportingWorker.pipelineVulnNumberOfShards | int | `3` | Number of shards for pipeline vulnerability index |
| scanningv2Reporting.reportingWorker.registryScopeNumberOfShards | int | `3` | Number of shards for registry scope index |
| scanningv2Reporting.reportingWorker.registryVulnNumberOfShards | int | `12` | Number of shards for registry vulnerability index |
| scanningv2Reporting.reportingWorker.replicaCount | int | `2` |  |
| scanningv2Reporting.reportingWorker.resources.scanningv2ReportingWorker.limits.cpu | int | `4` |  |
| scanningv2Reporting.reportingWorker.resources.scanningv2ReportingWorker.limits.memory | string | `"8Gi"` |  |
| scanningv2Reporting.reportingWorker.resources.scanningv2ReportingWorker.requests.cpu | int | `2` |  |
| scanningv2Reporting.reportingWorker.resources.scanningv2ReportingWorker.requests.memory | string | `"2Gi"` |  |
| scanningv2Reporting.reportingWorker.storeUpsert | bool | `true` | Configuration to determine if upsert operation should be used in store operations instead of index |
| scanningv2Reporting.reportingWorker.workerPoolSize | int | `8` | Size of the worker pool used by the reporting worker on each pod |
| scanningv2Reporting.repositoryPrefix | string | `"secure"` |  |
| scanningv2Reporting.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2Reporting.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2Reporting.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2Reporting.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2Reporting.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Reporting.storageDriver | string | `""` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-riskmanager

![Version: 2.0.0-260311100325-main-va1e8d64](https://img.shields.io/badge/Version-2.0.0--260311100325--main--va1e8d64-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning riskmanager API

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.scanningv2Riskmanager.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.dnsName | string | `"change-me.com"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2riskmanager.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2riskmanager.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2riskmanager.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2riskmanager.db | string | `"riskmanager"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2riskmanager.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2riskmanager.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2riskmanager.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2riskmanager.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2riskmanager.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2riskmanager.username | string | `"riskmanager"` |  |
| global.legacyRedis.redisClientsSecure.scanning.password | string | `nil` |  |
| global.legacyRedis.redisClientsSecure.scanning.pubCaCrt | string | `nil` |  |
| global.legacyRedis.redisClientsSecure.scanning.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| scanningv2Riskmanager.audit.enabled | string | `"true"` |  |
| scanningv2Riskmanager.exceptionScheduler.aboutToExpireExceptionsMaxDays | int | `30` |  |
| scanningv2Riskmanager.exceptionScheduler.deleteExpiredExceptionsGraceDaysPeriod | int | `90` |  |
| scanningv2Riskmanager.exceptionScheduler.interval | string | `"24h"` |  |
| scanningv2Riskmanager.exceptionScheduler.startDelay | string | `"10s"` |  |
| scanningv2Riskmanager.ingressV2.defaultServiceName | string | `"sysdigcloud-scanningv2-riskmanager-api-http"` |  |
| scanningv2Riskmanager.ingressV2.defaultServicePort | int | `7000` |  |
| scanningv2Riskmanager.ingressV2.name | string | `"sysdigcloud-scanningv2-riskmanager-api-ingress"` |  |
| scanningv2Riskmanager.ingressV2.paths.sysdigcloudScanningv2ExceptionsApi.isPrivate | bool | `true` |  |
| scanningv2Riskmanager.ingressV2.paths.sysdigcloudScanningv2ExceptionsApi.isPublic | bool | `true` |  |
| scanningv2Riskmanager.ingressV2.paths.sysdigcloudScanningv2ExceptionsApi.path | string | `"/api/exception/v1"` |  |
| scanningv2Riskmanager.ingressV2.paths.sysdigcloudScanningv2RiskmanagerApi.isPrivate | bool | `true` |  |
| scanningv2Riskmanager.ingressV2.paths.sysdigcloudScanningv2RiskmanagerApi.isPublic | bool | `true` |  |
| scanningv2Riskmanager.ingressV2.paths.sysdigcloudScanningv2RiskmanagerApi.path | string | `"/api/scanning/riskmanager/v2"` |  |
| scanningv2Riskmanager.ingressV2.paths.sysdigcloudScanningv2RiskmanagerApiV1beta1.isPublicApi | bool | `true` |  |
| scanningv2Riskmanager.ingressV2.paths.sysdigcloudScanningv2RiskmanagerApiV1beta1.path | string | `"/secure/vulnerability/v1beta1/accepted-risks"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-riskmanager-api"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-riskmanager-api"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/riskmanager/v2"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-riskmanager-api-http"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-exception-api"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-scanningv2-exception-api"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[1].path | string | `"/api/exception/v1"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-scanningv2-riskmanager-api-http"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-riskmanager-api-v1beta1"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-scanningv2-riskmanager-api-v1beta1"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[2].path | string | `"/secure/vulnerability/v1beta1/accepted-risks"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-scanningv2-riskmanager-api-http"` |  |
| scanningv2Riskmanager.ingress[0].hosts[0].paths[2].servicePort | int | `7000` |  |
| scanningv2Riskmanager.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Riskmanager.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Riskmanager.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Riskmanager.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Riskmanager.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Riskmanager.ingress[0].name | string | `"sysdigcloud-scanningv2-riskmanager-api-ingress"` |  |
| scanningv2Riskmanager.maxDefinitions | string | `"{}"` |  |
| scanningv2Riskmanager.nats.secure.enabled | string | `"true"` |  |
| scanningv2Riskmanager.nats.url | string | `"nats"` |  |
| scanningv2Riskmanager.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Riskmanager.replicaCount | int | `3` |  |
| scanningv2Riskmanager.repositoryPrefix | string | `"secure"` |  |
| scanningv2Riskmanager.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2Riskmanager.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2Riskmanager.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2Riskmanager.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2Riskmanager.resources.scanningv2RiskmanagerApi.limits.cpu | int | `1` |  |
| scanningv2Riskmanager.resources.scanningv2RiskmanagerApi.limits.memory | string | `"1Gi"` |  |
| scanningv2Riskmanager.resources.scanningv2RiskmanagerApi.requests.cpu | int | `1` |  |
| scanningv2Riskmanager.resources.scanningv2RiskmanagerApi.requests.memory | string | `"1Gi"` |  |
| scanningv2Riskmanager.riskmanagerJanitor.aboutToExpireRisksMaxDays | int | `30` |  |
| scanningv2Riskmanager.riskmanagerJanitor.tickPeriod | string | `"24h"` |  |
| scanningv2Riskmanager.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Riskmanager.store.timeout | string | `"15s"` |  |
| scanningv2Riskmanager.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 60\n    endpointOverrides:\n      scanners_endpoint_limit: 1000\n      public_api_endpoint_limit: 100\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-runtimeview

![Version: 2.0.0-260310120538-main-va68374e](https://img.shields.io/badge/Version-2.0.0--260310120538--main--va68374e-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning Runtime View

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.dnsName | string | `"change-me.com"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Runtimeview.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Runtimeview.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Runtimeview.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Runtimeview.db | string | `"scanningv2_runtimeview"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Runtimeview.host | string | `"localhost"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Runtimeview.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Runtimeview.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Runtimeview.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Runtimeview.sslmode | string | `"required"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Runtimeview.username | string | `"scanningv2_runtimeview_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.zones.endpoint | string | `"secure-iac-policy-service:8080"` |  |
| global.zones.platformService.endpoint | string | `"sysdigcloud-platform-zones-service-grpc:8091"` |  |
| global.zones.platformService.tlsSkip | string | `"true"` |  |
| global.zones.tlsSkip | string | `"true"` |  |
| scanningv2Runtimeview.analyticsEnabled | bool | `false` |  |
| scanningv2Runtimeview.authorizationServiceEndpoint | string | `"sysdig-authorization-service:9602"` |  |
| scanningv2Runtimeview.ingressV2.defaultServiceName | string | `"sysdigcloud-scanningv2-runtimeview-http"` |  |
| scanningv2Runtimeview.ingressV2.defaultServicePort | int | `7000` |  |
| scanningv2Runtimeview.ingressV2.name | string | `"sysdigcloud-scanningv2-runtimeview-ingress"` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2IsRunning.isPrivate | bool | `true` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2IsRunning.isPublic | bool | `true` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2IsRunning.path | string | `"/api/scanning/runtime/v2/workflows/isRunning"` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2Labels.isPrivate | bool | `true` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2Labels.isPublic | bool | `true` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2Labels.path | string | `"/api/scanning/runtime/v2/workflows/labels"` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2PublicV1.isPrivate | bool | `true` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2PublicV1.isPublic | bool | `true` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2PublicV1.path | string | `"/secure/vulnerability/v1/runtime-results"` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2PublicV1Beta1.isPrivate | bool | `true` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2PublicV1Beta1.isPublic | bool | `true` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2PublicV1Beta1.path | string | `"/secure/vulnerability/v1beta1/runtime-results"` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2Results.isPrivate | bool | `true` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2Results.isPublic | bool | `true` |  |
| scanningv2Runtimeview.ingressV2.paths.sysdigcloudScanningv2RuntimeviewV2Results.path | string | `"/api/scanning/runtime/v2/workflows/results"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-runtimeview-running"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-runtimeview-running"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/runtime/v2/workflows/isRunning"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-runtimeview-http"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-runtimeview-labels"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-scanningv2-runtimeview-labels"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[1].path | string | `"/api/scanning/runtime/v2/workflows/labels"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-scanningv2-runtimeview-http"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-runtimeview-results"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-scanningv2-runtimeview-results"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[2].path | string | `"/api/scanning/runtime/v2/workflows/results"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-scanningv2-runtimeview-http"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[2].servicePort | int | `7000` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[3].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-runtimeview-vulnerability"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[3].openshiftRouteName | string | `"sysdigcloud-scanningv2-runtimeview-vulnerability"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[3].path | string | `"/secure/vulnerability/v1beta1/runtime-results"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[3].serviceName | string | `"sysdigcloud-scanningv2-runtimeview-http"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[3].servicePort | int | `7000` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[4].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-runtimeview-results-v1"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[4].openshiftRouteName | string | `"sysdigcloud-scanningv2-runtimeview-results-v1"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[4].path | string | `"/secure/vulnerability/v1/runtime-results"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[4].serviceName | string | `"sysdigcloud-scanningv2-runtimeview-http"` |  |
| scanningv2Runtimeview.ingress[0].hosts[0].paths[4].servicePort | int | `7000` |  |
| scanningv2Runtimeview.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Runtimeview.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Runtimeview.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Runtimeview.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Runtimeview.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Runtimeview.ingress[0].name | string | `"sysdigcloud-scanningv2-runtimeview-ingress"` |  |
| scanningv2Runtimeview.loggingLevel | string | `"INFO"` |  |
| scanningv2Runtimeview.nats.scanresult.batcher.enabled | bool | `true` |  |
| scanningv2Runtimeview.nats.scanresult.batcher.flushPeriod | string | `"1s"` |  |
| scanningv2Runtimeview.nats.scanresult.batcher.flushingRoutines | int | `2` |  |
| scanningv2Runtimeview.nats.scanresult.batcher.maxBatchSize | int | `4` |  |
| scanningv2Runtimeview.nats.scanresult.batcher.maxBufferSize | int | `4` |  |
| scanningv2Runtimeview.nats.scanresult.batcher.timeout | string | `"180s"` |  |
| scanningv2Runtimeview.nats.scanresult.durable | string | `"runtimeview-scanresults"` |  |
| scanningv2Runtimeview.nats.scanresult.name | string | `"runtimeview-scanresults"` |  |
| scanningv2Runtimeview.nats.scanresult.pullBatch | int | `4` |  |
| scanningv2Runtimeview.nats.scanresult.stream | string | `"secure-vm-scanner-scan-response"` |  |
| scanningv2Runtimeview.nats.scanresult.subject | string | `"secure.vm.scanner.scan.response.runtime.*.*"` |  |
| scanningv2Runtimeview.nats.secure.enabled | string | `"true"` |  |
| scanningv2Runtimeview.nats.url | string | `"nats"` |  |
| scanningv2Runtimeview.nats.workload.batcher.enabled | bool | `true` |  |
| scanningv2Runtimeview.nats.workload.batcher.flushPeriod | string | `"1s"` |  |
| scanningv2Runtimeview.nats.workload.batcher.flushingRoutines | int | `6` |  |
| scanningv2Runtimeview.nats.workload.batcher.maxBatchSize | int | `16` |  |
| scanningv2Runtimeview.nats.workload.batcher.maxBufferSize | int | `16` |  |
| scanningv2Runtimeview.nats.workload.batcher.timeout | string | `"180s"` |  |
| scanningv2Runtimeview.nats.workload.durable | string | `"runtimeview-workloads"` |  |
| scanningv2Runtimeview.nats.workload.name | string | `"runtimeview-workloads"` |  |
| scanningv2Runtimeview.nats.workload.pullBatch | int | `16` |  |
| scanningv2Runtimeview.nats.workload.stream | string | `"secure-vm-scanner-workloads"` |  |
| scanningv2Runtimeview.nats.workload.subject | string | `"secure.vm.scanner.workloads.runtime.*"` |  |
| scanningv2Runtimeview.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Runtimeview.remotebody.enabled | bool | `false` |  |
| scanningv2Runtimeview.remotebody.pullerBackends | string | `"s3"` |  |
| scanningv2Runtimeview.remotebody.s3.cloudProvider | string | `""` |  |
| scanningv2Runtimeview.remotebody.s3.region | string | `""` |  |
| scanningv2Runtimeview.replicaCount | int | `2` |  |
| scanningv2Runtimeview.repositoryPrefix | string | `"secure"` |  |
| scanningv2Runtimeview.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2Runtimeview.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2Runtimeview.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2Runtimeview.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2Runtimeview.resources.scanningv2Runtimeview.limits.cpu | int | `2` |  |
| scanningv2Runtimeview.resources.scanningv2Runtimeview.limits.memory | string | `"4Gi"` |  |
| scanningv2Runtimeview.resources.scanningv2Runtimeview.requests.cpu | int | `2` |  |
| scanningv2Runtimeview.resources.scanningv2Runtimeview.requests.memory | string | `"4Gi"` |  |
| scanningv2Runtimeview.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| scanningv2Runtimeview.scaler.enabled | bool | `true` |  |
| scanningv2Runtimeview.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| scanningv2Runtimeview.scaler.worker.maxReplicaCount | int | `10` |  |
| scanningv2Runtimeview.scaler.worker.messagesInQueueThreshold | int | `10000` |  |
| scanningv2Runtimeview.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Runtimeview.store.janitorDelta | string | `"8h"` |  |
| scanningv2Runtimeview.store.janitorTick | string | `"1h"` |  |
| scanningv2Runtimeview.store.scanResponseTTL | string | `"1h"` |  |
| scanningv2Runtimeview.store.timeout | string | `"15s"` |  |
| scanningv2Runtimeview.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 60\n    endpointOverrides:\n      public_api_read: 60\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |
| scanningv2Runtimeview.useAuthorizationService | bool | `false` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-sbom

![Version: 2.0.0-260311111208-main-v4b37b4d](https://img.shields.io/badge/Version-2.0.0--260311111208--main--v4b37b4d-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Sbom API

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","hostname":"sysdigcloud-elasticsearch","port":9200,"scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"useCertManager":false,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.legacyRedis.redisClientsSecure.scanning.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `"change_me"` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.enabled | bool | `false` |  |
| global.legacyRedis.redisTls.sentinel.masterSet | string | `"primary"` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.tls | bool | `false` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.scaler.authenticationRef | string | `""` |  |
| global.scaler.clusterName | string | `""` |  |
| global.scaler.serverAddress | string | `""` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| scanningv2Sbom.audit.enabled | bool | `true` |  |
| scanningv2Sbom.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| scanningv2Sbom.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| scanningv2Sbom.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| scanningv2Sbom.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| scanningv2Sbom.features.customerMetrics.enabled | bool | `false` |  |
| scanningv2Sbom.features.layerAnalysis.enabled | bool | `true` |  |
| scanningv2Sbom.features.persistSbom.natsjs.consumerName | string | `"sbom-api"` |  |
| scanningv2Sbom.features.persistSbom.natsjs.consumerPullBatch | int | `8` |  |
| scanningv2Sbom.features.persistSbom.natsjs.enabled | bool | `true` |  |
| scanningv2Sbom.features.persistSbom.natsjs.tlsEnabled | bool | `true` |  |
| scanningv2Sbom.features.persistSbom.natsjs.url | string | `"nats"` |  |
| scanningv2Sbom.features.persistSbom.natsjs.workerPoolSize | int | `4` |  |
| scanningv2Sbom.features.refresher.enabled | bool | `true` |  |
| scanningv2Sbom.features.refresher.scheduledAt | string | `"11:00:00"` |  |
| scanningv2Sbom.features.tpaEnrichment.enabled | bool | `false` |  |
| scanningv2Sbom.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-sbom-api-1"` |  |
| scanningv2Sbom.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-sbom-api"` |  |
| scanningv2Sbom.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/sbom/v2"` |  |
| scanningv2Sbom.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-sbom-api-http"` |  |
| scanningv2Sbom.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Sbom.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-sbom-api-2"` |  |
| scanningv2Sbom.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-scanningv2-sbom-api-2"` |  |
| scanningv2Sbom.ingress[0].hosts[0].paths[1].path | string | `"/secure/vulnerability/v1beta1/sboms"` |  |
| scanningv2Sbom.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-scanningv2-sbom-api-http"` |  |
| scanningv2Sbom.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| scanningv2Sbom.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Sbom.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Sbom.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Sbom.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Sbom.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Sbom.ingress[0].name | string | `"sysdigcloud-scanningv2-sbom-ingress"` |  |
| scanningv2Sbom.opensearch.forceMigrations | bool | `false` |  |
| scanningv2Sbom.opensearch.queryProfiler.enabled | bool | `false` |  |
| scanningv2Sbom.opensearch.queryProfiler.latencyTreshold | string | `"1s"` |  |
| scanningv2Sbom.opensearch.readEncodedSbom | string | `"true"` |  |
| scanningv2Sbom.opensearch.writeEncodedSbom | string | `"true"` |  |
| scanningv2Sbom.pprof.enabled | bool | `false` |  |
| scanningv2Sbom.pprof.port | string | `"6060"` |  |
| scanningv2Sbom.redis | string | `nil` |  |
| scanningv2Sbom.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Sbom.remotebody.pullerBackends | string | `"s3"` |  |
| scanningv2Sbom.remotebody.s3.bucket | string | `""` |  |
| scanningv2Sbom.remotebody.s3.cloudProvider | string | `""` |  |
| scanningv2Sbom.remotebody.s3.region | string | `""` |  |
| scanningv2Sbom.replicaCount | int | `2` |  |
| scanningv2Sbom.repositoryPrefix | string | `"secure"` |  |
| scanningv2Sbom.resources.scanningv2SbomApi.limits.cpu | int | `2` |  |
| scanningv2Sbom.resources.scanningv2SbomApi.limits.memory | string | `"2Gi"` |  |
| scanningv2Sbom.resources.scanningv2SbomApi.requests.cpu | int | `2` |  |
| scanningv2Sbom.resources.scanningv2SbomApi.requests.memory | string | `"2Gi"` |  |
| scanningv2Sbom.scaler.api.cpuThreshold | int | `70` |  |
| scanningv2Sbom.scaler.api.maxReplicaCount | int | `15` |  |
| scanningv2Sbom.scaler.api.memoryThreshold | int | `70` |  |
| scanningv2Sbom.scaler.api.minReplicaCount | int | `2` |  |
| scanningv2Sbom.scaler.api.scanRequestInQueueThreshold | int | `2000` |  |
| scanningv2Sbom.scaler.enabled | bool | `false` |  |
| scanningv2Sbom.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Sbom.serviceDependencies.api.endpoint | string | `"http://sysdigcloud-api:8080"` |  |
| scanningv2Sbom.serviceDependencies.api.tlsSkip | string | `"false"` |  |
| scanningv2Sbom.serviceDependencies.pkgmeta.endpoint | string | `"sysdigcloud-scanningv2-pkgmeta-api-grpc:6000"` |  |
| scanningv2Sbom.serviceDependencies.pkgmeta.tlsSkip | bool | `true` |  |
| scanningv2Sbom.stats.enabled | bool | `false` |  |
| scanningv2Sbom.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 60\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-scanengine

![Version: 2.0.0-260223093009-main-vd562d21](https://img.shields.io/badge/Version-2.0.0--260223093009--main--vd562d21-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scan Engine

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.dnsName | string | `""` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.scanningv2.enabled | bool | `true` |  |
| scanningv2Scanengine.checkFilteredInUseFiles | bool | `false` |  |
| scanningv2Scanengine.customerMetrics.enabled | bool | `false` |  |
| scanningv2Scanengine.fingerprintsApi.enabled | string | `"true"` |  |
| scanningv2Scanengine.fingerprintsApi.grpc.endpoint | string | `"sysdigcloud-fingerprints-files-grpc:6000"` |  |
| scanningv2Scanengine.fingerprintsApi.grpc.tlsSkip | string | `"true"` |  |
| scanningv2Scanengine.handleTimeout | string | `"5m"` |  |
| scanningv2Scanengine.loggingLevel | string | `"INFO"` |  |
| scanningv2Scanengine.maxRetries | int | `3` |  |
| scanningv2Scanengine.natsJS.consumer.ackWait | string | `"1800s"` |  |
| scanningv2Scanengine.natsJS.consumer.maxInFlight | int | `2048` |  |
| scanningv2Scanengine.natsJS.consumer.msgMaxRetries | int | `30` |  |
| scanningv2Scanengine.natsJS.consumer.msgRetryTimeout | string | `"120s"` |  |
| scanningv2Scanengine.natsJS.consumer.nakDeliverBackOff | string | `"2s,5s,10s"` |  |
| scanningv2Scanengine.natsJS.consumer.name | string | `"scanengineworker.requests-consumer"` |  |
| scanningv2Scanengine.natsJS.consumer.pullBatch | int | `8` |  |
| scanningv2Scanengine.natsJS.consumer.streamName | string | `"secure-vm-scanner-scan-request"` |  |
| scanningv2Scanengine.natsJS.consumer.subject | string | `"secure.vm.scanner.scan.request.*.*"` |  |
| scanningv2Scanengine.natsJS.reqreply.enabled | bool | `true` |  |
| scanningv2Scanengine.natsJS.reqreply.subject | string | `"secure.vm.scanner.scan.reqreply.*.*"` |  |
| scanningv2Scanengine.natsJS.secure.enabled | string | `"true"` |  |
| scanningv2Scanengine.natsJS.url | string | `"nats"` |  |
| scanningv2Scanengine.policiesApi.grpc.endpoint | string | `"sysdigcloud-scanningv2-policies-api-grpc:6000"` |  |
| scanningv2Scanengine.policiesApi.grpc.tlsSkip | string | `"true"` |  |
| scanningv2Scanengine.probes.readiness.endpoint | string | `"/probes/readiness"` |  |
| scanningv2Scanengine.probes.readiness.port | int | `25001` |  |
| scanningv2Scanengine.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Scanengine.remotebody.enabled | bool | `false` |  |
| scanningv2Scanengine.remotebody.pusherBackend | string | `"s3"` |  |
| scanningv2Scanengine.remotebody.s3.accessKeyId | string | `""` |  |
| scanningv2Scanengine.remotebody.s3.bucket | string | `""` |  |
| scanningv2Scanengine.remotebody.s3.cloudProvider | string | `""` |  |
| scanningv2Scanengine.remotebody.s3.endpoint | string | `""` |  |
| scanningv2Scanengine.remotebody.s3.presignedUrlTtl | string | `"3h"` |  |
| scanningv2Scanengine.remotebody.s3.region | string | `""` |  |
| scanningv2Scanengine.remotebody.s3.secretAccessKey | string | `""` |  |
| scanningv2Scanengine.remotebody.s3.serviceAccountName | string | `"nats-remotebody-rw"` |  |
| scanningv2Scanengine.remotebody.s3.usePresignedUrl | bool | `false` |  |
| scanningv2Scanengine.remotebody.thresholdBytes | string | `"8388608"` |  |
| scanningv2Scanengine.replicaCount | int | `2` |  |
| scanningv2Scanengine.repositoryPrefix | string | `"secure"` |  |
| scanningv2Scanengine.resources.scanningv2ScanengineWorker.limits.cpu | int | `2` |  |
| scanningv2Scanengine.resources.scanningv2ScanengineWorker.limits.memory | string | `"4Gi"` |  |
| scanningv2Scanengine.resources.scanningv2ScanengineWorker.requests.cpu | float | `1.5` |  |
| scanningv2Scanengine.resources.scanningv2ScanengineWorker.requests.memory | string | `"3Gi"` |  |
| scanningv2Scanengine.riskManagerApi.grpc.endpoint | string | `"sysdigcloud-scanningv2-riskmanager-api-grpc:6000"` |  |
| scanningv2Scanengine.riskManagerApi.grpc.tlsSkip | string | `"true"` |  |
| scanningv2Scanengine.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| scanningv2Scanengine.scaler.clusterName | string | `""` |  |
| scanningv2Scanengine.scaler.enabled | bool | `false` |  |
| scanningv2Scanengine.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| scanningv2Scanengine.scaler.worker.cpuThreshold | int | `70` |  |
| scanningv2Scanengine.scaler.worker.maxReplicaCount | int | `40` |  |
| scanningv2Scanengine.scaler.worker.memoryThreshold | int | `70` |  |
| scanningv2Scanengine.scaler.worker.scanRequestInQueueThreshold | int | `2000` |  |
| scanningv2Scanengine.vulnsApi.grpc.endpoint | string | `"sysdigcloud-scanningv2-vulns-api-grpc-headless:6000"` |  |
| scanningv2Scanengine.vulnsApi.grpc.tlsSkip | string | `"true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-scanrequestor

![Version: 2.0.0-260209125133-main-v11a3075](https://img.shields.io/badge/Version-2.0.0--260209125133--main--v11a3075-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning Scan Requestor

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.cassandra.password | string | `""` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.cassandra.useCertManager | bool | `false` |  |
| global.cassandra.user | string | `"cassandrauser"` |  |
| global.dnsName | string | `""` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2ScanRequestor.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2ScanRequestor.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2ScanRequestor.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2ScanRequestor.db | string | `"scanningv2_scanrequestor"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2ScanRequestor.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2ScanRequestor.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2ScanRequestor.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2ScanRequestor.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2ScanRequestor.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2ScanRequestor.username | string | `"scanningv2_scanrequestor_user"` |  |
| global.legacyRedis.redisClientsSecure.scanning.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.legacyS3.s3.scanRequestor | object | `{}` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| scanningv2Scanrequestor.arnRole | string | `""` |  |
| scanningv2Scanrequestor.customerMetricsEnabled | bool | `false` |  |
| scanningv2Scanrequestor.enabled | bool | `true` |  |
| scanningv2Scanrequestor.expiryGracePeriodHours | int | `8` |  |
| scanningv2Scanrequestor.gcpServiceAccount | string | `""` |  |
| scanningv2Scanrequestor.ingressV2.defaultServiceName | string | `"sysdigcloud-scanningv2-scanrequestor-api-http"` |  |
| scanningv2Scanrequestor.ingressV2.defaultServicePort | int | `7000` |  |
| scanningv2Scanrequestor.ingressV2.name | string | `"sysdigcloud-scanningv2-scanrequestor-ingress"` |  |
| scanningv2Scanrequestor.ingressV2.paths.sysdigcloudScanningv2ScanrequestorScannow.isPrivate | bool | `true` |  |
| scanningv2Scanrequestor.ingressV2.paths.sysdigcloudScanningv2ScanrequestorScannow.isPublic | bool | `true` |  |
| scanningv2Scanrequestor.ingressV2.paths.sysdigcloudScanningv2ScanrequestorScannow.path | string | `"/api/scanning/scanrequestor/v2/scanrequests"` |  |
| scanningv2Scanrequestor.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-scanrequestor-scannow"` |  |
| scanningv2Scanrequestor.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-scanrequestor-scanrequests"` |  |
| scanningv2Scanrequestor.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/scanrequestor/v2/scanrequests"` |  |
| scanningv2Scanrequestor.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-scanrequestor-api-http"` |  |
| scanningv2Scanrequestor.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Scanrequestor.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Scanrequestor.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Scanrequestor.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Scanrequestor.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Scanrequestor.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Scanrequestor.ingress[0].name | string | `"sysdigcloud-scanningv2-scanrequestor-ingress"` |  |
| scanningv2Scanrequestor.loggingLevel | string | `"INFO"` |  |
| scanningv2Scanrequestor.nats.ise.durable | string | `"scanrequestor-ise-events"` |  |
| scanningv2Scanrequestor.nats.ise.maxDeliver | int | `10` |  |
| scanningv2Scanrequestor.nats.ise.maxInFlight | int | `2048` |  |
| scanningv2Scanrequestor.nats.ise.nakDeliverBackoff | string | `"15s"` |  |
| scanningv2Scanrequestor.nats.ise.name | string | `"ise-events"` |  |
| scanningv2Scanrequestor.nats.ise.pullBatch | int | `48` |  |
| scanningv2Scanrequestor.nats.ise.stream | string | `"secure-vm-ise-extract-response"` |  |
| scanningv2Scanrequestor.nats.ise.subject | string | `"secure.vm.ise.extract.response.ondemand.scanrequestor.*"` |  |
| scanningv2Scanrequestor.nats.partitionProcessing.durable | string | `"scanrequestor-partition-processing-request"` |  |
| scanningv2Scanrequestor.nats.partitionProcessing.maxDeliver | int | `1` |  |
| scanningv2Scanrequestor.nats.partitionProcessing.maxInFlight | int | `2048` |  |
| scanningv2Scanrequestor.nats.partitionProcessing.messenger.fetchTimeout | string | `"5m"` |  |
| scanningv2Scanrequestor.nats.partitionProcessing.messenger.handleTimeout | string | `"5m"` |  |
| scanningv2Scanrequestor.nats.partitionProcessing.name | string | `"scanrequestor-partition-processing-request"` |  |
| scanningv2Scanrequestor.nats.partitionProcessing.pullBatch | int | `16` |  |
| scanningv2Scanrequestor.nats.partitionProcessing.stream | string | `"secure-vm-scanrequestor-partition-processing-request"` |  |
| scanningv2Scanrequestor.nats.partitionProcessing.subject | string | `"secure.vm.scanrequestor.partition.processing.requests"` |  |
| scanningv2Scanrequestor.nats.persistSbomResponse.durable | string | `"scanrequestor-persistsbom-response"` |  |
| scanningv2Scanrequestor.nats.persistSbomResponse.maxDeliver | int | `10` |  |
| scanningv2Scanrequestor.nats.persistSbomResponse.name | string | `"scanrequestor-persistsbom-response"` |  |
| scanningv2Scanrequestor.nats.persistSbomResponse.pullBatch | int | `20` |  |
| scanningv2Scanrequestor.nats.persistSbomResponse.stream | string | `"secure-vm-sbomapi-persist-sbom-response"` |  |
| scanningv2Scanrequestor.nats.persistSbomResponse.subject | string | `"secure.vm.sbomapi.persist-sbom.response.*.*.success"` |  |
| scanningv2Scanrequestor.nats.policies.durable | string | `"scanrequestor-policies-events"` |  |
| scanningv2Scanrequestor.nats.policies.maxDeliver | int | `10` |  |
| scanningv2Scanrequestor.nats.policies.maxInFlight | int | `2048` |  |
| scanningv2Scanrequestor.nats.policies.messenger.fetchTimeout | string | `"30s"` |  |
| scanningv2Scanrequestor.nats.policies.messenger.pullTimeoutRetryMaxWait | string | `"10s"` |  |
| scanningv2Scanrequestor.nats.policies.name | string | `"scanrequestor-policies-events"` |  |
| scanningv2Scanrequestor.nats.policies.pullBatch | int | `48` |  |
| scanningv2Scanrequestor.nats.policies.stream | string | `"secure-vm-policies-events"` |  |
| scanningv2Scanrequestor.nats.policies.subject | string | `"secure.vm.policies.events.>"` |  |
| scanningv2Scanrequestor.nats.riskaccept.durable | string | `"scanrequestor-riskmanager-events"` |  |
| scanningv2Scanrequestor.nats.riskaccept.maxDeliver | int | `10` |  |
| scanningv2Scanrequestor.nats.riskaccept.maxInFlight | int | `2048` |  |
| scanningv2Scanrequestor.nats.riskaccept.messenger.fetchTimeout | string | `"30s"` |  |
| scanningv2Scanrequestor.nats.riskaccept.messenger.pullTimeoutRetryMaxWait | string | `"10s"` |  |
| scanningv2Scanrequestor.nats.riskaccept.name | string | `"scanrequestor-riskaccept-events"` |  |
| scanningv2Scanrequestor.nats.riskaccept.pullBatch | int | `48` |  |
| scanningv2Scanrequestor.nats.riskaccept.stream | string | `"secure-vm-riskmanager-events"` |  |
| scanningv2Scanrequestor.nats.riskaccept.subject | string | `"secure.vm.riskmanager.events.risk.update"` |  |
| scanningv2Scanrequestor.nats.scanresponses.durable | string | `"scanrequestor-scanresponses-runtime"` |  |
| scanningv2Scanrequestor.nats.scanresponses.maxDeliver | int | `10` |  |
| scanningv2Scanrequestor.nats.scanresponses.maxInFlight | int | `1024` |  |
| scanningv2Scanrequestor.nats.scanresponses.messenger.asyncHandlerRoutines | int | `3` |  |
| scanningv2Scanrequestor.nats.scanresponses.name | string | `"scanrequestor-scanresponses-runtime"` |  |
| scanningv2Scanrequestor.nats.scanresponses.pullBatch | int | `10` |  |
| scanningv2Scanrequestor.nats.scanresponses.stream | string | `"secure-vm-scanner-scan-response"` |  |
| scanningv2Scanrequestor.nats.scanresponses.subject | string | `"secure.vm.scanner.scan.response.*.*.*"` |  |
| scanningv2Scanrequestor.nats.secure.enabled | string | `"true"` |  |
| scanningv2Scanrequestor.nats.url | string | `"nats"` |  |
| scanningv2Scanrequestor.nats.vulnsetl.durable | string | `"scanrequestor-vulns-events"` |  |
| scanningv2Scanrequestor.nats.vulnsetl.maxDeliver | int | `10` |  |
| scanningv2Scanrequestor.nats.vulnsetl.maxInFlight | int | `2048` |  |
| scanningv2Scanrequestor.nats.vulnsetl.name | string | `"scanrequestor-vulns-events"` |  |
| scanningv2Scanrequestor.nats.vulnsetl.pullBatch | int | `16` |  |
| scanningv2Scanrequestor.nats.vulnsetl.stream | string | `"secure-vm-vulns-events"` |  |
| scanningv2Scanrequestor.nats.vulnsetl.subject | string | `"secure.vm.vulns.events.>"` |  |
| scanningv2Scanrequestor.nats.workloads.durable | string | `"scanrequestor-workloads-runtime"` |  |
| scanningv2Scanrequestor.nats.workloads.maxDeliver | int | `5` |  |
| scanningv2Scanrequestor.nats.workloads.maxInFlight | int | `2048` |  |
| scanningv2Scanrequestor.nats.workloads.name | string | `"scanrequestor-workloads-runtime"` |  |
| scanningv2Scanrequestor.nats.workloads.pullBatch | int | `48` |  |
| scanningv2Scanrequestor.nats.workloads.stream | string | `"secure-vm-scanner-workloads"` |  |
| scanningv2Scanrequestor.nats.workloads.subject | string | `"secure.vm.scanner.workloads.*.*"` |  |
| scanningv2Scanrequestor.partitionProcessing.requestsPerPartitionLimit | int | `25` |  |
| scanningv2Scanrequestor.partitionProcessing.requestsPerPartitionLimitPerc | int | `4` |  |
| scanningv2Scanrequestor.partitionProcessing.usePercentLimit | string | `"false"` |  |
| scanningv2Scanrequestor.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Scanrequestor.remotebody.enabled | bool | `false` |  |
| scanningv2Scanrequestor.remotebody.pullerBackends | string | `"s3"` |  |
| scanningv2Scanrequestor.remotebody.s3.cloudProvider | string | `""` |  |
| scanningv2Scanrequestor.remotebody.s3.region | string | `""` |  |
| scanningv2Scanrequestor.replicaCount | int | `1` |  |
| scanningv2Scanrequestor.repositoryPrefix | string | `"secure"` |  |
| scanningv2Scanrequestor.requestPartitionProcessingScheduler.startDelay | string | `"10s"` |  |
| scanningv2Scanrequestor.rescanOutdatedThresholdHours | int | `20` |  |
| scanningv2Scanrequestor.resources.minioCli.limits.cpu | string | `"100m"` |  |
| scanningv2Scanrequestor.resources.minioCli.limits.memory | string | `"64Mi"` |  |
| scanningv2Scanrequestor.resources.minioCli.requests.cpu | string | `"100m"` |  |
| scanningv2Scanrequestor.resources.minioCli.requests.memory | string | `"64Mi"` |  |
| scanningv2Scanrequestor.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2Scanrequestor.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2Scanrequestor.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2Scanrequestor.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2Scanrequestor.resources.scanningv2Scanrequestor.limits.cpu | int | `2` |  |
| scanningv2Scanrequestor.resources.scanningv2Scanrequestor.limits.memory | string | `"2Gi"` |  |
| scanningv2Scanrequestor.resources.scanningv2Scanrequestor.requests.cpu | int | `2` |  |
| scanningv2Scanrequestor.resources.scanningv2Scanrequestor.requests.memory | string | `"2Gi"` |  |
| scanningv2Scanrequestor.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| scanningv2Scanrequestor.scaler.clusterName | string | `""` |  |
| scanningv2Scanrequestor.scaler.enabled | bool | `false` |  |
| scanningv2Scanrequestor.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| scanningv2Scanrequestor.scaler.sr.cpuThreshold | int | `70` |  |
| scanningv2Scanrequestor.scaler.sr.maxReplicaCount | int | `10` |  |
| scanningv2Scanrequestor.scaler.sr.memoryThreshold | int | `70` |  |
| scanningv2Scanrequestor.scaler.sr.partitionsToProcessThreshold | int | `5000` |  |
| scanningv2Scanrequestor.scaler.sr.workloadsInQueueThreshold | int | `2000` |  |
| scanningv2Scanrequestor.serviceAccount | string | `"change-me"` |  |
| scanningv2Scanrequestor.storage.cassandra.compressionEnabled | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.compressionThreshold | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.datacenter | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.hosts | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.keyspace | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.maxReadRequests | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.maxWriteRequests | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.protocolVersion | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.replicationFactor | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.replicationStrategy | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.requestTimeout | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.sslCaPath | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.sslCertPath | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.sslEnabled | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.sslKeyPath | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.sslVerifyHostname | string | `""` |  |
| scanningv2Scanrequestor.storage.cassandra.ttlSec.events | string | `nil` |  |
| scanningv2Scanrequestor.storage.cassandra.ttlSec.metadata | string | `nil` |  |
| scanningv2Scanrequestor.storage.cassandra.ttlSec.state | string | `nil` |  |
| scanningv2Scanrequestor.storage.requestStore.enabled | bool | `false` |  |
| scanningv2Scanrequestor.storage.type | string | `""` |  |
| scanningv2Scanrequestor.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 5\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |
| scanningv2Scanrequestor.usePkgMasksEval | string | `"true"` |  |
| scanningv2Scanrequestor.vulnerabilityDBVersion | string | `"V3"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-scanresults

![Version: 2.0.0-260311080849-main-v7145a11](https://img.shields.io/badge/Version-2.0.0--260311080849--main--v7145a11-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning Scan Results

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.scanningv2Scanresults.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.dnsName | string | `"change-me.com"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.db | string | `"scan_results_db"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.maxconnections | int | `64` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2Scanresults.username | string | `"scan_results_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| global.scaler.clusterName | string | `"change_me"` |  |
| global.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.zones.platformService.endpoint | string | `"sysdigcloud-platform-zones-service-grpc:8091"` |  |
| global.zones.platformService.tlsSkip | string | `"true"` |  |
| scanningv2Scanresults.analyticsEnabled | bool | `false` |  |
| scanningv2Scanresults.enableCustomerLevelMetrics | bool | `true` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-scanresults-v1"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-scanresults-v1"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/scanresults/v1"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-scanresults-api-http"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-scanresults-v2"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-scanningv2-scanresults-v2"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[1].path | string | `"/api/scanning/scanresults/v2"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-scanningv2-scanresults-api-http"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[2].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-scanresults-vuln-pipeline"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[2].openshiftRouteName | string | `"sysdigcloud-scanningv2-scanresults-vuln-pipeline"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[2].path | string | `"/secure/vulnerability/v1beta1/pipeline-results"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[2].serviceName | string | `"sysdigcloud-scanningv2-scanresults-api-http"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[2].servicePort | int | `7000` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[3].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-scanresults-vuln-results"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[3].openshiftRouteName | string | `"sysdigcloud-scanningv2-scanresults-vuln-results"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[3].path | string | `"/secure/vulnerability/v1beta1/results"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[3].serviceName | string | `"sysdigcloud-scanningv2-scanresults-api-http"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[3].servicePort | int | `7000` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[4].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-scanresults-vuln-pipeline-v1"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[4].openshiftRouteName | string | `"sysdigcloud-scanningv2-scanresults-vuln-pipeline-v1"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[4].path | string | `"/secure/vulnerability/v1/pipeline-results"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[4].serviceName | string | `"sysdigcloud-scanningv2-scanresults-api-http"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[4].servicePort | int | `7000` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[5].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-scanresults-vuln-results-v1"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[5].openshiftRouteName | string | `"sysdigcloud-scanningv2-scanresults-vuln-results-v1"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[5].path | string | `"/secure/vulnerability/v1/results"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[5].serviceName | string | `"sysdigcloud-scanningv2-scanresults-api-http"` |  |
| scanningv2Scanresults.ingress[0].hosts[0].paths[5].servicePort | int | `7000` |  |
| scanningv2Scanresults.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Scanresults.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Scanresults.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Scanresults.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Scanresults.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Scanresults.ingress[0].name | string | `"sysdigcloud-scanningv2-scanresults-ingress"` |  |
| scanningv2Scanresults.loggingLevel | string | `"INFO"` |  |
| scanningv2Scanresults.nats.js.ackWait | string | `"5m"` |  |
| scanningv2Scanresults.nats.js.consumerName | string | `"scanresults-api"` |  |
| scanningv2Scanresults.nats.js.enabled | bool | `true` |  |
| scanningv2Scanresults.nats.js.streamName | string | `"secure-vm-scanner-scan-response"` |  |
| scanningv2Scanresults.nats.js.subjectFilter | string | `"secure.vm.scanner.scan.response.*.*.success"` |  |
| scanningv2Scanresults.nats.js.tlsEnabled | bool | `true` |  |
| scanningv2Scanresults.nats.js.url | string | `"nats"` |  |
| scanningv2Scanresults.partman.autovaccum.analyzeScaleFactor | string | `"0.0001"` |  |
| scanningv2Scanresults.partman.retention.admissionController | string | `"2"` |  |
| scanningv2Scanresults.partman.retention.pipeline | string | `"90"` |  |
| scanningv2Scanresults.partman.retention.registry | string | `"90"` |  |
| scanningv2Scanresults.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Scanresults.remotebody.enabled | bool | `false` |  |
| scanningv2Scanresults.remotebody.lazyLoad.enabled | bool | `false` |  |
| scanningv2Scanresults.remotebody.pullerBackends | string | `"s3"` |  |
| scanningv2Scanresults.remotebody.s3.cloudProvider | string | `""` |  |
| scanningv2Scanresults.remotebody.s3.region | string | `""` |  |
| scanningv2Scanresults.replicaCount | int | `1` |  |
| scanningv2Scanresults.repositoryPrefix | string | `"secure"` |  |
| scanningv2Scanresults.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2Scanresults.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2Scanresults.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2Scanresults.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2Scanresults.resources.scanningv2Scanresults.limits.cpu | int | `2` |  |
| scanningv2Scanresults.resources.scanningv2Scanresults.limits.memory | string | `"4Gi"` |  |
| scanningv2Scanresults.resources.scanningv2Scanresults.requests.cpu | int | `2` |  |
| scanningv2Scanresults.resources.scanningv2Scanresults.requests.memory | string | `"4Gi"` |  |
| scanningv2Scanresults.scaler.enabled | bool | `true` |  |
| scanningv2Scanresults.scaler.worker.maxReplicaCount | int | `15` |  |
| scanningv2Scanresults.scaler.worker.messagesInQueueThreshold | int | `1000` |  |
| scanningv2Scanresults.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Scanresults.serviceDependencies.vulnsApi.grpc.endpoint | string | `"sysdigcloud-scanningv2-vulns-api-grpc-headless:6000"` |  |
| scanningv2Scanresults.serviceDependencies.vulnsApi.grpc.tlsSkip | string | `"true"` |  |
| scanningv2Scanresults.serviceDependencies.zonesApi.grpc.endpoint | string | `"secure-iac-policy-service:8080"` |  |
| scanningv2Scanresults.serviceDependencies.zonesApi.grpc.tlsSkip | string | `"true"` |  |
| scanningv2Scanresults.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 60\n    endpointOverrides:\n      public_api_read: 100\n      export_api: 10\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-vulns

![Version: 2.0.1-260310153148-main-vbc16f45](https://img.shields.io/badge/Version-2.0.1--260310153148--main--vbc16f45-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning Vulns

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.deployment | string | `"kubernetes"` |  |
| global.dnsName | string | `""` |  |
| global.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.legacyRedis.redisClientsSecure.scanning.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `"change_me"` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.legacyS3.s3.vulnsApi.bucket | string | `"change-me-bucket-name"` |  |
| global.legacyS3.s3.vulnsApi.bucketPrefix | string | `"etl/artifacts"` |  |
| global.legacyS3.s3.vulnsApi.cloudProvider | string | `"aws"` |  |
| global.legacyS3.s3.vulnsApi.region | string | `"change-me-region-name"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.scaler.authenticationRef | string | `""` |  |
| global.scaler.clusterName | string | `""` |  |
| global.scaler.serverAddress | string | `""` |  |
| global.scanningv2.airgappedFeeds | bool | `false` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.scanningv2.proxy.enable | bool | `false` |  |
| global.secure.enabled | bool | `true` |  |
| scanningv2Vulns.audit.enabled | bool | `true` |  |
| scanningv2Vulns.debug | string | `""` |  |
| scanningv2Vulns.eventStoreEnabled | string | `"true"` |  |
| scanningv2Vulns.ingressV2.defaultServiceName | string | `"sysdigcloud-scanningv2-vulns-api-http"` |  |
| scanningv2Vulns.ingressV2.defaultServicePort | int | `7000` |  |
| scanningv2Vulns.ingressV2.name | string | `"sysdigcloud-scanningv2-vulns-ingress"` |  |
| scanningv2Vulns.ingressV2.paths.sysdigcloudScanningv2VulnsApi.isPrivate | bool | `true` |  |
| scanningv2Vulns.ingressV2.paths.sysdigcloudScanningv2VulnsApi.isPublic | bool | `true` |  |
| scanningv2Vulns.ingressV2.paths.sysdigcloudScanningv2VulnsApi.path | string | `"/api/scanning/vulns/v1"` |  |
| scanningv2Vulns.ingressV2.paths.sysdigcloudScanningv2VulnsApiV2.isPrivate | bool | `true` |  |
| scanningv2Vulns.ingressV2.paths.sysdigcloudScanningv2VulnsApiV2.isPublic | bool | `true` |  |
| scanningv2Vulns.ingressV2.paths.sysdigcloudScanningv2VulnsApiV2.path | string | `"/api/scanning/vulns/v2"` |  |
| scanningv2Vulns.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-vulns-api"` |  |
| scanningv2Vulns.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-vulns-api"` |  |
| scanningv2Vulns.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/vulns/v1"` |  |
| scanningv2Vulns.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-vulns-api-http"` |  |
| scanningv2Vulns.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2Vulns.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-vulns-api-2"` |  |
| scanningv2Vulns.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-scanningv2-vulns-api-2"` |  |
| scanningv2Vulns.ingress[0].hosts[0].paths[1].path | string | `"/api/scanning/vulns/v2"` |  |
| scanningv2Vulns.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-scanningv2-vulns-api-http"` |  |
| scanningv2Vulns.ingress[0].hosts[0].paths[1].servicePort | int | `7000` |  |
| scanningv2Vulns.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2Vulns.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2Vulns.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2Vulns.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2Vulns.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2Vulns.ingress[0].name | string | `"sysdigcloud-scanningv2-vulns-ingress"` |  |
| scanningv2Vulns.installationType | string | `"saas"` |  |
| scanningv2Vulns.mainDBDir | string | `"/tmp"` |  |
| scanningv2Vulns.nats.eventDbUpdateSubject | string | `"secure.vm.vulns.events.db.update"` |  |
| scanningv2Vulns.nats.secure.enabled | bool | `true` |  |
| scanningv2Vulns.nats.url | string | `"nats"` |  |
| scanningv2Vulns.pyroscope.enabled | bool | `false` |  |
| scanningv2Vulns.pyroscope.loggingEnabled | bool | `false` |  |
| scanningv2Vulns.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2Vulns.replicaCount | int | `2` |  |
| scanningv2Vulns.repositoryPrefix | string | `"secure"` |  |
| scanningv2Vulns.resources.scanningv2VulnsApi.limits.cpu | int | `3` |  |
| scanningv2Vulns.resources.scanningv2VulnsApi.limits.memory | string | `"4Gi"` |  |
| scanningv2Vulns.resources.scanningv2VulnsApi.requests.cpu | int | `2` |  |
| scanningv2Vulns.resources.scanningv2VulnsApi.requests.memory | string | `"4Gi"` |  |
| scanningv2Vulns.sbomAPIGrpcAddress | string | `"sysdigcloud-scanningv2-sbom-api-grpc-headless:6000"` |  |
| scanningv2Vulns.scaler.api.cpuThreshold | int | `70` |  |
| scanningv2Vulns.scaler.api.maxReplicaCount | int | `15` |  |
| scanningv2Vulns.scaler.api.memoryThreshold | int | `70` |  |
| scanningv2Vulns.scaler.api.minReplicaCount | int | `2` |  |
| scanningv2Vulns.scaler.api.scanRequestInQueueThreshold | int | `2000` |  |
| scanningv2Vulns.scaler.enabled | bool | `false` |  |
| scanningv2Vulns.serviceAccountName | string | `"sysdig"` |  |
| scanningv2Vulns.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 300\n    endpointOverrides:\n      vuln_detail_api: 100\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |
| scanningv2Vulns.vulnDBVersion | string | `"V3B4"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# scanningv2-workloaddetector

![Version: 1.0.0-260312161601-main-v868734b](https://img.shields.io/badge/Version-1.0.0--260312161601--main--v868734b-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Scanning Workload Detector

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.deployment | string | `"kubernetes"` |  |
| global.dnsName | string | `""` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2WorkloadDetector.admindb | string | `"root_db"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2WorkloadDetector.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2WorkloadDetector.adminusername | string | `"root_user"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2WorkloadDetector.db | string | `"scanningv2_workloaddetector"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2WorkloadDetector.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2WorkloadDetector.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2WorkloadDetector.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scanningv2WorkloadDetector.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scanningv2WorkloadDetector.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scanningv2WorkloadDetector.username | string | `"scanningv2_workloaddetector_user"` |  |
| global.legacyRedis.redisClientsSecure.scanning.tls | bool | `false` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useCertManager | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.scanningv2.enabled | bool | `true` |  |
| global.secretsManagement.generate | bool | `true` |  |
| scanningv2WorkloadDetector.enabled | bool | `true` |  |
| scanningv2WorkloadDetector.ingressV2.defaultServiceName | string | `"sysdigcloud-scanningv2-workloaddetector-api-http"` |  |
| scanningv2WorkloadDetector.ingressV2.defaultServicePort | int | `7000` |  |
| scanningv2WorkloadDetector.ingressV2.name | string | `"sysdigcloud-scanningv2-workloaddetector-ingress"` |  |
| scanningv2WorkloadDetector.ingressV2.paths.sysdigcloudScanningv2WorkloadDetectorV2.isPrivate | bool | `true` |  |
| scanningv2WorkloadDetector.ingressV2.paths.sysdigcloudScanningv2WorkloadDetectorV2.isPublic | bool | `true` |  |
| scanningv2WorkloadDetector.ingressV2.paths.sysdigcloudScanningv2WorkloadDetectorV2.path | string | `"/api/scanning/workloaddetector/v2"` |  |
| scanningv2WorkloadDetector.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-scanningv2-workloaddetector-v2"` |  |
| scanningv2WorkloadDetector.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-scanningv2-workloaddetector-v2"` |  |
| scanningv2WorkloadDetector.ingress[0].hosts[0].paths[0].path | string | `"/api/scanning/workloaddetector/v2"` |  |
| scanningv2WorkloadDetector.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-scanningv2-workloaddetector-api-http"` |  |
| scanningv2WorkloadDetector.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| scanningv2WorkloadDetector.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| scanningv2WorkloadDetector.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| scanningv2WorkloadDetector.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| scanningv2WorkloadDetector.ingress[0].labels.role | string | `"ingress-config"` |  |
| scanningv2WorkloadDetector.ingress[0].labels.tier | string | `"infra"` |  |
| scanningv2WorkloadDetector.ingress[0].name | string | `"sysdigcloud-scanningv2-workloaddetector-ingress"` |  |
| scanningv2WorkloadDetector.logLevel | string | `"INFO"` |  |
| scanningv2WorkloadDetector.mds.endpoint | string | `"sysdigcloud-metadata-service-server:5300"` |  |
| scanningv2WorkloadDetector.nats.detections.durable | string | `"workloaddetector-detections"` |  |
| scanningv2WorkloadDetector.nats.detections.maxDeliver | int | `5` |  |
| scanningv2WorkloadDetector.nats.detections.maxInFlight | int | `2048` |  |
| scanningv2WorkloadDetector.nats.detections.name | string | `"workloaddetector-detections"` |  |
| scanningv2WorkloadDetector.nats.detections.pullBatch | int | `48` |  |
| scanningv2WorkloadDetector.nats.detections.stream | string | `"secure-vm-scanner-workloads-detection"` |  |
| scanningv2WorkloadDetector.nats.detections.subject | string | `"secure.vm.scanner.workloads-detection.*"` |  |
| scanningv2WorkloadDetector.nats.secure.enabled | string | `"true"` |  |
| scanningv2WorkloadDetector.nats.url | string | `"nats"` |  |
| scanningv2WorkloadDetector.partitionProcessing.maxPartitionsPerRequest | int | `25` |  |
| scanningv2WorkloadDetector.partitionProcessing.scheduler.startDelay | string | `"10s"` |  |
| scanningv2WorkloadDetector.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| scanningv2WorkloadDetector.replicaCount | int | `2` |  |
| scanningv2WorkloadDetector.repositoryPrefix | string | `"secure"` |  |
| scanningv2WorkloadDetector.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| scanningv2WorkloadDetector.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| scanningv2WorkloadDetector.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| scanningv2WorkloadDetector.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| scanningv2WorkloadDetector.resources.scanningv2WorkloadDetector.limits.cpu | int | `1` |  |
| scanningv2WorkloadDetector.resources.scanningv2WorkloadDetector.limits.memory | string | `"1Gi"` |  |
| scanningv2WorkloadDetector.resources.scanningv2WorkloadDetector.requests.cpu | int | `1` |  |
| scanningv2WorkloadDetector.resources.scanningv2WorkloadDetector.requests.memory | string | `"1Gi"` |  |
| scanningv2WorkloadDetector.scaler.api.cpuThreshold | int | `70` |  |
| scanningv2WorkloadDetector.scaler.api.maxReplicaCount | int | `5` |  |
| scanningv2WorkloadDetector.scaler.api.memoryThreshold | int | `70` |  |
| scanningv2WorkloadDetector.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| scanningv2WorkloadDetector.scaler.clusterName | string | `""` |  |
| scanningv2WorkloadDetector.scaler.enabled | bool | `false` |  |
| scanningv2WorkloadDetector.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| scanningv2WorkloadDetector.serviceAccountName | string | `"sysdig"` |  |
| scanningv2WorkloadDetector.storage.event | string | `nil` |  |
| scanningv2WorkloadDetector.storage.metadata | string | `nil` |  |
| scanningv2WorkloadDetector.tierlimitsconfig | string | `"apiRateLimits:\n  tierDependent: true\n  default:\n    limit: 10\nfeatureEndpointToggles:\n  tierDependent: false\n  default:\n    enabled: true"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-config-service

![Version: 1.23.731-260312194542-main-vd02e9449](https://img.shields.io/badge/Version-1.23.731--260312194542--main--vd02e9449-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Config Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.iac.imagePullSecrets[0] | string | `"sysdigcloud-pull-secret"` |  |
| global.namespace | string | `"sysdig"` |  |
| image.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-config-service"` |  |
| image.tag | string | `"1.23.731-260312194542-main-vd02e9449"` |  |
| secureConfigService.configmap.enabled | bool | `false` |  |
| secureConfigService.enabled | bool | `true` |  |
| secureConfigService.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureConfigService.replicaCount | int | `3` |  |
| secureConfigService.repositoryPrefix | string | `"secure"` |  |
| secureConfigService.resources.configService.limits.cpu | string | `"500m"` |  |
| secureConfigService.resources.configService.limits.memory | string | `"500Mi"` |  |
| secureConfigService.resources.configService.requests.cpu | string | `"250m"` |  |
| secureConfigService.resources.configService.requests.memory | string | `"250Mi"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-graph-gatherer

![Version: 3.0.1-260219171917-main-v8d836d7](https://img.shields.io/badge/Version-3.0.1--260219171917--main--v8d836d7-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Graph VM Gatherer

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdig"` |  |
| secureGraphGatherer.audit.enabled | bool | `false` |  |
| secureGraphGatherer.azure.natsdetails | string | `"cloudingestion-azure-1,cloudingestion.azure.1.>;cloudingestion-azure-2,cloudingestion.azure.2.>;cloudingestion-azure-3,cloudingestion.azure.3.>;cloudingestion-azure-4,cloudingestion.azure.4.>"` |  |
| secureGraphGatherer.consumer.secureEvents.durable | string | `"graph-gatherer-secureevents"` |  |
| secureGraphGatherer.consumer.secureEvents.name | string | `"graph-gatherer-secureevents"` |  |
| secureGraphGatherer.consumer.secureEvents.queue | string | `"graph-gatherer-secureevents"` |  |
| secureGraphGatherer.consumer.secureEvents.streamName | string | `"events"` |  |
| secureGraphGatherer.consumer.secureEvents.subject | string | `"events.source.events.policy.>"` |  |
| secureGraphGatherer.enabled | bool | `true` |  |
| secureGraphGatherer.natsJs.secure.enabled | bool | `true` |  |
| secureGraphGatherer.natsJs.url | string | `"nats"` |  |
| secureGraphGatherer.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureGraphGatherer.repositoryPrefix | string | `"secure"` |  |
| secureGraphGatherer.resources.graphgatherer.limits.cpu | int | `2` |  |
| secureGraphGatherer.resources.graphgatherer.limits.memory | string | `"2Gi"` |  |
| secureGraphGatherer.resources.graphgatherer.requests.cpu | string | `"250m"` |  |
| secureGraphGatherer.resources.graphgatherer.requests.memory | string | `"250Mi"` |  |
| secureGraphGatherer.runtime.enabled | bool | `true` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-graph-ingestion

![Version: 3.1.0-260312225349-main-v2e28e1f](https://img.shields.io/badge/Version-3.1.0--260312225349--main--v2e28e1f-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Graph Ingestion

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.secureGraphIngestion.serviceToken | string | `"test"` |  |
| global.apps | string | `"secure"` |  |
| global.iac.imagePullSecrets[0] | string | `"sysdigcloud-pull-secret"` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.neo4jDatabases.graphingestion.adminpassword | string | `"test1234"` |  |
| global.neo4jDatabases.graphingestion.adminusername | string | `"neo4j"` |  |
| global.neo4jDatabases.graphingestion.db | string | `"neo4j"` |  |
| global.neo4jDatabases.graphingestion.endpoint | string | `"bolt://neo4j:7687"` |  |
| global.neo4jDatabases.graphingestion.maxConnectionPoolSize | int | `100` |  |
| global.neo4jDatabases.graphingestion.password | string | `"test1234"` |  |
| global.neo4jDatabases.graphingestion.tx_timeout | string | `"120s"` |  |
| global.neo4jDatabases.graphingestion.username | string | `"neo4j"` |  |
| global.neo4jDatabases.onprem.graphingestion.adminpassword | string | `"test1234"` |  |
| global.neo4jDatabases.onprem.graphingestion.adminusername | string | `"neo4j"` |  |
| global.neo4jDatabases.onprem.graphingestion.db | string | `"neo4j"` |  |
| global.neo4jDatabases.onprem.graphingestion.enabled | bool | `false` |  |
| global.neo4jDatabases.onprem.graphingestion.enabledForMigration | bool | `false` |  |
| global.neo4jDatabases.onprem.graphingestion.endpoint | string | `"bolt://host.docker.internal:7687"` |  |
| global.neo4jDatabases.onprem.graphingestion.maxConnectionPoolSize | int | `100` |  |
| global.neo4jDatabases.onprem.graphingestion.migrationUserPrefix | string | `""` |  |
| global.neo4jDatabases.onprem.graphingestion.password | string | `"test1234"` |  |
| global.neo4jDatabases.onprem.graphingestion.tx_timeout | string | `"120s"` |  |
| global.neo4jDatabases.onprem.graphingestion.username | string | `"neo4j"` |  |
| secureGraphIngestion.alertManager.enabled | bool | `false` |  |
| secureGraphIngestion.audit.enabled | bool | `false` |  |
| secureGraphIngestion.backend.backendEndpoint | string | `"sysdigcloud-api:8080"` |  |
| secureGraphIngestion.backoffLimit | int | `0` |  |
| secureGraphIngestion.cleaner.agents.deleteNodesOlderThan | string | `"2160h"` |  |
| secureGraphIngestion.cleaner.agents.frequency | string | `"6h"` |  |
| secureGraphIngestion.cleaner.cyclesWaitingTime | string | `"3s"` |  |
| secureGraphIngestion.cleaner.deleteNodesOlderThan | string | `"168h"` |  |
| secureGraphIngestion.cleaner.events.deleteNodesOlderThan | string | `"2160h"` |  |
| secureGraphIngestion.cleaner.events.frequency | string | `"6h"` |  |
| secureGraphIngestion.cleaner.frequencies | string | `"events:6h,resources:2h,assets:1h,vmv2:1h,externalVulnAssets:48h"` |  |
| secureGraphIngestion.cleaner.generic.deleteNodesOlderThan | string | `"168h"` |  |
| secureGraphIngestion.cleaner.generic.frequency | string | `"2h"` |  |
| secureGraphIngestion.cleaner.maxDeleteCycles | string | `"50"` |  |
| secureGraphIngestion.cleaner.threats.deleteNodesOlderThan | string | `"2160h"` |  |
| secureGraphIngestion.cleaner.threats.frequency | string | `"6h"` |  |
| secureGraphIngestion.cleaner.txTimeout | string | `"3m"` |  |
| secureGraphIngestion.compliance.policiesEndpoint | string | `"secure-iac-policy-service:8080"` |  |
| secureGraphIngestion.compliance.zonesEndpoint | string | `"sysdigcloud-platform-zones-service-grpc:8091"` |  |
| secureGraphIngestion.componentHealthManager.enabled | bool | `false` |  |
| secureGraphIngestion.controls.sync.enabled | bool | `true` |  |
| secureGraphIngestion.copier.maxParallelism | int | `10` |  |
| secureGraphIngestion.copier.syncInterval | string | `"10m"` |  |
| secureGraphIngestion.enableNewRbac | bool | `false` |  |
| secureGraphIngestion.enableZonesV2 | bool | `false` |  |
| secureGraphIngestion.enabled | bool | `true` |  |
| secureGraphIngestion.events.enableScanEvents | bool | `true` |  |
| secureGraphIngestion.integrations.enabled | bool | `true` |  |
| secureGraphIngestion.integrations.nats.sourceCodePullBatchSize | int | `100` |  |
| secureGraphIngestion.integrations.nats.vmPullBatchSize | int | `100` |  |
| secureGraphIngestion.integrations.sourceCode.DeleteNodesOlderThan | string | `"48h"` |  |
| secureGraphIngestion.integrations.sourceCode.enableRepo | bool | `true` |  |
| secureGraphIngestion.integrations.sourceCode.graphQueryBatchSize | int | `100000` |  |
| secureGraphIngestion.integrations.vm.DeleteNodesOlderThan | string | `"48h"` |  |
| secureGraphIngestion.integrations.vm.enableHost | bool | `true` |  |
| secureGraphIngestion.integrations.vm.graphQueryBatchSize | int | `100000` |  |
| secureGraphIngestion.managedMigrations.enable | bool | `false` |  |
| secureGraphIngestion.managedMigrations.maxConnectionAttempts | int | `1` |  |
| secureGraphIngestion.managedMigrations.timeout | string | `"15m"` |  |
| secureGraphIngestion.managedMigrations.txRetryTimeout | string | `"300s"` |  |
| secureGraphIngestion.message.disallowedCustomers | string | `""` |  |
| secureGraphIngestion.message.dynamicCustomerFiltering | bool | `true` |  |
| secureGraphIngestion.natsBackoffSeconds | int | `5` |  |
| secureGraphIngestion.natsJs.jetstreamPublishAsyncTimeout | string | `"30s"` |  |
| secureGraphIngestion.natsJs.secure.enabled | bool | `true` |  |
| secureGraphIngestion.natsJs.streamMaxBytes | string | `"17179869184"` |  |
| secureGraphIngestion.natsJs.url | string | `"nats"` |  |
| secureGraphIngestion.natsRetries | int | `3` |  |
| secureGraphIngestion.ownershipAttribution.customLabels.cacheCleanupInterval | string | `"12h"` |  |
| secureGraphIngestion.ownershipAttribution.customLabels.cacheExpirationTime | string | `"6h"` |  |
| secureGraphIngestion.ownershipAttribution.customLabels.circuitBreakerMaxFailures | int | `5` |  |
| secureGraphIngestion.ownershipAttribution.customLabels.circuitBreakerTTL | string | `"1h"` |  |
| secureGraphIngestion.ownershipAttribution.customLabels.enabled | bool | `false` |  |
| secureGraphIngestion.ownershipAttribution.customLabels.maxAttempts | int | `3` |  |
| secureGraphIngestion.ownershipAttribution.customLabels.timeout | string | `"1s"` |  |
| secureGraphIngestion.ownershipAttribution.enableAwsResources | bool | `false` |  |
| secureGraphIngestion.ownershipAttribution.enableAzureResources | bool | `false` |  |
| secureGraphIngestion.ownershipAttribution.enableGcpResources | bool | `false` |  |
| secureGraphIngestion.ownershipAttribution.enableKubeResources | bool | `false` |  |
| secureGraphIngestion.ownershipAttribution.enableVMRuntimeImages | bool | `false` |  |
| secureGraphIngestion.postureScanCompletedStreamEnabled | bool | `false` |  |
| secureGraphIngestion.realtime.enabled | bool | `false` |  |
| secureGraphIngestion.realtime.messageBatchSize | string | `"100"` |  |
| secureGraphIngestion.regionsV2.enable | bool | `false` |  |
| secureGraphIngestion.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureGraphIngestion.remotebody.pullerBackends | string | `"s3"` |  |
| secureGraphIngestion.remotebody.s3.bucket | string | `""` |  |
| secureGraphIngestion.remotebody.s3.cloudProvider | string | `""` |  |
| secureGraphIngestion.remotebody.s3.region | string | `""` |  |
| secureGraphIngestion.repositoryPrefix | string | `"secure"` |  |
| secureGraphIngestion.resources.graphIngestion.limits.cpu | int | `2` |  |
| secureGraphIngestion.resources.graphIngestion.limits.memory | string | `"6Gi"` |  |
| secureGraphIngestion.resources.graphIngestion.requests.cpu | string | `"250m"` |  |
| secureGraphIngestion.resources.graphIngestion.requests.memory | string | `"250Mi"` |  |
| secureGraphIngestion.resources.neo4jinit.limits.cpu | string | `"500m"` |  |
| secureGraphIngestion.resources.neo4jinit.limits.memory | string | `"500Mi"` |  |
| secureGraphIngestion.resources.neo4jinit.requests.cpu | string | `"100m"` |  |
| secureGraphIngestion.resources.neo4jinit.requests.memory | string | `"100Mi"` |  |
| secureGraphIngestion.runNeo4jMigrations | bool | `true` |  |
| secureGraphIngestion.sageLabels.enable | bool | `false` |  |
| secureGraphIngestion.segmentToken | string | `"test"` |  |
| secureGraphIngestion.skipZeroTotalScans | bool | `false` |  |
| secureGraphIngestion.threats.enable | bool | `false` |  |
| secureGraphIngestion.vm.additionalAIPackages | string | `""` |  |
| secureGraphIngestion.vm.allowedCustomers | string | `""` |  |
| secureGraphIngestion.vm.dedicatedConsumerCustomerIDs | string | `""` |  |
| secureGraphIngestion.vm.enableMixAndBatch | bool | `false` |  |
| secureGraphIngestion.vm.enableScanEvents | bool | `true` |  |
| secureGraphIngestion.vm.enableScanEventsRelationship | bool | `false` |  |
| secureGraphIngestion.vm.enableServerless | bool | `true` |  |
| secureGraphIngestion.vm.enableSmartBatching | bool | `false` |  |
| secureGraphIngestion.vm.enableV1Ingestion | bool | `true` |  |
| secureGraphIngestion.vm.enableV2 | bool | `true` |  |
| secureGraphIngestion.vm.enableV2Container | bool | `true` |  |
| secureGraphIngestion.vm.enableV2DeleteNodes | bool | `true` |  |
| secureGraphIngestion.vm.enableV2Host | bool | `true` |  |
| secureGraphIngestion.vm.enableV2HostOnprem | bool | `true` |  |
| secureGraphIngestion.vm.enableV2Ingestion | bool | `true` |  |
| secureGraphIngestion.vm.enableV2K8s | bool | `true` |  |
| secureGraphIngestion.vm.enableV2Pipeline | bool | `false` |  |
| secureGraphIngestion.vm.enableV2VulnPkgCache | bool | `true` |  |
| secureGraphIngestion.vm.enableVulnerabilityNodes | bool | `false` |  |
| secureGraphIngestion.vm.enableWorkloadScanEvent | bool | `false` |  |
| secureGraphIngestion.vm.forwardingEnabled | bool | `false` |  |
| secureGraphIngestion.vm.lockOnDeletion | bool | `true` |  |
| secureGraphIngestion.vm.preserveVulnTimestamp | bool | `true` |  |
| secureGraphIngestion.vm.scanFindingsEnabled | bool | `false` |  |
| secureGraphIngestion.vm.useUnbufferedHandler | bool | `false` |  |
| secureGraphIngestion.vm.v2BatchQueueConfig | string | `""` |  |
| secureGraphIngestion.vm.v2BatchSize | string | `"10"` |  |
| secureGraphIngestion.vm.v2DecoderBufferSize | string | `"40"` |  |
| secureGraphIngestion.vm.v2DecoderWorkers | string | `"4"` |  |
| secureGraphIngestion.vm.v2DeleteNodesOlderThan | string | `"168h"` |  |
| secureGraphIngestion.vm.v2ItemsBatchSize | string | `"1000000"` |  |
| secureGraphIngestion.vm.v2ParallelDelete | bool | `false` |  |
| secureGraphIngestion.vm.v2ParallelStep | bool | `false` |  |
| secureGraphIngestion.vm.v2ProcessingWorkers | string | `"1"` |  |
| secureGraphIngestion.vm.vmEventsItemsBatchSize | string | `"10000"` |  |
| secureGraphIngestion.vmMessageBatchSize | int | `100` |  |
| secureGraphIngestion.zones.cache.cleanupInterval | string | `"60m"` |  |
| secureGraphIngestion.zones.cache.expirationTime | string | `"30m"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-graph-query

![Version: 3.0.0-260311001027-main-vc536ee1](https://img.shields.io/badge/Version-3.0.0--260311001027--main--vc536ee1-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure Graph Query

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.secureGraphQuery.serviceToken | string | `"test"` |  |
| global.apps | string | `"secure"` |  |
| global.iac.imagePullSecrets[0] | string | `"sysdigcloud-pull-secret"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.neo4jDatabases.graphquery.adminpassword | string | `"test1234"` |  |
| global.neo4jDatabases.graphquery.adminusername | string | `"neo4j"` |  |
| global.neo4jDatabases.graphquery.db | string | `"neo4j"` |  |
| global.neo4jDatabases.graphquery.endpoint | string | `"bolt://neo4j:7687"` |  |
| global.neo4jDatabases.graphquery.password | string | `"test1234"` |  |
| global.neo4jDatabases.graphquery.username | string | `"neo4j"` |  |
| global.topologySpreadConstraintsEnabled | bool | `true` |  |
| secureGraphQuery.audit.enabled | bool | `false` |  |
| secureGraphQuery.db.txtimeout | string | `"60s"` |  |
| secureGraphQuery.enabled | bool | `true` |  |
| secureGraphQuery.image.graphqlApi.imagePullSecrets[0] | string | `"sysdigcloud-pull-secret"` |  |
| secureGraphQuery.image.graphquery.imagePullSecrets[0] | string | `"sysdigcloud-pull-secret"` |  |
| secureGraphQuery.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-graph-query"` |  |
| secureGraphQuery.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-graph-query"` |  |
| secureGraphQuery.ingress[0].hosts[0].paths[0].path | string | `"/api/graph/v1"` |  |
| secureGraphQuery.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-graph-query"` |  |
| secureGraphQuery.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| secureGraphQuery.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| secureGraphQuery.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| secureGraphQuery.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| secureGraphQuery.ingress[0].labels.role | string | `"ingress-config"` |  |
| secureGraphQuery.ingress[0].labels.tier | string | `"infra"` |  |
| secureGraphQuery.ingress[0].name | string | `"secure-graph-query-ingress"` |  |
| secureGraphQuery.logging | string | `"info"` |  |
| secureGraphQuery.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureGraphQuery.replicaCount | int | `3` |  |
| secureGraphQuery.repositoryPrefix | string | `"secure"` |  |
| secureGraphQuery.resources.graphquery.limits.cpu | int | `2` |  |
| secureGraphQuery.resources.graphquery.limits.memory | string | `"4Gi"` |  |
| secureGraphQuery.resources.graphquery.requests.cpu | string | `"250m"` |  |
| secureGraphQuery.resources.graphquery.requests.memory | string | `"250Mi"` |  |
| secureGraphQuery.securityContext.readOnlyRootFilesystem | bool | `true` |  |
| secureGraphQuery.securityContext.runAsRoot | bool | `false` |  |
| secureGraphQuery.segmentToken | string | `"test"` |  |
| secureGraphQuery.serviceAccountName | string | `"sysdig"` |  |
| secureGraphQuery.useNewComplianceQuery | bool | `false` |  |
| secureGraphQuery.useParallelCount | bool | `true` |  |
| secureGraphQuery.vmv2.enabled | bool | `true` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-iac-agenthandler

![Version: 1.23.731-260312123143-main-ve5a23782](https://img.shields.io/badge/Version-1.23.731--260312123143--main--ve5a23782-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

IAC Agent Handler Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| file://../common-v2 | iac-common | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dbImage.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-agenthandler-db-migrations-postgres"` |  |
| dbImage.tag | string | `"1.23.731-260312123143-main-ve5a23782"` |  |
| global.apps | string | `"secure"` |  |
| global.iac.enabled | bool | `true` |  |
| global.iac.natsjs.endpoint | string | `"nats"` |  |
| global.iac.natsjs.insecure.enabled | bool | `false` |  |
| global.iac.natsjs.tls.enabled | bool | `true` |  |
| global.infraRegistryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| global.legacyPostgres.postgresDatabases.agenthandler.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.agenthandler.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.agenthandler.db | string | `"agenthandler"` |  |
| global.legacyPostgres.postgresDatabases.agenthandler.forceSkipDbDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.agenthandler.gke.sqlproxy.enabled | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.agenthandler.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.agenthandler.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.agenthandler.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.agenthandler.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.agenthandler.username | string | `"agenthandlerdbuser"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.posture.kspm.enabled | bool | `true` |  |
| global.scaler.clusterName | string | `""` |  |
| image.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-agenthandler"` |  |
| image.tag | string | `"1.23.731-260312123143-main-ve5a23782"` |  |
| secureIacAgenthandler.audit.enabled | bool | `false` |  |
| secureIacAgenthandler.autoscale.enabled | bool | `true` |  |
| secureIacAgenthandler.autoscale.minReplicaCount | int | `1` |  |
| secureIacAgenthandler.dbImage.repository | string | `"cspm-agenthandler-db-migrations-postgres"` |  |
| secureIacAgenthandler.enabled | bool | `true` |  |
| secureIacAgenthandler.image.repository | string | `"cspm-agenthandler"` |  |
| secureIacAgenthandler.ingress[0].annotations."ingress.kubernetes.io/affinity" | string | `"cookie"` |  |
| secureIacAgenthandler.ingress[0].annotations."ingress.kubernetes.io/session-cookie-name" | string | `"INGRESSCOOKIEAPI"` |  |
| secureIacAgenthandler.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-iac-agenthandler-service"` |  |
| secureIacAgenthandler.ingress[0].hosts[0].paths[0].apiGatewayStickySessions | bool | `true` |  |
| secureIacAgenthandler.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-iac-agenthandler-service"` |  |
| secureIacAgenthandler.ingress[0].hosts[0].paths[0].path | string | `"/api/cspm/v1/agenthandler"` |  |
| secureIacAgenthandler.ingress[0].hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| secureIacAgenthandler.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-iac-agenthandler-service"` |  |
| secureIacAgenthandler.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| secureIacAgenthandler.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| secureIacAgenthandler.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| secureIacAgenthandler.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| secureIacAgenthandler.ingress[0].labels.role | string | `"ingress-config"` |  |
| secureIacAgenthandler.ingress[0].labels.tier | string | `"infra"` |  |
| secureIacAgenthandler.ingress[0].name | string | `"sysdigcloud-secure-iac-agenthandler-ingress"` |  |
| secureIacAgenthandler.persistScanRequests | bool | `true` |  |
| secureIacAgenthandler.port | int | `8080` |  |
| secureIacAgenthandler.prom.enabled | bool | `true` |  |
| secureIacAgenthandler.prom.httpFineMetricsEnabled | bool | `true` |  |
| secureIacAgenthandler.prom.httpFineMetricsStripPrefix | string | `"/api/cspm/v1/agenthandler"` |  |
| secureIacAgenthandler.prom.port | int | `25000` |  |
| secureIacAgenthandler.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureIacAgenthandler.replacePubSubWithJetstream | bool | `false` |  |
| secureIacAgenthandler.replicaCount | int | `1` |  |
| secureIacAgenthandler.repositoryPrefix | string | `"secure"` |  |
| secureIacAgenthandler.resources.postgresqlinit.limits.cpu | string | `"200m"` |  |
| secureIacAgenthandler.resources.postgresqlinit.limits.memory | string | `"256Mi"` |  |
| secureIacAgenthandler.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| secureIacAgenthandler.resources.postgresqlinit.requests.memory | string | `"128Mi"` |  |
| secureIacAgenthandler.resources.secureIacAgenthandler.limits.cpu | int | `2` |  |
| secureIacAgenthandler.resources.secureIacAgenthandler.limits.memory | string | `"16Gi"` |  |
| secureIacAgenthandler.resources.secureIacAgenthandler.requests.cpu | float | `0.2` |  |
| secureIacAgenthandler.resources.secureIacAgenthandler.requests.memory | string | `"200Mi"` |  |
| secureIacAgenthandler.secureDataHostScanResultEncoderEnabled | bool | `false` |  |
| secureIacAgenthandler.secureDataKubeScanResultEncoderEnabled | bool | `false` |  |
| secureIacAgenthandler.serviceName | string | `"secure-iac-agenthandler"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-iac-clusteranalysis

![Version: 1.23.731-260211132202-main-ve28a6040](https://img.shields.io/badge/Version-1.23.731--260211132202--main--ve28a6040-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

IAC Cluster Analysis Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| file://../common-v2 | iac-common | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dbImage.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-clusteranalysis-db-migrations-postgres"` |  |
| dbImage.tag | string | `"1.23.731-260211132202-main-ve28a6040"` |  |
| global.api.serviceTokens.secureIac.serviceToken | string | `""` |  |
| global.apps | string | `"secure"` |  |
| global.iac.audit.workers | int | `5` |  |
| global.iac.enabled | bool | `true` |  |
| global.iac.graphdb.enabled | bool | `true` |  |
| global.iac.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.iac.natsjs.insecure.enabled | bool | `false` |  |
| global.iac.natsjs.panicOnClosedConnection | bool | `true` |  |
| global.iac.natsjs.tls.enabled | bool | `true` |  |
| global.iac.telemetry.segmentToken | string | `""` |  |
| global.infraRegistryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.db | string | `"clusteranalysis"` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.forceSkipDbDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.gke.sqlproxy.enabled | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.idleConns | string | `"1"` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.idleTimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.maxConnLife | string | `"1h"` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.maxConns | int | `3` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.maxUserConns | int | `100` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.clusteranalysis.username | string | `"clusteranalysisdbuser"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.posture.kspm.enabled | bool | `true` |  |
| image.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-clusteranalysis"` |  |
| image.tag | string | `"1.23.731-260211132202-main-ve28a6040"` |  |
| secureIacClusterAnalysis.audit.enabled | bool | `true` |  |
| secureIacClusterAnalysis.autoscale.enabled | bool | `true` |  |
| secureIacClusterAnalysis.autoscale.scaleDownSelectPolicy | string | `"Disabled"` |  |
| secureIacClusterAnalysis.dbImage.repository | string | `"cspm-clusteranalysis-db-migrations-postgres"` |  |
| secureIacClusterAnalysis.deleteStaleDataBatchSize | int | `100` |  |
| secureIacClusterAnalysis.dumpHeapProfileEnabled | bool | `false` |  |
| secureIacClusterAnalysis.enabled | bool | `true` |  |
| secureIacClusterAnalysis.graphDryRun | bool | `false` |  |
| secureIacClusterAnalysis.grpcMaxMsgSizeMbs | int | `700` |  |
| secureIacClusterAnalysis.image.repository | string | `"cspm-clusteranalysis"` |  |
| secureIacClusterAnalysis.ingress[0].annotations."ingress.kubernetes.io/affinity" | string | `"cookie"` |  |
| secureIacClusterAnalysis.ingress[0].annotations."ingress.kubernetes.io/session-cookie-name" | string | `"INGRESSCOOKIEAPI"` |  |
| secureIacClusterAnalysis.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-iac-clusteranalysis-service"` |  |
| secureIacClusterAnalysis.ingress[0].hosts[0].paths[0].apiGatewayStickySessions | bool | `true` |  |
| secureIacClusterAnalysis.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-iac-clusteranalysis-service"` |  |
| secureIacClusterAnalysis.ingress[0].hosts[0].paths[0].path | string | `"/api/cspm/v1/clusteranalysis"` |  |
| secureIacClusterAnalysis.ingress[0].hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| secureIacClusterAnalysis.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-iac-clusteranalysis-service"` |  |
| secureIacClusterAnalysis.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| secureIacClusterAnalysis.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| secureIacClusterAnalysis.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| secureIacClusterAnalysis.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| secureIacClusterAnalysis.ingress[0].labels.role | string | `"ingress-config"` |  |
| secureIacClusterAnalysis.ingress[0].labels.tier | string | `"infra"` |  |
| secureIacClusterAnalysis.ingress[0].name | string | `"sysdigcloud-secure-iac-clusteranalysis-ingress"` |  |
| secureIacClusterAnalysis.livenessDefaultProbeEnabled | bool | `true` |  |
| secureIacClusterAnalysis.port | int | `8080` |  |
| secureIacClusterAnalysis.postgresEnabled | bool | `true` |  |
| secureIacClusterAnalysis.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureIacClusterAnalysis.replicaCount | int | `1` |  |
| secureIacClusterAnalysis.repos.pg.enableFullQueryLog | bool | `false` |  |
| secureIacClusterAnalysis.repos.pg.log.slowQueryThreshold | string | `"500ms"` |  |
| secureIacClusterAnalysis.repos.pg.read | string | `"all"` |  |
| secureIacClusterAnalysis.repos.pg.write | string | `"all"` |  |
| secureIacClusterAnalysis.repositoryPrefix | string | `"secure"` |  |
| secureIacClusterAnalysis.resources.postgresqlinit.limits.cpu | string | `"200m"` |  |
| secureIacClusterAnalysis.resources.postgresqlinit.limits.memory | string | `"256Mi"` |  |
| secureIacClusterAnalysis.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| secureIacClusterAnalysis.resources.postgresqlinit.requests.memory | string | `"128Mi"` |  |
| secureIacClusterAnalysis.resources.secureIacClusterAnalysis.limits.cpu | string | `"1"` |  |
| secureIacClusterAnalysis.resources.secureIacClusterAnalysis.limits.memory | string | `"700Mi"` |  |
| secureIacClusterAnalysis.resources.secureIacClusterAnalysis.requests.cpu | string | `"200m"` |  |
| secureIacClusterAnalysis.resources.secureIacClusterAnalysis.requests.memory | string | `"200Mi"` |  |
| secureIacClusterAnalysis.serviceName | string | `"secure-iac-clusteranalysis"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-iac-compliance

![Version: 1.23.731-260312150320-main-v4778be31](https://img.shields.io/badge/Version-1.23.731--260312150320--main--v4778be31-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

IAC Compliance Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| file://../common-v2 | iac-common | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dbImage.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-compliance-db-migrations-postgres"` |  |
| dbImage.tag | string | `"1.23.731-260312150320-main-v4778be31"` |  |
| global.apps | string | `"secure"` |  |
| global.complianceReview.allowedTenants | string | `"709521"` |  |
| global.complianceReview.newComplianceViewPreLoadTenantIds | string | `""` |  |
| global.complianceReview.newComplianceWorkflowChunkPolicies | int | `10` |  |
| global.complianceReview.newWorkflow | bool | `true` |  |
| global.complianceReview.taskTrackingRetentionDays | int | `7` |  |
| global.iac.audit.workers | int | `5` |  |
| global.iac.clusterEnvironment | string | `"aws"` |  |
| global.iac.graphdb.enabled | bool | `true` |  |
| global.iac.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.iac.metrics.annotations."prometheus.io/path" | string | `"/metrics"` |  |
| global.iac.metrics.annotations."prometheus.io/port" | string | `"25000"` |  |
| global.iac.metrics.annotations."prometheus.io/scrape" | string | `"true"` |  |
| global.iac.natsjs.endpoint | string | `"nats"` |  |
| global.iac.natsjs.insecure.enabled | bool | `false` |  |
| global.iac.natsjs.panicOnClosedConnection | bool | `true` |  |
| global.iac.natsjs.tls.enabled | bool | `true` |  |
| global.iac.telemetry.segmentToken | string | `""` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.db | string | `"cspmcompliance"` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.forceSkipDbDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.idleConns | int | `10` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.idleTimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.maxConnLife | string | `"1h"` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.maxConns | int | `15` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.maxUserConns | int | `100` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.cspmCompliance.username | string | `"compliancedbuser"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.neo4jDatabases.graphquery.db | string | `"neo4j"` |  |
| global.neo4jDatabases.graphquery.endpoint | string | `""` |  |
| global.neo4jDatabases.graphquery.password | string | `""` |  |
| global.neo4jDatabases.graphquery.username | string | `""` |  |
| global.posture.kspm.enabled | bool | `true` |  |
| global.scaler.clusterName | string | `""` |  |
| image.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-compliance"` |  |
| image.tag | string | `"1.23.731-260312150320-main-v4778be31"` |  |
| secureIacCompliance.audit.enabled | bool | `true` |  |
| secureIacCompliance.autoscale.enabled | bool | `true` |  |
| secureIacCompliance.dbImage.repository | string | `"cspm-compliance-db-migrations-postgres"` |  |
| secureIacCompliance.dumpHeapProfileEnabled | bool | `false` |  |
| secureIacCompliance.enabled | bool | `true` |  |
| secureIacCompliance.graphQueryBackoffDelay | string | `"1m"` |  |
| secureIacCompliance.graphQueryRetries | int | `10` |  |
| secureIacCompliance.grpcClientBackoffMultiplier | int | `2` |  |
| secureIacCompliance.grpcClientInitialBackoff | string | `"0.1s"` |  |
| secureIacCompliance.grpcClientMaxAttempts | int | `5` |  |
| secureIacCompliance.grpcClientMaxBackoff | string | `"1s"` |  |
| secureIacCompliance.grpcMaxMsgSizeMbs | int | `700` |  |
| secureIacCompliance.image.repository | string | `"cspm-compliance"` |  |
| secureIacCompliance.ingress[0].annotations."ingress.kubernetes.io/affinity" | string | `"cookie"` |  |
| secureIacCompliance.ingress[0].annotations."ingress.kubernetes.io/session-cookie-name" | string | `"INGRESSCOOKIEAPI"` |  |
| secureIacCompliance.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-iac-compliance-service"` |  |
| secureIacCompliance.ingress[0].hosts[0].paths[0].apiGatewayStickySessions | bool | `true` |  |
| secureIacCompliance.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-iac-compliance-service"` |  |
| secureIacCompliance.ingress[0].hosts[0].paths[0].path | string | `"/api/cspm/v1/compliance"` |  |
| secureIacCompliance.ingress[0].hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| secureIacCompliance.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-iac-compliance-service"` |  |
| secureIacCompliance.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| secureIacCompliance.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| secureIacCompliance.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| secureIacCompliance.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| secureIacCompliance.ingress[0].labels.role | string | `"ingress-config"` |  |
| secureIacCompliance.ingress[0].labels.tier | string | `"infra"` |  |
| secureIacCompliance.ingress[0].name | string | `"sysdigcloud-secure-iac-compliance-ingress"` |  |
| secureIacCompliance.livenessDefaultProbeEnabled | bool | `true` |  |
| secureIacCompliance.port | int | `8080` |  |
| secureIacCompliance.readinessDefaultProbeEnabled | bool | `true` |  |
| secureIacCompliance.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureIacCompliance.replicaCount | int | `1` |  |
| secureIacCompliance.repositoryPrefix | string | `"secure"` |  |
| secureIacCompliance.resources.postgresqlinit.limits.cpu | string | `"200m"` |  |
| secureIacCompliance.resources.postgresqlinit.limits.memory | string | `"256Mi"` |  |
| secureIacCompliance.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| secureIacCompliance.resources.postgresqlinit.requests.memory | string | `"128Mi"` |  |
| secureIacCompliance.resources.secureIacCompliance.limits.cpu | int | `2` |  |
| secureIacCompliance.resources.secureIacCompliance.limits.memory | string | `"2Gi"` |  |
| secureIacCompliance.resources.secureIacCompliance.requests.cpu | int | `1` |  |
| secureIacCompliance.resources.secureIacCompliance.requests.memory | string | `"200Mi"` |  |
| secureIacCompliance.serviceName | string | `"secure-iac-compliance"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-iac-inventory

![Version: 1.23.731-260311171409-main-v1b40a1bc](https://img.shields.io/badge/Version-1.23.731--260311171409--main--v1b40a1bc-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

IAC Inventory Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| file://../common-v2 | iac-common | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dbImage.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-inventory-db-migrations-postgres"` |  |
| dbImage.tag | string | `"1.23.731-260311171409-main-v1b40a1bc"` |  |
| global.api.serviceTokens.secureIac.serviceToken | string | `"test-token"` |  |
| global.apps | string | `"secure"` |  |
| global.iac.audit.workers | int | `5` |  |
| global.iac.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.iac.metrics.annotations."prometheus.io/path" | string | `"/metrics"` |  |
| global.iac.metrics.annotations."prometheus.io/port" | string | `"25000"` |  |
| global.iac.metrics.annotations."prometheus.io/scrape" | string | `"true"` |  |
| global.iac.natsjs.endpoint | string | `"nats"` |  |
| global.iac.natsjs.insecure.enabled | bool | `false` |  |
| global.iac.natsjs.tls.enabled | bool | `true` |  |
| global.iac.telemetry.segmentToken | string | `""` |  |
| global.legacyPostgres.postgresDatabases.inventory.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.inventory.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.inventory.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.inventory.db | string | `"inventory"` |  |
| global.legacyPostgres.postgresDatabases.inventory.forceSkipDbDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.inventory.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.inventory.idleConns | int | `10` |  |
| global.legacyPostgres.postgresDatabases.inventory.idleTimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.inventory.maxConnLife | string | `"1h"` |  |
| global.legacyPostgres.postgresDatabases.inventory.maxConns | int | `15` |  |
| global.legacyPostgres.postgresDatabases.inventory.maxUserConns | int | `100` |  |
| global.legacyPostgres.postgresDatabases.inventory.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.inventory.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.inventory.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.inventory.username | string | `"inventorydbuser"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.posture.kspm.enabled | bool | `true` |  |
| global.scaler.clusterName | string | `""` |  |
| global.secure.sysqlApi.serviceToken | string | `"CHANGEME"` |  |
| image.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-inventory"` |  |
| image.tag | string | `"1.23.731-260311171409-main-v1b40a1bc"` |  |
| secureIacInventory.audit.enabled | bool | `true` |  |
| secureIacInventory.autoscale.enabled | bool | `true` |  |
| secureIacInventory.dbImage.repository | string | `"cspm-inventory-db-migrations-postgres"` |  |
| secureIacInventory.dbImage.tag | string | `"main"` |  |
| secureIacInventory.dumpHeapProfileEnabled | bool | `false` |  |
| secureIacInventory.enabled | bool | `true` |  |
| secureIacInventory.grpcMaxMsgSizeMbs | int | `700` |  |
| secureIacInventory.image.repository | string | `"cspm-inventory"` |  |
| secureIacInventory.ingress[0].annotations."ingress.kubernetes.io/affinity" | string | `"cookie"` |  |
| secureIacInventory.ingress[0].annotations."ingress.kubernetes.io/session-cookie-name" | string | `"INGRESSCOOKIEAPI"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-iac-inventory-service"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[0].apiGatewayStickySessions | bool | `true` |  |
| secureIacInventory.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-iac-inventory-service"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[0].path | string | `"/api/cspm/v1/inventory"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-iac-inventory-service"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| secureIacInventory.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"secure-iac-inventory-service-1"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[1].apiGatewayStickySessions | bool | `true` |  |
| secureIacInventory.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"secure-iac-inventory-service-1"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[1].path | string | `"/secure/inventory/v1"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[1].pathType | string | `"ImplementationSpecific"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[1].serviceName | string | `"secure-iac-inventory-service"` |  |
| secureIacInventory.ingress[0].hosts[0].paths[1].servicePort | int | `8081` |  |
| secureIacInventory.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| secureIacInventory.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| secureIacInventory.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| secureIacInventory.ingress[0].labels.role | string | `"ingress-config"` |  |
| secureIacInventory.ingress[0].labels.tier | string | `"infra"` |  |
| secureIacInventory.ingress[0].name | string | `"sysdigcloud-secure-iac-inventory-ingress"` |  |
| secureIacInventory.initDb.enabled | bool | `true` |  |
| secureIacInventory.livenessDefaultProbeEnabled | bool | `true` |  |
| secureIacInventory.livenessProbe.enabled | bool | `true` |  |
| secureIacInventory.openApiPort | int | `8081` |  |
| secureIacInventory.port | int | `8080` |  |
| secureIacInventory.readinessDefaultProbeEnabled | bool | `true` |  |
| secureIacInventory.readinessProbe.enabled | bool | `true` |  |
| secureIacInventory.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureIacInventory.replicaCount | int | `1` |  |
| secureIacInventory.reportingCustomerIds | string | `"1"` |  |
| secureIacInventory.reportingFrequency | string | `"24h"` |  |
| secureIacInventory.reportingPageSize | string | `"1000"` |  |
| secureIacInventory.reportingPolicyIds | string | `"285044"` |  |
| secureIacInventory.repositoryPrefix | string | `"secure"` |  |
| secureIacInventory.resources.postgresqlinit.limits.cpu | string | `"200m"` |  |
| secureIacInventory.resources.postgresqlinit.limits.memory | string | `"256Mi"` |  |
| secureIacInventory.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| secureIacInventory.resources.postgresqlinit.requests.memory | string | `"128Mi"` |  |
| secureIacInventory.resources.secureIacInventory.limits.cpu | int | `2` |  |
| secureIacInventory.resources.secureIacInventory.limits.memory | string | `"2Gi"` |  |
| secureIacInventory.resources.secureIacInventory.requests.cpu | int | `1` |  |
| secureIacInventory.resources.secureIacInventory.requests.memory | string | `"50Mi"` |  |
| secureIacInventory.serviceName | string | `"secure-iac-inventory"` |  |
| secureIacInventory.startupProbe.enabled | bool | `true` |  |
| secureIacInventory.startupProbe.failureThreshold | int | `3` |  |
| secureIacInventory.startupProbe.initialDelaySeconds | int | `5` |  |
| secureIacInventory.startupProbe.periodSeconds | int | `10` |  |
| secureIacInventory.startupProbe.successThreshold | int | `1` |  |
| secureIacInventory.startupProbe.timeoutSeconds | int | `5` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-iac-policy

![Version: 1.23.731-260312194542-main-vd02e9449](https://img.shields.io/badge/Version-1.23.731--260312194542--main--vd02e9449-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

IAC Policy Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| file://../common-v2 | iac-common | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dbImage.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-policy-db-migrations-postgres"` |  |
| dbImage.tag | string | `"1.23.731-260312194542-main-vd02e9449"` |  |
| global.apps | string | `"secure"` |  |
| global.iac.audit.workers | int | `5` |  |
| global.iac.clusterEnvironment | string | `"aws"` |  |
| global.iac.enableOci | bool | `false` |  |
| global.iac.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.iac.metrics.annotations."prometheus.io/path" | string | `"/metrics"` |  |
| global.iac.metrics.annotations."prometheus.io/port" | string | `"25000"` |  |
| global.iac.metrics.annotations."prometheus.io/scrape" | string | `"true"` |  |
| global.iac.natsjs.endpoint | string | `"nats"` |  |
| global.iac.natsjs.insecure.enabled | bool | `false` |  |
| global.iac.natsjs.panicOnClosedConnection | bool | `true` |  |
| global.iac.natsjs.tls.enabled | bool | `true` |  |
| global.iac.telemetry.segmentToken | string | `""` |  |
| global.legacyPostgres.postgresDatabases.policy.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.policy.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.policy.db | string | `"policy"` |  |
| global.legacyPostgres.postgresDatabases.policy.forceSkipDbDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.policy.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.policy.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.policy.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.policy.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.policy.username | string | `"policydbuser"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.posture.kspm.enabled | bool | `true` |  |
| global.scaler.clusterName | string | `""` |  |
| image.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-policy"` |  |
| image.tag | string | `"1.23.731-260312194542-main-vd02e9449"` |  |
| secureIacPolicy.audit.enabled | bool | `true` |  |
| secureIacPolicy.autoscale.enabled | bool | `true` |  |
| secureIacPolicy.configServiceEndpoint | string | `"secure-config-service"` |  |
| secureIacPolicy.configServicePort | int | `8080` |  |
| secureIacPolicy.configServicePullInterval | string | `"15m"` |  |
| secureIacPolicy.configServiceSyncWrite | bool | `false` |  |
| secureIacPolicy.dbImage.repository | string | `"cspm-policy-db-migrations-postgres"` |  |
| secureIacPolicy.disableRequirementRiskView | bool | `false` |  |
| secureIacPolicy.dumpHeapProfileEnabled | bool | `false` |  |
| secureIacPolicy.enableWindows | bool | `false` |  |
| secureIacPolicy.enabled | bool | `true` |  |
| secureIacPolicy.graphDryRun | bool | `false` |  |
| secureIacPolicy.grpcMaxMsgSizeMbs | int | `700` |  |
| secureIacPolicy.image.repository | string | `"cspm-policy"` |  |
| secureIacPolicy.ingress[0].annotations."ingress.kubernetes.io/affinity" | string | `"cookie"` |  |
| secureIacPolicy.ingress[0].annotations."ingress.kubernetes.io/session-cookie-name" | string | `"INGRESSCOOKIEAPI"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-iac-policy-service"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[0].apiGatewayStickySessions | bool | `true` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-iac-policy-service"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[0].path | string | `"/api/cspm/v1/policy"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-iac-policy-service"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"secure-iac-policy-zones-service"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[1].apiGatewayStickySessions | bool | `true` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"secure-iac-policy-zones-service"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[1].path | string | `"/api/cspm/v1/zones"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[1].pathType | string | `"ImplementationSpecific"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[1].serviceName | string | `"secure-iac-policy-service"` |  |
| secureIacPolicy.ingress[0].hosts[0].paths[1].servicePort | int | `8080` |  |
| secureIacPolicy.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| secureIacPolicy.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| secureIacPolicy.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| secureIacPolicy.ingress[0].labels.role | string | `"ingress-config"` |  |
| secureIacPolicy.ingress[0].labels.tier | string | `"infra"` |  |
| secureIacPolicy.ingress[0].name | string | `"sysdigcloud-secure-iac-policy-ingress"` |  |
| secureIacPolicy.isOnprem | bool | `false` |  |
| secureIacPolicy.livenessDefaultProbeEnabled | bool | `true` |  |
| secureIacPolicy.port | int | `8080` |  |
| secureIacPolicy.readinessDefaultProbeEnabled | bool | `true` |  |
| secureIacPolicy.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureIacPolicy.replicaCount | int | `4` |  |
| secureIacPolicy.repositoryPrefix | string | `"secure"` |  |
| secureIacPolicy.resources.postgresqlinit.limits.cpu | string | `"200m"` |  |
| secureIacPolicy.resources.postgresqlinit.limits.memory | string | `"256Mi"` |  |
| secureIacPolicy.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| secureIacPolicy.resources.postgresqlinit.requests.memory | string | `"128Mi"` |  |
| secureIacPolicy.resources.secureIacPolicy.limits.cpu | int | `2` |  |
| secureIacPolicy.resources.secureIacPolicy.limits.memory | string | `"16Gi"` |  |
| secureIacPolicy.resources.secureIacPolicy.requests.cpu | float | `0.2` |  |
| secureIacPolicy.resources.secureIacPolicy.requests.memory | string | `"200Mi"` |  |
| secureIacPolicy.saveZonesV2API | bool | `false` |  |
| secureIacPolicy.serviceName | string | `"secure-iac-policy"` |  |
| secureIacPolicy.useZonesV2API | bool | `false` |  |
| secureIacPolicy.zoneServiceEndpoint | string | `"sysdigcloud-platform-zones-service-grpc"` |  |
| secureIacPolicy.zonesGrpcPort | int | `8091` |  |
| secureIacPolicy.zonesPort | int | `8090` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-iac-scheduler

![Version: 1.23.731-260223160854-main-vab7c18f6](https://img.shields.io/badge/Version-1.23.731--260223160854--main--vab7c18f6-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

IAC Scheduler Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| file://../common-v2 | iac-common | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dbImage.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-scheduler-db-migrations-postgres"` |  |
| dbImage.tag | string | `"1.23.731-260223160854-main-vab7c18f6"` |  |
| global.apps | string | `"secure"` |  |
| global.iac.apps | string | `"secure"` |  |
| global.iac.audit.workers | int | `5` |  |
| global.iac.cloudauth.endpoint | string | `"sysdigcloud-cloudauth-api-grpc:6000"` |  |
| global.iac.enabled | bool | `true` |  |
| global.iac.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.iac.metrics.annotations."prometheus.io/path" | string | `"/metrics"` |  |
| global.iac.metrics.annotations."prometheus.io/port" | string | `"25000"` |  |
| global.iac.metrics.annotations."prometheus.io/scrape" | string | `"true"` |  |
| global.iac.namespace | string | `"sysdig"` |  |
| global.iac.natsjs.endpoint | string | `"nats"` |  |
| global.iac.natsjs.insecure.enabled | bool | `false` |  |
| global.iac.natsjs.tls.enabled | bool | `true` |  |
| global.iac.posture.kspm.enabled | bool | `true` |  |
| global.iac.telemetry.segmentToken | string | `""` |  |
| global.infraRegistryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| global.legacyPostgres.postgresDatabases.scheduler.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.scheduler.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.scheduler.db | string | `"schedule"` |  |
| global.legacyPostgres.postgresDatabases.scheduler.forceSkipDbDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.scheduler.gke.sqlproxy.enabled | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.scheduler.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.scheduler.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.scheduler.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.scheduler.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.scheduler.username | string | `"schedulerdbuser"` |  |
| global.legacyRedis.redisClientsSecure.scheduler.tls | bool | `false` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.password | string | `""` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.namespace | string | `"sysdig"` |  |
| global.posture.kspm.enabled | bool | `true` |  |
| global.scaler.clusterName | string | `""` |  |
| image.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-scheduler"` |  |
| image.tag | string | `"1.23.731-260223160854-main-vab7c18f6"` |  |
| secureIacScheduler.audit.enabled | bool | `true` |  |
| secureIacScheduler.autoscale.enabled | bool | `false` |  |
| secureIacScheduler.autoscale.maxReplicaCount | int | `1` |  |
| secureIacScheduler.autoscale.minReplicaCount | int | `1` |  |
| secureIacScheduler.dbImage.repository | string | `"cspm-scheduler-db-migrations-postgres"` |  |
| secureIacScheduler.dumpHeapProfileEnabled | bool | `false` |  |
| secureIacScheduler.enableMultiInstanceSupport | bool | `false` |  |
| secureIacScheduler.enabled | bool | `true` |  |
| secureIacScheduler.grpcMaxMsgSizeMbs | int | `700` |  |
| secureIacScheduler.image.repository | string | `"cspm-scheduler"` |  |
| secureIacScheduler.ingress[0].annotations."ingress.kubernetes.io/affinity" | string | `"cookie"` |  |
| secureIacScheduler.ingress[0].annotations."ingress.kubernetes.io/session-cookie-name" | string | `"INGRESSCOOKIEAPI"` |  |
| secureIacScheduler.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-iac-scheduler-service"` |  |
| secureIacScheduler.ingress[0].hosts[0].paths[0].apiGatewayStickySessions | bool | `true` |  |
| secureIacScheduler.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-iac-scheduler-service"` |  |
| secureIacScheduler.ingress[0].hosts[0].paths[0].path | string | `"/api/cspm/v1/tasks"` |  |
| secureIacScheduler.ingress[0].hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| secureIacScheduler.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-iac-scheduler-service"` |  |
| secureIacScheduler.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| secureIacScheduler.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| secureIacScheduler.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| secureIacScheduler.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| secureIacScheduler.ingress[0].labels.role | string | `"ingress-config"` |  |
| secureIacScheduler.ingress[0].labels.tier | string | `"infra"` |  |
| secureIacScheduler.ingress[0].name | string | `"sysdigcloud-secure-iac-scheduler-ingress"` |  |
| secureIacScheduler.livenessDefaultProbeEnabled | bool | `true` |  |
| secureIacScheduler.maxPolledScheduledTasks | int | `50` |  |
| secureIacScheduler.maxRevaluationTasks | int | `100` |  |
| secureIacScheduler.natsjs.consumer.ackWait | string | `"600s"` |  |
| secureIacScheduler.natsjs.consumer.durable | string | `"secure-iac-agenthandler-consumer-durable"` |  |
| secureIacScheduler.natsjs.consumer.maxInFlight | int | `1024` |  |
| secureIacScheduler.natsjs.consumer.msgMaxRetries | int | `3` |  |
| secureIacScheduler.natsjs.consumer.nakDeliverBackOff | string | `"10s"` |  |
| secureIacScheduler.natsjs.consumer.name | string | `"secure-iac-agenthandler-consumer"` |  |
| secureIacScheduler.natsjs.consumer.pullBatch | int | `10` |  |
| secureIacScheduler.natsjs.consumer.streamName | string | `"secure-iac-agenthandler"` |  |
| secureIacScheduler.natsjs.consumer.subject | string | `"agenthandler.>"` |  |
| secureIacScheduler.pendingPublishPollDuration | string | `"30s"` |  |
| secureIacScheduler.port | int | `8080` |  |
| secureIacScheduler.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureIacScheduler.replicaCount | int | `1` |  |
| secureIacScheduler.repositoryPrefix | string | `"secure"` |  |
| secureIacScheduler.resources.postgresqlinit.limits.cpu | string | `"200m"` |  |
| secureIacScheduler.resources.postgresqlinit.limits.memory | string | `"256Mi"` |  |
| secureIacScheduler.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| secureIacScheduler.resources.postgresqlinit.requests.memory | string | `"128Mi"` |  |
| secureIacScheduler.resources.secureIacScheduler.limits.cpu | int | `1` |  |
| secureIacScheduler.resources.secureIacScheduler.limits.memory | string | `"2Gi"` |  |
| secureIacScheduler.resources.secureIacScheduler.requests.cpu | float | `0.2` |  |
| secureIacScheduler.resources.secureIacScheduler.requests.memory | string | `"200Mi"` |  |
| secureIacScheduler.scheduleTasksPollDuration | string | `"30s"` |  |
| secureIacScheduler.serviceName | string | `"secure-iac-scheduler"` |  |
| secureIacScheduler.skipDuplicatedPendingTasks | bool | `false` |  |
| secureIacScheduler.stuckTasksPollDuration | string | `"10m"` |  |
| secureIacScheduler.taskLifespanDuration | string | `"720h"` |  |
| secureIacScheduler.taskPurgePollDuration | string | `"30m"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-iac-workload

![Version: 1.23.731-260223173951-main-v1c6494f6](https://img.shields.io/badge/Version-1.23.731--260223173951--main--v1c6494f6-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

IAC Workload Service

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| file://../common-v2 | iac-common | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 1.0.0 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.13.2 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| dbImage.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-workload-db-migrations-postgres"` |  |
| dbImage.tag | string | `"1.23.731-260223173951-main-v1c6494f6"` |  |
| global.apps | string | `"secure"` |  |
| global.iac.audit.workers | int | `5` |  |
| global.iac.graphdb.enabled | bool | `true` |  |
| global.iac.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| global.iac.metrics."prometheus.io/path" | string | `"/metrics"` |  |
| global.iac.metrics."prometheus.io/port" | string | `"25000"` |  |
| global.iac.metrics."prometheus.io/scrape" | string | `"true"` |  |
| global.iac.namespace | string | `"sysdig"` |  |
| global.iac.natsjs.endpoint | string | `"nats"` |  |
| global.iac.natsjs.insecure.enabled | bool | `false` |  |
| global.iac.natsjs.panicOnClosedConnection | bool | `true` |  |
| global.iac.natsjs.tls.enabled | bool | `true` |  |
| global.iac.services.acengine.enabled | bool | `false` |  |
| global.iac.telemetry.segmentToken | string | `""` |  |
| global.legacyPostgres.postgresDatabases.workload.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.workload.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.workload.db | string | `"workload"` |  |
| global.legacyPostgres.postgresDatabases.workload.forceSkipDbDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.workload.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.workload.idleConns | int | `10` |  |
| global.legacyPostgres.postgresDatabases.workload.idleTimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.workload.maxConnLife | string | `"1h"` |  |
| global.legacyPostgres.postgresDatabases.workload.maxConns | int | `15` |  |
| global.legacyPostgres.postgresDatabases.workload.maxUserConns | int | `100` |  |
| global.legacyPostgres.postgresDatabases.workload.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.workload.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.workload.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.workload.username | string | `"workloaddbuser"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.posture.kspm.enabled | bool | `true` |  |
| global.scaler.clusterName | string | `""` |  |
| image.repository | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker/secure/cspm-workload"` |  |
| image.tag | string | `"1.23.731-260223173951-main-v1c6494f6"` |  |
| secureIacWorkload.audit.enabled | bool | `true` |  |
| secureIacWorkload.autoscale.enabled | bool | `true` |  |
| secureIacWorkload.autoscale.profiles[0].enabled | bool | `true` |  |
| secureIacWorkload.autoscale.profiles[0].name | string | `"Memory + CPU + Collector results - Pending messages"` |  |
| secureIacWorkload.autoscale.scaleDownSelectPolicy | string | `"Disabled"` |  |
| secureIacWorkload.dbImage.repository | string | `"cspm-workload-db-migrations-postgres"` |  |
| secureIacWorkload.enabled | bool | `true` |  |
| secureIacWorkload.graphDryRun | bool | `false` |  |
| secureIacWorkload.grpcMaxMsgSizeMbs | int | `700` |  |
| secureIacWorkload.iaFindingsEnabled | bool | `true` |  |
| secureIacWorkload.image.repository | string | `"cspm-workload"` |  |
| secureIacWorkload.ingress[0].annotations."ingress.kubernetes.io/affinity" | string | `"cookie"` |  |
| secureIacWorkload.ingress[0].annotations."ingress.kubernetes.io/session-cookie-name" | string | `"INGRESSCOOKIEAPI"` |  |
| secureIacWorkload.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-iac-workload-service"` |  |
| secureIacWorkload.ingress[0].hosts[0].paths[0].apiGatewayStickySessions | bool | `true` |  |
| secureIacWorkload.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-iac-workload-service"` |  |
| secureIacWorkload.ingress[0].hosts[0].paths[0].path | string | `"/api/cspm/v1/kube"` |  |
| secureIacWorkload.ingress[0].hosts[0].paths[0].pathType | string | `"ImplementationSpecific"` |  |
| secureIacWorkload.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-iac-workload-service"` |  |
| secureIacWorkload.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| secureIacWorkload.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| secureIacWorkload.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| secureIacWorkload.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| secureIacWorkload.ingress[0].labels.role | string | `"ingress-config"` |  |
| secureIacWorkload.ingress[0].labels.tier | string | `"infra"` |  |
| secureIacWorkload.ingress[0].name | string | `"sysdigcloud-secure-iac-workload-ingress"` |  |
| secureIacWorkload.livenessDefaultProbeEnabled | bool | `true` |  |
| secureIacWorkload.mongoEnabled | bool | `false` |  |
| secureIacWorkload.natsJetstreamEnabled | bool | `true` |  |
| secureIacWorkload.natsjs.iac_request.consumer.ackWait | string | `"2m"` |  |
| secureIacWorkload.natsjs.iac_request.consumer.concurrentRoutinesCount | int | `3` |  |
| secureIacWorkload.natsjs.iac_request.consumer.deliverPolicyAll | bool | `true` |  |
| secureIacWorkload.natsjs.iac_request.consumer.durable | string | `"secureiac-manifestextractor-codescan-workload-durable"` |  |
| secureIacWorkload.natsjs.iac_request.consumer.handleTimeout | string | `"5m"` |  |
| secureIacWorkload.natsjs.iac_request.consumer.maxDeliver | int | `3` |  |
| secureIacWorkload.natsjs.iac_request.consumer.maxInFlight | int | `2048` |  |
| secureIacWorkload.natsjs.iac_request.consumer.name | string | `"secureiac-manifestextractor-codescan-workload"` |  |
| secureIacWorkload.natsjs.iac_request.consumer.pull | bool | `true` |  |
| secureIacWorkload.natsjs.iac_request.consumer.pullBatch | int | `25` |  |
| secureIacWorkload.natsjs.iac_request.consumer.stream | string | `"secure-iac-manifestextractor-codescan-request"` |  |
| secureIacWorkload.natsjs.iac_request.consumer.subject | string | `"secure.iac.manifestextractor.codescan.request.k8s"` |  |
| secureIacWorkload.natsjsCodeScanEnabled | bool | `true` |  |
| secureIacWorkload.port | int | `8080` |  |
| secureIacWorkload.postgresEnabled | bool | `true` |  |
| secureIacWorkload.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureIacWorkload.replicaCount | int | `1` |  |
| secureIacWorkload.repos.pg.enableFullQueryLog | bool | `false` |  |
| secureIacWorkload.repos.pg.log.slowQueryThreshold | string | `"500ms"` |  |
| secureIacWorkload.repos.pg.read | string | `"all"` |  |
| secureIacWorkload.repos.pg.write | string | `"all"` |  |
| secureIacWorkload.repositoryPrefix | string | `"secure"` |  |
| secureIacWorkload.resources.postgresqlinit.limits.cpu | string | `"200m"` |  |
| secureIacWorkload.resources.postgresqlinit.limits.memory | string | `"256Mi"` |  |
| secureIacWorkload.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| secureIacWorkload.resources.postgresqlinit.requests.memory | string | `"128Mi"` |  |
| secureIacWorkload.resources.secureIacWorkload.limits.cpu | int | `2` |  |
| secureIacWorkload.resources.secureIacWorkload.limits.memory | string | `"2Gi"` |  |
| secureIacWorkload.resources.secureIacWorkload.requests.cpu | float | `0.2` |  |
| secureIacWorkload.resources.secureIacWorkload.requests.memory | string | `"50Mi"` |  |
| secureIacWorkload.serviceName | string | `"secure-iac-workload"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-query-storage-api

![Version: 0.1.0-260304152653-main-v58e062c](https://img.shields.io/badge/Version-0.1.0--260304152653--main--v58e062c-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig Query Storage API

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"secure"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.queryStorageApi.admindb | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.queryStorageApi.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.queryStorageApi.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.queryStorageApi.db | string | `"sysql"` |  |
| global.legacyPostgres.postgresDatabases.queryStorageApi.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.queryStorageApi.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.queryStorageApi.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.queryStorageApi.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.queryStorageApi.username | string | `"sysqluser"` |  |
| global.monitor.endpoint | string | `"http://localhost"` |  |
| global.monitor.legacy | bool | `false` |  |
| global.monitor.skipTLS | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.secretsManagement.generate | bool | `true` |  |
| global.secure.sysqlApi.serviceToken | string | `nil` |  |
| global.secureRepositoryPrefix | string | `"secure"` |  |
| secureQueryStorageApi.audit.enabled | bool | `false` |  |
| secureQueryStorageApi.auth.disabled | bool | `false` |  |
| secureQueryStorageApi.cron.enabled | bool | `true` |  |
| secureQueryStorageApi.cron.schedule | string | `"0 0 * * * "` |  |
| secureQueryStorageApi.enabled | bool | `true` |  |
| secureQueryStorageApi.host | string | `"0.0.0.0"` |  |
| secureQueryStorageApi.image.pullSecret | string | `"sysdigcloud-pull-secret"` |  |
| secureQueryStorageApi.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-query-storage-api"` |  |
| secureQueryStorageApi.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-query-storage-api"` |  |
| secureQueryStorageApi.ingress[0].hosts[0].paths[0].path | string | `"/api/query-storage/v1"` |  |
| secureQueryStorageApi.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-query-storage-api"` |  |
| secureQueryStorageApi.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| secureQueryStorageApi.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| secureQueryStorageApi.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| secureQueryStorageApi.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| secureQueryStorageApi.ingress[0].labels.role | string | `"ingress-config"` |  |
| secureQueryStorageApi.ingress[0].labels.tier | string | `"infra"` |  |
| secureQueryStorageApi.ingress[0].name | string | `"query-storage-api-ingress"` |  |
| secureQueryStorageApi.initDb.enabled | bool | `true` |  |
| secureQueryStorageApi.initDb.image.pullSecret | string | `"sysdigcloud-pull-secret"` |  |
| secureQueryStorageApi.livenessProbe.enabled | bool | `true` |  |
| secureQueryStorageApi.logging | string | `"info"` |  |
| secureQueryStorageApi.port | int | `8080` |  |
| secureQueryStorageApi.readinessProbe.enabled | bool | `true` |  |
| secureQueryStorageApi.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureQueryStorageApi.replicas | int | `1` |  |
| secureQueryStorageApi.reporting.historyLimitCount | int | `20` |  |
| secureQueryStorageApi.reporting.historyLimitDays | int | `30` |  |
| secureQueryStorageApi.reporting.maxRows | int | `10000` |  |
| secureQueryStorageApi.reporting.pageSize | int | `1000` |  |
| secureQueryStorageApi.repositoryPrefix | string | `"secure"` |  |
| secureQueryStorageApi.resources.janitor.limits.cpu | string | `"100m"` |  |
| secureQueryStorageApi.resources.janitor.limits.memory | string | `"128Mi"` |  |
| secureQueryStorageApi.resources.janitor.requests.cpu | string | `"100m"` |  |
| secureQueryStorageApi.resources.janitor.requests.memory | string | `"128Mi"` |  |
| secureQueryStorageApi.resources.postgresqlinit.limits.cpu | string | `"200m"` |  |
| secureQueryStorageApi.resources.postgresqlinit.limits.memory | string | `"256Mi"` |  |
| secureQueryStorageApi.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| secureQueryStorageApi.resources.postgresqlinit.requests.memory | string | `"128Mi"` |  |
| secureQueryStorageApi.resources.queryStorageApi.limits.cpu | int | `2` |  |
| secureQueryStorageApi.resources.queryStorageApi.limits.memory | string | `"2Gi"` |  |
| secureQueryStorageApi.resources.queryStorageApi.requests.cpu | string | `"250m"` |  |
| secureQueryStorageApi.resources.queryStorageApi.requests.memory | string | `"250Mi"` |  |
| secureQueryStorageApi.securityContext.readOnlyRootFilesystem | bool | `true` |  |
| secureQueryStorageApi.securityContext.runAsRoot | bool | `false` |  |
| secureQueryStorageApi.segmentToken | string | `""` |  |
| secureQueryStorageApi.serviceAccountName | string | `"sysdig"` |  |
| secureQueryStorageApi.serviceName | string | `"secure-query-storage-api"` |  |
| secureQueryStorageApi.serviceToken | string | `nil` |  |
| secureQueryStorageApi.startupProbe.enabled | bool | `true` |  |
| secureQueryStorageApi.startupProbe.failureThreshold | int | `3` |  |
| secureQueryStorageApi.startupProbe.initialDelaySeconds | int | `5` |  |
| secureQueryStorageApi.startupProbe.periodSeconds | int | `10` |  |
| secureQueryStorageApi.startupProbe.successThreshold | int | `1` |  |
| secureQueryStorageApi.startupProbe.timeoutSeconds | int | `5` |  |
| secureQueryStorageApi.sysql.api.address | string | `"secure-sysql-api:6000"` |  |
| secureQueryStorageApi.sysql.api.receiveMessageSize | int | `8388608` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# secure-resource-ingestion

![Version: 3.0.0-260312144637-main-v4c6c8c7](https://img.shields.io/badge/Version-3.0.0--260312144637--main--v4c6c8c7-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Secure resource ingestion

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.secureResourceIngestion.serviceToken | string | `"overwriteMe"` |  |
| global.apps | string | `"secure"` |  |
| global.cloudProvider.name | string | `""` |  |
| global.cloudProvider.region | string | `""` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.admindbname | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.dbname | string | `"resource_ingestion"` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.hashpartitioncount | int | `32` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.host | string | `"sysdig-postgres"` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.maxconnections | int | `50` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.schema | string | `"resource_ingestion"` |  |
| global.legacyPostgres.postgresDatabases.resourceingestion.username | string | `"resource_ingestion_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.postgresImageName | string | `"postgres"` |  |
| global.postgresImageVersion | string | `"12.7.0.1"` |  |
| secureResourceIngestion.auth.endpoint.url | string | `"http://sysdigcloud-api:8080"` |  |
| secureResourceIngestion.auth.skipTls | bool | `false` |  |
| secureResourceIngestion.clusterIngestedResourcesPublisherEnabled | bool | `false` |  |
| secureResourceIngestion.clusterIngestionEnabled | bool | `false` |  |
| secureResourceIngestion.configservice.url | string | `"http://secure-config-service:8080"` |  |
| secureResourceIngestion.enabled | bool | `true` |  |
| secureResourceIngestion.fullCloudScanIngestedResourcesPublisherEnabled | bool | `false` |  |
| secureResourceIngestion.fullCloudScanResultsIngestionEnabled | bool | `false` |  |
| secureResourceIngestion.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-resource-ingestion"` |  |
| secureResourceIngestion.ingress[0].hosts[0].paths[0].apiGatewayStickySessions | bool | `true` |  |
| secureResourceIngestion.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-resource-ingestion"` |  |
| secureResourceIngestion.ingress[0].hosts[0].paths[0].path | string | `"/api/secure-data/resourceingestion/v1"` |  |
| secureResourceIngestion.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-resource-ingestion-api-http"` |  |
| secureResourceIngestion.ingress[0].hosts[0].paths[0].servicePort | int | `7000` |  |
| secureResourceIngestion.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| secureResourceIngestion.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| secureResourceIngestion.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| secureResourceIngestion.ingress[0].labels.role | string | `"ingress-config"` |  |
| secureResourceIngestion.ingress[0].labels.tier | string | `"infra"` |  |
| secureResourceIngestion.ingress[0].name | string | `"secure-resource-ingestion-ingress"` |  |
| secureResourceIngestion.ingressesEnabled | bool | `false` |  |
| secureResourceIngestion.k8sWorkloadIngestedResourcesPublisherEnabled | bool | `false` |  |
| secureResourceIngestion.k8sWorkloadIngestionEnabled | bool | `false` |  |
| secureResourceIngestion.logLevel | string | `"info"` |  |
| secureResourceIngestion.nats.consumer.realtime.name | string | `"resource-ingestion-realtime"` |  |
| secureResourceIngestion.nats.consumer.realtime.stream.name | string | `"secure-data-resources"` |  |
| secureResourceIngestion.nats.consumer.realtime.subject | string | `"secure.data.resources.realtime"` |  |
| secureResourceIngestion.nats.consumer.scanresults.name | string | `"resource-ingestion"` |  |
| secureResourceIngestion.nats.consumer.scanresults.stream.name | string | `"secure-data-resources"` |  |
| secureResourceIngestion.nats.consumer.scanresults.subject | string | `"secure.data.resources.scanresults"` |  |
| secureResourceIngestion.nats.tlsEnabled | bool | `true` |  |
| secureResourceIngestion.nats.url | string | `"nats"` |  |
| secureResourceIngestion.objectStorage.bucket | string | `"mybucket"` |  |
| secureResourceIngestion.objectStorage.endpoint | string | `"myendpoint"` |  |
| secureResourceIngestion.objectStorage.type | string | `"mytype"` |  |
| secureResourceIngestion.realTimeScanEnabled | bool | `false` |  |
| secureResourceIngestion.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| secureResourceIngestion.replicaCount | int | `1` |  |
| secureResourceIngestion.repositoryPrefix | string | `"secure"` |  |
| secureResourceIngestion.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| secureResourceIngestion.resources.postgresqlinit.limits.memory | string | `"500Mi"` |  |
| secureResourceIngestion.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| secureResourceIngestion.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| secureResourceIngestion.resources.resourceingestion.limits.cpu | int | `2` |  |
| secureResourceIngestion.resources.resourceingestion.limits.memory | string | `"4Gi"` |  |
| secureResourceIngestion.resources.resourceingestion.requests.cpu | string | `"250m"` |  |
| secureResourceIngestion.resources.resourceingestion.requests.memory | string | `"250Mi"` |  |
| secureResourceIngestion.scaler.authenticationRef | string | `"keda-monitor-operations-prodmon"` |  |
| secureResourceIngestion.scaler.enabled | bool | `true` |  |
| secureResourceIngestion.scaler.maxReplicaCount | int | `10` |  |
| secureResourceIngestion.scaler.minReplicaCount | int | `1` |  |
| secureResourceIngestion.scaler.serverAddress | string | `"https://prodmon.app.sysdig.com/prometheus"` |  |
| secureResourceIngestion.scaler.thresholds.cpuThreshold | int | `100` |  |
| secureResourceIngestion.scaler.thresholds.memoryThreshold | int | `90` |  |
| secureResourceIngestion.scaler.thresholds.messagesThreshold | int | `70` |  |
| secureResourceIngestion.serviceAccount.annotations | object | `{}` |  |
| secureResourceIngestion.zoneservice.url | string | `"sysdigcloud-platform-zones-service-grpc:8091"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# sysdig-certificate-exporter

![Version: 0.2.0](https://img.shields.io/badge/Version-0.2.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 3.15.4](https://img.shields.io/badge/AppVersion-3.15.4-informational?style=flat-square)

the Sysdig Certificate Exporter helm chart

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.namespace | string | `"sysdig"` |  |
| global.tolerations | list | `[]` |  |
| sysdigCertificateExporter.blackbox.enabled | bool | `false` |  |
| sysdigCertificateExporter.blackbox.podListenPort | string | `"9115"` |  |
| sysdigCertificateExporter.blackbox.version | string | `"0.0.29"` |  |
| sysdigCertificateExporter.cacheEnabled | bool | `true` |  |
| sysdigCertificateExporter.cacheMaxDuration | string | `"300"` |  |
| sysdigCertificateExporter.debug | bool | `false` |  |
| sysdigCertificateExporter.enabled | bool | `true` |  |
| sysdigCertificateExporter.exposePerCertificateErrorMetrics | bool | `true` |  |
| sysdigCertificateExporter.exposeRelativeMetrics | bool | `true` |  |
| sysdigCertificateExporter.hostNetwork | bool | `false` |  |
| sysdigCertificateExporter.podListenPort | string | `"9793"` |  |
| sysdigCertificateExporter.resources.sslExporter.limits.cpu | string | `"100m"` |  |
| sysdigCertificateExporter.resources.sslExporter.limits.memory | string | `"40Mi"` |  |
| sysdigCertificateExporter.resources.sslExporter.requests.cpu | string | `"10m"` |  |
| sysdigCertificateExporter.resources.sslExporter.requests.memory | string | `"20Mi"` |  |
| sysdigCertificateExporter.resources.sslExporterBlackbox.limits.cpu | string | `"100m"` |  |
| sysdigCertificateExporter.resources.sslExporterBlackbox.limits.memory | string | `"300Mi"` |  |
| sysdigCertificateExporter.resources.sslExporterBlackbox.requests.cpu | string | `"20m"` |  |
| sysdigCertificateExporter.resources.sslExporterBlackbox.requests.memory | string | `"50Mi"` |  |
| sysdigCertificateExporter.runAsGroup | string | `"1000"` |  |
| sysdigCertificateExporter.runAsUser | string | `"1000"` |  |
| sysdigCertificateExporter.version | string | `"0.0.33"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# sysdig-common-config

![Version: 0.4.6](https://img.shields.io/badge/Version-0.4.6-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 0.1.0](https://img.shields.io/badge/AppVersion-0.1.0-informational?style=flat-square)

Legacy shared configuration for OnPrem/Installer

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.12.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| cassandra | object | `{}` |  |
| elasticsearch.mastersReplicaCount | int | `1` |  |
| elasticsearch.replicaCount | int | `1` |  |
| elasticsearch.workloadName | string | `"elasticsearch"` |  |
| global.apps | string | `"monitor secure"` |  |
| global.cassandra.replicaCount | int | `1` |  |
| global.cassandra.sslCaCrt | string | `"change_me"` |  |
| global.cassandra.workloadName | string | `"cassandra"` |  |
| global.certificate.serverCrt | string | `"change_me"` |  |
| global.certificate.serverKey | string | `"change_me"` |  |
| global.cloudProvider.isMultiAZ | bool | `true` |  |
| global.elasticsearch.hostname | string | `"elasticsearch-example-hostname"` |  |
| global.elasticsearch.serviceAccount | string | `"elasticsearch"` |  |
| global.enableRedisTlsUpgrade | bool | `false` |  |
| global.kafka.name | string | `"kafka"` |  |
| global.kafka.secure.enabled | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.quartz.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.quartz.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.sysdig.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.sysdig.password | string | `nil` |  |
| global.legacyRedis.redisTls.enabled | bool | `false` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.sysdigRedis.password | string | `"change_me"` |  |
| global.meerkat.enabled | bool | `false` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.nats.enabled | bool | `true` |  |
| global.networkEncryption.enabled | bool | `false` |  |
| global.postgresql.ha.enabled | bool | `false` |  |
| global.postgresql.ha.replicas | int | `1` |  |
| global.scanningv2.customCerts | bool | `false` |  |
| global.storageClassName | string | `"default"` |  |
| global.storageClassType | string | `"gp2"` |  |
| global.zookeeper.name | string | `"zookeeper"` |  |
| kafka.replicaCount | int | `1` |  |
| nats.cluster.replicas | int | `1` |  |
| postgresql.rootDb | string | `"change_me"` |  |
| postgresql.rootUser | string | `"change_me"` |  |
| sysdigCommonConfig.hostPathConfigs.hostPathCustomPaths.cassandra | string | `"/var/lib/cassandra"` |  |
| sysdigCommonConfig.hostPathConfigs.hostPathCustomPaths.elasticsearch | string | `"/usr/share/elasticsearch"` |  |
| sysdigCommonConfig.hostPathConfigs.hostPathCustomPaths.kafka | string | `"/var/lib/kafka"` |  |
| sysdigCommonConfig.hostPathConfigs.hostPathCustomPaths.natsJs | string | `"/var/lib/nats-js"` |  |
| sysdigCommonConfig.hostPathConfigs.hostPathCustomPaths.neo4j | string | `"/var/lib/neo4j"` |  |
| sysdigCommonConfig.hostPathConfigs.hostPathCustomPaths.postgresql | string | `"/var/lib/postgresql/data/pgdata"` |  |
| sysdigCommonConfig.hostPathConfigs.hostPathCustomPaths.redis | string | `"/redis-upgrade"` |  |
| sysdigCommonConfig.hostPathConfigs.hostPathCustomPaths.zookeeper | string | `"/var/lib/zookeeper"` |  |
| sysdigCommonConfig.hostPathConfigs.hostPathNodesMapping | object | `{}` |  |
| sysdigCommonConfig.nats | object | `{}` |  |
| sysdigCommonConfig.postgresql.rootPassword | string | `""` |  |
| sysdigCommonConfig.pvStorageSize.large | object | `{}` |  |
| sysdigCommonConfig.pvStorageSize.medium.cassandra | string | `"150Gi"` |  |
| sysdigCommonConfig.pvStorageSize.medium.elasticsearch | string | `"150Gi"` |  |
| sysdigCommonConfig.pvStorageSize.medium.natsJs | string | `"150Gi"` |  |
| sysdigCommonConfig.pvStorageSize.medium.redis | string | `"100Gi"` |  |
| sysdigCommonConfig.pvStorageSize.small | object | `{}` |  |
| sysdigCommonConfig.size | string | `"medium"` | -------------------------------------------------------------- |
| sysdigCommonConfig.skipNamespace | bool | `false` |  |
| sysdigCommonConfig.skipPullSecret | bool | `false` |  |
| sysdigCommonConfig.skipServiceAccount | bool | `false` |  |
| sysdigCommonConfig.skipStorageClass | bool | `false` |  |
| zookeeper.replicaCount | int | `1` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# sysql-api

![Version: 0.5.11-260309160029-main-v99476e5](https://img.shields.io/badge/Version-0.5.11--260309160029--main--v99476e5-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig SysQL API Server

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| clickhouse.dataBaseConfig.dbName | string | `"sysdig"` |  |
| clickhouse.dataBaseConfig.endPoint | string | `"clickhouse.sysdig.svc.cluster.local:9000"` |  |
| clickhouse.dataBaseConfig.insecureSkipVerify | bool | `false` |  |
| clickhouse.dataBaseConfig.maxConnections | int | `32` |  |
| clickhouse.dataBaseConfig.tlsEnabled | bool | `false` |  |
| clickhouse.olapdbReporting.password | string | `"password"` |  |
| clickhouse.olapdbReporting.readTimeoutSeconds | int | `300` |  |
| clickhouse.olapdbReporting.username | string | `"reader"` |  |
| global.apps | string | `"secure"` |  |
| global.clickhouse.enabled | bool | `true` |  |
| global.clickhouse.readerPassword | string | `"password"` |  |
| global.clickhouse.tls.enabled | bool | `false` |  |
| global.clickhouse.tls.fips | bool | `false` |  |
| global.clickhouse.tls.useCertManager | bool | `false` |  |
| global.cloudProvider.isMultiAZ | string | `nil` |  |
| global.dnsName | string | `"change-me.com"` |  |
| global.monitor.endpoint | string | `"http://sysdigcloud-api:8080"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.neo4j.certManager.enabled | bool | `false` |  |
| global.neo4jDatabases.graphquery.endpoint | string | `"bolt://host.docker.internal:7687"` |  |
| global.neo4jDatabases.graphquery.password | string | `nil` |  |
| global.neo4jDatabases.graphquery.username | string | `"neo4j"` |  |
| global.neo4jDatabases.streamTimeoutPerRowSecs | int | `30` |  |
| global.olapdb.insecureSkipVerify | bool | `false` |  |
| global.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| global.repositoryPrefix | string | `"secure"` |  |
| global.secure.olapdbReporting.clickhouse.enabled | bool | `true` |  |
| global.secure.sysqlApi.enabled | bool | `true` |  |
| global.secure.sysqlApi.serviceToken | string | `nil` |  |
| global.secureRepositoryPrefix | string | `"secure"` |  |
| sysdig.secure.olapdbReporting.clickhouse.enabled | bool | `true` |  |
| sysqlApi.enabled | bool | `true` |  |
| sysqlApi.grpc_server.concurrencyLimitPerConnection | int | `16` |  |
| sysqlApi.grpc_server.disableHealthCheck | bool | `false` |  |
| sysqlApi.grpc_server.enableRateLimiter | bool | `false` |  |
| sysqlApi.grpc_server.enabled | bool | `true` |  |
| sysqlApi.grpc_server.maxBlockingThreads | int | `100` |  |
| sysqlApi.grpc_server.maxConcurrentStreams | int | `250` |  |
| sysqlApi.grpc_server.minWorkerThreads | int | `4` |  |
| sysqlApi.grpc_server.port | int | `6000` |  |
| sysqlApi.grpc_server.threadKeepAlive | string | `"60s"` |  |
| sysqlApi.host | string | `"0.0.0.0"` |  |
| sysqlApi.http_server.enabled | bool | `true` |  |
| sysqlApi.http_server.maxBlockingThreads | int | `512` |  |
| sysqlApi.http_server.port | int | `8080` |  |
| sysqlApi.http_server.threadKeepAlive | string | `"60s"` |  |
| sysqlApi.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"secure-sysql-api"` |  |
| sysqlApi.ingress[0].hosts[0].paths[0].apiGatewayTimeoutSeconds | int | `360` |  |
| sysqlApi.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"secure-sysql-api"` |  |
| sysqlApi.ingress[0].hosts[0].paths[0].openshiftTargetPort | int | `8080` |  |
| sysqlApi.ingress[0].hosts[0].paths[0].openshiftTargetTLSPort | int | `443` |  |
| sysqlApi.ingress[0].hosts[0].paths[0].path | string | `"/api/sysql"` |  |
| sysqlApi.ingress[0].hosts[0].paths[0].serviceName | string | `"secure-sysql-api"` |  |
| sysqlApi.ingress[0].hosts[0].paths[0].servicePort | int | `80` |  |
| sysqlApi.ingress[0].hosts[0].paths[0].serviceTLSPort | int | `443` |  |
| sysqlApi.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| sysqlApi.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| sysqlApi.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| sysqlApi.ingress[0].labels.role | string | `"ingress-config"` |  |
| sysqlApi.ingress[0].labels.tier | string | `"infra"` |  |
| sysqlApi.ingress[0].name | string | `"secure-sysql-api"` |  |
| sysqlApi.maxConnectionAgeGraceSec | int | `600` |  |
| sysqlApi.maxConnectionAgeSec | int | `900` |  |
| sysqlApi.maxTimeToFirstByteSec | int | `300` |  |
| sysqlApi.neo4j.databases_map | string | `nil` |  |
| sysqlApi.neo4j.defaultDb | string | `"neo4j"` |  |
| sysqlApi.neo4j.fetchSize | int | `1000` |  |
| sysqlApi.neo4j.maxConnections | int | `32` |  |
| sysqlApi.neo4j.skip_ssl_validation | bool | `false` |  |
| sysqlApi.neo4jTLSGenerator.enabled | bool | `true` |  |
| sysqlApi.requiresUserTeam | bool | `true` |  |
| sysqlApi.resources.sysqlApi.limits.cpu | int | `8` |  |
| sysqlApi.resources.sysqlApi.limits.memory | string | `"10Gi"` |  |
| sysqlApi.resources.sysqlApi.requests.cpu | int | `4` |  |
| sysqlApi.resources.sysqlApi.requests.memory | string | `"4Gi"` |  |
| sysqlApi.responseBufferSize | int | `1` |  |
| sysqlApi.scaler.enabled | bool | `true` |  |
| sysqlApi.scaler.maxReplicaCount | int | `10` |  |
| sysqlApi.scaler.minReplicaCount | int | `4` |  |
| sysqlApi.scaler.thresholds.cpuThreshold | int | `90` |  |
| sysqlApi.scaler.thresholds.memoryThreshold | int | `90` |  |
| sysqlApi.securityContext.runAsRoot | bool | `false` |  |
| sysqlApi.serviceAccountName | string | `"sysdig"` |  |
| sysqlApi.sysql.customer_rate_limiter.burst_size | int | `250` |  |
| sysqlApi.sysql.customer_rate_limiter.enabled | bool | `true` |  |
| sysqlApi.sysql.customer_rate_limiter.refill_interval | string | `"1s"` |  |
| sysqlApi.sysql.feature_flags.enable_customer_id_impersonation | bool | `false` |  |
| sysqlApi.sysql.feature_flags.enable_customer_id_routing | bool | `false` |  |
| sysqlApi.sysql.grpc_default_version | string | `"0.14.35"` |  |
| sysqlApi.sysql.index_mapping.analytics/v1-alpha | string | `"0.2.0+clickhouse"` |  |
| sysqlApi.sysql.index_mapping.v1 | string | `"0.14.35"` |  |
| sysqlApi.sysql.index_mapping.v2 | string | `"0.16.73"` |  |
| sysqlApi.sysql.index_mapping.v3-alpha | string | `"0.17.47"` |  |
| sysqlApi.sysql.index_path | string | `"/usr/local/indexes"` |  |
| sysqlApi.sysql.instance_rate_limiter.burst_size | int | `500` |  |
| sysqlApi.sysql.instance_rate_limiter.enabled | bool | `true` |  |
| sysqlApi.sysql.instance_rate_limiter.refill_interval | string | `"1s"` |  |
| sysqlApi.sysql.issuer_rate_limiter.burst_size | int | `100` |  |
| sysqlApi.sysql.issuer_rate_limiter.enabled | bool | `true` |  |
| sysqlApi.sysql.issuer_rate_limiter.refill_interval | string | `"1s"` |  |
| sysqlApi.sysql.limit | int | `50` |  |
| sysqlApi.sysql.maxLimit | int | `10000` |  |
| sysqlApi.userCacheMaxSize | int | `1000` |  |
| sysqlApi.userCacheTimeToLive | int | `3600` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# ticketing

![Version: 5.1.1-260311143806-main-v146dafc](https://img.shields.io/badge/Version-5.1.1--260311143806--main--v146dafc-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Ticketing

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.10.1 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.api.serviceTokens.ticketing.serviceToken | string | `nil` |  |
| global.apps | string | `"secure"` |  |
| global.gke.sqlproxy.enabled | bool | `false` |  |
| global.infraRepositoryPrefix | string | `"infra"` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.legacyPostgres.postgresDatabases.ticketing.admindb | string | `"anchore"` |  |
| global.legacyPostgres.postgresDatabases.ticketing.adminpassword | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.ticketing.adminusername | string | `"postgres"` |  |
| global.legacyPostgres.postgresDatabases.ticketing.db | string | `"ticketing"` |  |
| global.legacyPostgres.postgresDatabases.ticketing.forceSkipDownMigrations | bool | `false` |  |
| global.legacyPostgres.postgresDatabases.ticketing.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.ticketing.idletxtimeout | string | `"60min"` |  |
| global.legacyPostgres.postgresDatabases.ticketing.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.ticketing.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.ticketing.sslmode | string | `"disable"` |  |
| global.legacyPostgres.postgresDatabases.ticketing.username | string | `"ticketing_user"` |  |
| global.namespace | string | `"sysdig"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.postgresImageName | string | `"postgres-12"` |  |
| global.postgresVersion | string | `"0.0.3"` |  |
| global.secure.ingestion.endpoint | string | `"sysdigcloud-events-ingestion:3000"` |  |
| ticketing.aesKey | string | `nil` |  |
| ticketing.audit.enabled | bool | `false` |  |
| ticketing.certman.cacheCleanupInterval | string | `"1m"` |  |
| ticketing.certman.cacheDefaultExpiration | string | `"15m"` |  |
| ticketing.certman.endpoint | string | `"sysdigcloud-certman:6000"` |  |
| ticketing.enabled | bool | `true` |  |
| ticketing.hardDeleteIntegrationAPIEnabled | bool | `false` |  |
| ticketing.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"sysdigcloud-ticketing-api-v2"` |  |
| ticketing.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"sysdigcloud-ticketing-api-v2"` |  |
| ticketing.ingress[0].hosts[0].paths[0].path | string | `"/api/ticketing/v2"` |  |
| ticketing.ingress[0].hosts[0].paths[0].serviceName | string | `"sysdigcloud-ticketing-api"` |  |
| ticketing.ingress[0].hosts[0].paths[0].servicePort | int | `7001` |  |
| ticketing.ingress[0].hosts[0].paths[1].apiGatewayRouteName | string | `"sysdigcloud-ticketing-public-api"` |  |
| ticketing.ingress[0].hosts[0].paths[1].openshiftRouteName | string | `"sysdigcloud-ticketing-public-api"` |  |
| ticketing.ingress[0].hosts[0].paths[1].path | string | `"/platform/jira/v1"` |  |
| ticketing.ingress[0].hosts[0].paths[1].serviceName | string | `"sysdigcloud-ticketing-api"` |  |
| ticketing.ingress[0].hosts[0].paths[1].servicePort | int | `7001` |  |
| ticketing.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| ticketing.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| ticketing.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| ticketing.ingress[0].labels.role | string | `"ingress-config"` |  |
| ticketing.ingress[0].labels.tier | string | `"infra"` |  |
| ticketing.ingress[0].name | string | `"sysdigcloud-ticketing-ingress"` |  |
| ticketing.jiraCacheCleanupInterval | string | `"1m"` |  |
| ticketing.jiraCacheDefaultExpiration | string | `"15m"` |  |
| ticketing.jiraClientBaseWait | string | `"1s"` |  |
| ticketing.jiraClientMaxRetries | int | `3` |  |
| ticketing.jiraClientMaxWait | string | `"30s"` |  |
| ticketing.jiraClientSkipVerifyCustomerIds | string | `""` |  |
| ticketing.jiraCreateIssuesCronExpr | string | `"0 0 * * * *"` |  |
| ticketing.jiraCreateIssuesOrchestratorInterval | string | `"5m"` |  |
| ticketing.jiraCreateIssuesWorkersMaxWait | string | `"5s"` |  |
| ticketing.jiraCreateIssuesWorkersMinWait | string | `"1s"` |  |
| ticketing.jiraLogRequestBodyOnErr | bool | `false` |  |
| ticketing.jiraMaxAttachmentSize | string | `"1048576"` |  |
| ticketing.jiraSyncIssuesCronExpr | string | `"0 0 * * * *"` |  |
| ticketing.jiraWebhooksEnabled | bool | `false` |  |
| ticketing.natsJS.addAttachmentConsumer.ackWait | string | `"5m"` |  |
| ticketing.natsJS.addAttachmentConsumer.deliverPolicyAll | bool | `true` |  |
| ticketing.natsJS.addAttachmentConsumer.durable | string | `"add_attachment_to_issue_consumer"` |  |
| ticketing.natsJS.addAttachmentConsumer.maxDeliver | int | `3` |  |
| ticketing.natsJS.addAttachmentConsumer.name | string | `"add_attachment_to_issue_consumer"` |  |
| ticketing.natsJS.addAttachmentConsumer.pull | bool | `true` |  |
| ticketing.natsJS.addAttachmentConsumer.streamName | string | `"jira_attachments"` |  |
| ticketing.natsJS.addAttachmentConsumer.subject | string | `"jira_attachments.add_to_issue"` |  |
| ticketing.natsJS.deleteAttachmentConsumer.ackWait | string | `"5m"` |  |
| ticketing.natsJS.deleteAttachmentConsumer.deliverPolicyAll | bool | `true` |  |
| ticketing.natsJS.deleteAttachmentConsumer.durable | string | `"delete_attachment_from_issue_consumer"` |  |
| ticketing.natsJS.deleteAttachmentConsumer.maxDeliver | int | `3` |  |
| ticketing.natsJS.deleteAttachmentConsumer.name | string | `"delete_attachment_from_issue_consumer"` |  |
| ticketing.natsJS.deleteAttachmentConsumer.pull | bool | `true` |  |
| ticketing.natsJS.deleteAttachmentConsumer.streamName | string | `"jira_attachments"` |  |
| ticketing.natsJS.deleteAttachmentConsumer.subject | string | `"jira_attachments.delete_from_issue"` |  |
| ticketing.natsJS.migrationFile | string | `"/nats/migrations/streams.json"` |  |
| ticketing.natsJS.secure.enabled | bool | `true` |  |
| ticketing.natsJS.streams.jiraAttachments.maxAge | string | `"86400000000000"` |  |
| ticketing.natsJS.streams.jiraAttachments.maxBytes | string | `"2147483648"` |  |
| ticketing.natsJS.streams.jiraAttachments.numReplicas | int | `3` |  |
| ticketing.natsJS.streams.jiraIssues.maxAge | string | `"86400000000000"` |  |
| ticketing.natsJS.streams.jiraIssues.maxBytes | string | `"2147483648"` |  |
| ticketing.natsJS.streams.jiraIssues.numReplicas | int | `3` |  |
| ticketing.natsJS.url | string | `"nats"` |  |
| ticketing.proxy.defaultNoProxy | string | `"localhost,127.0.0.1,kubernetes.default.svc,*.svc.cluster.local,172.21.0.0/16,172.17.0.0/16,192.168.0.0/16"` |  |
| ticketing.proxy.enable | bool | `false` |  |
| ticketing.proxy.host | string | `"workload-egress-http-proxy.egress-proxy"` |  |
| ticketing.proxy.noProxy | string | `""` |  |
| ticketing.proxy.port | int | `3128` |  |
| ticketing.proxy.protocol | string | `"http"` |  |
| ticketing.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| ticketing.replicaCount | int | `2` |  |
| ticketing.repositoryPrefix | string | `"secure"` |  |
| ticketing.resources.postgresqlinit.limits.cpu | string | `"500m"` |  |
| ticketing.resources.postgresqlinit.limits.memory | string | `"150Mi"` |  |
| ticketing.resources.postgresqlinit.requests.cpu | string | `"100m"` |  |
| ticketing.resources.postgresqlinit.requests.memory | string | `"100Mi"` |  |
| ticketing.resources.ticketingApi.limits.cpu | string | `"200m"` |  |
| ticketing.resources.ticketingApi.limits.memory | string | `"200Mi"` |  |
| ticketing.resources.ticketingApi.requests.cpu | string | `"40m"` |  |
| ticketing.resources.ticketingApi.requests.memory | string | `"80Mi"` |  |
| ticketing.serviceAccountName | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# ui-admin

![Version: 6.0.0-260226112330-main-v954c680](https://img.shields.io/badge/Version-6.0.0--260226112330--main--v954c680-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

ui-admin

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.2.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor secure"` |  |
| global.iks.brandingEnabled | bool | `false` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.uiRegistryName | string | `""` |  |
| global.uiRegistryName | string | `""` |  |
| global.uiRepositoryPrefix | string | `""` |  |
| global.uiRepositoryPrefix | string | `""` |  |
| global.uiVersion | string | `""` |  |
| global.uiVersion | string | `""` |  |
| uiAdmin.enabled | bool | `false` |  |
| uiAdmin.host | string | `"change.me"` |  |
| uiAdmin.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"ui-admin"` |  |
| uiAdmin.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"ui-admin"` |  |
| uiAdmin.ingress[0].hosts[0].paths[0].path | string | `"/admin"` |  |
| uiAdmin.ingress[0].hosts[0].paths[0].serviceName | string | `"ui-admin"` |  |
| uiAdmin.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| uiAdmin.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| uiAdmin.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| uiAdmin.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| uiAdmin.ingress[0].labels.role | string | `"ingress-config"` |  |
| uiAdmin.ingress[0].labels.tier | string | `"infra"` |  |
| uiAdmin.ingress[0].name | string | `"ui-admin-ingress"` |  |
| uiAdmin.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| uiAdmin.replicaCount | int | `3` |  |
| uiAdmin.repositoryPrefix | string | `"ui"` |  |
| uiAdmin.resources.uiAdmin.limits.cpu | int | `1` |  |
| uiAdmin.resources.uiAdmin.limits.memory | string | `"500Mi"` |  |
| uiAdmin.resources.uiAdmin.requests.cpu | string | `"500m"` |  |
| uiAdmin.resources.uiAdmin.requests.memory | string | `"100Mi"` |  |
| uiAdmin.serviceAccountName | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# ui-inspect

![Version: 6.0.0-260217222836-main-vba02181](https://img.shields.io/badge/Version-6.0.0--260217222836--main--vba02181-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

ui-inspect

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.2.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor secure"` |  |
| global.iks.brandingEnabled | bool | `false` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.uiRegistryName | string | `""` |  |
| global.uiRegistryName | string | `""` |  |
| global.uiRepositoryPrefix | string | `""` |  |
| global.uiRepositoryPrefix | string | `""` |  |
| global.uiVersion | string | `""` |  |
| global.uiVersion | string | `""` |  |
| uiInspect.enabled | bool | `false` |  |
| uiInspect.host | string | `"change.me"` |  |
| uiInspect.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"ui-inspect"` |  |
| uiInspect.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"ui-inspect"` |  |
| uiInspect.ingress[0].hosts[0].paths[0].path | string | `"/sysdig-inspect"` |  |
| uiInspect.ingress[0].hosts[0].paths[0].serviceName | string | `"ui-inspect"` |  |
| uiInspect.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| uiInspect.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| uiInspect.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| uiInspect.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| uiInspect.ingress[0].labels.role | string | `"ingress-config"` |  |
| uiInspect.ingress[0].labels.tier | string | `"infra"` |  |
| uiInspect.ingress[0].name | string | `"ui-inspect-ingress"` |  |
| uiInspect.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| uiInspect.replicaCount | int | `3` |  |
| uiInspect.repositoryPrefix | string | `"ui"` |  |
| uiInspect.resources.uiInspect.limits.cpu | int | `1` |  |
| uiInspect.resources.uiInspect.limits.memory | string | `"500Mi"` |  |
| uiInspect.resources.uiInspect.requests.cpu | string | `"500m"` |  |
| uiInspect.resources.uiInspect.requests.memory | string | `"100Mi"` |  |
| uiInspect.serviceAccountName | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# ui-monitor

![Version: 6.0.0-260312231207-main-v77dac133](https://img.shields.io/badge/Version-6.0.0--260312231207--main--v77dac133-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

ui-monitor

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.2.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor secure"` |  |
| global.iks.brandingEnabled | bool | `false` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.uiRegistryName | string | `""` |  |
| global.uiRegistryName | string | `""` |  |
| global.uiRepositoryPrefix | string | `""` |  |
| global.uiRepositoryPrefix | string | `""` |  |
| global.uiVersion | string | `""` |  |
| global.uiVersion | string | `""` |  |
| uiMonitor.enabled | bool | `false` |  |
| uiMonitor.host | string | `"change.me"` |  |
| uiMonitor.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"ui-monitor"` |  |
| uiMonitor.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"ui-monitor"` |  |
| uiMonitor.ingress[0].hosts[0].paths[0].path | string | `"/"` |  |
| uiMonitor.ingress[0].hosts[0].paths[0].serviceName | string | `"ui-monitor"` |  |
| uiMonitor.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| uiMonitor.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| uiMonitor.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| uiMonitor.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| uiMonitor.ingress[0].labels.role | string | `"ingress-config"` |  |
| uiMonitor.ingress[0].labels.tier | string | `"infra"` |  |
| uiMonitor.ingress[0].name | string | `"ui-monitor-ingress"` |  |
| uiMonitor.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| uiMonitor.replicaCount | int | `3` |  |
| uiMonitor.repositoryPrefix | string | `"ui"` |  |
| uiMonitor.resources.uiMonitor.limits.cpu | int | `1` |  |
| uiMonitor.resources.uiMonitor.limits.memory | string | `"500Mi"` |  |
| uiMonitor.resources.uiMonitor.requests.cpu | string | `"500m"` |  |
| uiMonitor.resources.uiMonitor.requests.memory | string | `"100Mi"` |  |
| uiMonitor.serviceAccountName | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# ui-secure

![Version: 6.0.0-260312231207-main-v77dac133](https://img.shields.io/badge/Version-6.0.0--260312231207--main--v77dac133-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

ui-secure

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.2.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.apps | string | `"monitor secure"` |  |
| global.iks.brandingEnabled | bool | `false` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.uiRegistryName | string | `""` |  |
| global.uiRegistryName | string | `""` |  |
| global.uiRepositoryPrefix | string | `""` |  |
| global.uiRepositoryPrefix | string | `""` |  |
| global.uiVersion | string | `""` |  |
| global.uiVersion | string | `""` |  |
| uiSecure.enabled | bool | `false` |  |
| uiSecure.host | string | `"change.me"` |  |
| uiSecure.ingress[0].hosts[0].paths[0].apiGatewayRouteName | string | `"ui-secure"` |  |
| uiSecure.ingress[0].hosts[0].paths[0].openshiftRouteName | string | `"ui-secure"` |  |
| uiSecure.ingress[0].hosts[0].paths[0].path | string | `"/secure"` |  |
| uiSecure.ingress[0].hosts[0].paths[0].serviceName | string | `"ui-secure"` |  |
| uiSecure.ingress[0].hosts[0].paths[0].servicePort | int | `8080` |  |
| uiSecure.ingress[0].labels."app.kubernetes.io/managed-by" | string | `"ingress-config"` |  |
| uiSecure.ingress[0].labels."app.kubernetes.io/name" | string | `"ingress-config"` |  |
| uiSecure.ingress[0].labels."app.kubernetes.io/part-of" | string | `"sysdigcloud"` |  |
| uiSecure.ingress[0].labels.role | string | `"ingress-config"` |  |
| uiSecure.ingress[0].labels.tier | string | `"infra"` |  |
| uiSecure.ingress[0].name | string | `"ui-secure-ingress"` |  |
| uiSecure.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| uiSecure.replicaCount | int | `3` |  |
| uiSecure.repositoryPrefix | string | `"ui"` |  |
| uiSecure.resources.uiSecure.limits.cpu | int | `1` |  |
| uiSecure.resources.uiSecure.limits.memory | string | `"500Mi"` |  |
| uiSecure.resources.uiSecure.requests.cpu | string | `"500m"` |  |
| uiSecure.resources.uiSecure.requests.memory | string | `"100Mi"` |  |
| uiSecure.serviceAccountName | string | `"sysdig"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# worker

![Version: 0.99.0-main.2026-03-12T16-20-42Z.v4cb19be](https://img.shields.io/badge/Version-0.99.0--main.2026--03--12T16--20--42Z.v4cb19be-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square)

Sysdig Worker

## Requirements

| Repository | Name | Version |
|------------|------|---------|
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | linkerd-partials | 0.0.5 |
| oci://us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-charts | sysdig-template | 1.14.0 |

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.admin.password | string | `""` |  |
| global.admin.username | string | `""` |  |
| global.apps | string | `"monitor"` |  |
| global.captures.cassandra.storage | bool | `true` |  |
| global.cassandra.datacenterName | string | `"DC1"` |  |
| global.cassandra.endpoint | string | `"sysdigcloud-cassandra"` |  |
| global.cassandra.port | int | `9042` |  |
| global.cassandra.replicaCount | int | `3` |  |
| global.cassandra.replicationStrategy | string | `"SimpleStrategy"` |  |
| global.cassandra.ssl | bool | `true` |  |
| global.cassandra.sslVerify | bool | `false` |  |
| global.cassandra.useCertManager | bool | `false` |  |
| global.collectorPort | int | `6443` |  |
| global.deployment | string | `"kubernetes"` |  |
| global.dnsName | string | `""` |  |
| global.elasticsearch | object | `{"basename":"elasticsearch","clientsConfigs":{"discovery":true,"signAWSRequests":false},"hostname":"sysdigcloud-elasticsearch","scheme":"https","tlsencryption":{"adminUser":"sysdig","enabled":true,"verifySSL":false}}` | elasticsearch shared values |
| global.elasticsearch.basename | string | `"elasticsearch"` | base string from which resource names will be constructed |
| global.elasticsearch.tlsencryption | object | `{"adminUser":"sysdig","enabled":true,"verifySSL":false}` | tls configuration |
| global.elasticsearch.tlsencryption.adminUser | string | `"sysdig"` | name of the admin user created by elasticsearch on initialization |
| global.elasticsearch.tlsencryption.enabled | bool | `true` | enable tls |
| global.iks.activityTrackerEnabled | bool | `false` |  |
| global.inactivitySettings.trackerEnabled | bool | `false` |  |
| global.inactivitySettings.trackerTimeout | int | `1800` |  |
| global.ingressNetworking | string | `"hostnetwork"` |  |
| global.installationType | string | `"local"` |  |
| global.internalIngestion.token | string | `nil` |  |
| global.kafka.broker.externalPort | int | `9093` |  |
| global.kafka.name | string | `"cp-kafka"` |  |
| global.kafka.namespace | string | `"sysdigcloud"` |  |
| global.kafka.secure.enabled | bool | `false` |  |
| global.kafka.secure.useCertManager | bool | `false` |  |
| global.kafkaReplicaCount | int | `3` |  |
| global.legacyPostgres.postgresDatabases.quartz.db | string | `"quartz"` |  |
| global.legacyPostgres.postgresDatabases.quartz.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.quartz.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.quartz.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.quartz.username | string | `"quartz_user"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.db | string | `"sysdig"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.host | string | `"sysdigcloud-postgresql"` |  |
| global.legacyPostgres.postgresDatabases.sysdig.password | string | `nil` |  |
| global.legacyPostgres.postgresDatabases.sysdig.port | int | `5432` |  |
| global.legacyPostgres.postgresDatabases.sysdig.username | string | `"sysdig_user"` |  |
| global.legacyRedis.redisClientsMonitor.cache.tls | bool | `true` |  |
| global.legacyRedis.redisClientsMonitor.common.tls | bool | `true` |  |
| global.legacyRedis.redisClientsMonitor.distributedJobs.tls | bool | `true` |  |
| global.legacyRedis.redisClientsMonitor.metering.tls | bool | `true` |  |
| global.legacyRedis.redisHa | bool | `false` |  |
| global.legacyRedis.redisTls.enabled | bool | `true` |  |
| global.legacyRedis.redisTls.endpoint | string | `"redistls"` |  |
| global.legacyRedis.redisTls.ha | bool | `false` |  |
| global.legacyRedis.redisTls.port | int | `6379` |  |
| global.legacyRedis.redisTls.sentinel.port | int | `26379` |  |
| global.legacyRedis.redisTls.useCertManager | bool | `false` |  |
| global.legacyRedis.sysdigRedis.endpoint | string | `"redis"` |  |
| global.legacyRedis.sysdigRedis.password | string | `""` |  |
| global.legacyRedis.useRedisTls | bool | `false` |  |
| global.legacyS3.s3.enabled | bool | `false` |  |
| global.meerkat.defaultNumCustomerShards | int | `8` |  |
| global.meerkat.enabled | bool | `false` |  |
| global.metadataService.enabled | bool | `true` |  |
| global.namespace | string | `"sysdigcloud"` |  |
| global.nats.certManager.enabled | bool | `false` |  |
| global.prometheus.enabled | bool | `true` |  |
| global.saml.certificate.name | string | `""` |  |
| global.secure.cloudauth.enabled | bool | `false` |  |
| global.secure.sysqlApi.enabled | bool | `true` |  |
| global.secure.sysqlApi.serviceToken | string | `nil` | sysqlApi token mounted from sysql-api chart secret |
| global.slack.client.endpoint | string | `""` |  |
| global.slack.client.id | string | `""` |  |
| global.slack.client.oauth.endpoint | string | `""` |  |
| global.slack.client.scope | string | `"incoming-webhook"` |  |
| global.slack.client.secret | string | `""` |  |
| global.smtpPassword | string | `""` |  |
| global.smtpProtocolSSL | bool | `false` |  |
| global.smtpProtocolTLS | bool | `false` |  |
| worker.cloudWatch.apiToken | string | `""` |  |
| worker.downtime.expirationJobEnabled | bool | `false` |  |
| worker.downtime.expirationJobNumberOfJobs | int | `1` |  |
| worker.downtime.internalIngestionJobEnabled | bool | `false` |  |
| worker.downtime.internalIngestionJobNumberOfJobs | int | `1` |  |
| worker.elasticsearchConfigRefs | object | `{"certsSecretName":"","configMapName":"","passwordsSecretName":""}` | structure that contains the references to elasticsearch instance secrets and configmaps. |
| worker.elasticsearchConfigRefs.certsSecretName | string | `""` | name of the elasticsearch secret containing the certificates |
| worker.elasticsearchConfigRefs.configMapName | string | `""` | name of the elasticsearch configmap containing ES configuration |
| worker.elasticsearchConfigRefs.passwordsSecretName | string | `""` | name of the elasticsearch secret containing the credentials |
| worker.enabled | bool | `true` |  |
| worker.jvmOptions | string | `""` |  |
| worker.registryName | string | `"us-docker.pkg.dev/sysdig-artifact-registry-dev/gar-docker"` |  |
| worker.replicaCount | int | `1` |  |
| worker.repositoryPrefix | string | `"monitor"` |  |
| worker.resources.worker.limits.cpu | int | `4` |  |
| worker.resources.worker.limits.memory | string | `"4Gi"` |  |
| worker.resources.worker.requests.cpu | int | `1` |  |
| worker.resources.worker.requests.memory | string | `"1Gi"` |  |

----------------------------------------------
Autogenerated from chart metadata using [helm-docs v1.14.2](https://github.com/norwoodj/helm-docs/releases/v1.14.2)

# zookeeper

![Version: 3.6.17](https://img.shields.io/badge/Version-3.6.17-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 7.9.4](https://img.shields.io/badge/AppVersion-7.9.4-informational?style=flat-square)

This is owned and maintained by Sysdig Infra team. It conditionally installs zookeeper

In this first version the `values.yaml` structure resembles the one used by the `installer` for compatibility reasons.

## Values

| Key | Type | Default | Description |
|-----|------|---------|-------------|
| global.airgappedRegistryName | string | `nil` | registry name for airgapped environments |
| global.airgappedRepositoryPrefix | string | `nil` | repository prefix for airgapped environments |
| global.airgapped_repository_prefix | string | `""` | repository prefix for airgapped environments |
| global.cloudProvider.isMultiAZ | bool | `false` |  |
| global.fastpathAggregator.enabled | bool | `false` |  |
| global.kafka.name | string | `"cp-kafka"` | used as base name to create kafka k8s objects |
| global.kafka.namespace | string | `"sysdig"` | namespace where to install zookeeper |
| global.kafka.secure.caCrt | string | `""` | base64 encoded CA certificate for kafka. These certs can be generated with: ```openssl req -x509 -nodes -sha256 -days 7300 -newkey rsa:4096 -subj '/C=US/ST=CA/L=SanFrancisco/O=Sysdig' -addext "keyUsage= digitalSignature, keyEncipherment, keyCertSign" -addext "extendedKeyUsage= serverAuth, clientAuth" -keyout "ca.key" -out "ca.crt"``` |
| global.kafka.secure.caKey | string | `""` | base64 encoded CA key for kafka |
| global.kafka.secure.enabled | bool | `false` | whether to enable TLS for kafka cluster |
| global.kafka.secure.fipsmode | bool | `false` | enable FIPS mode |
| global.kafka.secure.securityProtocol | string | `"SSL"` | define security protocol |
| global.kafka.secure.sslClientAuth | string | `"requested"` | set the encryption requirements for kafka clients. can be none, requested, or required |
| global.kafka.secure.sslKeystorePassword | string | `nil` | password for java ssl keystore. If not explicitly provided it will be randomly generated by helm. |
| global.kafka.secure.sslTruststorePassword | string | `nil` | password for java ssl truststore. If not explicitly provided it will be randomly generated by helm. |
| global.kafka.secure.useCertManager | bool | `false` | whether to use cert-manager for certificate management |
| global.kafka.serviceAccount | string | `""` | name of an already existing serviceAccount to be used for default workloads, if empty, will create a new one |
| global.kafkaCASecretName | string | `"kafka-ca-secret"` | name of the secret exported by cert manager |
| global.kafkaCruiseControl.enabled | bool | `true` | if false, scales deployment to 0 replicas |
| global.kafkaOpts | string | `""` | used to fill KAFKA_OPTS. Could used be to enable debugging "-Djava.security.debug=sunpkcs11" |
| global.meerkat.enabled | bool | `false` |  |
| global.storageClassProvisioner | string | `""` |  |
| global.zookeeper.clientPort | int | `2181` | zookeeper client port |
| global.zookeeper.name | string | `"zookeeper"` | used as base name to create zookeeper k8s objects |
| global.zookeeper.secureClientPort | int | `2182` | zookeeper secure client port |
| zookeeper.autoPurgePurgeInterval | int | `1` |  |
| zookeeper.autoPurgeSnapRetainCount | int | `3` |  |
| zookeeper.enableAuditLogs | bool | `false` | enable audit logs in ZK |
| zookeeper.enableMetrics | bool | `false` | zookeeper config |
| zookeeper.exporter.livenessProbe.initialDelaySeconds | int | `90` | zookeeper exporter container initial delay seconds for liveness probe |
| zookeeper.exporter.livenessProbe.periodSeconds | int | `30` | zookeeper exporter liveness probe frequency of checks |
| zookeeper.exporter.livenessProbe.timeoutSeconds | int | `30` | zookeeper exporter liveness probe timeout |
| zookeeper.exporter.readinessProbe.initialDelaySeconds | int | `30` | zookeeper exporter container initial delay seconds for readiness probe |
| zookeeper.exporter.readinessProbe.periodSeconds | int | `10` | zookeeper exporter readiness probe frequency of checks |
| zookeeper.exporter.readinessProbe.timeoutSeconds | int | `30` | zookeeper exporter readiness probe timeout |
| zookeeper.extraLabels | object | `{"owners":"infra"}` | extra labels for zookeeper objects |
| zookeeper.imageName | string | `"cp-zookeeper-7"` | name of the zookeeper image |
| zookeeper.initLimit | int | `10` |  |
| zookeeper.jmxPort | int | `9010` | zookeeper jmx port |
| zookeeper.leaderElectionPort | int | `3888` |  |
| zookeeper.maxClientCnxns | int | `60` |  |
| zookeeper.multiCluster | object | `{"enabled":false,"roles":["source","target"],"side":"source"}` | zookeeper migration config (using linkerd multicluster) |
| zookeeper.nodeAffinityLabel | string | `nil` | label on which create nodeAffinity |
| zookeeper.nodeAffinityMode | string | `"preferred"` | make nodeAffinity "required" or "preferred" |
| zookeeper.persistentVolumeClaim.size | string | `"20Gi"` | zookeeper data pvc size |
| zookeeper.persistentVolumeClaim.storageClassName | string | `"sysdig"` | zookeeper data pvc storage class name |
| zookeeper.portUnification | bool | `false` |  |
| zookeeper.productCategory.enabled | bool | `false` |  |
| zookeeper.productCategory.label | string | `"monitor"` |  |
| zookeeper.registryName | string | `"quay.io"` | default registry name |
| zookeeper.replicaCount | int | `3` | zookeeper replica count |
| zookeeper.repositoryPrefix | string | `"sysdig"` | default repository prefix |
| zookeeper.resources.zookeeper | object | `{"limits":{"cpu":"250m","memory":"500Mi"},"requests":{"cpu":"100m","memory":"128Mi"}}` | zookeeper pods resources |
| zookeeper.resources.zookeeper_exporter.limits.cpu | string | `"1"` |  |
| zookeeper.resources.zookeeper_exporter.limits.memory | string | `"500Mi"` |  |
| zookeeper.resources.zookeeper_exporter.requests.cpu | string | `"300m"` |  |
| zookeeper.resources.zookeeper_exporter.requests.memory | string | `"100Mi"` |  |
| zookeeper.resources.zookeeper_init.limits.cpu | string | `"100m"` |  |
| zookeeper.resources.zookeeper_init.limits.memory | string | `"200Mi"` |  |
| zookeeper.resources.zookeeper_init.requests.cpu | string | `"50m"` |  |
| zookeeper.resources.zookeeper_init.requests.memory | string | `"100Mi"` |  |
| zookeeper.server.livenessProbe.initialDelaySeconds | int | `60` | zookeeper server container initial delay seconds for liveness probe |
| zookeeper.server.livenessProbe.periodSeconds | int | `10` | zookeeper server liveness probe frequency of checks |
| zookeeper.server.livenessProbe.timeoutSeconds | int | `5` | zookeeper server liveness probe timeout |
| zookeeper.server.readinessProbe.initialDelaySeconds | int | `60` | zookeeper server container initial delay seconds for readiness probe |
| zookeeper.server.readinessProbe.periodSeconds | int | `10` | zookeeper server readiness probe frequency of checks |
| zookeeper.server.readinessProbe.timeoutSeconds | int | `5` | zookeeper server readiness probe timeout |
| zookeeper.serverPort | int | `2888` | zookeeper server port |
| zookeeper.serverlist | string | `""` | overrides the ZOOKEEPER_SERVER env var if not empty string. ZOOKEEPER_SERVER is calculated otherwise |
| zookeeper.sslEnabledProtocols | string | `"TLSv1.2"` | define the SSL/TLS enabled protocols |
| zookeeper.sslQuorum | bool | `true` |  |
| zookeeper.sslQuorumTlsProtocol | string | `"TLSv1.2,TLSv1.3"` | zookeeper SSL quorum TLS protocol |
| zookeeper.syncLimit | int | `5` |  |
| zookeeper.tickTime | int | `2000` |  |
| zookeeper.topologySpreadConstraints.hostname | object | `{"whenUnsatisfiable":"DoNotSchedule"}` | Topology Spread toleration for hostname spread. Can be `DoNotSchedule` for a hard constraint or `ScheduleAnyway` for a soft constraint. |
| zookeeper.topologySpreadConstraints.multiAZ | object | `{"whenUnsatisfiable":"DoNotSchedule"}` | Topology Spread toleration for multiAZ spread. Can be `DoNotSchedule` for a hard constraint or `ScheduleAnyway` for a soft constraint. |
| zookeeper.updateStrategy | string | `"RollingUpdate"` | which update strategy to use "OnDelete" or "RollingRestart" for zookeeper |
| zookeeper.version | string | `"1.6.14"` | zookeeper image tag |
| zookeeper.zookeeperExporterVersion | string | `"v1.0.22-ubi"` | zookeeper exporter version |

