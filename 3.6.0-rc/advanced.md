# Advanced Configuration

## Table of Contents  
   * [SMTP Configs for Email Notifications](#smtp-configs-for-email-notifications)
   * [Configure AWS Credentials Using the Installer](#configure-aws-credentials-using-the-installer)
   * [Use hostPath for Static Storage of Sysdig Components](#use-hostpath-for-static-storage-of-sysdig-components)
     * [Parameters](#parameters)
     * [Example](#example)
   * [Run Only Sysdig Pods on a Node Using Taints and Tolerations](#run-only-sysdig-pods-on-a-node-using-taints-and-tolerations)
   * [Patching Process](#patching-process)

## SMTP Configs for Email Notifications

The available fields for SMTP configuration are documented in the [configuration_parameters.md](configuration_parameters.md). Each includes `SMTP` in its name. 
For example:    

```yaml
sysdig:
  smtpServer: smtp.sendgrid.net
  smtpServerPort: 587
  #User,Password can be empty if the server does not require authentication
  smtpUser: apikey
  smtpPassword: XY.abcdefghijk
  smtpProtocolTLS: true
  smtpProtocolSSL: false
  #Optional Email Header
  smtpFromAddress: sysdig@mycompany.com
```
To configure email settings to be used for a notification channel, copy the parameters and appropriate values into your `values.yaml`               

## Configure AWS Credentials Using the Installer

The available fields for AWS credentials are documented in the [configuration_parameters.md.](configuration_parameters.md#sysdigaccesskey) 

```yaml
sysdig:      
  accessKey: my_awesome_aws_access_key
  secretKey: my_super_secret_secret_key
```

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

If you have a large shared Kubernetes cluster and want to dedicate a few nodes for just the Sysdig backend component installation, you can use the Kubernetes concept of [taints and tolerations](https://kubernetes.io/docs/concepts/configuration/taintandtoleration/).

The basic process is:

1. Assign labels and taints to the relevant nodes.
2. Review the sample [node-labels-and-taints values.yaml](examples/node-labels-and-taints/values.yaml) in the Sysdig github repo.
3. Copy that section to your own `values.yaml` file and edit with labels and taints you assigned.
    
Example from the sample file:

```yaml
# To make the ‘tolerations’ code sample below functional, assign nodes the taint 
# dedicated=sysdig:NoSchedule. E.g:
# kubectl taint my-awesome-node01 dedicated=sysdig:NoSchedule
  tolerations:
    - key: "dedicated"
      operator: "Equal"
      value: sysdig
      effect: "NoSchedule"
# To make the Label code sample below functional, assign nodes the label 
# role=sysdig. 
# e.g: kubectl label nodes my-awesome-node01 role=sysdig
  nodeaffinityLabel:
    key: role
    value: sysdig
```

# Patching Process

https://docs.sysdig.com/en/frequently-used-installer-configurations.html#UUID-32b26a75-cf1c-494b-bb3e-cf9f3607da11_section-5db0e898dc647-idm45530487323952
