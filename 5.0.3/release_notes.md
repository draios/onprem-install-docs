Release 5.0.2 December 13, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 5.0.2 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.0, 5.0.1

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

Current version: 5.0.2

| **sha256sum** | **Installer binary ** |
|---|---|
| 50f0c3bb44f7d065bc286d3b4a087a4fa2814e70cfa04dd930ac2e49089c1feb | installer-darwin-amd64 |
| c0da8ac9cd93fd1476c4eea9d84d0c12d1622584059a724fcc438de02578641f | installer-linux-amd64 |
| 3ce037f0f8747e28bc52879a7b95d21d2505161690d411eb80319bf052952df7 | installer-windows-amd64.exe |
