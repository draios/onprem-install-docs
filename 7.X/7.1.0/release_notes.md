Release 7.1.0 Feb, 2025
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

Current version: 7.1.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| 28114bf6f9d3de80673fb8d8b250ffddf8a164c81a176bbe2c6d3e41e98d41e9 | installer-darwin-amd64 |
| 683c33d3a38d69730fba449e7e97e624cd29fd574eb1187d93613807a60b5e6b | installer-darwin-arm64 |
| 6f9e115bb1a50f7dcd211b7802c7c53300246daca3ba8a6118f4a2d2655cc916 | installer-linux-amd64 |
| bb16f96f7639b11265fff294558099418974b11318b933cc8ce36c5de1782744 | installer-linux-arm |
| c6eb20190d72421f8b6058c6711cc7768689035e028ca49cf00d5912aca742b5 | installer-linux-arm64 |

