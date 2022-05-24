Release 5.0.5 April, 2022
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 5.0.5 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.X

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
| Anchore (image scanning)   | 0.8.1.32 |
| NATS Exporter              | 0.7.0 |
| NATS Streaming             | 0.22.0 |
| HA Proxy                   | 0.10 |


### Installer binaries sha256sum

Current version: 5.0.5-1

| **sha256sum** | **Installer binary ** |
|---|---|
| c488a9e4a55dc631d57a81748b326bb9bf830d559307a1b661a8318d8967f39a | installer-darwin-amd64 |
| b77919f36ff8b1b898a9e10907b7a78834caea1ac63c96d36166af72aa85d428 | installer-linux-amd64 |
| b8daa8ca99179d106656ca4bb4494c5ece2c00b074abf9b9a8f7915a40f438f3 | installer-windows-amd64.exe |
