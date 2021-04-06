Release 4.0.0 April 06, 2020
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 4.0.0 has been tested and qualified against the following:

Supported Upgrade From: 3.6.2

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.16.15, 1.17.17, 1.18.16, 1.19.8, 1.20.4 |
| OpenShift                   | 3.11, 4.4 |
| GKE                         | 1.18.12-gke.1210 |
| EKS                         | 1.18 |
| Rancher                     | 2.5.3 |

### Sysdig Agent Version

Qualified with agent release 11.0.0

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.0.12 |
| ElasticSearch              | 6.8.6 |
| Cassandra                  | release_version: 2.1.21 cql_version: 3.2.1 |
| RDS                        | 8.0.16 |
| Postgres (image scanning)  | 12.5|
| Anchore (image scanning)   | 0.9.1 |
| NATS Exporter              | 0.6.2 |
| NATS Streaming             | 0.17.0 |
| HA Proxy                   | 0.10 |


### Installer binaries sha256sum

| **sha256sum** | **Installer binary ** |
|---|---|
| c7837a9bc973dbdf6b9039069fe63a523b04275105937a24cf4fe56682a8cb58 | installer-darwin-amd64 |
| ed6663c68295a53a3565eb2b180aedb578f926a3c0d84b16c2a43591aa0bfdbd | installer-linux-amd64 |
| e3d9ea674a6b038d7f4a3e8713a4397346f36b60940cec41ecf4a3ddd757ae48 | installer-windows-amd64.exe |
