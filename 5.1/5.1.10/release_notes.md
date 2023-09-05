Release 5.1.10 September, 2023
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 5.1.10 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.X

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.18.20, 1.19.13, 1.20.9, 1.21.3, 1.22.8, 1.23.5, 1.24.10 |
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

Current version: 5.1.10-1

| **sha256sum** | **Installer binary** |
|---|---|
| 055348b177e6597ef43d50599c2ba8238c0949a66660af55d0e7ddaa2e1846bc | installer-darwin-amd64 |
| 94805ade8c1bdc2c35e15b5eafe30babbf3fb8e06658be895f9f2f1717f9bcf2 | installer-linux-amd64 |
| a41ffb1df8b379bb73a08561e1757d7029e7455007a7c95c478303f2f07f7396 | installer-windows-amd64.exe |

