# Command: `update-license`

Prerequisite: `kubectl` version `1.20.0` or greater.

This command performs the minimal changes and restarts to apply a new license.
For more details, see [Upgrade On-Premises License](https://docs.sysdig.com/en/docs/administration/on-premises-deployments/upgrade-an-on-premises-license/).

## Modified Secrets

```sh
sysdigcloud-api-secret
sysdigcloud-collector-secrets
sysdigcloud-worker-secret
sysdigcloud-anchore-secret
```

## Modified ConfigMaps

```sh
sysdigcloud-scanningv2-pkgmeta-api-config
sysdigcloud-scanningv2-vulns-api-config
```

## Restarted Deployments

```sh
sysdigcloud-api
sysdigcloud-collector
sysdigcloud-worker
sysdigcloud-scanningv2-pkgmeta-api
sysdigcloud-scanningv2-vulns-api
sysdigcloud-anchore-core
sysdigcloud-anchore-policy-engine
sysdigcloud-anchore-api
sysdigcloud-anchore-catalog
```
