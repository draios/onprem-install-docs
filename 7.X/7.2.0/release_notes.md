Release 7.2.0 Apr, 2025
===

To review all the features, see [Sysdig On-Premises Release Notes](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/).

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
| Redis                      | 6.2.14 |
| OpenSearch                 | 2.18.0 |
| Cassandra                  | 6.1.0 |
| Postgres                   | 15.8 |
| NATS JetStream             | 2.10.14 |
| HA Proxy                   | 0.14.7 |


### Checksum for Installer Binaries

Current version: 7.2.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| 96792f6fd32277ed79e2d8e392c04d37242e2a75c570b7b355704ae4c9803826 | installer-darwin-amd64 |
| 29c1ca926d19b8721a696c322b855706d8c5bc47767c6c252cbd1444db0deae4 | installer-darwin-arm64 |
| 0bca7642b29a5556dc8027e664bdc3b6da7ae65b44ece638e0d9027ee93ed32c | installer-linux-amd64 |
| 1125bce13395eccc6c153fc5e8c57afc8ad68533c1b8b4b5ee0687027cc19a4c | installer-linux-arm |
| 9e040c10180912071403b9f4f410df7c50e750a4ed9f191b92b5b898cc731dd0 | installer-linux-arm64 |