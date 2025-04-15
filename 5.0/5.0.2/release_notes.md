Release 5.0.2 December 13, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/

Upgrade Matrix
---

Sysdig Platform version 5.0.2 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.0, 5.0.1

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.16.15, 1.17.17, 1.18.20, 1.19.13, 1.20.9, 1.21.3 |
| OpenShift                   | 3.11, 4.7 |
| GKE                         | 1.19.11-gke.1701 |
| EKS                         | 1.20 |
| Rancher                     | 2.5.7 |

### Sysdig Agent Version

Qualified with agent release 11.4.1

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.0.14 |
| ElasticSearch              | 6.8.6 |
| Cassandra                  | Fresh: 3.11.11 - Upgrade: 2.1.22.4 |
| Postgres                   | 12.8 |
| Anchore (image scanning)   | 0.9.1 |
| NATS Exporter              | 0.7.0 |
| NATS Streaming             | 0.22.0 |
| HA Proxy                   | 0.10 |


### Installer binaries sha256sum

Current version: 5.0.2

| **sha256sum** | **Installer binary ** |
|---|---|
| b4764355bad9d9d8c1ef3b1294fcce00f18435ed7323d07dea652fe7404a59b7 | installer-darwin-amd64 |
| f344008326ebc50ca0e57b7e378a1b9572de9cb5c4499091d29f18f6224c4a5d | installer-linux-amd64 |
| 7555e5bea1eac1bd2dc3e8c8f74b86f1a46a16066c993fda7ceb85198712816a | installer-windows-amd64.exe |
