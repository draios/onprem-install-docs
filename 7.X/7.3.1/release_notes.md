Release 7.3.1 Aug, 2025
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

Current version: 7.3.1-1

| **sha256sum** | **Installer binary** |
|---|---|
| b6eabd9b05c2bce5548a3b72af995f20735c591bb9012683ed677be43548e018 | installer-darwin-amd64 |
| 111f55f1fbb7814f2c83f0138316348f098aaf7cf3b0b19d5a99a47fcd375ce1 | installer-darwin-arm64 |
| 10800bf8b62ee455f3d7e0a051c9168530200d65d7bd9001c70aa18d0fef68bd | installer-linux-amd64 |
| cb6c5ef47c109175499697d10358d22048e236db535dbdf716b537fae9dd8f0c | installer-linux-arm |
| 4612c160b9a2dab73a9c8f94a5861d5f5ead8060c3df3b824a0656c236737a7d | installer-linux-arm64 |

