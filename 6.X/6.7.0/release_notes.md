Release 6.7.0 Dec, 2023
===

Review the full feature [release notes](https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html).

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

Current version: 6.7.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| 64ed1915764e98920511a0dc4a44b12d49fd46d59800f26990c9c2b9e77cb14e | installer-darwin-amd64 |
| 18df4007e9934b6ae71c20ebb5ea217130e8cd82f8366a45b3aefef318e92d75 | installer-darwin-arm64 |
| f8e62b61f6dd7f175f6e2c2d136677fcb662439f0b024cc7b237469b5ac5a88e | installer-linux-amd64 |
| 4360bb895d11f95c3cd1eb553d52b21469f9d6193bc911e4c1bffe67c0684c50 | installer-linux-arm |
| b1f4f7af04598412b39bd6115233806199cb4ff3a203165a4d3283ffb40d24c2 | installer-linux-arm64 |