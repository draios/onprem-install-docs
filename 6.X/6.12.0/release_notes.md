Release 6.12.0 May, 2024
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
| OpenSearch                 | 1.3.15 |
| Cassandra                  | 4.1.4 |
| Postgres                   | 12.13 |
| NATS JetStream             | 2.10.10 |
| HA Proxy                   | 0.14.6 |


### Checksum for Installer Binaries

Current version: 6.12.0-1

| **sha256sum** | **Installer binary** |
|---|---|
~/sysdig/automation/onprem-automation/releases ~/sysdig/onprem-install-docs/6.X
~/sysdig/onprem-install-docs/6.X
