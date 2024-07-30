Release 6.13.0 May, 2024
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
| OpenSearch                 | 1.3.15 |
| Cassandra                  | 4.1.4 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.10.10 |
| HA Proxy                   | 0.14.6 |


### Checksum for Installer Binaries

Current version: 6.13.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| 35212d71be4b87308b2993d1f0fcc485778c6ff681e651a8df370d30b8a1f3ba | installer-darwin-amd64 |
| 3c8907483b5e6618d7141162d8edf6599a127c4571b2063bb4fae1add4b7355c | installer-darwin-arm64 |
| d491f03f72becb507fd76884ac51ac42463562ec493bead4014538103ba90d25 | installer-linux-amd64 |
| dd89a96ab50f55f4f01da3678fa32ec60d9689c482efcbb8ea30a052a417a742 | installer-linux-arm |
| a0162aad9b3609e407287f5956d6ea52c2b4402a31cef398917daf49f2cc97eb | installer-linux-arm64 |
