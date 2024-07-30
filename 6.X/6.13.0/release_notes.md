Release 6.13.0 May, 2024
===

Review the full feature [release notes](https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html).

Upgrade Matrix
---

Supported Upgrade From 6.X versions.

**Upgrade From Version 5.X or previous are NOT SUPPORTED.**

## Using MinIO in the Sysdig On-premises Environments

Starting from release v6.6.0 we have added MinIO to the Sysdig stack (specifically importing the MinIO binary from upstream) for use in conjunction with our services.

Download the MinIO source code from [minio](https://github.com/minio/minio). It is licensed under the [AGPL 3.0](https://github.com/minio/minio/blob/master/LICENSE).

Copyright: MinIO Project, (C) 2015-2023 MinIO, Inc. This product includes software developed at [MinIO, Inc](https://min.io/)

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.2.9 |
| OpenSearch                 | 1.3.15 |
| Cassandra                  | 4.1.4 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.10.10 |
| HA Proxy                   | 0.14.6 |


### Checksum for Installer Binaries

Current version: 6.13.0-1

| **sha256sum** | **Installer binary** |
|---|---|
~/sysdig/automation/onprem-automation/releases ~/sysdig/onprem-install-docs/6.X ~/sysdig/onprem-install-docs
| d36e8238834ffc3c64233ce3aac6d7112dbb0b645413a9ca93fd6b9c3d6957c7 | installer-darwin-amd64 |
| de753f4d2496af2665dd8b8acc0b8018e71c938c284e99901ae50a63225a531f | installer-darwin-arm64 |
| 029459dd8e19224e5833f2b6ebce8b1ce09539f405acd6c15cdbce4a056ad3b9 | installer-linux-amd64 |
| 7029db30b6dd145ae78f84c697c39aaca05f039390c67e67605d050997a6ac3c | installer-linux-arm |
| eec99fa16fcd145ecab40428af80dafad58ff5c00563f31a4c4ddd538742ca27 | installer-linux-arm64 |

~/sysdig/onprem-install-docs/6.X ~/sysdig/onprem-install-docs
