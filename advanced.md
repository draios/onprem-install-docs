# Advanced configuration

## SMTP Configs for Email Notifications

https://docs.sysdig.com/en/frequently-used-installer-configurations.html#UUID-32b26a75-cf1c-494b-bb3e-cf9f3607da11_UUID-98c88350-ca7a-685c-1d89-45b3e43d0839

## Configure AWS Credentials Using the Installer

https://docs.sysdig.com/en/frequently-used-installer-configurations.html#UUID-32b26a75-cf1c-494b-bb3e-cf9f3607da11_section-idm23195535090299

## Use hostPath for Static Storage of Sysdig Components

As described in the Installation Storage Requirements, the Installer
assumes usage of a dynamic storage provider (AWS or GKE). In case these are
not used in your environment, add the entries below to the values.yaml to
configure static storage.

Based on the `size` entered in the values.yaml file (small/medium/large), the
Installer assumes a minimum number of replicas and nodes to be provided.
You will enter the names of the nodes on which you will run the Cassandra,
ElasticSearch, mySQL and Postgres components of Sysdig in the values.yaml, as
in the parameters and example below.

### Parameters

`storageClassProvisioner`: hostPath.<br>
`sysdig.cassandra.hostPathNodes`: The number of nodes configured here needs to
be at minimum 1 when configured `size` is `small`, 3 when configured `size` is
`medium` and 6 when configured `size` is large.<br>
`elasticsearch.hostPathNodes`: The number of nodes configured here needs to be
be at minimum 1 when configured `size` is `small`, 3 when configured `size` is
`medium` and 6 when configured `size` is large.<br>
`sysdig.mysql.hostPathNodes`: When sysdig.mysqlHa is configured to true this has
to be at least 3 nodes and when sysdig.mysqlHa is not configured it should be
at least one node.<br>
`sysdig.postgresql.hostPathNodes`: This can be ignored if Sysdig Secure is not
licensed or used on this environment. If Secure is used, then the parameter
should be set to 1, regardless of the environment size setting.<br>

### Example

```yaml
storageClassProvisioner: hostPath
elasticsearch:
  hostPathNodes:
    - my-cool-host1.com
    - my-cool-host2.com
    - my-cool-host3.com
    - my-cool-host4.com
    - my-cool-host5.com
    - my-cool-host6.com
sysdig:
  cassandra:
    hostPathNodes:
      - my-cool-host1.com
      - my-cool-host2.com
      - my-cool-host3.com
      - my-cool-host4.com
      - my-cool-host5.com
      - my-cool-host6.com
  mysql:
    hostPathNodes:
      - my-cool-host1.com
  postgresql:
    hostPathNodes:
      - my-cool-host1.com
```

## Run Only Sysdig Pods on a Node Using Taints and Tolerations

https://docs.sysdig.com/en/frequently-used-installer-configurations.html#UUID-32b26a75-cf1c-494b-bb3e-cf9f3607da11_section-idm4574289599260831641288416009

# Patching Process

https://docs.sysdig.com/en/frequently-used-installer-configurations.html#UUID-32b26a75-cf1c-494b-bb3e-cf9f3607da11_section-5db0e898dc647-idm45530487323952
