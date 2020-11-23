Release 3.6.1 November 23, 2020
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 3.6.1 has been tested and qualified against the following:

Supported Upgrade From: 3.2.2, 3.5.1, (3.6.0 if it was installed)

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.13.4, 14.10, 1.15.12, 1.16.13, 1.17.9, 1.18.6 |
| OpenShift                   | 3.11, 4.4 |
| GKE                         |1.14.10-gke.36 |
| EKS                         |v1.17.7-eks-bffbac|
| Rancher                     | v2.3.3|
| IBM                         | Unqualified |
| PKS                         | Unqualified |

### Sysdig Agent Version

Qualified with agent release 10.6.0

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 4.0.12 |
| MySQL                      | 5.6.44, 8.0.16|
| MySQL HA                   | 8.0.16 |
| ElasticSearch              | 6.8.6 |
| Cassandra                  | release_version: 2.1.21 cql_version: 3.2.1 |
| RDS                        | 8.0.16 |
| Postgres (image scanning)  | 12.4|
| Anchore (image scanning)   | 0.8.1 |
| NATS Exporter              | 0.6.0.1 |
| NATS Streaming             | 0.17.0 |
| HA Proxy                   | 0.6.2|


### Installer binaries sha256sum

| **sha256sum** | **Installer binary ** |
|---|---|
| 53c0abed589a2ac425cbf5468039705fd63cdb3cd631b1ed6b7c3d20ac84a217 | installer-darwin-amd64 |
| 223d818dd43d5a3d6ef4b8f7152382a74984a4943d487913b013b60edb2a2706 | installer-linux-amd64 |
| 75417fe747a208ceeb38c37a54a5a4706ded78b1ca6982c3bd41a3febaae5bc5 | installer-windows-amd64.exe |
