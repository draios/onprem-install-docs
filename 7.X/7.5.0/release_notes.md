Release 7.5.0 Nov, 2025
===

To review all the features, see [Sysdig On-Premises Release Notes](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/).

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
| Redis                      | 6.2.14 |
| OpenSearch                 | 2.18.0 |
| Cassandra                  | 6.1.0 |
| Postgres                   | 15.8 |
| NATS JetStream             | 2.10.14 |
| HA Proxy                   | 0.14.7 |
| Neo4J                      | 5.19.0 |


### Checksum for Installer Binaries

Current version: 7.5.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| 8549d825d1dce718321d212694ee49866b19237bfb6a26775c5fb1abf37592ab | installer-darwin-amd64 |
| 175ea200124377857bdf53de9d8ed0567b8da6140a68d3c4d07c7676a1be3170 | installer-darwin-arm64 |
| 50b3c1e4ce75a8de905a24cbf4d9a7c8527bac9f80d34a3a0ffd683e28732aa1 | installer-linux-amd64 |
| ad509165b296535e80711162da35b6c2a519bdbc86433c85073d3b3daa012190 | installer-linux-arm |
| 465665db2ab5f161a56d57cedd76d9a33b21969c73ccf6dc73bf5c1f1127ef33 | installer-linux-arm64 |