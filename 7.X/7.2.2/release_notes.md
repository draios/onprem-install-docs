Release 7.2.2 Sep, 2026
===

To review all the features, see [Sysdig On-Premises Release Notes](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/).

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
| Redis                      | 6.2.14 |
| OpenSearch                 | 2.18.0 |
| Cassandra                  | 6.1.0 |
| Postgres                   | 15.8 |
| NATS JetStream             | 2.10.14 |
| HA Proxy                   | 0.14.7 |
| Neo4J                      | 5.19.0 |


### Checksum for Installer Binaries

Current version: 7.2.2-1

| **sha256sum** | **Installer binary** |
|---|---|
| b2e82a6824e127c7951d9d917f4402774d9b04bd1053696a37b8b375c27e9ccf | installer-darwin-amd64 |
| 831268a5a6cba0f3fb93d7f441f736e66166671a036b5ca26f6be82f0e2d3af0 | installer-darwin-arm64 |
| 2692b8e837ce08a2722f64a3f1ebd4d9124913691c3cdbdb5d0f0a22d64af04d | installer-linux-amd64 |
| 5d665178dccdd13fa98bab2422e91f261b3b6f06add5498a333a68c9b89af38f | installer-linux-arm |
| 0fb204055f0154328bc31fb563cfc35c1810826953f9319c513d7e77ee376001 | installer-linux-arm64 |