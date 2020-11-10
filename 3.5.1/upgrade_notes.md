# Upgrade

## Overview

From version 3.5.0, both installing and upgrading with the installer has been simplified. Upgrade differs from Install in that you run an installer diff to discover the differences between the old and new versions and then installer deploy for the new version.

Some guidance from Sysdig Support may be warranted in highly customized installations. 

Refer to the appropriate workflow, depending on your environment:

  - [Quickstart Install](README.md#quickstart-install)
  - [Airgapped Installation Options](README.md#airgapped-installation-options)

## Upgrade Notes

### Postgres Version Update v10.x to 12.x
Version 3.5.0 upgrade includes an automatic Postgres version upgrade. Depending on the size of your database, that can take some time.

The data migration takes approximately 1 min per 1 GiB of data. The speed of data migration ultimately depends on the underlying storage media.

To complete the Postgres upgrade, you must also ensure there is sufficient disk space in the volume when using a local-disk storage provisioner in Kubernetes. For example, if your current Postgres size is 100 GiB, ensure there is at least another 100 GiB space free in the volume. This is required temporarily for copying the data during the upgrade.

### 3.5.0 - 3.5.1 Elasticsearch Upgrade
Upgrading from version 3.5.0 to 3.5.1 also upgrades Elasticsearch. Due to the Elasticsearch update strategy of ondelete, the pods will only be upgraded when they are restarted:
 
  ```image: quay.io/sysdig/elasticsearch:6.8.3.9```

## Release Notes

- See [Release Notes](release_notes.md) for upgrade matrix, supported platforms & link to full feature notes