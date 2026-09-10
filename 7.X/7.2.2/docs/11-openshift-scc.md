<!-- Space: IONP -->
<!-- Parent: Installer -->
<!-- Parent: Git Synced Docs -->
<!-- Title: Openshift SCC -->
<!-- Layout: plain -->

# Openshift SCC

In an openshift scenario, we need to leverage openshift SCC (Security Context Constraint) to make the sysdig workload run with the proper configuration. We will use 2 scc for the service accounts:

* **privileged**: It allows to run privileged container, but it's used when the container must run as the root user.
* **nonroot-v2**: Available from Openshift 4.11. It allows to run the container as any user with uid > 0 and to set the seccomp profile.

If the openshift version is less than 4.11 every serviceaccount will have the `privileged` scc, since `anyuid` is not enough because `seccompProfile` statement is not allowed in the `anyuid` SCC.

One important concept is that even if we give to a service account multiple SCCs, only one will be used at runtime. And also if we give privileged+nonroot-v2 you may find some cases in which the privileged SCC is not selected but nonroot-v2 is selected instead. This happens because in the deployment there are no evidences that the container needs to run with that SCC and so the least privilege SCC is selected.

More details on the SCC [documentation](https://docs.openshift.com/container-platform/4.14/authentication/managing-security-context-constraints.html).

Here you can find a table with all the Service Accounts and the reason behind the given SCC in Openshift >= 4.11:

|        Service Account        |    SCC     | Reason                                                                                                                                                    |
| :---------------------------: | :--------: | :-------------------------------------------------------------------------------------------------------------------------------------------------------- |
|            sysdig             | privileged | it's widely used across many workloads, and some worloads require to run with user 0                                                                      |
|       sysdig-with-root        | privileged |                                                                                                                                                           |
|     sysdigcloud-cassandra     | privileged | Needs to run as user 0 in hostpath scenario                                                                                                               |
|     sysdig-elasticsearch      | privileged | Actually not used but it may be used for elasticsearch                                                                                                    |
|         postgres-pod          | privileged | Needs to run as user 0 in hostpath scenario                                                                                                               |
|      sysdig-meerkat-api       | privileged | The dockerfile has `sysdig` as USER, and the kubelet cannot verify that user `sysdig` does not have uid 0. After the hardening this could be set to nonroot-v2 |
|   sysdig-meerkat-collector    | privileged | The dockerfile has `sysdig` as USER, and the kubelet cannot verify that user `sysdig` does not have uid 0. After the hardening this could be set to nonroot-v2 |
|   sysdig-meerkat-aggregator   | privileged | The dockerfile has `sysdig` as USER, and the kubelet cannot verify that user `sysdig` does not have uid 0. After the hardening this could be set to nonroot-v2 |
|   sysdig-meerkat-datastream   | privileged | The dockerfile has `sysdig` as USER, and the kubelet cannot verify that user `sysdig` does not have uid 0. After the hardening this could be set to nonroot-v2 |
|     node-labels-to-files      | nonroot-v2 | Needs to run with uid 1000 and seccompProfile set                                                                                                         |
|     elasticsearch-pre-job     | nonroot-v2 | Needs to run with uid 1000 and seccompProfile set                                                                                                         |
|    elasticsearch-post-job     | nonroot-v2 | Needs to run with uid 1000 and seccompProfile set                                                                                                         |
|      ingress-controller       | nonroot-v2 | Needs to run with uid 1000 and seccompProfile set                                                                                                         |
| sysdigcloud-postgres-operator | nonroot-v2 | Needs to run with uid 1000 and seccompProfile set                                                                                                         |
|       metadata-service        | nonroot-v2 | Needs to run with uid 1000 and seccompProfile set                                                                                                         |
|             redis             | nonroot-v2 | Needs to run with uid 1000 and seccompProfile set                                                                                                         |
|    sysdigcloud-promqlator     | nonroot-v2 | Needs to run with uid 1000 and seccompProfile set                                                                                                         |
|  sysdig-certificate-exporter  | nonroot-v2 | Needs to run with uid 1000 and seccompProfile set                                                                                                         |
