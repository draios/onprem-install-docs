   * [Installer](#installer)
   * [Installation Overview](#installation-overview)
      * [Install vs Upgrade](#Install-vs-Upgrade)
      * [Prerequisites](#prerequisites)
   * [Quickstart Install](#quickstart-install)
   * [Airgapped Installation Options](#airgapped-installation-options)
      * [Airgapped with Multi-Homed Installation Machine](#airgapped-with-multi-homed-installation-machine)
      * [Full Airgap Install](#full-airgap-install)
   * [Upgrades](upgrade.md)
   * [Permissions](#permissions)
   * [Additional Installer Resources](#Additional-Installer-Resources)
      * [Configuration Parameters and Examples](configuration_parameters.md)
      * [Advanced Configuration](advanced.md)
      * [Example values.yaml](examples/README.md)

# Installer

The Sysdig Installer tool is a binary containing a collection of scripts that help automate the on-premises deployment of the Sysdig platform (Sysdig Monitor and/or Sysdig Secure), for environments using Kubernetes or OpenShift. Use the Installer to install or upgrade your Sysdig platform. It is recommended as a replacement for the earlier Kubernetes manual installation and upgrade procedures.

# Installation Overview

To install, you will download the installer binary and a values.yaml file, provide a few basic parameters, and launch the Installer. In a normal installation, the rest is automatically configured and deployed.

You can perform a quick install if your environment has access to the internet, or a partial or full airgapped installation, as needed. Each is described below.

## Install vs Upgrade

With Sysdig Platform 3.5.0, the installer has been simplified from previous versions. Upgrade differs from Install in that you run an `installer diff` to discover the differences between the old and new versions and then `installer deploy` for the new version.

If you are installing the Sysdig Platform for the first time, ignore the *ForUpgradeOnly* step in the process. If you are upgrading, check the [Upgrade notes](upgrade.md) before you begin.

## Prerequisites

### Requirements for Installation Machine with Internet Access

- kubectl or oc binary
- A domain name you are in control of.

### Additional Requirements for Airgapped Environments

- Edited sysdig-chart/values.yaml, with airgap registry details updated
- Network and authenticated access to the private registry
- Network access to quay.io

### Access Requirements

- Sysdig license key (Monitor and/or Secure)
- Quay pull secret

### Storage Requirements

You may use dynamic or static storage on a variety of platforms to store the Sysdig platform components (stateful sets). Different configuration parameters and values are used during the install, depending on which scenario you have.

**Use Case 1: Default, undefined (AWS/GKE)**

If you will use dynamic storage on AWS or GKE and haven't configured any storage class there yet, then the Quick Install streamlines the process for you.

-   `storageclassProvision``er:` Enter `aws` or `gke`. The installer will create the appropriate storage class and then use it for all the Sysdig platform stateful sets.

-   `storageclassName`: Leave empty.

**Use Case 2: Dynamic, predefined**

It is also possible that you are using dynamic storage but have already created storage classes there. This dynamic storage could be AWS, GKE, or any other functioning dynamic storage you use.  In this case, you would enter: 

-   `storageclassProvisioner`: Leave empty; anything put here would be ignored.

-   `storageclass``Name`: Provide the name of the pre-configured storage class you want to use. The installer will use this storage class for all the Sysdig platform stateful sets.

**Use Case 3: Static Storage **

In cases where dynamic storage is not available, you can use static storage for the Sysdig stateful sets. In this case, you would use:

-   `storageclassProvisioner`: Enter `hostpath`, then define the nodes for the four main Sysdig components: ElasticSearch, Cassandra, MySQL, and Postgres.storageclassProvisioner

-   See [Advanced Configurations](advanced.md#use-hostpath-for-static-storage-of-sysdig-components) for details.

# Quickstart Install

This install assumes the Kubernetes cluster has network access to pull images from quay.io.

1.  Have your Sysdig Technical Account Manager download the installer binary that matches your OS from the the  page [TODO: Donald].

2.  **For Upgrades Only:** Copy the current version of [values.yaml](values.yaml) to your working directory.\]

-   ./installer-image import -n sysdig --certs-directory certs -o values.yaml

    > **Note**
    >
    > If you will be editing for an OpenShift installation and want to review a sample, see openshift-with-hostpath values.yaml. .

3.  Edit the following values:

    -   **size:** Specifies the size of the cluster. Size defines CPU, Memory, Disk, and Replicas. Valid options are: small, medium and large

    -   **quaypullsecret:** quay.io provided with your Sysdig purchase confirmation mail

    -   **storageClassProvisioner:** Review Storage Requirements, above.

    <!-- -->

    -   If you have the default use case, enter `aws` or `gke` in the `storageClassProvisioner` field. Otherwise, refer to Use Case 2 or 3.

    <!-- -->

    -   **sysdig.license:** Sysdig license key provided with your Sysdig purchase confirmation mail

    -   **sysdig.dnsname:** The domain name the Sysdig APIs will be served on. Note that the master node may not be used as the DNS name when using hostNetwork mode.

    -   **sysdig.collector.dnsName: (OpenShift installs only) **Domain name the Sysdig collector will be served on. When not configured it defaults to whatever is configured for sysdig.dnsName. Note that the master node may not be used as the DNS name when using hostNetwork mode.

    -   **deployment**: **(OpenShift installs only)** Add `deployment: openshift` to the root of the `values.yaml` file.

    -   **sysdig.ingressNetworking:** The networking construct used to expose the Sysdig API and collector.Options are:

        -   **hostnetwork:** sets the hostnetworking in the ingress daemonset and opens host ports for api and collector. This does not create a Kubernetes service.

        -   **loadbalancer:** creates a service of type loadbalancer and expects that your Kubernetes cluster can provision a load balancer with your cloud provider.

        -   **nodeport:** creates a service of type nodeport.The node ports can be customized with:

        <!-- -->

        -   `sysdig.ingressNetworkingInsecureApiNodePort`

            `sysdig.ingressNetworkingApiNodePort`

            `sysdig.ingressNetworkingColle``ctorNodePort`

            When not configured, `sysdig.ingressNetworking` defaults to `hostnetwork`.

    > **Note**
    >
    > If doing an airgapped install , you would also edit the following values:


    -   **airgapped\_registry\_name:** The URL of the airgapped (internal) docker registry. This URL is used for installations where the Kubernetes cluster can not pull images directly from Quay

    -   **airgapped\_repository\_prefix:** This defines custom repository prefix for airgapped\_registry. Tags and pushes images as `airgapped_registry_name/airgapped_repository_prefix``/image_name:tag`

    -   **airgapped\_registry\_password:** The password for the configured airgapped\_registry\_username. Ignore this parameter if the registry does not require authentication.

    -   **airgapped\_registry\_username:** The username for the configured airgapped\_registry\_name. Ignore this parameter if the registry does not require authentication.

-   **[For Upgrades Only]** Generate and review the diff of changes the installer is about to introduce:

        ./installer diff

    This will generate the differences between the installed environment and the upgrade version. The changes will be displayed in your terminal.

    If you want to override a change, based on your environment's custom settings, then contact Sysdig Support for assistance.

- Run the installer:

    ```bash
    ./installer deploy
    ``` 

- See [*Output*](#output) (below) to finish.

    > **Note**
    >
    > Save the `values.yaml `file in a secure location; it will be used for future upgrades.
    >
    > There will also be a generated directory containing various Kubernetes configuration `yaml` files that were applied by the Installer against your cluster. It is not necessary to keep the generated directory, as the Installer can regenerate it consistently with the same `values.yaml `file.

# Airgapped Installation Options

The Installer can be used to install in airgapped environments, either with
a multi-homed installation machine that has internet access, or in an
environment with no internet access.

## Airgapped with Multi-Homed Installation Machine

This assumes a private docker registry is used and the installation machine has
network access to pull from quay.io and push images to the private registry.

The Prerequisites and workflow are the same as in the Quickstart Install, with
the following exceptions:

- In step 2, add the airgap registry information.
- After step 3, make the installer push sysdig images to the airgapped registry by running:
```bash
./installer airgap
```
  That will pull all the images into `images_archive` directory as `tar` files
  and push them to the airgapped registry
- Run the Installer.
-   If you are upgrading, run the diff as directed in Step 4.
```bash
./installer deploy
```

## Full Airgap Install

This assumes a private docker registry is used and the installation machine
does not have network access to pull from quay.io, but can push images to the
private registry.

In this situation, a machine with network access (called the “jump machine”)
will pull an image containing a self-extracting tarball which can be copied to
the installation machine.

### Access Requirements
-   Sysdig license key (Monitor and/or Secure) 
-   Quay pull secret
-   Anchore license file (if Sysdig Secure is licensed)

### Requirements for jump machine

- Network access to quay.io
- Docker
- jq

### Requirements for installation machine

- Network access to Kubernetes cluster
- Docker
- Network and authenticated access to the private registry
- Edited sysdig-chart/values.yaml, with airgap registry details updated
- **Host Disk Space Requirements:** `/tmp `\> 4 GB; directory from which the installer is run \>8GB; and `/var/lib/docker `\> 4GB.

    > **NOTE:** 
    >
    >The environment variable `TMPDIR` can be used to override the` /tmp` directory.

### Docker Log In to quay.io

Retrieve Quay username and password from Quay pull secret and login using credentials.
   
```bash
AUTH=$(echo REPLACE_WITH_quaypullsecret | base64 --decode | jq -r '.auths."quay.io".auth'| base64 --decode)
QUAY_USERNAME=${AUTH%:*}
QUAY_PASSWORD=${AUTH#*:}
docker login -u "$QUAY_USERNAME" -p "$QUAY_PASSWORD" quay.io 
```

### Workflow

#### On the Jump Machine

- Follow the Docker Log In to quay.io steps, above.
- Pull the image containing the self-extracting tar:
  ```bash
  docker pull quay.io/sysdig/installer:3.6.0-rc-uber
  ```
- Extract the tarball:
  ```bash
  docker create --name uber_image quay.io/sysdig/installer:3.6.0-rc-uber
  docker cp uber_image:/sysdig_installer.tar.gz .
  docker rm uber_image
  ```
- Copy the tarball to the installation machine.

#### On the Installation Machine:

- Copy the current version sysdig-chart/values.yaml to your working directory.
  ```bash
  wget https://github.com/draios/onprem-install-docs/blob/main/3.6.0-rc/values.yaml
  ```
- Edit the following values:

  - [`size`](configuration_parameters.md#size): Specifies the size of the cluster. Size
    defines CPU, Memory, Disk, and Replicas. Valid options are: small, medium and
    large
  - [`quaypullsecret`](configuration_parameters.md#quaypullsecret): quay.io provided with
    your Sysdig purchase confirmation mail
  - [`storageClassProvider`](configuration_parameters.md#storageClassProvider): Review Storage Requirements, above. If you have the default use case, enter `aws` or `gke` in the `storageClassProvisioner` field. Otherwise, refer to Use Case 2 or 3.
  - [`sysdig.license`](configuration_parameters.md#sysdiglicense): Sysdig license key
    provided with your Sysdig purchase confirmation mail
  - [`sysdig.dnsName`](configuration_parameters.md#sysdigdnsName): The domain name the Sysdig APIs will be served on. Note that the master node may not be used as the DNS name when using hostNetwork mode.
  - [`sysdig.collector.dnsName`](configuration_parameters.md#sysdigcollectordnsName):
    **(OpenShift installs only)** Domain name the Sysdig collector will be served on. When not configured it defaults to whatever is configured for sysdig.dnsName. Note that the master node may not be used as the DNS name when using hostNetwork mode.
  - [`deployment`](configuration_parameters.md#deployment): **(OpenShift installs only)** Add `deployment: openshift` to the root of the `values.yaml` file.
  - [`sysdig.ingressNetworking`](configuration_parameters.md#sysdigingressnetworking):
    The networking construct used to expose the Sysdig API and collector. Options
    are:
    - hostnetwork: sets the hostnetworking in the ingress daemonset and opens
      host ports for api and collector. This does not create a Kubernetes service.
    - loadbalancer: creates a service of type loadbalancer and expects that
      your Kubernetes cluster can provision a load balancer with your cloud provider.
    - nodeport: creates a service of type nodeport. The node ports can be
      customized with:
      ```yaml
      sysdig:
        ingressNetworkingInsecureApiNodePort: 30001
        ingressNetworkingApiNodePort: 30002
        ingressNetworkingCollectorNodePort: 30002
      ```
  - [`airgapped_registry_name`](configuration_parameters.md#airgapped_registry_name):
    The URL of the airgapped (internal) docker registry. This URL is used for
    installations where the Kubernetes cluster can not pull images directly from
    Quay.
  - [`airgapped_repository_prefix`](configuration_parameters.md#airgapped_repository_prefix):
      This defines custom repository prefix for airgapped_registry.
      Tags and pushes images as airgapped_registry_name/airgapped_repository_prefix/image_name:tag
  - [`airgapped_registry_password`](configuration_parameters.md#airgapped_registry_password):
    The password for the configured airgapped_registry_username. Ignore this
    parameter if the registry does not require authentication.
  - [`airgapped_registry_username`](configuration_parameters.md#airgapped_registry_username):
    The username for the configured airgapped_registry_name. Ignore this
    parameter if the registry does not require authentication.

- Copy the tarball file to the directory where you have your values.yaml file.
- Run:
```bash
installer airgap --tar-file sysdig_installer.tar.gz
```

> **Note:** 
>
>The above step will extract the images into `images_archive` directory relative to where the installer was run and push the images to the airgapped_registry

-  **[For Upgrades Only]** Generate and review the diff of changes the installer is about to introduce:

    ```bash
    ./installer diff
    ```

    This will generate the differences between the installed environment and the upgrade version. The changes will be displayed in your terminal.

    If you want to override a change, based on your environment's custom settings, then contact Sysdig Support for assistance.

- Run the Installer:
  ```bash
  ./installer deploy
  ```
- On successful run of Installer towards the end of your terminal you should
  see the below:

  ```
  All Pods Ready.....Continuing
  Congratulations, your Sysdig installation was successful!
  You can now login to the UI at "https://awesome-domain.com:443" with:

  username: "configured-username@awesome-domain.com"
  password: "awesome-password"
  ```

> **NOTE**: 
>
> Save the values.yaml file in a secure location; it will be used for future upgrades. 
>
> There will also be a generated directory containing various Kubernetes configuration yaml files which were applied by Installer against
your cluster. It is not necessary to keep the generated directory, as the Installer can regenerate is consistently with the same values.yaml file.

### Updating Vulnerability Feed in Airgapped Environments

> **NOTE:** 
>
> Sysdig Secure users who install in an airgapped environment do not have internet access to the continuous checks of vulnerability databases that are used in image scanning. (See also: [/document/preview/117822\#UUIDc24a6ed8cdde754219092e4b32b6fd79](file:////document/preview/117822#UUIDc24a6ed8cdde754219092e4b32b6fd79).)How Sysdig Image Scanning Works

As of **installer version 3.2.0-9**, airgapped environments can also receive periodic vulnerability database updates.

When you install with the \"`airgapped_`\" parameters enabled (see [/document/preview/206196\#UUIDc198e7424136aa205f91d28f1495bfaf](file:////document/preview/206196#UUIDc198e7424136aa205f91d28f1495bfaf) instructions), the installer will automatically push the latest vulnerability database to your environment. Follow the steps below to reinstall/refresh the vuln db, or use the script and chron job to schedule automated updates (daily, weekly, etc.).Full Airgap Install

To automatically update the vulnerability database, you can:

- Download the image file [quay.io/sysdig/vuln-feed-database:latest](https://quay.io/sysdig/vulnfeeddatabase:latest) from the Sysdig registry to the jump box server and save it locally.
- Move the file from the jump box server to the airgapped environment (if needed)
- Load the image file and push it to the airgapped image registry.
- Restart the pod `sysdigcloud-feeds-db`
- Restart the pod `feeds-api`

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

# Configuration Parameters and Examples

For the full dictionary of configuration parameters, see:
[configuration_parameters.md](configuration_parameters.md)

# Permissions

## General
* CRU on the sysdig namespace
* CRU on StorageClass (only Read is required if the storageClass already exists)
* CRUD on Secrets/ServiceAccount/ConfigMap/Deployment/CronJob/Job/StatefulSet/Service/DaemonSet in the sysdig namespace.
* CRUD on role/rolebinding in sysdig namespace (if sysdig ingress controller is deployed)
* CRU on the ingress-controller(this is the name of the object) ClusterRole/ClusterRoleBinding (if sysdig ingress controller is deployed)
* Get Nodes (for validations).

## MultiAZ enabled
* CRU on the node-labels-to-files(this is the name of the object) ClusterRole/ClusterRoleBinding (for multi-AZ deployments)

## HostPath
* CRU on PV
* CRU on PVC in sysdig namespace

## Openshift
* CRUD on route in the sysdig namespace
* CRUD on openshift SCC in the sysdig namespace

## Network policies enabled
* CRUD on networkpolicies in sysdig namespace (if networkpolicies are enabled, this is an alpha feature customers should not enable it)

# Output

A successful installation should display output in the terminal such as:

    All Pods Ready.....Continuing
    Congratulations, your Sysdig installation was successful!
    You can now login to the UI at "https://awesome-domain.com:443" with:

    username: "configured-username@awesome-domain.com"
    password: "awesome-password"

There will also be a generated directory containing various Kubernetes configuration `yaml` files which were applied by installer against your cluster. It is not necessary to keep the generated directory, as the installer can regenerate consistently with the same `values.yaml` file.

