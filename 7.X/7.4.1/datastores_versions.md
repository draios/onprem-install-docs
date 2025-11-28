# Supported Datastore Components

This document lists the versions of all backend datastore components included in this Sysdig On-Premises release. These components are deployed as part of the Kubernetes installation using StatefulSets.

## Component Versions

The following table shows the version of each datastore component used in this release:

| **Component** | **Version (Kubernetes with StatefulSets)** |
|---|---|
| Redis                      | 6.2.14 |
| OpenSearch                 | 2.18.0 |
| Cassandra                  | 4.1.8 |
| PostgreSQL                 | 15.8 |
| NATS JetStream             | 2.10.14 |
| HA Proxy                   | 3.2.1 |
| Neo4j                      | 5.26.5 |

## Notes

- These versions are automatically managed by the Sysdig installer
- Component versions may vary depending on your deployment configuration
- For more information about component compatibility, refer to the [official release notes](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/)
