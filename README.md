# Sysdig Onprem Install Documentation

The Sysdig Platform is a highly available application for securing and monitoring cloud-native infrastructures.

## Table of Contents
  * [Oversight Services Now Offered for All Installs and Upgrades](#oversight-services-now-offered-for-all-installs-and-upgrades)
  * [Supported Migration Paths](#supported-migration-paths)

## Oversight Services Now Offered for All Installs and Upgrades

> **Note**
>
> As part of our continued focus on our customers, we are now offering oversight services for all on-premise installs and upgrades. Your Technical Account Manager (TAM), in conjunction with our support organization and Professional Services \[where applicable\], will work with you to:

-   Assess your environment to ensure it is configured correctly

-   Review your infrastructure to validate the appropriate storage capacities are available

-   Review and provide recommendations for backing up your Sysdig data

-   Work with you to ensure our teams are ready to assist you during the installation and upgrade process

-   Provide the software for the install

-   Be available during the process to ensure a successful deployment

> You can always review the process in the documentation.
>
> If you are a new customer looking to explore Sysdig, please head over [here](https://sysdig.com/company/freetrial/) to sign up for a trial on our SaaS Platform. Alternatively, you can contact us [here](https://sysdig.com/company/contactus/).

## K8s support matrix

Sysdig platform continuously being validated at multiple K8s flavors including kOps, Openshift4, EKS, GKE, AKS, IKS, ROKS or RKE2. You can find below the K8s version support matrix. If you have a question about a custom flavor or K8s version, share it with your technical account manager (TAM).

| Install version | Validated K8s versions |
|---|---|
| 5.0.X | 1.16, 1.17, 1.18, 1.19, 1.20, 1.21 |
| <= 5.1.9 | 1.18, 1.19, 1.20, 1.21, 1.22, 1.23, 1.24 |
| >= 5.1.10 | 1.23, 1.24, 1.25, 1.26, 1.27, 1.28 |
| 6.0.X, 6.1.X | 1.23, 1.24, 1.25, 1.26 |
| >= 6.2.X | 1.23, 1.24, 1.25, 1.26, 1.27, 1.28, 1.29 |
| 7.X | 1.28, 1.29, 1.30, 1.31, 1.32, 1.33 |


## Supported Migration Paths

In general, Sysdig tests and supports direct upgrades from **two releases** back to the current version.

Beyond info at this repo, take a look at our [Sysdig On-Premises Release Notes](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/)


|Install version | Supported Upgrade From | Latest Release |
|---|---|---|
| 7.x (by request) | 6.X | [7.X](7.X) (*)|
| 6.x (by request) | 5.0.X, 5.1.X 6.X.X | [6.X](6.X) (*)|
| 5.1 (by request) | 4.0.X, 5.0.X, 5.1.X | [5.1](5.1) |
| 5.0 (by request) | 4.0.X, 5.0.X | [5.0](5.0) |
| 4.0 (by request) | 3.6.X, 4.0.X | [4.0](4.0) |
| 3.6 (by request) | 3.2.X, 3.5.X, 3.6.X | [3.6](3.6) |
> Reference:
> - (*) Upgrade from 5.X to 6.X is supported only until 6.11, since 6.12 the direct upgrade from 5.X is not supported, please check the upgrade path warnings for each version below.


**⚠️ Upgrade Path Warning**

Before upgrading to the latest version, please note these critical requirements:
1. **Before Upgrading 6.7.x (for upgrades from 6.5.X or above):**
    - In v6.7.0, the nats.js PVC requirements have been increased if your **NATS storage size is below 100GB**, as a result, it is necessary to [resize the PVCs](6.X/6.7.0/docs/09-natsJs-pvc-size-increase.md) before initiating the installer upgrade. Open a support case for guidance and assistance with the upgrade process.

2. **Before Upgrading to 6.9.x (for upgrades from 5.x or above):**
    - If you are currently using on-prem version **5.x** and plan to upgrade to **v6.9.0**, ensure you have upgraded your data store to Cassandra v3 before proceeding with the upgrade to v6.9.0.

3. **Before Upgrading to 6.12.x (for upgrades from 5.x):**
    - For fresh installations and upgrades to version v6.12.0, OpenSearch v2 is included. If you are currently using **on-prem version 5.x** and plan to upgrade to v6.12.0, ensure that you have first migrated your environment to OpenSearch v1 by upgrading to **any on-prem 6.x** before proceeding with the upgrade to version v6.12.0.

Failure to follow these steps may result in upgrade failures or data inconsistencies. Verify your current configuration before upgrading.

For the full migration table, see [On-Premises Version Support](https://docs.sysdig.com/en/administration/sysdig-onprem-release-support/#version-support).

## Release history

### Version 7.x

- [7.3.0 Release, June 2025](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/#730-release-june-2025)
- [7.2.0 Release, April 2025](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/#720-release-april-2025)
- [7.1.0 Release, April 2025](https://docs.sysdig.com/en/release-notes/sysdig-on-premises-release-notes/#710-release-april-2025)
- [7.0.0 Release, February 2025](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#700-release-february-2025)

### Version 6.x

- [6.16.2 Release, January 2025](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#6162-hotfix-release-january-2025)
- [6.16.1 Release, January 2025](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#6161-release-january-2025)
- [6.15.1 Release, December 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#6151-release-december-2024)
- [6.14.0 Release, September 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#6140-release-september-2024)
- [6.13.0 Release, July 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#6130-release-july-2024)
- [6.12.0 Release, June 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#6120-release-june-2024)
- [6.7.2 Release, May 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#672-hotfix-release-may-2024)
- [6.11.0 Release, May 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#6110-release-may-2024)
- [6.10.0 Release, April 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#6100-release-april-2024)
- [6.4.6 Release, March 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#646-hotfix-release-march-2024)
- [6.9.1 Release, March 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#691-hotfix-release-march-2024)
- [6.7.1 Release, March 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#671-hotfix-release-march-2024)
- [6.4.5 Release, March 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#645-hotfix-release-march-2024)
- [6.9.0 Release, February 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#690-release-february-2024)
- [6.4.4 Release, February 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#644-hotfix-release-february-2024)
- [6.8.0 Release, January 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#680-release-january-2024)
- [6.4.3 Release, January 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#643-hotfix-release-january-2024)
- [6.7.0 Release, December 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#670-release-december-2023)
- [6.4.2 Release, December 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#642-release-december-2023)
- [6.6.0 Release, November 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#660-release-november-2023)
- [6.5.1 Release, October 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#651-hotfix-release-october-2023)
- [6.5.0 Release, September 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#650-release-september-2023)
- [6.4.1 Release, August 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#641-release-august-2023)
- [6.4.0 Release, July 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#640-release-july-2023)
- [6.3.0 Release, July 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#630-release-july-2023)
- [6.2.1 Release, June 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#621-release-june-2023)
- [6.1.2 Release, May 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#612-release-may-2023)
- [6.1.1 Release, May 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#611-release-may-2023)
- [6.0.2 Hotfix Release, April 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#602-hotfix-release-april-2023)
- [6.0.0 Release, April 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#600-release-april-2023)

### Version 5.x

- [5.1.12 Hotfix Release, January 2024](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#5112-hotfix-release-january-2024)
- [5.1.11 Hotfix Release, September 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#5111-hotfix-release-september-2023)
- [5.1.10 Hotfix Release, September 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#5110-hotfix-release-september-2023)
- [5.1.9 Hotfix Release, April 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#519-hotfix-release-april-2023)
- [5.1.8 Hotfix Release, February 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#518-hotfix-release-february-2023)
- [5.1.7 Hotfix Release, January 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#517-hotfix-release-january-2023)
- [5.1.6 Hotfix Release, January 2023](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#516-hotfix-release-january-2023)
- [5.1.5 Hotfix Release, December 2022](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#515-hotfix-release-december-2022)
- [5.1.4 Hotfix Release, November 2022](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#514-hotfix-release-november-2022)
- [5.1.3 Hotfix Release, September 2022](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#513-hotfix-release-september-2022)
- [5.1.2-2 Hotfix Release, July 2022](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#512-2-hotfix-release-july-2022)
- [5.1.2 Hotfix Release, May 2022](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#512-hotfix-release-may-2022)
- [5.1.1 Hotfix Release, May 2022](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#511-hotfix-release-may-2022)
- [5.1.0 Release, March 2022](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#510-release-march-2022)
- [5.0.5 Hotfix Release for CVE-2022-22965](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#505-hotfix-release-for-cve-2022-22965)

### Version 4.x (5.0.x)

- [4.0.8 Hotfix Release, July 2022](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#408-hotfix-release-july-2022)
- [4.0.7/5.0.4 Hotfix Release for CVE-2021-44228 in Apache’s log4j (3.6.4, 4.0.7, 5.0.4)](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#407504-hotfix-release--for-cve-2021-44228-in-apaches-log4j-364-407-504)
- [4.0.6/5.0.3 Hotfix Release for CVE-2021-44228 in Apache’s log4j (3.6.3, 4.0.6, 5.0.3)](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/#406503-hotfix-release--for-cve-2021-44228-in-apaches-log4j-363-406-503)
