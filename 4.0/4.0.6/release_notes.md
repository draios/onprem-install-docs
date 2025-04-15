Release 4.0.6 December 14, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/

Upgrade Matrix
---

Sysdig Platform version 4.0.6 has been tested and qualified against the following:

Supported Upgrade From: 3.6.2, 4.0.0, 4.0.1, 4.0.2, 4.0.3, 4.0.4, 4.0.5

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

Current version: 4.0.6-1

| **sha256sum** | **Installer binary ** |
|---|---|
| c670cdbc92290e777f5fe79f6f7df0ea5fdae630cbe108db48f7adb9ca470b00 | installer-darwin-amd64 |
| ef316f288f939465d6c01235db52fea20baab543248b1997b484c25aec568aa1 | installer-linux-amd64 |
| 90169c63ebf3878cd23db1e81e5743c68b6b0c966ee86fb88ca09ee6ec8d9317 | installer-windows-amd64.exe |
