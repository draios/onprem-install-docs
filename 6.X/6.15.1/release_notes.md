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

Current version: 6.15.1-1

| **sha256sum** | **Installer binary** |
|---|---|
| 6dd53ead774522c924680113a8e351c8f633dcaf0a92fbef3694b87bcbc9e13d | installer-darwin-amd64 |
| c763eaea7fc4a5a52824a0cb6bb31da508d9972cec13dfc330ed04e1d613929c | installer-darwin-arm64 |
| 013b0c009dfbfd793433277a9c8aa327a31a279c40dabb386f1d4c1326fcc021 | installer-linux-amd64 |
| d0433580453c47661e6523797f3cb3375fd894ac3f9ec9f87949bc78c7cb2aec | installer-linux-arm |
| 4862d8a55cec657cdfd63e5f893d142bc672967d9bbbd88c4ac9cc5f9f0544b2 | installer-linux-arm64 |

