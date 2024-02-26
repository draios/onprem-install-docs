Release 6.9.0 Feb, 2024
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
| HA Proxy                   | 0.14.5 |


### Checksum for Installer Binaries

Current version: 6.9.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| 5e3b147c836b3c75034b568dc32fe61c15038c75fe595e85a617faa7897cf17d | installer-darwin-amd64 |
| 7520619b2c76b73e5c36835d4cc41d4040c2f1ed8772ec1e4a7ea61466de31eb | installer-darwin-arm64 |
| 983e42022d5fe7b19bd9b3e4b88199ae8128f4e4791b4c5b81c4e25aaba08475 | installer-linux-amd64 |
| dde2fc4bfd7309840233267bea012671da12dd05061180295c2d0d1f8d328507 | installer-linux-arm |
| 808d3ae6670944421a9eef063de3db7fc1be31b5b22bdd04e5f449022a2ca45c | installer-linux-arm64 |