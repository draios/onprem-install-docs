Release 6.5.0 Sept, 2023
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

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

Current version: 6.

| **sha256sum** | **Installer binary** |
|---|---|
|  | installer-darwin-amd64 |
|  | installer-darwin-arm64 |
|  | installer-linux-amd64 |
|  | installer-linux-arm |
|  | installer-linux-arm64 |
