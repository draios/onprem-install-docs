Release 5.1.2 May, 2022
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 5.1.1 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.X

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.18.20, 1.19.13, 1.20.9, 1.21.3, 1.22.8, 1.23.5 |
| OpenShift                   | 3.11, 4.9 |
| GKE                         | 1.19.11-gke.1701 |
| EKS                         | 1.20 |
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

Current version: 5.1.2-1

| **sha256sum** | **Installer binary ** |
|---|---|
| 5a55b6ef876f223b0085bba40460bffad8d6cb7166f7e9e156ebf2051061eceb | installer-darwin-amd64 |
| bcd2d4cadcd4a16ddcfd950009db9a8d2e5b39ea942ba5952ddab4afdd2ad9ac | installer-linux-amd64 |
| 1b9c7620bf467927a0675b8a6167764a9a97a14c999f05c9b356adf611cbd739 | installer-windows-amd64.exe |
