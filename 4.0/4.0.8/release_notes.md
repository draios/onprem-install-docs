Release 4.0.8 ~~July, 2022~~ Updated Dec, 2022
===

Review the full feature release notes here: https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/

Patch Release updates in 4.0.8-2 (from 4.0.8-1)
---
1. Uber Image is updated with correct images
2. Fixes NodeAffinity in migration jobs

Upgrade Matrix
---

Sysdig Platform version 4.0.8 has been tested and qualified against the following:

Supported Upgrade From: 3.6.2, 4.0.0, 4.0.1, 4.0.2, 4.0.3, 4.0.4, 4.0.5, 4.0.6, 4.0.7

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

Current version: 4.0.8-2

| **sha256sum** | **Installer binary ** |
|---|---|
| 2ee753d526926c2f30c0ca9c1d9b3b9ad088c127e5b83b90e0c6efdefbcb4fab | installer-darwin-amd64 |
| b5f4d5a92243b7a028eb9bbf7f8eb9b325209486ba0799807600c0a93042ab4d | installer-linux-amd64 |
| e37912583552712341f87c3a3c23f868f0ae47fc8bd41c613f5ba11673ad2fd9 | installer-windows-amd64.exe |
