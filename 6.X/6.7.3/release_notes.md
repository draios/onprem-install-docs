Release 6.7.3 Jul, 2024
===

Review the [Sysdig On-Premises Release Notes](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/).

## Using MinIO in the Sysdig On-premises Environments

Starting from release v6.6.0 we have added MinIO to the Sysdig stack (specifically importing the MinIO binary from upstream) for use in conjunction with our services.

Download the MinIO source code from [minio](https://github.com/minio/minio). It is licensed under the [AGPL 3.0](https://github.com/minio/minio/blob/master/LICENSE).

Copyright: MinIO Project, (C) 2015-2023 MinIO, Inc. This product includes software developed at [MinIO, Inc](https://min.io/)

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.2.9 |
| OpenSearch                 | 1.3.9 |
| Cassandra                  | 3.11.16 |
| Postgres                   | 12.13 |
| NATS Streaming             | 0.24.6 |
| HA Proxy                   | 0.14.3 |


### Checksum for Installer Binaries

Current version: 6.7.3-1

| **sha256sum** | **Installer binary** |
|---|---|
| 3d4a97c973dbb6b9903311b9e2da395d964a312d8de11f5b7446a4183a46cf23 | installer-darwin-amd64 |
| 8964a37cbe800329b311b57dafefcd6507b48fd3879222c10a664c835b2132d1 | installer-darwin-arm64 |
| 867f690a15179607a8fc0eb4585a55ae2d0a51fa95646e4c438ddd01c5c3a6a8 | installer-linux-amd64 |
| cc35eaa5cb8cd3f76436f67978a6259992b45973b8579f935e85c9c1ea6c0f3d | installer-linux-arm |
| f1ead013fe0ed5205a69c63d4d96f217a08fc7459b2ab8ea20a3114261ed65da | installer-linux-arm64 |