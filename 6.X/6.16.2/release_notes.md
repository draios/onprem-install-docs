Release 6.16.2 Jan, 2024
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
| OpenSearch                 | 2.11.1 |
| Cassandra                  | 4.1.5 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.10.14 |
| HA Proxy                   | 0.14.7 |


### Checksum for Installer Binaries

Current version: 6.16.2-1

| **sha256sum** | **Installer binary** |
|---|---|
| 5c0bb45b127e1ed3c326e310f414cc110800d1c3af5db15ebe32c9be1b6c2744 | installer-darwin-amd64 |
| b03a451aed513174dd9323232e0f64e1010dbe6bd22111a5b9f976a4ba7f2ed8 | installer-darwin-arm64 |
| 1acbaf51c960ed3d73cceee76495b3036d40a884f84362b4c9d57ccd960e6edc | installer-linux-amd64 |
| fca8e596344b0de0497c856e39d7ab0979b5e001134b4033a3bec393d9853e34 | installer-linux-arm |
| 1b272840a96f271e8b28e84127b71ad0c0b7ff93ee0d70537285fb765742af91 | installer-linux-arm64 |

