# Advanced Configuration

## Table of Contents  
   * [Upgrade License](#upgrade-license)
   * [SMTP Configs for Email Notifications](#smtp-configs-for-email-notifications)
   * [Configure AWS Credentials Using the Installer](#configure-aws-credentials-using-the-installer)
   * [Use hostPath for Static Storage of Sysdig Components](#use-hostpath-for-static-storage-of-sysdig-components)
     * [Parameters](#parameters)
     * [Example](#example)
   * [Run Only Sysdig Pods on a Node Using Taints and Tolerations](#run-only-sysdig-pods-on-a-node-using-taints-and-tolerations)
   * [Replace a Self-Signed Cert with Custom Cert](#replace-a-self-signed-cert-with-custom-cert)
   * [Optional: Custom Self-Signed Certificate](#optional-custom-self-signed-certificate)
   * [Patching Process](#patching-process)
   
## Upgrade License

On-premises environments may require a license upgrade to renew, extend an expiration date, enable new features, add a service (Sysdig Secure), or change the number of licensed agents.

- set [sysdig.license](configuration_parameters.md#sysdiglicense) in values.yaml
```yaml
sysdig:
  license: XYZ
```
- Rerun Installer

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

If you have a large shared Kubernetes cluster and want to dedicate a few nodes for just the Sysdig backend component installation, you can use the Kubernetes concept of [taints and tolerations](https://kubernetes.io/docs/concepts/scheduling-eviction/taint-and-toleration/).

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

## Replace a Self-Signed Cert with Custom Cert

Installer automatically generates a self-signed certificate during install. To use a custom certificate you would

- Add your cert and key to the /certs directory ex: (server.crt, server.key)
​
- Update values.yaml:

    ```yaml
    sysdig:  
      certificate:    
        crt: certs/server.crt    
        key: certs/server.key
    ```
- Rerun Installer

The [configuration\_parameter.md](configuration_parameters.md#sysdigcertificatecrt) gives full details on `sysdig.certificate.crt` and `sysdig.certificate.key`

## Optional: Custom Self-Signed Certificate

Sysdig Monitor/Cloud/etc uses a self-signed SSL/TLS security certificate, unless a custom certificate is provided.

The example command below creates a custom, unsigned certificate called `MyCert.pem`; the certificate has a private key called `MyCert.key`, and is valid for five years
​
```bash
sudo openssl req -new -x509 -sha256 -days 1825 -nodes -out ./MyCert.pem -keyout ./MyCert.key
```

# Patching Process

Patching can be used to customize or "tweak" the default behavior of the Installer to accommodate the unique requirements of a specific environment. Use patching to modify the parameters that are not exposed by the`values.yaml`. Refer to the `configuration_parameters.md` for more detail about various parameters.  

The most common use case for patching is during updates. When generating the differences between an existing installation and the upgrade, you may see previously customized configurations that the upgrade would overwrite, but that you want to preserve.

### Patching Process

If you have run ` generate diff ` and found a configuration that you need to tweak (e.g. the installer will delete something you want to keep, or you need to add something that isn't there), then follow these general steps:

-   Create an `overlays `directory in the same location as the `values.yaml`.

> **Note**
> This directory, and the patch.yaml you create for it, must be kept. The installer will use it during future upgrades of Sysdig.

-   Create a `.yaml` file to be used for patching. You can name it whatever you want; we will call it patch.yaml for this example.

-   Patch files must include, at a minimum:

```text
    -   `apiVersion`

    -   `kind`

    -   `metadata.name`
```

Then you add the specific configuration required for your needs. See one example below.

You will need this patch definition for every Kubernetes object you want to patch.

-   Run `generate diff `again and check that the outcome will be what you want.

-   When satisfied, complete the update by changing the scripts value to deploy and running the installer. If you want to add another patch, you can either add a separate `.yaml `file or a new YAML document separated by `---`. 

The recommended practice is to use a single patch per Kubernetes object.

### Example

Presume you have the following generated configuration:

```yaml
    apiVersion: v1
    kind: Service
    metadata:
      annotations: {}
      labels:
        app: sysdigcloud
        role: api
      name: sysdigcloud-api
      namespace: sysdigcloud
    spec:
      clusterIP: None
      ports:
      - name: api
        port: 8080
        protocol: TCP
        targetPort: 8080
      selector:
        app: sysdigcloud
        role: api
      sessionAffinity: None
      type: ClusterIP
```

#### To Add to the Generated Configuration

Suppose you want to add an extra label `my-awesome-label: my-awesome-value` to the Service object. Then in the patch.yaml, you would put the following:

```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: sysdigcloud-api
      labels:
        my-awesome-label: my-awesome-value
```

Run the installer again, and the configuration would be as follows:

```yaml
    apiVersion: v1
    kind: Service
    metadata:
      annotations: {}
      labels:
        app: sysdigcloud
        role: api
        my-awesome-label: my-awesome-value
      name: sysdigcloud-api
      namespace: sysdigcloud
    spec:
      clusterIP: None
      ports:
      - name: api
        port: 8080
        protocol: TCP
        targetPort: 8080
      selector:
        app: sysdigcloud
        role: api
      sessionAffinity: None
      type: ClusterIP
```

#### To Remove from the Generated Configuration

Supposed you wanted to remove all the labels. Then in the patch.yaml, you would put the following:

```yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: sysdigcloud-api
      labels:
```

Run the installer again, and the configuration would be as follows:

```yaml
    apiVersion: v1
    kind: Service
    metadata:
      annotations: {}
      name: sysdigcloud-api
      namespace: sysdigcloud
    spec:
      clusterIP: None
      ports:
      - name: api
        port: 8080
        protocol: TCP
        targetPort: 8080
      selector:
        app: sysdigcloud
        role: api
      sessionAffinity: None
      type: ClusterIP
```