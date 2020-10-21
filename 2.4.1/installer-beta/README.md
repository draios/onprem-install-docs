# Sysdig onprem configurator.

Configurator is a collection of scripts to automate the deployment of
sysdigcloud.

## Usage

For full usage instructions see [usage.md](docs/usage.md).

### Quickstart

#### Requirements for installation machine

- Network access to Kubernetes cluster
- Docker
- Bash
- [jq](https://stedolan.github.io/jq/)
- Network access to quay.io
- Network and authenticated access to the private registry
- Edited [sysdig-chart/values.yaml](sysdig-chart/values.yaml), with airgap
registry details updated


#### Logging in to quay.io

- Retrieve quay username and password from quaypullsecret, e.g:
```bash
AUTH=$(echo <REPLACE_WITH_quaypullsecret> | base64 --decode | jq -r '.auths."quay.io".auth'| base64 --decode)
QUAY_USERNAME=${AUTH%:*}
QUAY_PASSWORD=${AUTH#*:}
```
- Use QUAY_USERNAME and QUAY_PASSWORD retrieved from previous step to login
to quay
```bash
docker login -u "$QUAY_USERNAME" -p "$QUAY_PASSWORD" quay.io
  ```

#### Quickstart Steps

- Login to quay.io see [Logging in to quay.io](#logging-in-to-quay-io)
- Copy [sysdig-chart/values.yaml](sysdig-chart/values.yaml) to your
working directory, you can do:
```bash
wget \
https://raw.githubusercontent.com/draios/configurator/2.4.1-3/sysdig-chart/values.yaml
```
- Update the `size`, `quaypullsecret`, `storageClassProvisioner`,
`sysdig.license` and `sysdig.dnsName`.  See [full configuration](docs/configuration.md)
 for all possible configuration options.
- Run
```bash
docker run -e HOST_USER=$(id -u) -e KUBECONFIG=/.kube/config \
  -v ~/.kube:/.kube:Z -v $(pwd):/manifests:Z \
  quay.io/sysdig/configurator:2.4.1-3
```

## Development

For development instructions see [development.md](docs/development.md)
