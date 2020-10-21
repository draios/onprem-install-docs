# Sysdig Onprem Install Documentation

## Table of Contents
  * [Sysdig Onprem Install Documentation](#sysdig-onprem-install-documentation)
      * [Oversight Services Now Offered for All Installs and Upgrades](#oversight-services-now-offered-for-all-installs-and-upgrades)
      * [Supported Migration Paths](#supported-migration-paths)
         * [For Kubernetes Environments](#for-kubernetes-environments)

## Oversight Services Now Offered for All Installs and Upgrades

> **Note**
>
> As part of our continued focus on our customers, we are now offering oversight services for all on-premise installs and upgrades. Your Technical Account Manager (TAM), in conjunction with our support organization and Professional Services \[where applicable\], will work with you to:

-   Assess your environment to ensure it is configured correctly

-   Review your infrastructure to validate the appropriate storage capacities are available

-   Review and provide recommendations for backing up your Sysdig data

-   Work with you to ensure our teams are ready to assist you during the install and upgrade process

-   Provide the software for the install

-   Be available during the process to ensure a successful deployment

> You can always review the process in the documentation.
>
> If you are a new customer looking to explore Sysdig, please head over [here](https://sysdig.com/company/freetrial/) to sign up for a trial on our SaaS Platform. Alternatively, you can contact us [here](https://sysdig.com/company/contactus/).

## Supported Migration Paths

In general, Sysdig tests and supports direct upgrade from [**five** releases](https://github.com/draios/sysdigcloudkubernetes/releases) back to the current version. Release-specific requirements are listed in the table below.

### For Kubernetes Environments


|Install version | Included Hotfixes | Supported Upgrade From | Notes | Baseline Documentation |
|---|---|---|---|---|
| [3.5.1 (by request)](3.5.1/README.md)| | 3.0, 3.2.x, (3.5.0 if it was installed) | New/changed modules in both Sysdig Secure and Sysdig Monitor, including: New Getting Started and Overview, new Dashboards, overhauled Secure Events Feed, new navigation bar icons and layout, changed Image scanning navigation and usage, new Secure vulnerability feed and benchmark test. | [3.5.1](https://github.com/draios/onprem-install-docs/tree/main/3.5.1)
| [3.2.2](3.2.0/README.md))| | 2.5.0, 3.2.0 | Hot fix | 	Installer Upgrade (2.5.0+) |
| [3.2.0](3.2.0/README.md) | 3.2.1, 3.2.2 | 2.5.0, 3.0.0 | In Sysdig Secure: Data retention limits for scan results, vulnerabiity comparison in scan results, redesigned Captures page, RBAC capability, activity audit improvement. In Sysdig Monitor and Secure: S3-compatible storage for Capture files. | |
| [3.0.0](3.0.0/README.md) | | 2.4.1, 2.5.0 | Beta Activity Audit feature, Beta Policy Advisor feature. | |
| [2.5.0](2.5.0/README.md) | | 2.3.0, 2.4.1 | New Installer tool for upgrading; new documentation site; inline scanning for Secure, other enhancements | |
| [2.4.1](2.4.1/installer-beta/README.md) | | 2.3.0 | Report service added; upgrade to Anchore license required | |
| 2.3.0 | | 1929, 2435 | Ability to secure Elasticsearch and the Cassandra DB with password authentication or SSL/TLS protection. | |
| 2435 | 2304, 2266, 2172 | Architecture changes to Dashboards(2304) & API pods (2172) | |
| 1929 | | | | legacy |
| 1765 | | |Migration Tool (MySQL Connector) & Architecture & Port 443 change | legacy |
| 1630 | 1586 | | | legacy |
| 1511 | 1472, 1402 | | | legacy |
| 1245 | | | | legacy |
| 1149 | | | Migration Tool (Unified Events) | legacy |
| 1091 | | | | legacy |
   

