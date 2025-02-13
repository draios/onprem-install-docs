<!-- Space: IONP -->
<!-- Parent: Installer -->
<!-- Parent: Git Synced Docs -->
<!-- Title: New Configuration Parameters -->
<!-- Layout: plain -->

# New Configuration Parameters

<br />

# global

## **global**

**Required**: `true`<br />
**Description**: `global` is the standard stanza used by Helm for shared configuration. See [this page](https://helm.sh/docs/chart_template_guide/subcharts_and_globals/#global-chart-values)<br />
**Default**: <br />
**Options**: <br />
**Example**:

```yaml
global:
  foo: bar
```

## **global.apps**

**Required**: `false`<br />
**Description**: Specifies the Sysdig Platform components to be installed.<br />
Combine multiple components by space separating them. Specify at least one
app, for example, `monitor`.<br />
**Options**: `monitor|monitor secure`<br />
**Default**: `monitor secure`<br />
**Example**:

```yaml
global:
  apps: monitor secure
```

## **global.airgappedRegistryName**

**Required**: `false`<br />
**Description**: The URL of the airgapped (internal) docker registry. This URL
is used for installations where the Kubernetes cluster can not pull images
directly from Quay. See [airgap instructions
multi-homed](../README.md#airgapped-with-multi-homed-installation-machine)
and [full airgap instructions](../README.md#full-airgap-install) for more
details.<br />
**Default**:<br />
**Options**:<br />
**Example**:

```yaml
global:
  airgappedRegistryName: my-awesome-domain.docker.io
```

## **global.airgappedRepositoryPrefix**

**Required**: `false`<br />
**Description**: This defines custom repository prefix for airgappedRegistryName.
Tags and pushes images as `airgappedRegistryName/airgappedRepositoryPrefix/image_name:tag`<br />
**Options**:<br />
**Default**: sysdig<br />
**Example**:

```yaml
global:
  airgappedRepositoryPrefix: foo/bar
```

## **global.clusterDomain**

**Required**: `false`<br />
**Description**: Domain of the kubernetes cluster.<br />
**Options**:<br />
**Default**: `cluster.local`<br />
**Example**:

```yaml
global:
  clusterDomain: cluster.local
```

## **global.namespace**

**Required**: `false`<br />
**Description**: Kubernetes namespace to deploy Sysdig Platform to.<br />
**Options**:<br />
**Default**: `sysdig`<br />
**Example**:

```yaml
global:
  namespace: sysdig
```

## **global.cloudProvider.name**

**Required**: `false`<br />
**Description**: The name of the cloud provider Sysdig Platform will run on.<br />
**Options**: `aws|gcp`<br />
**Default**:<br />
**Example**:

```yaml
global:
  cloudProvider:
    name: aws
```

## **global.cloudProvider.isMultiAZ**

**Required**: `false`<br />
**Description**: Specifies whether the underlying Kubernetes cluster is
deployed in multiple availability zones. The parameter requires
[`global.cloudProvider.name`](#globalcloudprovidername) to be configured. <br />
If enabled, all of the datastores will be deployed with `podAntiAffinity` on the zone label against other pods of the same statefulset.
If kubernetesServerVersion > 1.19, Cassandra will be deployed with `topologySpreadConstraints` instead of `podAntiAffinity`.
**Options**: `true|false`<br />
**Default**: `false`<br />
**Example**:

```yaml
global:
  cloudProvider:
    isMultiAZ: false
```

## **global.cloudProvider.region**

**Required**: `false`<br />
**Description**: The cloud provider region the underlying Kubernetes Cluster
runs on. This parameter is required if
[`global.cloudProvider.name`](#globalcloudprovidername) is configured.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
global:
  cloudProvider:
    region: us-east-1
```

## **global.prometheus.enabled**

**Required**: `false`<br />
**Description**: Enables Prometheus services.<br />
**Options**: `true|false`<br />
**Default**: `true`<br />
**Example**:

```yaml
global:
  prometheus:
    enabled: true
```

## **global.tolerations**

**Required**: `false`<br />
**Description**:
[Toleration](https://kubernetes.io/docs/concepts/configuration/taint-and-toleration/)
that will be created on Sysdig platform pods, this can be combined with
[nodeaffinityLabel.key](#nodeaffinitylabelkey) and
[nodeaffinityLabel.value](#nodeaffinitylabelvalue) to ensure only Sysdig
Platform pods run on particular nodes<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
global:
  tolerations:
    - key: "dedicated"
      operator: "Equal"
      value: sysdig
      effect: "NoSchedule"
```

## **global.nodeaffinityLabel.key**

**Required**: `false`<br />
**Description**: The key of the label that is used to configure the nodes that the
Sysdig Platform pods are expected to run on. The nodes are expected to have
been labeled with the key.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
global:
  nodeaffinityLabel:
    key: instancegroup
```

## **global.nodeaffinityLabel.value**

**Required**: `false`<br />
**Description**: The value of the label that is used to configure the nodes
that the Sysdig Platform pods are expected to run on. The nodes are expected
to have been labeled with the value of
[`global.nodeaffinityLabel.key`](#globalnodeaffinitylabelkey), and is required if
[`global.nodeaffinityLabel.key`](#globalnodeaffinitylabelkey) is configured.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
global:
  nodeaffinityLabel:
    value: sysdig
```

## **global.dnsName**

**Required**: `true`<br />
**Description**: The domain name the Sysdig APIs will be served on.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
global:
  dnsName: my-awesome-domain-name.com
```

## **global.deployment**

**Required**: `false`<br />
**Description**: The name of the Kubernetes installation.<br />
**Options**: `iks|kubernetes|openshift|goldman`<br />
**Default**: `kubernetes`<br />
**Example**:

```yaml
global:
  deployment: kubernetes
```

## **global.ingressClassName**

**Required**: `false`<br />
**Description**: Ingress class name to assign on generated `Ingress` resources. This is useful in cases where the value of [`ingressNetworking`](#sysdigingressnetworking) is set to `external` and the targeted Ingress controller has a class name which is different from the default.

**Options**: <br />

**Default**: `haproxy`
**Example**:

```yaml
global:
  ingressClassName: haproxy
```

## **global.monitorRegistryName**

**Required**: `false`<br />
**Description**: One of the many options to customize the "registry" part of the `image`.

**Options**: <br />

**Default**: ``
**Example**:

```yaml
global:
  monitorRegistryName: foo
```

## **global.monitorRepositoryPrefix**

**Required**: `false`<br />
**Description**: One of the many options to customize the "prefix" part of the `image`. 

**Options**: <br />

**Default**: ``
**Example**:

```yaml
global:
  monitorRepositoryPrefix: bar
```

## **global.monitorVersion**

**Required**: `false`<br />
**Description**: The docker image tag of the Sysdig Monitor. **Do not modify
this unless you know what you are doing as modifying it could have unintended
consequences**<br />
**Options**:<br />
**Default**: TBD<br />
**Example**:

```yaml
global:
  monitorVersion: 6.12.0
```

## **global.size**

**Required**: `true`<br />
**Description**: Specifies the size of the cluster. Size defines CPU, Memory,
Disk, and Replicas.<br />
**Options**: `small|medium|large`<br />
**Default**:<br />
**Example**:

```yaml
global:
  size: medium
```

## **global.redis**

**Required**: `???`<br />
**Description**: A new stanza for the new Redis lookup function in the helm-template-library. Additional documentation is WIP.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
global:
  redis:
    redisInstance0:
    redisInstance1:
```

## **global.redis**

**Required**: `???`<br />
**Description**: A new stanza for the new Redis lookup function in the helm-template-library. Additional documentation is WIP.<br />
**Options**:<br />
**Default**:<br />
**Example**:

```yaml
global:
  redis:
    redisInstance0:
    redisInstance1:
```

## **global.certificate.generate**

**Required**: `false`<br />
**Description**: Determines if Installer should generate self-signed
certificates for the domain configured in `global.dnsName`.<br />
**Options**: `true|false`<br />
**Default**: `true`<br />
**Example**:

```yaml
global:
  certificate:
    generate: true
```

## **global.certificate.crt**

**Required**: `false`<br />
**Description**: Path(the path must be in same directory as `values.yaml` file
and must be relative to `values.yaml`) to user provided certificate that will
be used in serving the Sysdig api, if `global.certificate.generate` is set to
`false` this has to be configured. The certificate common name or subject
altername name must match configured `global.dnsName`.<br />
**Options**:<br />
**Default**: `true`<br />
**Example**:

```yaml
global:
  certificate:
    crt: certs/server.crt
```

## **global.certificate.key**

**Required**: `false`<br />
**Description**: Path(the path must be in same directory as `values.yaml` file
and must be relative to `values.yaml`) to user provided key that will be used
in serving the sysdig api, if `global.certificate.generate` is set to `false`
this has to be configured. The key must match the certificate in
`global.certificate.crt`.<br />
**Options**:<br />
**Default**: `true`<br />
**Example**:

```yaml
global:
  certificate:
    key: certs/server.key
```

## **global.certificate.customCA**

**Required**: `false`<br />
**Description**:
The Sysdig platform may sometimes open connections over SSL to certain external services, including:

- LDAP over SSL
- SAML over SSL
- OpenID Connect over SSL
- HTTPS Proxies
- SMTPS SMTP over SSL<br />

If the signing authorities for the certificates presented by these services are not well-known to the Sysdig Platform
(e.g., if you maintain your own Certificate Authority), they are not trusted by default.

To allow the Sysdig platform to trust these certificates, use this configuration to upload one or more
PEM-format CA certificates. You must ensure you've uploaded all certificates in the CA approval chain to the root CA.

This configuration when set expects certificates with .crt, .pem or .p12 extensions under certs/custom-java-certs/
in the same level as `values.yaml`.<br />

**Options**: `true|false`<br />
**Default**: false<br />
**Example**:

```bash
#In the example directory structure below, certificate1.crt and certificate2.crt will be added to the trusted list.
# certificate3.p12 will be loaded to the keystore together with it's private key.
bash-5.0$ find certs values.yaml
certs
certs/custom-java-certs
certs/custom-java-certs/certificate1.crt
certs/custom-java-certs/certificate2.crt
certs/custom-java-certs/certificate3.p12
certs/custom-java-certs/certificate3.p12.passwd

values.yaml
```

```yaml
global:
  certificate:
    customCA: true
```


# promqlator

## **promqlator.replicaCount**

**Required**: `false`<br />
**Description**: Number of Promqlator services replicas.<br />
**Options**:<br />
**Default**:<br />

| cluster-size | count |
| ------------ | ----- |
| small        | 1     |
| medium       | 3     |
| large        | 5     |

**Example**:

```yaml
promqlator:
  replicaCount: 3
```

## **promqlator.promqlatorVersion**

**Required**: `false`<br />
**Description**: Docker image tag of Sysdig Promqlator service, relevant when `global.prometheus.enabled` or `promqlator.enabled` is `true`.<br />
**Options**:<br />
**Default**: 0.99.0-2022-07-12T09-19-16Z.93c0642b55<br />
**Example**:

```yaml
promqlator:
  promqlatorVersion: 0.99.0-2022-07-12T09-19-16Z.93c0642b55
```

## **promqlator.enabled**

**Required**: `false`<br />
**Description**: Feature flag for this service<br />
**Options**:<br />
**Default**: `true`<br />
**Example**:

```yaml
promqlator:
  enabled: true
```

# promchap

## **promchap.resources.promchap.limits.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu assigned to Promchap containers<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 1      |
| medium       | 2      |
| large        | 3      |

**Example**:

```yaml
promchap:
  resources:
    promchap:
      limits:
        cpu: 1
```

## **promchap.resources.promchap.limits.memory**

**Required**: `false`<br />
**Description**: The amount of memory assigned to Promchap containers<br />
**Options**:<br />
**Default**:

| cluster-size | limits |
| ------------ | ------ |
| small        | 1Gi    |
| medium       | 2Gi    |
| large        | 4Gi    |

**Example**:

```yaml
promchap:
  resources:
    promchap:
      limits:
        memory: 1Gi
```

## **promchap.resources.promchap.requests.cpu**

**Required**: `false`<br />
**Description**: The amount of cpu required to schedule Promchap containers<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 250m     |
| medium       | 500m     |
| large        | 1        |

**Example**:

```yaml
promchap:
  resources:
    promchap:
      requests:
        cpu: 250m
```

## **promchap.resources.promchap.requests.memory**

**Required**: `false`<br />
**Description**: The amount of memory required to schedule Promchap containers<br />
**Options**:<br />
**Default**:

| cluster-size | requests |
| ------------ | -------- |
| small        | 300Mi    |
| medium       | 500Mi    |
| large        | 1Gi      |

**Example**:

```yaml
promchap:
  resources:
    promchap:
      requests:
        memory: 300Mi
```

## **promchap.promchapVersion**

**Required**: `false`<br />
**Description**: Docker image tag of Sysdig Prometheus Chaperone service, relevant when `global.prometheus.enabled` is `true` and `promchap.enabled` is also `true`.<br />
**Options**:<br />
**Default**: 0.99.0-2022-07-04T12-52-09Z.d68003f677<br />
**Example**:

```yaml
promchap:
  promchapVersion: 0.99.0-2022-07-04T12-52-09Z.d68003f677
```
