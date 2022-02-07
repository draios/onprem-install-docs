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

Current version: 5.0.4-3

| **sha256sum** | **Installer binary ** |
|---|---|
| 3e304d389cd9e8261df5cccfadedde641c6acd08f950407a0f1247aa888490a3 | installer-darwin-amd64 |
| 0361a24e3a62e2bdd62e8f8a5a0bfe8195a4ff012b18d984fcf7b9229c326ec2 | installer-linux-amd64 |
| 3b1e13760738bf1d4eaee44a85fa77c3840e0e99c39441b1e6268d8ce9157263 | installer-windows-amd64.exe |
