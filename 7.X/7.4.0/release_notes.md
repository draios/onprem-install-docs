Release 7.4.0 Aug, 2025
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
| Neo4J                      | 5.19.0 |


### Checksum for Installer Binaries

Current version: 7.4.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| a495e60c3407a648f404997ed9d4208825fcebbc762efb7853fecaad08f6a7b2 | installer-darwin-amd64 |
| 0205b6ef14c6a3f4a27a50c0b8a6c351a1af0a180870b7631b3ec8b86cc3f5a9 | installer-darwin-arm64 |
| 21f258603f6838bc3ce7d1e84275f7475e61374b76dfa8c1f99fb78dabc4aa42 | installer-linux-amd64 |
| b634e702902728baac88dfb75784888645c9bed42e6e1e72c3208d514d59f648 | installer-linux-arm |
| 254db4a567346e177535a6975d3c720bf39f6e07b16c595805b5cc75b7e20801 | installer-linux-arm64 |

