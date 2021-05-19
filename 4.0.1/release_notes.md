Release 4.0.1 April 29, 2020
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Upgrade Matrix
---

Sysdig Platform version 4.0.1 has been tested and qualified against the following:

Supported Upgrade From: 3.6.2, 4.0.0

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.16.15, 1.17.17, 1.18.16, 1.19.8, 1.20.4 |
| OpenShift                   | 3.11, 4.4 |
| GKE                         | 1.18.12-gke.1210 |
| EKS                         | 1.18 |
| Rancher                     | 2.5.3 |

### Sysdig Agent Version

Qualified with agent release 11.2.0

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.0.12 |
| ElasticSearch              | 6.8.6 |
| Cassandra                  | release_version: 2.1.21 cql_version: 3.2.1 |
| Postgres (image scanning)  | 12.5|
| Anchore (image scanning)   | 0.9.1 |
| NATS Exporter              | 0.6.2 |
| NATS Streaming             | 0.17.0 |
| HA Proxy                   | 0.10 |


### Installer binaries sha256sum

Current version: 4.0.1-3

| **sha256sum** | **Installer binary ** |
|---|---|
| f120740b001c329d9f03f9a61a3b94b09bbceea0285a5670f83bfaced305a3b4 | installer-darwin-amd64 |
| 27c7c41eab5906d996dbdbccf4c5a5d6cd4d40c4b5a8be41796fbe71dc5c9dd7 | installer-linux-amd64 |
| 480a99de51935ff6ef6217b53b1d878bc3adfb63d9e41f72564ed43694984ccd | installer-windows-amd64.exe |
