Release 4.0.0 March 20, 2020
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 4.0.0 has been tested and qualified against the following:

Supported Upgrade From: 3.6.2

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.16.15, 1.17.17, 1.18.16, 1.19.8, 1.20.4 |
| OpenShift                   | 3.11, 4.4 |
| GKE                         | 1.18.12-gke.1210 |
| EKS                         | 1.18 |
| Rancher                     | 2.5.3 |

### Sysdig Agent Version

Qualified with agent release 11.0.0

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.0.12 |
| ElasticSearch              | 6.8.6 |
| Cassandra                  | release_version: 2.1.21 cql_version: 3.2.1 |
| RDS                        | 8.0.16 |
| Postgres (image scanning)  | 12.5|
| Anchore (image scanning)   | 0.9.1 |
| NATS Exporter              | 0.6.2 |
| NATS Streaming             | 0.17.0 |
| HA Proxy                   | 0.10 |


### Installer binaries sha256sum

| **sha256sum** | **Installer binary ** |
|---|---|
| 53c0abed589a2ac425cbf5468039705fd63cdb3cd631b1ed6b7c3d20ac84a217 | installer-darwin-amd64 |
| 223d818dd43d5a3d6ef4b8f7152382a74984a4943d487913b013b60edb2a2706 | installer-linux-amd64 |
| 75417fe747a208ceeb38c37a54a5a4706ded78b1ca6982c3bd41a3febaae5bc5 | installer-windows-amd64.exe |
