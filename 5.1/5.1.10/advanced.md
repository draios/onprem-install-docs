# Advanced Configuration

## Use hostPath for Static Storage of Sysdig Components

As described in the Installation Storage Requirements, the Installer
assumes the usage of a dynamic storage provider (AWS or GKE). In case these are
not used in your environment, add the entries below to the `values.yaml` to
configure static storage.

Based on the `size` entered in the values.yaml file (small/medium/large), the installer assumes a minimum number of replicas and nodes to be provided.
You will enter the names of the nodes on which you will run the Cassandra,
ElasticSearch, MySQL, and Postgres components of Sysdig in the `values.yaml`, as
in the parameters and example below.

### Parameters

- `storageClassProvisioner`: hostPath.
- `sysdig.cassandra.hostPathNodes`: The number of nodes configured here needs to
be at minimum 1 when configured `size` is `small`, 3 when configured `size` is
`medium` and 6 when configured `size` is large.
- `elasticsearch.hostPathNodes`: The number of nodes configured here needs to be
be at minimum 1 when configured `size` is `small`, 3 when configured `size` is
`medium` and 6 when configured `size` is large.
- `sysdig.mysql.hostPathNodes`: When sysdig.mysqlHa is configured to true this has
to be at least 3 nodes and when sysdig.mysqlHa is not configured it should be
at least one node.
- `sysdig.postgresql.hostPathNodes`: This can be ignored if Sysdig Secure is not
licensed or used in this environment. If Secure is used, then the parameter
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


## Installer on EKS

### Create a Cluster

Please do not use `eksctl` 0.10.0 and 0.10.1 as those are known to be defective. For more information, see kubernetes/kubernetes#73906 (comment)
```bash
eksctl create cluster \
   --name=eks-installer1 \
   --node-type=m5.4xlarge \
   --nodes=3 \
   --version 1.14 \
   --region=us-east-1 \
   --vpc-public-subnets=<subnet1,subnet2>
```

### Additional Configuration for the Installer

EKS uses `aws-iam-authenticator` to authorize `kubectl` commands.
aws-iam-authenticator needs aws credentials mounted from **~/.aws** to the installer.
```bash
docker run  \
  -v ~/.aws:/.aws \
  -e HOST_USER=$(id -u) \
  -e KUBECONFIG=/.kube/config \
  -v ~/.kube:/.kube:Z \
  -v $(pwd):/manifests:Z \
  quay.io/sysdig/installer:<InstallerVersion>
```

### Running Airgapped EKS

```bash
EKS=true bash sysdig_installer.tar.gz
```

The above ensures the `~/.aws` directory is correctly mounted for the airgap
installer container.

### Exposing the Sysdig Endpoint

Get the external IP/endpoint for the ingress service.
```bash
kubectl -n <namespace>  get service haproxy-ingress-service
```
In `route53` create an A record with the DNS name pointing to the external IP/endpoint.

### Guidelines

Make sure that subnets have an internet gateway configured and have enough IP addresses.

## Airgapped Installations

### Update the Feeds Database Automatically

Use this procedure to automatically update the feeds database:

1. Download the image file quay.io/sysdig/vuln-feed-database:latest from the Sysdig registry to the jumpbox server and save it locally.
2. (optional) Move the file from the jumpbox server to the customer airgapped environment. 
3. Load the image file and push it to the customer's airgapped image registry.
4. Restart the pod `sysdigcloud-feeds-db`.
5. Restart the `feeds-api` pod.

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

The script can be scheduled using a cron job that runs every day.
```bash
0 8 * * * feeds-database-update.sh >/dev/null 2>&1
```
