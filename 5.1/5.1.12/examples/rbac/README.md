# RBAC for Installer v0.0.0a ((work in progress) 

- RBAC resources required to run the `installer`
- Each of the three directories contains YAMLs for a specific case:

## [readonly](readonly)
- Readonly access to the namespace and minimal resources necessary for the installer to `generate` and `secure-diff` the existing install (or for a new install)

## [external-ingress](external-ingress)
- More restrictive RBAC access rights by using an external `ingress` object
- TBD
  
## [fullaccess](fullaccess)
- Allows the execution of `installer` as-is, including rights for `StorageClass` and `IngressController`

## [openshift](openshift)
- TBD

## Instructions

- For each usecase we provide YAMLs to create the necessary RBAC resources
- This example assumes that Sysdig will be installed in the `sysdigcloud` namespace
- Apply these YAMLs to your cluster from an `admin` level account
- Create a `kubeconfig` for the ServiceAccount installer
- Use the `kubeconfig` to execute the installer
