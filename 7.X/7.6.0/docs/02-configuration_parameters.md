# Configuration Parameters (Deprecated)

## Deprecation Notice

**This documentation file has been deprecated as of release 7.5.0.**

The parameter hierarchy in the installer's `values.yaml` configuration file has undergone significant changes. As a result, this documentation is no longer maintained.

### Migration Tool Available

Starting with **release 7.4.0**, the installer includes a `migrate-values` command that automatically migrates your configuration from the old parameter hierarchy to the new structure.

To migrate your existing `values.yaml` file, run:

```bash
./installer migrate-values --config /path/to/your/values.yaml
```

For more information about this feature, see the [7.4.0 Release Notes](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/#740-release-august-2025).

### Next Steps

If you have questions about configuration parameters or need assistance with your deployment:

2. **Contact Sysdig Support**: Our support team can provide guidance on the current configuration structure and help with any migration issues
3. **Review Release Notes**: Check the release notes for version 7.4.0 and later for details about configuration changes

### Backwards Compatibility

Please note that any configuration changes that are **not backwards compatible** will be clearly announced in the release notes for the respective version. We recommend reviewing the release notes carefully when upgrading to ensure a smooth transition.
