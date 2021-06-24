Release 4.0.2 June 29, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 4.0.2 has been tested and qualified against the following:

Supported Upgrade From: 3.6.2, 4.0.0, 4.0.1

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

Current version: 4.0.2-1

| **sha256sum** | **Installer binary ** |
|---|---|
| 1bdd4d2e4f8dbaa1ca22e80f3d3202c19254311a378b5aa25f36df3c080c9c30 | installer-darwin-amd64 |
| 819b94755609071e43d3a9aa679ea42694f7807321c8864693558bbd98bc20ea | installer-linux-amd64 |
| a2ea9303589ccb6f19db0482e0330cf5f420f3b08e735b4ded32ba7aea927a17 | installer-windows-amd64.exe |
