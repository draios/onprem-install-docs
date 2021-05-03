Release 4.0.1 April 29, 2020
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 4.0.1 has been tested and qualified against the following:

Supported Upgrade From: 3.6.2, 4.0.0

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.16.15, 1.17.17, 1.18.16, 1.19.8, 1.20.4 |
| OpenShift                   | 3.11, 4.4 |
| GKE                         | 1.18.12-gke.1210 |
| EKS                         | 1.18 |
| Rancher                     | 2.5.3 |

### Sysdig Agent Version

Qualified with agent release 11.2.0

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.0.12 |
| ElasticSearch              | 6.8.6 |
| Cassandra                  | release_version: 2.1.21 cql_version: 3.2.1 |
| Postgres (image scanning)  | 12.5|
| Anchore (image scanning)   | 0.9.1 |
| NATS Exporter              | 0.6.2 |
| NATS Streaming             | 0.17.0 |
| HA Proxy                   | 0.10 |


### Installer binaries sha256sum

| **sha256sum** | **Installer binary ** |
|---|---|
| 4a1a02fe6d02631c352063383b546995cca3d8dbbd41aa30f5ad77edbb5b5fdb | installer-darwin-amd64 |
| 77366a38cde944a800205ac65ba63c22a0ca382419f33ddfa9219af9a5929d4a | installer-linux-amd64 |
| 1a169b684e70c38c70e14be281834cfbf14b1730b199e825818fffe02bab4a8f | installer-windows-amd64.exe |
