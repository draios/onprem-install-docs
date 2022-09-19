Release 5.1.3 Sept, 2022
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 5.1.3 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.X

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.18.20, 1.19.13, 1.20.9, 1.21.3, 1.22.8, 1.23.5 |
| OpenShift                   | 3.11, 4.9, 4.10, 4.11 |
| GKE                         | 1.19.11-gke.1701 |
| EKS                         | 1.20, 1.21, 1.22 |
| Rancher                     | 2.5.7 |

### Sysdig Agent Version

Qualified with agent release 11.4.1

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.0.12 |
| ElasticSearch              | 6.8.6 |
| Cassandra                  | Fresh: 3.11.11 - Upgrade: 2.1.22.5 |
| Postgres                   | 12.10 |
| Anchore (image scanning)   | 0.8.1.32 |
| NATS Exporter              | 0.9.2 |
| NATS Streaming             | 0.22.0 |
| HA Proxy                   | 0.13 (Old K8s versions: 0.10) |


### Installer binaries sha256sum

Current version: 5.1.3-1

| **sha256sum** | **Installer binary ** |
|---|---|
| 80b0b5ab5199f8c9062f376ae6296574c87d3ba030af18bdd792baef8fc8e6a1 | installer-darwin-amd64 |
| 620e81a02e56549a75ddaf19608a085d9a0cc7bdaa45130bb4b9646d468d2db9 | installer-linux-amd64 |
| f0e808f0a0000b052afa3be9c1b4f11a46151b9409bb09d158bc10674122a76f | installer-windows-amd64.exe |
