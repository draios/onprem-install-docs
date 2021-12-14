Release 3.6.3 December 14, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 3.6.3 has been tested and qualified against the following:

Supported Upgrade From: 3.2.2, 3.5.1, (3.6.0, 3.6.1 or 3.6.2 if it was installed)

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

Qualified with agent release 10.7.0

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
| d438aefcf8aa26dcb3367cc0840926527976841329c6c50b642107c45381798f | installer-darwin-amd64 |
| 7c8f0ef8564e61eff4a3540658a6e4b5947b8553c62f96587e3f1e9ffd8daede | installer-linux-amd64 |
| 96437c465f3fe4c66668b1f704299012ed98640d8a3cfb7ded538791d6ea2d33 | installer-windows-amd64.exe |
