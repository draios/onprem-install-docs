# Sysdig Onprem Install Documentation

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

+-------------+-------------+-------------+-------------+-------------+
| Install     | Incl.       | Supported   | Notes       | Baseline    |
| Version     | Hotfixes    | Upgrade     |             | Documentati |
|             |             | From        |             | on          |
+=============+=============+=============+=============+=============+
| 3.5.1       |             | 3.0, 3.2.x, | New/changed | [/document/ |
|             |             | (3.5.0 if   | modules in  | preview/210 |
| (by         |             | it was      | both Sysdig | 785\#UUIDc9 |
| request)    |             | installed)  | Secure and  | 6fc79135351 |
|             |             |             | Sysdig      | b0b2abca6ff |
|             |             |             | Monitor,    | a42ee5c3](f |
|             |             |             | including:  | ile:////doc |
|             |             |             | New Getting | ument/previ |
|             |             |             | Started and | ew/210785#U |
|             |             |             | Overview,   | UIDc96fc791 |
|             |             |             | new         | 35351b0b2ab |
|             |             |             | Dashboards, | ca6ffa42ee5 |
|             |             |             | overhauled  | c3)         |
|             |             |             | Secure      | with        |
|             |             |             | Events      | oversite    |
|             |             |             | Feed, new   | assistance  |
|             |             |             | navigation  | from Sysdig |
|             |             |             | bar icons   | SupportInst |
|             |             |             | and layout, | aller       |
|             |             |             | changed     | Upgrade     |
|             |             |             | Image       | (3.5.0-3.5. |
|             |             |             | scanning    | 1)          |
|             |             |             | navigation  |             |
|             |             |             | and usage,  |             |
|             |             |             | new Secure  |             |
|             |             |             | vulnerabili |             |
|             |             |             | ty          |             |
|             |             |             | feed and    |             |
|             |             |             | benchmark   |             |
|             |             |             | test,       |             |
+-------------+-------------+-------------+-------------+-------------+
| [3.2.2](htt |             | 2.5.0,      | Hot fix     | [/document/ |
| ps://github |             | 3.2.0       |             | preview/152 |
| .com/draios |             |             |             | 368\#UUIDda |
| /sysdigclou |             |             |             | 9c9c5425e03 |
| dkubernetes |             |             |             | 4eb6c891e3a |
| /releases/t |             |             |             | 6954c618](f |
| ag/3.2.2)   |             |             |             | ile:////doc |
|             |             |             |             | ument/previ |
|             |             |             |             | ew/152368#U |
|             |             |             |             | UIDda9c9c54 |
|             |             |             |             | 25e034eb6c8 |
|             |             |             |             | 91e3a6954c6 |
|             |             |             |             | 18)Installe |
|             |             |             |             | r           |
|             |             |             |             | Upgrade     |
|             |             |             |             | (2.5.0+)    |
|             |             |             |             |             |
|             |             |             |             | [/document/ |
|             |             |             |             | preview/152 |
|             |             |             |             | 368\#UUIDda |
|             |             |             |             | 9c9c5425e03 |
|             |             |             |             | 4eb6c891e3a |
|             |             |             |             | 6954c618](f |
|             |             |             |             | ile:////doc |
|             |             |             |             | ument/previ |
|             |             |             |             | ew/152368#U |
|             |             |             |             | UIDda9c9c54 |
|             |             |             |             | 25e034eb6c8 |
|             |             |             |             | 91e3a6954c6 |
|             |             |             |             | 18)Installe |
|             |             |             |             | r           |
|             |             |             |             | Upgrade     |
|             |             |             |             | (2.5.0+)    |
+-------------+-------------+-------------+-------------+-------------+
| [3.2.0](htt | 3.2.1,      | 2.5.0,      | In Sysdig   | [/document/ |
| ps://github | 3.2.2       | 3.0.0       | Secure:     | preview/152 |
| .com/draios |             |             | Data        | 368\#UUIDda |
| /sysdigclou |             |             | retention   | 9c9c5425e03 |
| dkubernetes |             |             | limits for  | 4eb6c891e3a |
| /releases/t |             |             | scan        | 6954c618](f |
| ag/3.2.0)   |             |             | results,    | ile:////doc |
|             |             |             | vulnerabiit | ument/previ |
|             |             |             | y           | ew/152368#U |
|             |             |             | comparison  | UIDda9c9c54 |
|             |             |             | in scan     | 25e034eb6c8 |
|             |             |             | results,    | 91e3a6954c6 |
|             |             |             | redesigned  | 18)Installe |
|             |             |             | Captures    | r           |
|             |             |             | page, RBAC  | Upgrade     |
|             |             |             | capability, | (2.5.0+)    |
|             |             |             | activity    |             |
|             |             |             | audit       |             |
|             |             |             | improvement |             |
|             |             |             | .           |             |
|             |             |             | In Sysdig   |             |
|             |             |             | Monitor and |             |
|             |             |             | Secure:     |             |
|             |             |             | S3-compatib |             |
|             |             |             | le          |             |
|             |             |             | storage for |             |
|             |             |             | Capture     |             |
|             |             |             | files.      |             |
+-------------+-------------+-------------+-------------+-------------+
| [3.0.0](htt |             | 2.4.1,      | Beta        | [/document/ |
| ps://github |             | 2.5.0       | Activity    | preview/152 |
| .com/draios |             |             | Audit       | 368\#UUIDda |
| /sysdigclou |             |             | feature,    | 9c9c5425e03 |
| dkubernetes |             |             | Beta Policy | 4eb6c891e3a |
| /releases/t |             |             | Advisor     | 6954c618](f |
| ag/3.0.0)   |             |             | feature.    | ile:////doc |
|             |             |             |             | ument/previ |
|             |             |             |             | ew/152368#U |
|             |             |             |             | UIDda9c9c54 |
|             |             |             |             | 25e034eb6c8 |
|             |             |             |             | 91e3a6954c6 |
|             |             |             |             | 18)Installe |
|             |             |             |             | r           |
|             |             |             |             | Upgrade     |
|             |             |             |             | (2.5.0+)    |
+-------------+-------------+-------------+-------------+-------------+
| [2.5.0](htt |             | 2.3.0,      | New         | [/document/ |
| ps://github |             | 2.4.1       | Installer   | preview/152 |
| .com/draios |             |             | tool for    | 368\#UUIDda |
| /sysdigclou |             |             | upgrading;  | 9c9c5425e03 |
| dkubernetes |             |             | new         | 4eb6c891e3a |
| /releases/t |             |             | documentati | 6954c618](f |
| ag/2.5.0)   |             |             | on          | ile:////doc |
|             |             |             | site;       | ument/previ |
|             |             |             | inline      | ew/152368#U |
|             |             |             | scanning    | UIDda9c9c54 |
|             |             |             | for Secure, | 25e034eb6c8 |
|             |             |             | other       | 91e3a6954c6 |
|             |             |             | enhancement | 18)Installe |
|             |             |             | s           | r           |
|             |             |             |             | Upgrade     |
|             |             |             |             | (2.5.0+)    |
+-------------+-------------+-------------+-------------+-------------+
| [2.4.1](htt |             | 2.3.0       | Report      | [Upgrade v  |
| ps://github |             |             | service     | 2.4.1](http |
| .com/draios |             |             | added;      | s://sysdigd |
| /sysdigclou |             |             | upgrade to  | ocs.atlassi |
| dkubernetes |             |             | Anchore     | an.net/wiki |
| /releases/t |             |             | license     | /spaces/Pla |
| ag/2.4.1)   |             |             | required    | tform/pages |
|             |             |             |             | /390561802/ |
|             |             |             |             | Upgrade+Sys |
|             |             |             |             | dig+v.+2.4. |
|             |             |             |             | 1+Kubernete |
|             |             |             |             | s)          |
+-------------+-------------+-------------+-------------+-------------+
| [2.3.0](htt |             | 1929, 2435  | Ability to  | [/document/ |
| ps://github |             |             | secure      | preview/112 |
| .com/draios |             |             | Elasticsear | 915\#UUID97 |
| /sysdigclou |             |             | ch          | a9aa8db1d92 |
| dkubernetes |             |             | and the     | e0acdf88214 |
| /releases/t |             |             | Cassandra   | ea626f63](f |
| ag/2.3.0)   |             |             | DB with     | ile:////doc |
|             |             |             | password    | ument/previ |
|             |             |             | authenticat | ew/112915#U |
|             |             |             | ion         | UID97a9aa8d |
|             |             |             | or SSL/TLS  | b1d92e0acdf |
|             |             |             | protection. | 88214ea626f |
|             |             |             |             | 63)Manual   |
|             |             |             |             | Upgrade     |
|             |             |             |             | (2.3.0 )    |
+-------------+-------------+-------------+-------------+-------------+
| [2435](http | \(2304) (22 | 1929, 1765  | Architectur | [/document/ |
| s://github. | 66) (2172)  |             | e           | preview/112 |
| com/draios/ |             |             | changes to  | 938\#UUID6e |
| sysdigcloud |             |             | Dashboards  | 3de441cc725 |
| kubernetes/ |             |             |             | 7ab54d76077 |
| releases/ta |             |             | & API pods. | 9a675a88](f |
| g/v2435)    |             |             |             | ile:////doc |
|             |             |             |             | ument/previ |
|             |             |             |             | ew/112938#U |
|             |             |             |             | UID6e3de441 |
|             |             |             |             | cc7257ab54d |
|             |             |             |             | 760779a675a |
|             |             |             |             | 88)Manual   |
|             |             |             |             | Upgrade     |
|             |             |             |             | (v2435)     |
|             |             |             |             |             |
|             |             |             |             | Note that   |
|             |             |             |             | this        |
|             |             |             |             | replaces    |
|             |             |             |             | 2172, 2266, |
|             |             |             |             | and 2304.   |
+-------------+-------------+-------------+-------------+-------------+
| [1929](http |             |             |             | legacy      |
| s://github. |             |             |             |             |
| com/draios/ |             |             |             |             |
| sysdigcloud |             |             |             |             |
| kubernetes/ |             |             |             |             |
| releases/ta |             |             |             |             |
| g/v1929)    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| [1765](http |             |             | Migration   | legacy      |
| s://github. |             |             | Tool (MySQL |             |
| com/draios/ |             |             | Connector)  |             |
| sysdigcloud |             |             |             |             |
| kubernetes/ |             |             | Architectur |             |
| releases/ta |             |             | e           |             |
| g/v1765)    |             |             | & Port 443  |             |
|             |             |             | change      |             |
+-------------+-------------+-------------+-------------+-------------+
| [1630](http | ((1586)     |             |             | legacy      |
| s://github. |             |             |             |             |
| com/draios/ |             |             |             |             |
| sysdigcloud |             |             |             |             |
| kubernetes/ |             |             |             |             |
| releases/ta |             |             |             |             |
| g/v1630)    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| [1511](http | \(1472) (14 |             |             | legacy      |
| s://github. | 02)         |             |             |             |
| com/draios/ |             |             |             |             |
| sysdigcloud |             |             |             |             |
| kubernetes/ |             |             |             |             |
| releases/ta |             |             |             |             |
| g/v1511)    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| [1245](http |             |             |             | legacy      |
| s://github. |             |             |             |             |
| com/draios/ |             |             |             |             |
| sysdigcloud |             |             |             |             |
| kubernetes/ |             |             |             |             |
| releases/ta |             |             |             |             |
| g/v1245)    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| [1149](http |             |             | Migration   | legacy      |
| s://github. |             |             | Tool        |             |
| com/draios/ |             |             | (Unified    |             |
| sysdigcloud |             |             | Events)     |             |
| kubernetes/ |             |             |             |             |
| releases/ta |             |             |             |             |
| g/v1149)    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+
| [1091](http |             |             |             | legacy      |
| s://github. |             |             |             |             |
| com/draios/ |             |             |             |             |
| sysdigcloud |             |             |             |             |
| kubernetes/ |             |             |             |             |
| releases/ta |             |             |             |             |
| g/v1091)    |             |             |             |             |
+-------------+-------------+-------------+-------------+-------------+


## Releases
* [3.6.0](https://github.com/draios/onprem-install-docs/blob/release/3.6.0/README.md)
