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

Current version: 6.8.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| b098f4d98a5efd4dc2ef83322da5c878c4dc747daa2e280c235bc6ab45c35b12 | installer-darwin-amd64 |
| 610a510f9ad87d49ac2767dab7c34e17ae291eb7969f9371ae66727193876c18 | installer-darwin-arm64 |
| ee85f675cd21ef01dbfbaf9c829b91b852203554c83c3248610f8ad33fbcf64a | installer-linux-amd64 |
| ec09e38180fab8db25813ce18d3d07e2d58a0baa4aea6ff80ee155d97b99fd74 | installer-linux-arm |
| 75fdb07928568bf4f109cc737e9015c65b2b744cbfdcf66258044e01b03d983d | installer-linux-arm64 |
