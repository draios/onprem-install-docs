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
| e9db69903e797f0027c8d6d2b728aa502400914de19e1a3e04ff927058cfea26 | installer-darwin-amd64 |
| 7e0598d8000dad1b6e08e60c08d3d6f53da8b1ea868f7b061664b502eb424302 | installer-darwin-arm64 |
| e6abf579fd2e33e8d711ca5bc2b53afdbe67680747686fdbc391c2cc80c88024 | installer-linux-amd64 |
| 4c204fd4971fdcb48097b6e1a82d7f2d5227832455c1d480747bc75393901113 | installer-linux-arm |
| 2e0764d3bebc04ff114d1358f75365d96f0b3cd822a75a36312cee9192590a09 | installer-linux-arm64 |

