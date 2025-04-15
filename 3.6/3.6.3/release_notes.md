Release 3.6.3 December 14, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/

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
| 9cdd26b1f74a30b87bcf08955b88482f590f4415b07daf6bcde7be3c5c0aca96 | installer-darwin-amd64 |
| 7d02cb56fff9ba321691b4baa52c71bd4680afdf943f364a652db661fdf582f2 | installer-linux-amd64 |
| c74877642703f34eb48f9a0fcf2f8ab1ed7133dd5622bfe32fc289c69bbf0635 | installer-windows-amd64.exe |
