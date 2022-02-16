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
| Anchore (image scanning)   | 0.8.1.34 |
| NATS Exporter              | 0.7.0 |
| NATS Streaming             | 0.22.0 |
| HA Proxy                   | 0.10 |


### Installer binaries sha256sum

Current version: 5.0.4-2

| **sha256sum** | **Installer binary ** |
|---|---|
| 22c44d96ec43c981022867a5472df65d91b05d9f0bcc8a5318ccc567007b7671 | installer-darwin-amd64 |
| 50414bb1c0220df9795f508b5dbd9ba1e420bf2320eb2841c7c66182b8debae7 | installer-linux-amd64 |
| 070a33b7573dbdcd4f3b30674c1fbc46c7f5a5ccc9987e111caf47bc1eb47762 | installer-windows-amd64.exe |
