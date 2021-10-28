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

Current version: 4.0.4-1

| **sha256sum** | **Installer binary ** |
|---|---|
| e54056c948b908dc23f194e4fac1e4bd84155c29e02ea089a3afe5292d19a6ec | installer-darwin-amd64 |
| e8066890cf8ec2b2551a92b3d5a4ad2ef7fac7f91f667c8b71c478c810fb27e4 | installer-linux-amd64 |
| ade480002b9d0bcf72c87a2685603900156ccc5bdcf093603f798165aaf46906 | installer-windows-amd64.exe |
