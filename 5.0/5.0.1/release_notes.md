Release 5.0.1 November 17, 2021
===

Review the full feature release notes here: https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/

Upgrade Matrix
---

Sysdig Platform version 5.0.1 has been tested and qualified against the following:

Supported Upgrade From: 4.0.X, 5.0.0

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

Current version: 5.0.1

| **sha256sum** | **Installer binary ** |
|---|---|
| 1ea0ad280d5b5584c49087c75411724cdb9c2e7839fd87a24a35237078b7ec73 | installer-darwin-amd64 |
| a15e286b2cc0ca792e7650cc7268eb99424e3934f9687380257b45f6c3152cdd | installer-linux-amd64 |
| bd1b1dc33a0a825bd0d0f577d32788d951637888c820c068d0c9a59e83b759e0 | installer-windows-amd64.exe |
