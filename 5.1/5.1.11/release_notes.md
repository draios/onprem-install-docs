Release 5.1.10 September, 2023
===

For additional information, review the full feature [release notes](https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html).

Upgrade Matrix
---

Sysdig Platform version 5.1.10 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.X

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.18.20, 1.19.13, 1.20.9, 1.21.3, 1.22.8, 1.23.5, 1.24.10, 1.25.13, 1.26.8, 1.27.5 |
| OpenShift                   | 3.11, 4.9, 4.10, 4.11, 4.12, 4.13 |
| GKE                         | 1.19.11-gke.1701 |
| EKS                         | 1.20, 1.21, 1.22, 1.23, 1.24, 1.25, 1.26, 1.27 |
| Rancher                     | 2.5.7 |

### Sysdig Agent Version

Qualified with agent release 11.4.1

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.0.12 |
| ElasticSearch              | 6.8.6 |
| Cassandra                  | Fresh: 3.11.11 - Upgrade: 2.1.22.5 |
| Postgres                   | 12.10 |
| Anchore (image scanning)   | 0.8.1.32 |
| NATS Exporter              | 0.9.2 |
| NATS Streaming             | 0.22.0 |
| HA Proxy                   | 0.13 (Old K8s versions: 0.10) |


### Sha256sum for the Installer Binaries 

Current version: 5.1.10-1

| **sha256sum** | **Installer binary** |
|---|---|
| 238f7a95dce2e64ec4154b13f3a7c05d387fe04cd45dfea366889eed7b82c030 | installer-darwin-amd64 |
| 27c69d54cc382cade91ad83f402a22a3135b4fc29a951a04ef513721a628aba8 | installer-linux-amd64 |
| 72cb2c6efb2755bf706994ef9db17ce32fed4b3e29c517a5a994916befea84fe | installer-windows-amd64.exe |
