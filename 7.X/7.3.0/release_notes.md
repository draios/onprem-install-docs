Release 7.3.0 June, 2025
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

Current version: 7.3.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| 42536d7e7f823fcb157a99a00df321a8449efa01610949667dc648de130c23a3 | installer-darwin-amd64 |
| ba86d0e01b4320fed257e7883972a3777fbb92a21cfafd77deace95bf0c6a828 | installer-darwin-arm64 |
| a5ab4e7d7d96eb354b29546a5889fa5b3149643012e4368fe4c88c522c71c56a | installer-linux-amd64 |
| f2f1b6a08b399399f1ac2c089a971240a6a4219f0e0a990d1e59787df22b2b29 | installer-linux-arm |
| 2cc7405d70616addb460a63c54b9e8768513973a73bdb82f5f5d5121fb7e8837 | installer-linux-arm64 |
