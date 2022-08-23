# Use this overlay when using OpenShift with Prometheus data ingestion

- make sure the Route `host` is different from the one used for the collectors.

```
apiVersion: route.openshift.io/v1
kind: Route
metadata:
  name: sysdigcloud-beacon-prom-remote-write
  namespace: sysdigcloud
spec:
  host: prometheus_ingestion.replace_with_you_domain_name_here
```

