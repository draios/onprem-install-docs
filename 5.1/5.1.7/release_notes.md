Release 5.1.7 Jan, 2023
===

Review the full feature release notes here: https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/

Upgrade Matrix
---

Sysdig Platform version 5.1.7 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.X

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.18.20, 1.19.13, 1.20.9, 1.21.3, 1.22.8, 1.23.5 |
| OpenShift                   | 3.11, 4.9, 4.10, 4.11 |
| GKE                         | 1.19.11-gke.1701 |
| EKS                         | 1.20, 1.21, 1.22 |
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


### Installer binaries sha256sum

Current version: 5.1.7-1

| **sha256sum** | **Installer binary ** |
|---|---|
| c206dca331fb5ddb567a091b89b1c3ee9ff3e39444ac855e11986d4cad9591bf |  installer-darwin-amd64 |
| cea696767d86fc959a7bb87f9507aabd0bd07cbf79543d167d157c2b824f5904 |  installer-linux-amd64 |
| 9ab80923e9667a7e6f84bd8d3a26485fac25ffe684b242b73c2d2f0ae01d2f30 |  installer-windows-amd64.exe |