Release 6.14.0 Sep, 2024
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
| OpenSearch                 | 2.10.0 |
| Cassandra                  | 4.1.5 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.10.10 |
| HA Proxy                   | 0.14.7 |


### Checksum for Installer Binaries

Current version: 6.14.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| 19b20e4b83812a5f32f6f0a4ddac803de0867dd11fc8704a38755bfda15f4c32 | installer-darwin-amd64 |
| 9237b7a061d693c49c260b60d20a1d4277c448c9b93ac6a75b2a78f18d412635 | installer-darwin-arm64 |
| 8095c1684ebab9bcd50ba21773216fa2e3d9a301ddc19f5b0dedc71a0bf035f0 | installer-linux-amd64 |
| 70b606537b38458b46da0790aa8469a2dc43bc8532660636f60d561a3554758e | installer-linux-arm |
| c7c90d6ef776d70bb22daab701e8fd1c31acab9b94f447e14676d873f2fd02af | installer-linux-arm64 |
