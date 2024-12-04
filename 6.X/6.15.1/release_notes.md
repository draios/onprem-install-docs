Release 6.15.1 Nov, 2024
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
| Redis                      | 6.2.9 |
| OpenSearch                 | 2.11.1 |
| Cassandra                  | 4.1.5 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.10.14 |
| HA Proxy                   | 0.14.7 |


### Checksum for Installer Binaries

Current version: 6.15.1-2

| **sha256sum** | **Installer binary** |
|---|---|
| 3a9913fac96ad80fbae5a9079f9a0278377da07c4e7e66cb677b8bc7196510d0 | installer-darwin-amd64 |
| 17a09ebd6ed4aa43cb70b902220356f2aa5898fcc8a5ad7181f1eb7d87c04343 | installer-darwin-arm64 |
| b51ee013d0efcae454d09adbbc349ac649d9edc06fc0d0d36215d46a897ae6f9 | installer-linux-amd64 |
| 73c5e4562a02100e3e6d093f524938833129f30c9ea1df128e53539322729390 | installer-linux-arm |
| b17c025f13bbecedf38009b70f2209bef0ab8fac12c0e568895464027070de18 | installer-linux-arm64 |

