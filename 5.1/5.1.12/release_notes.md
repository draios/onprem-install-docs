Release 5.1.12 January, 2024
===

For additional information, Review the [Sysdig On-Premises Release Notes](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/).

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
| 1037fb2ecb24bd6fe949e7c2342fd83292dad1b2fa276c2b7ba7ed2ffc5a7b85 | installer-darwin-amd64 |
| 7113d94fc4dcd4f7035406b0994d299182b696f8fb698a0d0294ff23793d2b49 | installer-linux-amd64 |
| 91f67ae3bfdb4947e76b566f038fcd9d8c1669eaa198819b2d2003ab91f79705 | installer-windows-amd64.exe |
