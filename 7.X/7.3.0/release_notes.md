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
| 27f90ce141da86f7a94af42deda23b037292e010b32b96b08195d8f70288f2a1 | installer-darwin-amd64 |
| f90e6dcce8c12270d33fc4fe8d7457945e2ecd585e3fc65402ed7e4c9f941864 | installer-darwin-arm64 |
| cfe5e6059a3ef0145a0466c8d8b0916e6645ed6364cb873cd1fe9f4b0b7a64f0 | installer-linux-amd64 |
| e3e12ab666120779ad8eb7f06a7308c6c249173ede5934357fe6c4aca8b65a27 | installer-linux-arm |
| 0e448617fae5ca28080656df180067034ed038f897adbcc6943911c11b4e4f05 | installer-linux-arm64 |
