Release 6.16.2 Jan, 2024
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

Current version: 6.16.2-1

| **sha256sum** | **Installer binary** |
|---|---|
| b822794106cd6b57c88800200484b45a8173b90a8ffb0ebbde049c9951f41594 | installer-darwin-amd64 |
| 1fc3519319bfb71f7d4f2db70552849a3dd89ec4045321cb800664885770188c | installer-darwin-arm64 |
| 4007ae693e8c88849ebd189d96d9905c91c786416c9658e00e5d5b35b44b81bf | installer-linux-amd64 |
| 439c94259b181796409070e1ab02c6d122e278e3b0a9efb6b41509aa78cb9255 | installer-linux-arm |
| 9d7e16739bee88d08c2637ea34cf31cc77a9aa5bd63412ac6236a84ef39bf26f | installer-linux-arm64 |

