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
| 427c1fc0d0480f8799fd00782e2609fd06271fe87c94d8489a341859f8c17121 | installer-darwin-amd64 |
| 52b8f3886f770cfd5e4fab74f1a881bb875eb07f6835ed1e029c6bdf86366884 | installer-linux-amd64 |
| c8250c5e601e8bb7d1102c98c732a46bdc079279f921e7b0b3cf7dce1bf6c40c | installer-windows-amd64.exe |
