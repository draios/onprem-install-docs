Release 3.6.4 December 16, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/

Upgrade Matrix
---

Sysdig Platform version 3.6.4 has been tested and qualified against the following:

Supported Upgrade From: 3.2.2, 3.5.1, (3.6.0, 3.6.1, 3.6.2 or 3.6.3 if it was installed)

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
| 8825b7d3c0834ffb329ac59a3e566a187bfed3bc6e98da7c056c12fe2d2a4253 | installer-darwin-amd64 |
| d69d1afb68fdb50d2d161aba0419e35eca46ea46e01fc3ea0fb09921fb4adf20 | installer-linux-amd64 |
| 0727011f174230055d00fb4cd1d74937f930bdd2b2655e27b0bf925cfdd0d10e | installer-windows-amd64.exe |
