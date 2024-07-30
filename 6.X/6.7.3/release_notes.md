Release 6.7.3 May, 2024
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
| Cassandra                  | 3.11.16 |
| Postgres                   | 12.13 |
| NATS Streaming             | 0.24.6 |
| HA Proxy                   | 0.14.3 |


### Checksum for Installer Binaries

Current version: 6.7.3-1

| **sha256sum** | **Installer binary** |
|---|---|
~/sysdig/automation/onprem-automation/releases ~/sysdig/onprem-install-docs/6.X
| fb9de2959483ab5c29eeb7feb7255fd1cffb6424afd1e00a04c2843011c82bec | installer-darwin-amd64 |
| 891f5a32195254df3cce511ec726c0280a1840aa4f60bd44e6f91cda44056bb5 | installer-darwin-arm64 |
| 8c3ca6287abb1d866063088538572974a67b49e2c2cd1160bad27ab4c6750cf4 | installer-linux-amd64 |
| 569487663845f97a2a1d4e8669617dd0e329cc4ff45011068c0f6a5c4a974503 | installer-linux-arm |
| f15cf7f5a92ab5e2c2ec40aa6ec9d1af2b7d9c39c5d6d45838e6031ca9096c00 | installer-linux-arm64 |

~/sysdig/onprem-install-docs/6.X
