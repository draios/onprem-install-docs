Release 6.10.0 Apr, 2024
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
| Cassandra                  | 4.1.3 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.9.17 |
| HA Proxy                   | 0.14.6 |


### Checksum for Installer Binaries

Current version: 6.10.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| ec48faa2083ebe4003dde68c821c20b4da8450b3b84ad27d21d043567fa617a7 | installer-darwin-amd64 |
| 2b894b5bae8470a27e3c0c4bc42d22c306d29fc423f76a071ab28d92854c0e5c | installer-darwin-arm64 |
| 4b9d17fefd83eb841c35268eef0ef6dc311e3fedcfb4ea13d32e613e24d48416 | installer-linux-amd64 |
| 187c2afa9df0a639424c00dcf43f85a942bd5660e0e539916d77739daf0bcf6f | installer-linux-arm |
| f10ea3081010a42c7191a2dfcbdbcd2480f8bd9e07c18a84094db9d20db0ca3f | installer-linux-arm64 |
