<!-- Space: TOOLS -->
<!-- Parent: Installer -->
<!-- Title: ScanningV2 Resources -->
<!-- Layout: plain -->

# ScanningV2 Resources Overview

## Small

```yaml
v.Sysdig.ScanningV2CollectorReplicaCount = 1
v.Sysdig.ScanningV2ScanResultsAPIReplicaCount = 1
v.Sysdig.ScanningV2RiskManagerAPIReplicaCount = 1
v.Sysdig.ScanningV2PoliciesAPIReplicaCount = 1
v.Sysdig.ScanningV2VulnsAPIReplicaCount = 1
v.Sysdig.ScanningV2PkgMetaAPIReplicaCount = 1
v.Sysdig.ScanningV2AgentsConfReplicaCount = 1

v.Sysdig.Resources.ScanningV2Collector.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2Collector.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2Collector.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2Collector.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2ScanResultsAPI.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2ScanResultsAPI.Limits.Memory = "500Mi"
v.Sysdig.Resources.ScanningV2ScanResultsAPI.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2ScanResultsAPI.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2RiskManagerAPI.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2RiskManagerAPI.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2RiskManagerAPI.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2RiskManagerAPI.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2PoliciesAPI.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2PoliciesAPI.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2PoliciesAPI.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2PoliciesAPI.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2VulnsAPI.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2VulnsAPI.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2VulnsAPI.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2VulnsAPI.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2PkgMeta.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2PkgMeta.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2PkgMeta.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2PkgMeta.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2AgentsConf.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2AgentsConf.Limits.Memory = "500Mi"
v.Sysdig.Resources.ScanningV2AgentsConf.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2AgentsConf.Requests.Memory = "100Mi"

v.Sysdig.Resources.ScanningV2ReportingAPI.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2ReportingAPI.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingAPI.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2ReportingAPI.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2ReportingGenerator.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2ReportingGenerator.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingGenerator.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2ReportingGenerator.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2ReportingJanitor.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingJanitor.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingJanitor.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2ReportingJanitor.Requests.Memory = "50Mi"

v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2ReportingScheduler.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2ReportingScheduler.Limits.Memory = "500Mi"
v.Sysdig.Resources.ScanningV2ReportingScheduler.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2ReportingScheduler.Requests.Memory = "100Mi"
```

## Medium

```yaml
v.Sysdig.ScanningV2CollectorReplicaCount = 2
v.Sysdig.ScanningV2ScanResultsAPIReplicaCount = 2
v.Sysdig.ScanningV2RiskManagerAPIReplicaCount = 2
v.Sysdig.ScanningV2PoliciesAPIReplicaCount = 2
v.Sysdig.ScanningV2VulnsAPIReplicaCount = 2
v.Sysdig.ScanningV2PkgMetaAPIReplicaCount = 2
v.Sysdig.ScanningV2AgentsConfReplicaCount = 2

v.Sysdig.Resources.ScanningV2Collector.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2Collector.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2Collector.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2Collector.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2ScanResultsAPI.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ScanResultsAPI.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ScanResultsAPI.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2ScanResultsAPI.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2RiskManagerAPI.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2RiskManagerAPI.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2RiskManagerAPI.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2RiskManagerAPI.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2PoliciesAPI.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2PoliciesAPI.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2PoliciesAPI.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2PoliciesAPI.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2VulnsAPI.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2VulnsAPI.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2VulnsAPI.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2VulnsAPI.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2PkgMeta.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2PkgMeta.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2PkgMeta.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2PkgMeta.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2AgentsConf.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2AgentsConf.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2AgentsConf.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2AgentsConf.Requests.Memory = "250Mi"

v.Sysdig.Resources.ScanningV2ReportingAPI.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingAPI.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingAPI.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2ReportingAPI.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2ReportingGenerator.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingGenerator.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2ReportingGenerator.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingGenerator.Requests.Memory = "1Gi"

v.Sysdig.Resources.ScanningV2ReportingJanitor.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingJanitor.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingJanitor.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2ReportingJanitor.Requests.Memory = "50Mi"

v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2ReportingScheduler.Limits.CPU = "500m"
v.Sysdig.Resources.ScanningV2ReportingScheduler.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingScheduler.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2ReportingScheduler.Requests.Memory = "250Mi"
```

## Large

```yaml
v.Sysdig.ScanningV2CollectorReplicaCount = 4
v.Sysdig.ScanningV2ScanResultsAPIReplicaCount = 4
v.Sysdig.ScanningV2RiskManagerAPIReplicaCount = 3
v.Sysdig.ScanningV2PoliciesAPIReplicaCount = 3
v.Sysdig.ScanningV2VulnsAPIReplicaCount = 3
v.Sysdig.ScanningV2PkgMetaAPIReplicaCount = 3
v.Sysdig.ScanningV2AgentsConfReplicaCount = 2

v.Sysdig.Resources.ScanningV2Collector.Limits.CPU = "2"
v.Sysdig.Resources.ScanningV2Collector.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2Collector.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2Collector.Requests.Memory = "1Gi"

v.Sysdig.Resources.ScanningV2ScanResultsAPI.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ScanResultsAPI.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2ScanResultsAPI.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2ScanResultsAPI.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2RiskManagerAPI.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2RiskManagerAPI.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2RiskManagerAPI.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2RiskManagerAPI.Requests.Memory = "1Gi"

v.Sysdig.Resources.ScanningV2PoliciesAPI.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2PoliciesAPI.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2PoliciesAPI.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2PoliciesAPI.Requests.Memory = "1Gi"

v.Sysdig.Resources.ScanningV2VulnsAPI.Limits.CPU = "2"
v.Sysdig.Resources.ScanningV2VulnsAPI.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2VulnsAPI.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2VulnsAPI.Requests.Memory = "1Gi"

v.Sysdig.Resources.ScanningV2PkgMeta.Limits.CPU = "2"
v.Sysdig.Resources.ScanningV2PkgMeta.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2PkgMeta.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2PkgMeta.Requests.Memory = "1Gi"

v.Sysdig.Resources.ScanningV2AgentsConf.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2AgentsConf.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2AgentsConf.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2AgentsConf.Requests.Memory = "500Mi"

v.Sysdig.Resources.ScanningV2ReportingAPI.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingAPI.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2ReportingAPI.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingAPI.Requests.Memory = "1Gi"

v.Sysdig.Resources.ScanningV2ReportingGenerator.Limits.CPU = "2"
v.Sysdig.Resources.ScanningV2ReportingGenerator.Limits.Memory = "4Gi"
v.Sysdig.Resources.ScanningV2ReportingGenerator.Requests.CPU = "2"
v.Sysdig.Resources.ScanningV2ReportingGenerator.Requests.Memory = "2Gi"

v.Sysdig.Resources.ScanningV2ReportingJanitor.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingJanitor.Limits.Memory = "1Gi"
v.Sysdig.Resources.ScanningV2ReportingJanitor.Requests.CPU = "250m"
v.Sysdig.Resources.ScanningV2ReportingJanitor.Requests.Memory = "50Mi"

v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerHost.Requests.Memory = "1Gi"

v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerK8s.Requests.Memory = "1Gi"

v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Requests.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingWorkerReg.Requests.Memory = "1Gi"

v.Sysdig.Resources.ScanningV2ReportingScheduler.Limits.CPU = "1"
v.Sysdig.Resources.ScanningV2ReportingScheduler.Limits.Memory = "2Gi"
v.Sysdig.Resources.ScanningV2ReportingScheduler.Requests.CPU = "500m"
v.Sysdig.Resources.ScanningV2ReportingScheduler.Requests.Memory = "500Mi"
```
