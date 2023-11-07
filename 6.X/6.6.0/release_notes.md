Release 6.6.0 Nov, 2023
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

## Use of MinIO in the Sysdig OnPrem

Starting from release 6.6.0 we have added MinIO to our stack (specifically importing the MinIO binary from upstream) for use in conjunction with our services.

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

Current version: 6.6.0-1

| **sha256sum** | **Installer binary** |
|---|---|
| 9b2e23b5551b9bfd8262900dc9ef2c52503a63c7b5c2fb0ec5c911d38f20085e | installer-darwin-amd64 |
| 96b61f4cd16d47ed90096af1d3cdd838c0e1da28937f0f96cfa5a68b8811e337 | installer-darwin-arm64 |
| 985399613e77a2088db05b02cebf0fbd158b0183e3974553fb6a68f940407832 | installer-linux-amd64 |
| 650f3b0cf998da30a1fa51e0dba25773a3ae305a012f8021dcc62b9aa9c2a5dc | installer-linux-arm |
| 8984a636dc9e92bfc40536cd33db84fdb967ed4b7fc413c28ae206b9416d6841 | installer-linux-arm64 |
