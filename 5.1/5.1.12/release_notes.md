Release 5.1.12 January, 2024
===

For additional information, review the full feature [release notes](https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html).

Upgrade Matrix
---

Sysdig Platform version 5.1.12 has been tested and qualified against the following:

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

Current version: 5.1.12-1

| **sha256sum** | **Installer binary** |
|---|---|
| 52b5e2d189d47798da1700669d861ffeefdc2da1bced175fa73e7c5138d22c71 | installer-darwin-amd64 |
| 7a947bfb491e096829ac11903821c31e680082623a4ae1019b2517ed6da6e976 | installer-linux-amd64 |
| 8005e025327628768ad08b5e44de52ead027c6ebd7f2c51626fa341940d50664 | installer-windows-amd64.exe |
