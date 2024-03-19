Release 6.9.1 Mar, 2024
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
| Cassandra                  | 4.1.3 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.9.17 |
| HA Proxy                   | 0.14.6 |


### Checksum for Installer Binaries

Current version: 6.9.1-1

| **sha256sum** | **Installer binary** |
|---|---|
| 6cf6e7190dae312e03c8ef4f9a03e6cb36573ae2dc0dccd8e5590cd46712fa8a | installer-darwin-amd64 |
| 9915c5fd147b5d84fb744b1d79bb00a2004f281f572484afb5d74c2551b1f9a1 | installer-darwin-arm64 |
| 0a44d36dbc1694418eb0633a57ce3ba979f575ae83eb0507a4fa2ecd887ef7a3 | installer-linux-amd64 |
| 865c59813fca8fcfb02167bf97eae94986b52572197460062748dc16dad001da | installer-linux-arm |
| 060a81be61cb3801e8fbfabf8cfd2f1cd06f95e804135264d17846828ee64d1d | installer-linux-arm64 |
