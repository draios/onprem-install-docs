**All paths in this README assume the user is at the root of the sysdigcloud-kubernetes repository**

# Enabling authentication on a new cluster

The following steps only highlight steps specific to the secure Elasticsearch update. Please follow normal procedure for installing the platform otherwise.

1. Run the following docker command to generate the root/admin certs to a directory within the current working directory.

        docker run -d -v "$(pwd)"/generated_elasticsearch_certs:/tools/out quay.io/sysdig/elasticsearch:1.0.1-es-certs

2. Generate the required kubernetes secret file.

        NAMESPACE=<replace-this>
        kubectl -n $NAMESPACE create secret generic ca-certs --from-file=generated_elasticsearch_certs

3. Generate the password secrets for the admin/readonly searchguard roles.

        SG_ADMIN_PASSWORD=$(date +%s | sha256sum | base64 | head -c 16)
        SG_READONLY_PASSWORD=$(date | sha256sum | base64 | head -c 16)
        kubectl -n $NAMESPACE create secret generic sg-admin-secret --from-literal=password=$SG_ADMIN_PASSWORD
        kubectl -n $NAMESPACE create secret generic sg-readonly-secret --from-literal=password=$SG_READONLY_PASSWORD

4. Create Searchguard config files.

        kubectl -n $NAMESPACE create secret generic sg-config-files --from-file=datastores/as_kubernetes_pods/manifests/elasticsearch/sgconfig

5. If you are monitoring the Elasticsearch cluster with `sysdig-agent`, ensure the `sysdig-agent` `configmap` has the following Elasticsearch configuration in the `data.dragent.yaml.app_checks` section:

        data:
          dragent.yaml: |
            app_checks:
              - name: elasticsearch
                check_module: elastic
                pattern:
                  port: 9200
                  comm: java
                conf:
                  url: https://sysdigcloud-elasticsearch:9200
                  username: readonly
                  password: <SG_READONLY_PASSWORD from step 3>
                  ssl_verify: false

    And restart the agent if necessary to apply the new configs.

        kubectl -n $NAMESPACE delete pod -l app=sysdig-agent

    **Note**: You may come across an error stating `Unverified HTTPS request is being made.` in the `sysdig-agent` logs. You may safely ignore this for now.

5. Update Kubernetes configs:
    * For the following files, uncomment the sections that have `## If enabling elasticsearch auth, uncomment <resource(s)>` above it.
      * `datastores/as_kubernetes_pods/manifests/elasticsearch/elasticsearch-statefulset.yaml`
      * `sysdigcloud/api-deployment.yaml`
      * `sysdigcloud/collector-deployment.yaml` (for openshift use: `sysdigcloud/openshift/openshift-collector-deployment.yaml`)
      * `sysdigcloud/worker-deployment.yaml`
    * In `sysdigcloud/config.yaml`, set `elasticsearch.searchguard.enabled: "true"`

6. Create the configmap and elasticsearch cluster.

        kubectl -n $NAMESPACE apply -f sysdigcloud/config.yaml
        kubectl -n $NAMESPACE apply -f datastores/as_kubernetes_pods/manifests/elasticsearch/elasticsearch-service.yaml
        kubectl -n $NAMESPACE apply -f datastores/as_kubernetes_pods/manifests/elasticsearch/elasticsearch-statefulset.yaml

7. Deploy the other services in the usual order.

# Enabling authentication on an existing cluster with standard Sysdig Elasticsearch setup

