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

-   Work with you to ensure our teams are ready to assist you during the install and upgrade process

-   Provide the software for the install

-   Be available during the process to ensure a successful deployment

> You can always review the process in the documentation.
>
> If you are a new customer looking to explore Sysdig, please head over [here](https://sysdig.com/company/freetrial/) to sign up for a trial on our SaaS Platform. Alternatively, you can contact us [here](https://sysdig.com/company/contactus/).

## K8s support matrix

Sysdig platform is continuosly being validated at multiple K8s flavors including k0ps, Openshift4, EKS, GKE, AKS, IKS, ROKS or RKE2. You can find below the K8s version support matrix. If you might have a question about a custom flavor or K8s version, please just share it with your TAM.

| Install version | Validated K8s versions |
|---|---|
| 5.0.X | 1.16, 1.17, 1.18, 1.19, 1.20, 1.21 |
| 5.1.X | 1.18, 1.19, 1.20, 1.21, 1.22, 1.23, 1.24 |
| 6.X | 1.23, 1.24, 1.25, 1.16 |

## Supported Migration Paths

In general, Sysdig tests and supports direct upgrade from **two releases** back to the current version.

Beyond info at this repo, take a look to our [Sysdig On-Premises Release Notes](https://docs.sysdig.com/en/docs/release-notes/sysdig-on-premises-release-notes/)


|Install version | Supported Upgrade From | Latest Release |
|---|---|---|
| 6.x (by request) | 5.0.X, 5.1.X 6.X.X | [6.X](6.X) |
| 5.1 (by request) | 4.0.X, 5.0.X, 5.1.X | [5.1](5.1) |
| 5.0 (by request) | 4.0.X, 5.0.X | [5.0](5.0) |
| 4.0 (by request) | 3.6.X, 4.0.X | [4.0](4.0) |
| 3.6 (by request) | 3.2.X, 3.5.X, 3.6.X | [3.6](3.6) |

See [docs.sysdig.com](https://docs.sysdig.com/en/on-premises-upgrades.html#UUID-99ec8b45-9aed-4aff-d86b-ad17bc8ef333_UUID-92d3fce4-1e95-4f25-056c-3cc177380de6) for the rest of the migration table.
