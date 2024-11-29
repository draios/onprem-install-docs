<!-- Space: TOOLS -->
<!-- Parent: Installer -->
<!-- Title: [BETA] Configuration Parameters -->
<!-- Layout: plain -->

# Beta Configuration Parameters

<br />

## **sysdig.iks.privateCollectorDNSName**

**Required**: `false`<br />
**Description**: The hostname that will be used in the Ingress to access Collectors from the private IKS ALBs.<br />
**Default**: ""<br />

**Example**:

```yaml
sysdig:
  iks:
    privateCollectorDNSName: ingest.private.jp-osa.monitoring.cloud.ibm.com
```

## **sysdig.iks.privateAPIDNSName**

**Required**: `false`<br />
**Description**: The hostname that will be used in the Ingress to access APIs from the private IKS ALBs.<br />
**Default**: ""<br />

**Example**:

```yaml
sysdig:
  iks:
    privateAPIDNSName: private.jp-osa.monitoring.cloud.ibm.com
```

## **sysdig.iks.privateIngressALBs**

**Required**: `false`<br />
**Description**: a list of ALB IDs to use for private ingress on the IBM platform<br />
**Default**: []

**Example**:

```yaml
sysdig:
  iks:
    privateIngressALBs:
      - private-crbvutcu8o0ouk5qn43bbg-alb1
      - private-crbvutcu8o0ouk5qn43bbg-alb2
      - private-crbvutcu8o0ouk5qn43bbg-alb3
```

## **sysdig.iks.publicIngressALBsReplicaCount**

**Required**: `false`<br />
**Description**: the number of replicas for the public ALBs in the IKS deployment; if not specified, the implicit replica count is 2<br />
**Default**: ""<br />

**Example**:

```yaml
sysdig:
  iks:
    publicIngressALBsReplicaCount: 4
```

## **sysdig.iks.publicIngressALBs**

**Required**: `false`<br />
**Description**: a list of ALB IDs to use for public ingress on the IBM platform<br />
**Default**: []

**Example**:

```yaml
sysdig:
  iks:
    publicIngressALBs:
      - public-crbvutcu8o0ouk5qn43bbg-alb4
      - public-crbvutcu8o0ouk5qn43bbg-alb5
      - public-crbvutcu8o0ouk5qn43bbg-alb6
```

## **sysdig.iks.privateIngressALBsReplicaCount**

**Required**: `false`<br />
**Description**: the number of replicas for the private ALBs in the IKS deployment; if not specified, the implicit replica count is 2<br />
**Default**: ""<br />

**Example**:

```yaml
sysdig:
  iks:
    privateIngressALBsReplicaCount: 4
```

## **sysdig.collector.privateIngressALBs**

**Required**: `false`<br />
**Description**: list of ALB IDS to use for private ingress on the IBM platform<br />
**Default**: []

**Example**:

```yaml
sysdig:
  collector:
    privateIngressALBs:
      - alb-id-1
      - alb-id-2
      - alb-id-3
```

