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
   * [Airgapped installations](#airgapped-installations)
   * [Updating Vulnerability Feed](#updating-vulnerability-feed)

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

## Patching Process

Patching can be used to customize or "tweak" the default behavior of the Installer to accommodate the unique requirements of a specific environment. Use patching to modify the parameters that are not exposed by the`values.yaml`. Refer to the `configuration_parameters.md` for more detail about various parameters.  

The most common use case for patching is during updates. When generating the differences between an existing installation and the upgrade, you may see previously customized configurations that the upgrade would overwrite, but that you want to preserve.

### About Patching Process

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
## Airgapped Installations

### Automatically Updating the Feeds Database in Airgapped Environments
This is a procedure that can be used to automatically update the feeds database:

1. download the image file quay.io/sysdig/vuln-feed-database:latest from Sysdig registry to the jumpbox server and save it locally
2. move the file from the jumpbox server to the customer airgapped environment (optional)
3. load the image file and push it to the customer's airgapped image registry
4. restart the pod sysdigcloud-feeds-db
5. restart the pod feeds-api

Finally, steps 1 to 5 will be performed periodically once a day.

This is an example script that contains all the steps:
```bash
#!/bin/bash
QUAY_USERNAME="<change_me>"
QUAY_PASSWORD="<change_me>"

# Download image
docker login quay.io/sysdig -u ${QUAY_USERNAME} -p ${QUAY_PASSWORD}
docker image pull quay.io/sysdig/vuln-feed-database:latest
# Save image
docker image save quay.io/sysdig/vuln-feed-database:latest -o vuln-feed-database.tar
# Optionally move image
mv vuln-feed-database.tar /var/shared-folder
# Load image remotely
ssh -t user@airgapped-host "docker image load -i /var/shared-folder/vuln-feed-database.tar"
# Push image remotely
ssh -t user@airgapped-host "docker tag vuln-feed-database:latest airgapped-registry/vuln-feed-database:latest"
ssh -t user@airgapped-host "docker image push airgapped-registry/vuln-feed-database:latest"
# Restart database pod
ssh -t user@airgapped-host "kubectl -n sysdigcloud scale deploy sysdigcloud-feeds-db --replicas=0"
ssh -t user@airgapped-host "kubectl -n sysdigcloud scale deploy sysdigcloud-feeds-db --replicas=1"
# Restart feeds-api pod
ssh -t user@airgapped-host "kubectl -n sysdigcloud scale deploy sysdigcloud-feeds-api --replicas=0"
ssh -t user@airgapped-host "kubectl -n sysdigcloud scale deploy sysdigcloud-feeds-api --replicas=1"
```

The script can be scheduled using a cron job that run every day
```bash
0 8 * * * feeds-database-update.sh >/dev/null 2>&1
```

### Updating Vulnerability Feed

> **NOTE:**
>
> Sysdig Secure users who install in an airgapped environment do not have internet access to the continuous checks of vulnerability databases that are used in image scanning. (See also: [/document/preview/117822\#UUIDc24a6ed8cdde754219092e4b32b6fd79](file:////document/preview/117822#UUIDc24a6ed8cdde754219092e4b32b6fd79).)How Sysdig Image Scanning Works

As of **installer version 3.2.0-9**, airgapped environments can also receive periodic vulnerability database updates.

When you install with the \"`airgapped_`\" parameters enabled (see [/document/preview/206196\#UUIDc198e7424136aa205f91d28f1495bfaf](file:////document/preview/206196#UUIDc198e7424136aa205f91d28f1495bfaf) instructions), the installer will automatically push the latest vulnerability database to your environment. Follow the steps below to reinstall/refresh the vuln db, or use the script and chron job to schedule automated updates (daily, weekly, etc.).Full Airgap Install

To automatically update the vulnerability database, you can:

1. Download the image file [quay.io/sysdig/vuln-feed-database:latest](https://quay.io/sysdig/vulnfeeddatabase:latest) from the Sysdig registry to the jump box server and save it locally.
2. Move the file from the jump box server to the airgapped environment (if needed)
3. Load the image file and push it to the airgapped image registry.
4. Restart the pod `sysdigcloud-feeds-db`
5. Restart the pod `feeds-api`

The following script (`feeds_database_update.sh`) performs the five steps:

```bash
    #!/bin/bash
    QUAY_USERNAME="<change_me>"
    QUAY_PASSWORD="<change_me>"

    # Download image
    docker login quay.io/sysdig -u ${QUAY_USERNAME} -p ${QUAY_PASSWORD}
    docker image pull quay.io/sysdig/vuln-feed-database:latest
    # Save image
    docker image save quay.io/sysdig/vuln-feed-database:latest -o vuln-feed-database.tar
    # Optionally move image
    mv vuln-feed-database.tar /var/shared-folder
    # Load image remotely
    ssh -t user@airgapped-host "docker image load -i /var/shared-folder/vuln-feed-database.tar"
    # Push image remotely
    ssh -t user@airgapped-host "docker tag vuln-feed-database:latest airgapped-registry/vuln-feed-database:latest"
    ssh -t user@airgapped-host "docker image push airgapped-registry/vuln-feed-database:latest"
    # Restart database pod
    ssh -t user@airgapped-host "kubectl -n sysdigcloud scale deploy sysdigcloud-feeds-db --replicas=0"
    ssh -t user@airgapped-host "kubectl -n sysdigcloud scale deploy sysdigcloud-feeds-db --replicas=1"
    # Restart feeds-api pod
    ssh -t user@airgapped-host "kubectl -n sysdigcloud scale deploy sysdigcloud-feeds-api --replicas=0"
    ssh -t user@airgapped-host "kubectl -n sysdigcloud scale deploy sysdigcloud-feeds-api --replicas=1"
```
Schedule a chron job to run the script on a chosen schedule (e.g. every day):

    0 8 * * * feeds-database-update.sh >/dev/null 2>&1

# Output

A successful installation should display output in the terminal such as:

    All Pods Ready.....Continuing
    Congratulations, your Sysdig installation was successful!
    You can now login to the UI at "https://awesome-domain.com:443" with:

    username: "configured-username@awesome-domain.com"
    password: "awesome-password"

There will also be a generated directory containing various Kubernetes configuration `yaml` files which were applied by installer against your cluster. It is not necessary to keep the generated directory, as the installer can regenerate consistently with the same `values.yaml` file.
