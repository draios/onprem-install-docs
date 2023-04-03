Release 6.0.1 March, 2023
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 6.0.1 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.X

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.18.20, 1.19.13, 1.20.9, 1.21.3, 1.22.8, 1.23.5, 1.24.10 |
| OpenShift                   | 3.11, 4.9, 4.10, 4.11 |
| GKE                         | 1.19.11-gke.1701 |
| EKS                         | 1.20, 1.21, 1.22 |
| Rancher                     | 2.5.7 |

### Sysdig Agent Version

Qualified with agent release 11.4.1

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.0.12 |
| ElasticSearch              | 6.8.6 |
| Cassandra                  | Fresh: 3.11.11 - Upgrade: 2.1.22.5 |
| Postgres                   | 12.10 |
| Anchore (image scanning)   | 0.8.1.32 |
| NATS Exporter              | 0.9.2 |
| NATS Streaming             | 0.22.0 |
| HA Proxy                   | 0.13 (Old K8s versions: 0.10) |


### Installer binaries sha256sum

Current version: 6.0.1-1

| **sha256sum** | **Installer binary ** |
|---|---|
| b821a4809956e39784bd1198a894474477138f2fdbb183f4a6ea90c4302e12c6 | installer-darwin-amd64 |
| b6d29140617d6ae517fc192fef84b70a8795daa59245ed5d970ae1ebe16d3415 | installer-darwin-arm64 |
| 5140ff6345e915390ae325ef9c73a86368b1bf8b31535949e209f3a1dcd6d2a2 | installer-linux-amd64 |
| d936794246c300655133544f131720d7d4e7c17106f132e6decb2b84ba790c4b | installer-linux-arm |
| 9d3b8433a994eb0d02a2e8489e9acab7775041c07b51a3c13c9728932cc6102a | installer-linux-arm64 |
