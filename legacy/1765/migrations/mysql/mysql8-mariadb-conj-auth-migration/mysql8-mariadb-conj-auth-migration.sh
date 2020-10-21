#!/bin/bash

# Bash Strict Mode
set -euo pipefail
IFS=$'\n\t'

################################################################################
# Static definitions 
################################################################################

# Pod name
POD_NAME=sysdig-mysql8-mariadb-conj-auth-migration

# Image name
IMAGE_NAME=quay.io/sysdig/onprem_migration:mysql8-mariadb-conj-auth-migration-1.0.0

# Default YAML definition
K8S_YAML_TEXT_DEFAULT="
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: sysdigcloud
    role: mysql8-mariadb-conj-auth-migration
  name: ${POD_NAME}
spec:
  restartPolicy: Never
  containers:
    - name: mysql8-mariadb-conj-auth-migration
      image: ${IMAGE_NAME}
      env:
        - name: MYSQL_HOST
          valueFrom:
            configMapKeyRef:
              name: sysdigcloud-config
              key: mysql.endpoint
        - name: MYSQL_PORT
          value: \"3306\"
        - name: MYSQL_ROOT_USER
          value: \"root\"
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            configMapKeyRef:
              name: sysdigcloud-config
              key: mysql.password
        - name: SYSDIG_ADMIN_USER
          valueFrom:
            configMapKeyRef:
              name: sysdigcloud-config
              key: mysql.user
        - name: SYSDIG_ADMIN_PASSWORD
          valueFrom:
            configMapKeyRef:
              name: sysdigcloud-config
              key: mysql.password
"

# Custom YAML definition - single quotes defer variable expansion
K8S_YAML_TEXT_CUSTOM_TEMPLATE='
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: sysdigcloud
    role: mysql8-mariadb-conj-auth-migration
  name: ${POD_NAME}
spec:
  restartPolicy: Never
  containers:
    - name: mysql8-mariadb-conj-auth-migration
      image: ${IMAGE_NAME}
      env:
        - name: MYSQL_HOST
          valueFrom:
            configMapKeyRef:
              name: sysdigcloud-config
              key: mysql.endpoint
        - name: MYSQL_PORT
          value: \"${MYSQL_PORT}\"
        - name: MYSQL_ROOT_USER
          value: \"${MYSQL_ROOT_USER}\"
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: mysql8-mariadb-conj-auth-migration-secret
              key: password
        - name: SYSDIG_ADMIN_USER
          valueFrom:
            configMapKeyRef:
              name: sysdigcloud-config
              key: mysql.user
        - name: SYSDIG_ADMIN_PASSWORD
          valueFrom:
            configMapKeyRef:
              name: sysdigcloud-config
              key: mysql.password
'

K8S_SECRET_PASSWORD_TEMPLATE='
apiVersion: v1
kind: Secret
metadata:
  name: mysql8-mariadb-conj-auth-migration-secret
type: Opaque
stringData:
  password: \"${MYSQL_ROOT_PASSWORD}\"
'

EXIT_CODE=0

################################################################################
# Script beginning
################################################################################

echo "Sysdig MySQL to MariaDB Connector Migration Tool"
echo "Please enter the required values (press Enter for default)."

# Read context and namespace
read -p "Sysdig Kubernetes context (default current-context): " KUBERNETES_CONTEXT
if [ -z ${KUBERNETES_CONTEXT} ]; then
  KUBERNETES_CONTEXT=$(kubectl config current-context);
fi
read -p "Sysdig Kubernetes namespace (default sysdigcloud): " KUBERNETES_NAMESPACE
if [ -z ${KUBERNETES_NAMESPACE} ]; then
  KUBERNETES_NAMESPACE=sysdigcloud;
fi
echo

KUBECTL_CMD="kubectl --context=${KUBERNETES_CONTEXT} -n ${KUBERNETES_NAMESPACE}"

# Try to perform the migration with the default YAML
echo "Running the migration script with default parameters."
echo "${K8S_YAML_TEXT_DEFAULT}" | eval "${KUBECTL_CMD} create -f -"
while true; do
  status=$(eval "${KUBECTL_CMD} describe pods ${POD_NAME} | grep \"Status:[ \t]*\"")
  is_running=$(echo ${status} | grep "Pending\|Running" || true)
  if [ -z "${is_running}" ]; then
    break
  fi
done

is_succeeded=$(echo ${status} | grep Succeeded || true)

# Default YAML succeeded --> Exit the script
if [ -n "${is_succeeded}" ]; then
  echo
  # Print the logs
  eval "${KUBECTL_CMD} logs ${POD_NAME}"
  echo
  # Cleanup
  echo "${K8S_YAML_TEXT_DEFAULT}" | eval "${KUBECTL_CMD} delete -f -"
  docker rmi -f ${IMAGE_NAME}
  exit $EXIT_CODE
fi

# Default YAML failed --> Cleanup and ask for custom parameters
echo "${K8S_YAML_TEXT_DEFAULT}" | eval "${KUBECTL_CMD} delete -f -"
echo

echo "Custom parameters required, please enter the values in the following prompts."
read -p "MySQL port (default 3306): " MYSQL_PORT
if [ -z "${MYSQL_PORT}" ]; then
  MYSQL_PORT=3306
fi
read -p "MySQL root username (default root): " MYSQL_ROOT_USER
if [ -z "${MYSQL_ROOT_USER}" ]; then
  MYSQL_ROOT_USER=root
fi
read -sp "MySQL root password:" MYSQL_ROOT_PASSWORD
echo
echo

echo "Running the migration script with custom parameters."
eval "K8S_SECRET_PASSWORD=\"$K8S_SECRET_PASSWORD_TEMPLATE\""
echo "${K8S_SECRET_PASSWORD}" | eval "${KUBECTL_CMD} create -f -"

# Try to perform the migration with the custom YAML
eval "K8S_YAML_TEXT_CUSTOM=\"$K8S_YAML_TEXT_CUSTOM_TEMPLATE\""
echo "${K8S_YAML_TEXT_CUSTOM}" | eval "${KUBECTL_CMD} create -f -"
while true; do
  status=$(eval "${KUBECTL_CMD} describe pods ${POD_NAME} | grep \"Status:[ \t]*\"")
  is_running=$(echo ${status} | grep "Pending\|Running" || true)
  if [ -z "${is_running}" ]; then
    break
  fi
done
echo

# Print the logs
eval "${KUBECTL_CMD} logs ${POD_NAME}"
is_succeeded=$(echo ${status} | grep Succeeded || true)
# If failed, inform the user and set the exit code to 1
if [ -z "${is_succeeded}" ]; then
  (>&2 echo "Failure: Please run the tool with correct parameters.")
  EXIT_CODE=1
fi
echo

# Cleanup
echo "${K8S_YAML_TEXT_CUSTOM}" | eval "${KUBECTL_CMD} delete -f -"
echo "${K8S_SECRET_PASSWORD}" | eval "${KUBECTL_CMD} delete -f -"
docker rmi -f ${IMAGE_NAME}
exit $EXIT_CODE
