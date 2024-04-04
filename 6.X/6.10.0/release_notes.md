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
| e345bcec58d501d845767e85a9ef8a68b4a2370a78fdd35cf901e4f9ff9cdbe7 | installer-darwin-amd64 |
| 32b06a51ac4d5812c50393b635120726562741a10ca83d519050554532a37983 | installer-darwin-arm64 |
| a7c0457cce06879759be0a92a665d914cc76bae86599e651989de6de8c366017 | installer-linux-amd64 |
| 63a3676016e1b479c8a4445e36fe5cedc9c2a3e8b19277a24e6e291458a8b9a4 | installer-linux-arm |
| 16f6889a0f6624bfa23e5229515e4c62c462a62becc75e2a454fc9c7200de0f1 | installer-linux-arm64 |
