Release 6.16.2 Jan, 2024
===

Review the [Sysdig On-Premises Release Notes](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/).

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

Current version: 6.16.2-1

| **sha256sum** | **Installer binary** |
|---|---|
| 8c466cf9e4ccad92b6b039e7f83c6ce2778ff124ed7a0870fbe3ddc90e790c72 | installer-darwin-amd64 |
| bccee25610deaf796e0d8919dc82ec5304055aa0c2143cc2357ef76a77348c40 | installer-darwin-arm64 |
| b280e3edf257e533287956a705018e67281a6d620359ca4226b6117d5c265244 | installer-linux-amd64 |
| 646a02470efffef48d613b0994503af9847e5dd344025779f92764ba0072fc32 | installer-linux-arm |
| b89ce74c75580a1fb7d1fce7b5bbc48f839c8695102d33c806ca52a56e586ebd | installer-linux-arm64 |

