Release 6.14.1 Sep, 2024
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

Current version: 6.14.1-1

| **sha256sum** | **Installer binary** |
|---|---|
| fb57a3f834c15df0d40adf9fab2bbc56dbba424de354e877686c008ee88f6a1d | installer-darwin-amd64 |
| 860c6e75e8fc5fd08500e4565d83c3c5f8f2c2ef866fcef50dec4df91ff40f4c | installer-darwin-arm64 |
| 54c8f2747d91b2d6987e12a8f5bfc48bd8c6bcd16d9d8ea8143606141f20a06e | installer-linux-amd64 |
| d3dabf968f22ab3ef737c5916f9dfb9327f418f0d182461fd8038f8c7abb9496 | installer-linux-arm |
| b0be26a44326e5b3dd613db048af1240b4f018284be7fb2ffe2059b22cf7e626 | installer-linux-arm64 |

