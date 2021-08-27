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
| 8015da26cb5e7db3f079a4a6229b06c29003c67456e6cd36042d2fb3678b4414 | installer-darwin-amd64 |
| 9bbe8cc1400751cd5d0604b642b3139a8200d57e7b7ffb60710f2ba7e5c94715 | installer-linux-amd64 |
| c86f83a144c091d76b110b482e16d1f007d3171b91fe7db54ed30049a6e58503 | installer-windows-amd64.exe |
