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
| Cassandra                  | Fresh: 3.11.11 - Upgrade: 2.1.22.4 |
| Postgres                   | 12.8 |
| Anchore (image scanning)   | 0.9.1 |
| NATS Exporter              | 0.7.0 |
| NATS Streaming             | 0.22.0 |
| HA Proxy                   | 0.10 |


### Installer binaries sha256sum

Current version: 5.0.0

| **sha256sum** | **Installer binary ** |
|---|---|
| d5756f07d24e817c59c7a4f89785ea2fbbb584eebe56be65dd0e70c7be7b5c47 | installer-darwin-amd64 |
| abef71213a94dbd85d3ff6462dcc8068a3b63f0ebaa4ef45007f4d60c799d0a0 | installer-linux-amd64 |
| 3f6270e76a2915d2eae31e0ab8911e2839a42acab36707c967dbcfbb2cef7077 | installer-windows-amd64.exe |
