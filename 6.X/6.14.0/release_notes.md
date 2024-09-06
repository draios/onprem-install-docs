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

| 709b5fb76b8cd518befad0d801542f01ca5640eecafc710e26c6ba26aa976e8a | installer-darwin-amd64 |
| 8b8024a248330638cae42fdbe6ee77cc4ca59519832326f474f46bb4c099fc7a | installer-darwin-arm64 |
| 5ba07f1eda776df2d6b3e57c28876278fa0a61749fc65aaf634187a4e3fc8ce7 | installer-linux-amd64 |
| ad17e60b025d2e035d3071dfffaf045ab0e50ca2ff13f3791309ab780f499f54 | installer-linux-arm |
| a96aa7b2df2d6b297cee63612aede0de28155ebb4a3a6aadb119252a78af78ae | installer-linux-arm64 |

