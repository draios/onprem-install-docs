Release 6.8.0 Jan, 2024
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

Current version: 6.8.0-2

| **sha256sum** | **Installer binary** |
|---|---|
| 2bd79691b3e85d884ab8e16973baeb5447e04e1cd0f8cd48acb63ec0065429f9 | installer-darwin-amd64 |
| 6ad263fd3b5a841efa68db57b1a24831c7039dc805cc7209350953bb2a73009b | installer-darwin-arm64 |
| 515d8a1c81343e213e3c61119f2d9e54bfb1dbb3ad18ecf1397b562e5aacf15b | installer-linux-amd64 |
| bb9eddb57dc0c0bc94acd3ceeb4ca9f961b7d2dcf070f32f23119740676348b1 | installer-linux-arm |
| 9337095de8f5eb11904f252666f86355e940e8ad0423a860bf8b292b971e2772 | installer-linux-arm64 |