Release 6.2.1 May, 2023
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

Note: 6.2.1 release introduces the new ScanningV2 engine, which still does not qualifies for air-gap environments.

Upgrade Matrix
---

Supported Upgrade From: 5.0.X, 5.1.x, 6.0.x, 6.1.x

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.21.14, 1.22.17, 1.23.17, 1.24.12, 1.25.8, 1.26.3 |
| OpenShift                   | 4.10, 4.11, 4.12 |
| GKE                         | v1.24.9-gke.3200 |
| EKS                         | 1.22 |

### Sysdig Agent Version

Qualified with agent release 11.4.1

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 6.2.7 |
| OpenSearch                 | 1.3.9 |
| Cassandra                  | 3.11.14 |
| Postgres                   | 12.13 |
| Anchore (image scanning)   | 0.9.4 |
| NATS Streaming             | 0.24.6 |
| HA Proxy                   | 0.14.2 |


### Checksum for Installer binaries

Current version: 6.2.1-1

| **sha256sum** | **Installer binary** |
|---|---|
| c11909bcface478fd635612fccc754611adc0fdf35f1d32992cb997152f52d29 | installer-darwin-amd64 |
| 18c8395648b1a9dd66aba66547ffc58ab6bffb716789f264811dc086037402df | installer-darwin-arm64 |
| 167505446035a46d1c48e05be50d181d7f83c9b60dc030719023518096653cd0 | installer-linux-amd64 |
| 48b27d1e386c4460f0546b8902c8faa12047479730ec3a01f227cedb660b6ec6 | installer-linux-arm |
| 15aa0e9b0ee66b59dda280944bb93b1d0b757fd340940af9c592c7dd9032b026 | installer-linux-arm64 |

