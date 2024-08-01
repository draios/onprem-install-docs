Release 6.11.1 Aug, 2024
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
| OpenSearch                 | 1.3.15 |
| Cassandra                  | 4.1.4 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.10.10 |
| HA Proxy                   | 0.14.6 |


### Checksum for Installer Binaries

Current version: 6.11.1-1

| **sha256sum** | **Installer binary** |
|---|---|
| f8510c5bb86539a977897111de851ed40b28925615e5da77826864bd637ec612 | installer-darwin-amd64 |
| a6e09c84c3dc1e8c66bbcf4187e9dfc397217aa713552c8d9033c122fb635772 | installer-darwin-arm64 |
| a551b687eb6b6555477df54286731ed9d6cff794c4d08da3f49c148336cd5abb | installer-linux-amd64 |
| c113be9fa5b5fd3be4ef10a92119ea9991216fc48c0869d8c7af027043011240 | installer-linux-arm |
| 9fbac8fac5d8db89bcf976cd918b2a4f13f369852336f85d1e0c9e5849bc75d4 | installer-linux-arm64 |