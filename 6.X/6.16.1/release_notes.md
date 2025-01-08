Release 6.16.1 Jan, 2024
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

Current version: 6.16.1-1

| **sha256sum** | **Installer binary** |
|---|---|
| 26eb77a8875148b0b72c4726db86748cfe571d388332ba250a3bcdda304bcd1b | installer-darwin-amd64 |
| f4e9dedee0d43f698eef511c811d17394fb7060c7073101c62320c5751f933a3 | installer-darwin-arm64 |
| 6d718a47ad9d4b9f73ed199968caf1ae582f6b18c7e66b759d75de4765923566 | installer-linux-amd64 |
| 3be6731ef1e038b80f26018ea1d751d8624fcf10f12129bab7efeb73fa5aa8a2 | installer-linux-arm |
| 51222532bea8a58a852cf2bf0e057b10def1cce84f33b0170381f31bbb1b1d44 | installer-linux-arm64 |