The following instructions highlight steps specific to the secure Elasticsearch update. Please follow normal procedure for upgrading the platform otherwise (taking special care to accomodate the provided `yaml` configurations to the customer's platform requirements and existing configurations, if necessary).

This will require downtime, as Elasticsearch must be completely restarted. It is recommended to do a full upgrade to the latest platform version; the `api`, `collector`, and `worker` backend components will need to be updated, which will cause other application components to break if they are not version-compatible.

1. Follow steps 1-5 from [Enabling authentication on a new cluster](#enabling-authentication-on-a-new-cluster)
2. Update `sysdigcloud/config.yaml` to have the following properties and values (also ensure the rest of the values are appropriate as this config will be applied in a later step):

        data:
          ...
          elasticsearch.hostname: sysdigcloud-elasticsearch # IMPORTANT: This replaces elasticsearch.url
          elasticsearch.searchguard.enabled: "true"
          elasticsearch.user: admin
          ...

3. In `datastores/as_kubernetes_pods/manifests/elasticsearch/elasticsearch-statefulset.yaml`, uncomment the sections that have the header `## If enabling elasticsearch auth, uncomment <list of resources>`.

    Please pay special attention to these fields when modifying the files to accomodate the existing environment:
    * `spec.replicas` and `spec.template.spec.containers[elasticsearch].env[ELASTICSEARCH_GOSSIP_NODES_NUM].value`
    * `spec.template.spec.containers[].resources`
    * `spec.volumeClaimTemplates[].spec.resources.requests.storage`
    * `spec.volumeClaimTemplates[].spec.storageClassName`

4. The existing api, collector, and worker deployments will need to be updated. Please modify the following files to accomodate the existing environment, and uncomment the sections that have `## If enabling elasticsearch auth, uncomment <resource(s)>` above it:
    * `sysdigcloud/api-deployment.yaml`
    * `sysdigcloud/collector-deployment.yaml`
    * `sysdigcloud/worker-deployment.yaml`

    Please pay special attention to these fields when modifying the files to accomodate the existing environment
    * `spec.replicas`
    * `spec.template.spec.containers[].resources`
    * `spec.template.spec.containers[].volumeMounts`
    * `spec.template.spec.volumes`

5. Apply new configurations for Elasticsearch

        kubectl -n $NAMESPACE apply -f sysdigcloud/config.yaml
        kubectl -n $NAMESPACE apply -f datastores/as_kubernetes_pods/manifests/elasticsearch/elasticsearch-service.yaml
        kubectl -n $NAMESPACE replace -f datastores/as_kubernetes_pods/manifests/elasticsearch/elasticsearch-statefulset.yaml

    * Note: If you get an error similar to `updates to statefulset spec for fields other than 'replicas', 'template', and 'updateStrategy' are forbidden` check that the `volumeClaimTemplates` in the yaml file matches the existing configuration.

6. Delete existing Elasticsearch pods

        kubectl -n $NAMESPACE delete po -l component=elasticsearch

7. Apply new configurations for api, collector, and worker:

        kubectl -n $NAMESPACE apply -f sysdigcloud/api-deployment.yaml
        kubectl -n $NAMESPACE apply -f sysdigcloud/collector-deployment.yaml
        kubectl -n $NAMESPACE apply -f sysdigcloud/worker-deployment.yaml

8. Apply new configurations for all other application components.

# Enabling authentication on an existing cluster with custom Elasticsearch setup

1. [Install Searchguard](https://docs.search-guard.com/latest/search-guard-installation) on your Elasticsearch cluster. **Be sure to install the same version of Searchguard as your Elasticsearch cluster**.
2. Add the Elasticsearch cluster's root certificate authority as a secret. The name of the cert file must be `root-ca.pem`.

        NAMESPACE=<replace-this>
        kubectl -n $NAMESPACE create secret generic ca-certs --from-file=<path to root-ca.pem>

3. Uncomment `elasticsearch.verifySSL` in `sysdig/config.yaml` and set the value appropriately. Make any other necessary changes to the configmap values and apply. Note: the new configmap replaces `elasticsearch.url` with `elasticsearch.hostname`.

        kubectl -n $NAMESPACE apply -f sysdigcloud/config.yaml

4. Follow step 5 from [Enabling authentication on a new cluster](#enabling-authentication-on-a-new-cluster).

5. Follow steps 4, 7, and 8 from [Enabling authentication on an existing cluster with standard Sysdig Elasticsearch setup](#enabling-authentication-on-an-existing-cluster-with-standard-sysdig-elasticsearch-setup).

# Search Guard Roles

We have included two Searchguard roles with this setup:
* `admin` has access to everything in the cluster and all indices
* `readonly` can only read indices and access monitoring endpoints for the cluster (e.g. `/_cat/health`)
