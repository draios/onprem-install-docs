# Upgrade

## Overview

From version 3.5.0, both installing and upgrading with the installer has been simplified. Upgrade differs from Install in that you run an installer diff to discover the differences between the old and new versions and then installer deploy for the new version.

Some guidance from Sysdig Support may be warranted in highly customized installations. 

Refer to the appropriate workflow, depending on your environment:

  - [Quickstart Install](README.md#quickstart-install)
  - [Airgapped Installation Options](README.md#airgapped-installation-options)

## Upgrade Notes

### Elastic search 6.8.6 upgrade

With Sysdig 3.6.0 install, ElasticSearch(ES) runs `privileged: false` by default. In most cases this should work automatically.

There are some cases where ElasticSearch will fail with an error like below

```bash
kubectl -n sysdig logs -f sysdigcloud-elasticsearch-0
...
+ grep cap_sys_admin
++ sysctl -nb vm.max_map_count
+ max_map_count=65530
+ [[ 65530 -ne 262144 ]]
+ echo 'sysctl vm.max_map_count is not set to the correct value, and I do not have the privileges to set it!'
+ exit 1
sysctl vm.max_map_count is not set to the correct value, and I do not have the privileges to set it!
```

There are 2 ways to fix this issue

1. run systemctl command on hosts that run ElasticSearch,

    ```bash
    VM_MAX_MAP_COUNT=${VM_MAX_MAP_COUNT:-262144}; sysctl -w vm.max_map_count=${VM_MAX_MAP_COUNT}
    ```

2. An initContainer which runs as `privileged: true` and `root` and set vm.max_map_count [example overlay](examples/elasticsearch-init-vmmaxmapcount)

## Release Notes

- See [Release Notes](release_notes.md) for upgrade matrix, supported platforms & link to full feature notes