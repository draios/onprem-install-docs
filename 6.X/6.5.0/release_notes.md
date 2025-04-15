Release 6.5.0 Sept, 2023
===

Review the full feature release notes here: https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/

## Use of MinIO in the Sysdig OnPrem

Starting from release 6.5.0 we have added MinIO to our stack (specifically importing the MinIO binary from upstream) for use in conjunction with our services.

The MinIO source code can be downloaded [here](https://github.com/minio/minio) and is licensed under the [AGPL 3.0](https://github.com/minio/minio/blob/master/LICENSE).

Copyright: MinIO Project, (C) 2015-2023 MinIO, Inc. This product includes software developed at [MinIO, Inc](https://min.io/)

### Sysdig Agent Version

Qualified with agent release

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.2.9 |
| OpenSearch                 | 1.3.9 |
| Cassandra                  | 3.11.16 |
| Postgres                   | 12.13 |
| NATS Streaming             | 0.24.6 |
| HA Proxy                   | 0.14.3 |


### Checksum for Installer binaries

Current version: 6.5.0

| **sha256sum** | **Installer binary** |
|---|---|
| a5b0d01a2a66b71e2713235932a7b65048fa509c92141e9046b782521d24c48b | installer-darwin-amd64 |
| 589217125ce4721ab5e0105513176e1460f581fda73100b73eadc896af9cbb47 | installer-darwin-arm64 |
| c9858a0d84b1cd57f7b33158b60fc00f404e6b6f63d31ffb2c316d18036f5da2 | installer-linux-amd64 |
| 0363266d1e970dd56c92b7c395914fb0b444aaddfc3ada67ab5e7a2ba5cc3ea1 | installer-linux-arm |
| 4c2047e5d19809c29d747b4d0022be4e3678207cf4a58aca5c6300b1625f167f | installer-linux-arm64 |
