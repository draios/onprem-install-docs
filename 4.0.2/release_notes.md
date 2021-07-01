Release 4.0.2 June 29, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 4.0.2 has been tested and qualified against the following:

Supported Upgrade From: 3.6.2, 4.0.0, 4.0.1

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.16.15, 1.17.17, 1.18.16, 1.19.8, 1.20.4 |
| OpenShift                   | 3.11, 4.4 |
| GKE                         | 1.18.12-gke.1210 |
| EKS                         | 1.18 |
| Rancher                     | 2.5.3 |

### Sysdig Agent Version

Qualified with agent release 11.3.0

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.0.12 |
| ElasticSearch              | 6.8.6 |
| Cassandra                  | release_version: 2.1.21 cql_version: 3.2.1 |
| Postgres (image scanning)  | 12.5|
| Anchore (image scanning)   | 0.8.1 |
| NATS Exporter              | 0.6.2 |
| NATS Streaming             | 0.17.0 |
| HA Proxy                   | 0.10 |


### Installer binaries sha256sum

Current version: 4.0.2-2

| **sha256sum** | **Installer binary ** |
|---|---|
| 2637faa9461a60ab9f646585839199d0d943b5d7a7ed9b2a3197e34dc0436838 | installer-darwin-amd64 |
| db94b477ff2b66b4645602fbbeea1522e9d2ac77019a62a2c2c1546892e0ce7b | installer-linux-amd64 |
| 9fe6b14606ef65124b38ef93ee11381d70333a46fee11c58940452520d239762 | installer-windows-amd64.exe |
