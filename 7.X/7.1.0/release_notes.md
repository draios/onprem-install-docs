Release 7.1.0 Apr, 2025
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

Current version: 7.1.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| feefbc110b624e537e82138d203f0bbc6bef76fcb340d671cb8740c35c69831c | installer-darwin-amd64 |
| 1cb1979f36c34dbccfedcc5244445829869ebc23e0c785d18393c80c2fd5e259 | installer-darwin-arm64 |
| cf2183e4b3533c11a2cf21d1ec6d51578e3615b7ed47f5f79df2169bfbc46d5d | installer-linux-amd64 |
| cc9e4183fbd7c67066638e79e8f7e85b8bac5ada8cff40fdc6de807973b1a766 | installer-linux-arm |
| 0c3006b74877ca29206bf56428b129b272d4aa949110d70d40c6bda6e8f79c15 | installer-linux-arm64 |

