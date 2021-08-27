Release 4.0.3 August 27, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 4.0.3 has been tested and qualified against the following:

Supported Upgrade From: 3.6.2, 4.0.0, 4.0.1, 4.0.2

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

Current version: 4.0.3-1

| **sha256sum** | **Installer binary ** |
|---|---|
| 46fc70cfdaf6a1d128115ede2479548e2b5187e67b0a8f4422d8bf9132ca1e32 | installer-darwin-amd64 |
| 318c64dd437695770e117ad950bd5d32cc97e011b80d25c8afd1c2064925e693 | installer-linux-amd64 |
| 8ea44753695744f79563f8d3f00bf6bbf90f4f1b1771251dc0e6be699438bd9e | installer-windows-amd64.exe |
