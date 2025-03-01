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
| Redis                      | 6.2.14 |
| OpenSearch                 | 2.18.0 |
| Cassandra                  | 4.1.7 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.10.14 |
| HA Proxy                   | 0.14.7 |


### Checksum for Installer Binaries

Current version: 7.1.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| 682f6583afac26347af6c17a86c5c9dabf51e023e7e7cfc9f22d0feae1fcf1f3 | installer-darwin-amd64 |
| 4aea1f7ab4def424b7fb5480d93c634db9b8c3f0140ce5f28b04ebcc731e7baf | installer-darwin-arm64 |
| d7a5caa566622e5bf94f26bdd53a17f295a281f17db6497fcc3f772da20c7e59 | installer-linux-amd64 |
| 541ca61c1fc515de78760395f17eb186c98839d59db4016f2ded9a2066c71154 | installer-linux-arm |
| 9e3618973606a577969667e3fa55f579645d8c6708e52e1560c08ee7681869a7 | installer-linux-arm64 |

