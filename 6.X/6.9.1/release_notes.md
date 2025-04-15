Release 6.9.1 Mar, 2024
===

Review the [Sysdig On-Premises Release Notes](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/).

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

Current version: 6.9.1-1

| **sha256sum** | **Installer binary** |
|---|---|
| 580dfa2ec3fd528b472c1d3a4d5f294966aefe4490dd8d0eb54bd3d62b74a50a | installer-darwin-amd64 |
| a67fcd3980b9915ce51536c4a65ab9f99df26dac0c6c72550fd020cfdc8c97db | installer-darwin-arm64 |
| 59934e2f19b51f5476e32b1c3a25e7afae9b4070982e1f7b7e4dff8ad5958c5c | installer-linux-amd64 |
| 7ffa847b190216a8ee9dc73ddb3ca3f83fccd44e9c5ca21c09a9ccdbe40f51dc | installer-linux-arm |
| f6d828c10b28072c780c681403c58ad09bb441ef58b47c7492e95373ca993831 | installer-linux-arm64 |
