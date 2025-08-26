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

Current version: 7.4.0-2

| **sha256sum** | **Installer binary** |
|---|---|
| acdbaf3ff2b06cd80e9daa3d671cc70624416879e1ece950bfd73385d1af2065 | installer-darwin-amd64 |
| a60eabca81abf9b4fd4562d41573dd6e22f546ad1e9b707784be2a769761a999 | installer-darwin-arm64 |
| 1226cfce5330d18620d83b93daf850a8b14f7916710b0012a150fe8be5519394 | installer-linux-amd64 |
| 3805095d81e44208162c8ec9c94565d40707b43a314bc77cc0c79c4ba07d9394 | installer-linux-arm |
| e5ea0a62578e685629e5e955fca3fa5582e8e9d1f3d444365470dd497b8d5b21 | installer-linux-arm64 |
