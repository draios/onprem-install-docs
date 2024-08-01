Release 6.11.1 Aug, 2024
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
| OpenSearch                 | 1.3.15 |
| Cassandra                  | 4.1.4 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.10.10 |
| HA Proxy                   | 0.14.6 |


### Checksum for Installer Binaries

Current version: 6.11.1-1

| **sha256sum** | **Installer binary** |
|---|---|
| 2fea88687beeb8600838b93e29e5a9d282de6b5fbee0a2a000b75eaa63cec505 | installer-darwin-amd64 |
| 224bdfcec57fcb191b3fc3029b0611623c24e528d1133a4e60b426b97f40e2ee | installer-darwin-arm64 |
| dd5506ce874312d6580eb29abcddf7df1d74cc852ca67d27401ba3877807670b | installer-linux-amd64 |
| 5817e80c09176ad7c998cdc3b7d9b7304b85c5a688d3734928dcb3bba4b03c42 | installer-linux-arm |
| 76ddfd8d6592e4ba4718ad2ebea3306beb62853b8cfed8844889c046be4aee7b | installer-linux-arm64 |
