Release 6.7.1 Mar, 2023
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
| Cassandra                  | 3.11.16 |
| Postgres                   | 12.13 |
| NATS Streaming             | 0.24.6 |
| HA Proxy                   | 0.14.3 |


### Checksum for Installer Binaries

Current version: 6.7.1-1

| **sha256sum** | **Installer binary** |
|---|---|
| 18b324c6d9a3a3c7e160bdf4ec6014d87d49075b05ef55f678e3466ee2fe7baf | installer-darwin-amd64 |
| 379bb60e83d7047451c48df356a449f0fca1f86fe3b84510d98ba2840d79e4f4 | installer-darwin-arm64 |
| 240fd0a3f15d5192234b423be1e4bd029537d327db214c50de3b7f324babf6a0 | installer-linux-amd64 |
| 84fea37a623b838ebf475d65a4a433595c86b504b6abd0380a289d2e95495158 | installer-linux-arm |
| b414d23f5dcedea595bd6358fe2345fc994c4578e0a57187b50fec94f32a1924 | installer-linux-arm64 |
