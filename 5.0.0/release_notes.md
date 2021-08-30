Release 5.0.0 DATE TBD
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 5.0.0 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X

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
| Cassandra                  | Fresh: 3.11.11 - Update: 2.1.22.4 |
| Postgres                   | 12.8 |
| Anchore (image scanning)   | 0.9.1 |
| NATS Exporter              | 0.7.0 |
| NATS Streaming             | 0.22.0 |
| HA Proxy                   | 0.10 |


### Installer binaries sha256sum

Current version: TBD

| **sha256sum** | **Installer binary ** |
|---|---|
| 899bdb4e901a29c6a2a6fff52242155945c9714bdf5af2baaca2f76d0c8140ac | installer-darwin-amd64 |
| ff5d29f8e30830d41b23600b41be19cbcba9916843a4f5d9c9100ef3957edc06 | installer-linux-amd64 |
| b11067ed642bbb89df47afe386de968ac39724c227e703f6e434ef89d282dd7e | installer-windows-amd64.exe |
