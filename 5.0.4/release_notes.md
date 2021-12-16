Release 5.0.4 December 16, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 5.0.4 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.0, 5.0.1, 5.0.2. 5.0.3

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

Current version: 5.0.4

| **sha256sum** | **Installer binary ** |
|---|---|
| d438aefcf8aa26dcb3367cc0840926527976841329c6c50b642107c45381798f | installer-darwin-amd64 |
| 7c8f0ef8564e61eff4a3540658a6e4b5947b8553c62f96587e3f1e9ffd8daede | installer-linux-amd64 |
| 96437c465f3fe4c66668b1f704299012ed98640d8a3cfb7ded538791d6ea2d33 | installer-windows-amd64.exe |
