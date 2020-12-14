Release 3.6.2 December 14, 2020
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 3.6.2 has been tested and qualified against the following:

Supported Upgrade From: 3.2.2, 3.5.1, (3.6.0 or 3.6.1 if it was installed)

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
| f4febbebb9bfc87b3ee393d5c4b641955c7f61419ec97b9180dd939b4a3c02a2 | installer-darwin-amd64 |
| 2ff1c7fcac37ec58f5a424d2ff62d9cee4c72e4c644dd73ecdfd3c8f7b1cd511 | installer-linux-amd64 |
| 476acaf9badaf9860677661160efb01c1bce37000e744d0102d02fd5387c7946 | installer-windows-amd64.exe |
