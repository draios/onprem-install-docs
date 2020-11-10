Release 3.5.1 August 24, 2020
===

Review the full feature release notes here: https://docs.sysdig.com/en/sysdig-on-premises-release-notes.html.

>Note
> 
>Version 3.5.1 includes a fix for vulnerabilities that were detected in version 3.5.0. It is recommended to skip version 3.5.0 and install version 3.5.1 instead. As of this release, all on-premises installs and upgrades include oversight services from Sysdig support.

Upgrade Matrix
---

Sysdig Platform version 3.5.1 has been tested and qualified against the following:

Supported Upgrade From: 3.5.0, 3.2.x, 3.0

### Supported Platforms

| **Platform** | **Version** |
|---|---|
| Vanilla Kubernetes          | 1.13.4, 14.10, 1.15.12, 1.16.13, 1.17.9, 1.18.6 |
| OpenShift                   | 4.4 --> 1.17.1+1aa1c48 |
| GKE                         | 1.14.10-gke.36 |
| EKS                         |v1.17.7-eks-bffbac|
| Rancher                     | v2.3.3|
| IBM                         | Unqualified |
| PKS                         | Unqualified |

### Sysdig Agent Version

Qualified with agent release 10.2.0

### Supported Backend Components

| **Components** | **Kubernetes with Statefulsets** |
|---|---|
| Redis                      | 4.0.12 |
| MySQL                      | 5.6.44, 8.0.16|
| MySQL HA                   | 8.0.16 |
| ElasticSearch              | 5.6.16 |
| Cassandra                  | release_version: 2.1.21 cql_version: 3.2.1 |
| RDS                        | 8.0.16 |
| Postgres (image scanning)  | 12.3 |
| Anchore (image scanning)   | 0.6.1 |
| NATS Exporter              | 0.6.0.1 |
| NATS Streaming             | 0.17.0.1 |
| HA Proxy                   | 1.9.15 |


> Note
>
> MySQL8: You can use MySQL8 for non-HA setups using the flag useMySQL8: true
>
> Postgres: Upgrading to 3.5.0 will also involve an automatic Postgres version upgrade from 10.6.x to 12.x. Depending on your database size, the upgrade could take some time. See [Postgres Version Update v10.x to 12.x](upgrade_notes.md#postgres-version-update-v10x-to-12x) for details.


### Installer binaries sha256sum

| **sha256sum** | **Installer binary ** |
|---|---|
| 66fda0380f36ea11b4b36067e462974aecbcd645665420bb62a6ccb9533ef201 | installer-darwin-amd64 |
| f2d1a783f162a5ba2f7cbad11672d30f8ae5409b350a5b3a6b9dcf2d653265c5 | installer-linux-amd64 |
| 9232c689ba0e62940a1742ee9d204ce684fe01ee041835be75e746a468396321 | installer-windows-amd64.exe |
