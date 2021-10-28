Release 4.0.5 October 28, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 4.0.5 has been tested and qualified against the following:

Supported Upgrade From: 3.6.2, 4.0.0, 4.0.1, 4.0.2, 4.0.3, 4.0.4

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

Current version: 4.0.5-1

| **sha256sum** | **Installer binary ** |
|---|---|
| 6ffd8d883a80ea6984b6aa160e2c61a73ec6234821b3b026545534db28427fb3 | installer-darwin-amd64 |
| 5e35b610d98e9b6de6298cd547eee354bdda04e8d46a00062d087e47e214b329 | installer-linux-amd64 |
| 55dc7ff7338c977ff9d01e85a7b2c815814adc8a2cebd1ff701941dfadb6df62 | installer-windows-amd64.exe |
