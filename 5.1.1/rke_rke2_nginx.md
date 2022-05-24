# Rancher RKE and RKE2 Nginx Configuration Notes

## Overview

Version 5.1.1-1 has the Ingres Objects created if the `sysdig.ingressNetworking` is set for `external`. This will assume the customer is using their own Ingress Controller.  In this case the default Ingress controller is Nginx.  We will provide the steps to configure Ngonx Ingress controller to pass through the TCP traffic to the collector pod in the Sysdig backend.

Some guidance from Sysdig Support may be warranted in highly customized installations. 

Redirect the collector `“port number”` using the Nginx tcp-services config map, if RKE/RKE2 is using port 6443 for the kube-apiserver on each node. (This is the default)

This can be accomplished by following the steps below.

Create the tcp-services configmap pointing to the collector port in the kube-system namespace, or whatever namespace the nginx ingress controller DaemonSet is running. 

---
```bash
apiVersion: v1
kind: ConfigMap
metadata:
  name: tcp-services
  namespace: kube-system
data:
  9443: “sysdigcloud/sysdigcloud-collector:6443”
```
Check to make sure the Nginx ingress controller Daemonset has the following args set for tcp-services as the SECOND line of the `"args:"` stanza: 

```bash
spec:
  template:
    spec:
      containers:
      - args:
        - /nginx-ingress-controller
        - --tcp-services-configmap=$(POD_NAMESPACE)/tcp-services
```

## Release Notes

- See [Release Notes](release_notes.md) for upgrade matrix, supported platforms & link to full feature notes
