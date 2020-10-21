#!/usr/bin/env python

import argparse
import json
import os
import re
import subprocess
import sys
import time

import yaml

CONTEXT = None
NAMESPACE = None
DRY_RUN = False


def parse_cli():
    global CONTEXT, NAMESPACE, DRY_RUN
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--router-yaml",
        required=True,
        help="Yaml that contains the mysql router"
    )
    parser.add_argument(
        "--cluster-yaml",
        required=True,
        help="Yaml that contains the mysql cluster"
    )
    parser.add_argument(
        "--deployment-yaml",
        required=True,
        help="Yaml that contains the existing mysql deployment"
    )
    parser.add_argument(
        "--upgrade-yaml",
        required=True,
        help="Yaml that contains the upgrade pod"
    )
    parser.add_argument(
        "--namespace",
        required=True,
        help="Namespace that sysdig is running in"
    )
    parser.add_argument(
        "--leave-old-db",
        required=False,
        default=True,
        action='store_false',
        help="Leave old mysql running behind service named sysdigcloud-mysql-old"
    )
    parser.add_argument(
        "--storageclass-name",
        required=True,
        help="Storageclassname that will be used in the mysql cluster and the mysql upgrade pod. This needs to exist before running this script."
    )
    parser.add_argument(
        "--kube-context",
        required=True,
        help="Kubectl context (not required if kubectl context is set before with - kubectl config use-context <context_name>)"
    )
    parser.add_argument(
        "--dry-run",
        default=False,
        action='store_true',
        help="Dry run"
    )
    parser.add_argument(
        "--dont-cleanup-job",
        default=False,
        action='store_true',
        help="Dry run"
    )
    args = parser.parse_args()
    CONTEXT = args.kube_context
    NAMESPACE = args.namespace
    DRY_RUN = args.dry_run
    return args


def kubectl_json_cmd(cmdstr):
    """
    run a kubelet command as if on the shell... sorta.
    Adds the context and '-o json' to all commands.

    Returns the parsed json.
    """
    cmdlist = cmdstr.split()
    try:
        cmdlist.remove('kubectl')
    except ValueError:
        pass
    cmdlist = ["kubectl", "--context", CONTEXT, "-n", NAMESPACE, "-o", "json"] + cmdlist
    output = subprocess.check_output(cmdlist)
    return json.loads(output)


def run_command(cmd, shell=False, fail_on_stderr=False):
    """
    If `cmd` will be a string with more than one word, `shell=True` must be set.
    If `cmd` will be a list, `shell` should be `False` (default setting).
    If doing multiple commands in the same `run_command()` call, require a string.
    """
    if DRY_RUN:
        print cmd
        return "", "", 0
    else:
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=shell)
        out, err = p.communicate()
        if err:
            print "------- Found Stderr!! -----------"
            print "out = {out}".format(out=out)
            print "err = {err}".format(err=err)
            print "exit code = {n}".format(n=p.returncode)
            if fail_on_stderr:
                raise Exception(err)
        return out, err, p.returncode


def check_for_executables(executable_list):
    for executable in executable_list:
        out, err, returncode = run_command(['which', executable])
        if executable not in out:
            sys.exit("Could not find executable ({executable}) in your $PATH".format(executable=executable))


def get_service_yaml(yaml_file):
    dicts = get_yaml_objects(yaml_file)
    for item in dicts:
        if "kind" in item and str(item["kind"]).lower() == "service":
            return item["metadata"]["name"]


def patch_router_yaml(yaml_file, tmp_mysql8_service):
    dicts = get_yaml_objects(yaml_file)
    for item in dicts:
        if "kind" in item and str(item["kind"]).lower() == "service":
            item["metadata"]["name"] = tmp_mysql8_service
    return dicts


def patch_cluster_yaml(yaml_file, storageclass_name):
    dicts = get_yaml_objects(yaml_file)
    for item in dicts:
        if "spec" in item and "volumeClaimTemplates" in item["spec"]:
            for pvc in item["spec"]["volumeClaimTemplates"]:
                if "spec" in pvc and "storageClassName" in pvc["spec"]:
                    pvc["spec"]["storageClassName"] = storageclass_name
    return dicts


def wait_for_3_pods(services):
    # wait up to 15 mins
    wait_time = 15 * 60
    start_time = int(time.time())
    while int(time.time()) < start_time + wait_time:
        time.sleep(15)
        succeed = True
        for service in services:
            cmd = "kubectl --context {context} -n {ns} get pods | grep {service}".format(
                ns=NAMESPACE,
                context=CONTEXT,
                service=service
            )
            out, err, exit_code = run_command(cmd, shell=True)
            ready_count = 0
            container_set = set()
            for word in str(out).split():
                if word == "Running":
                    ready_count += 1
                match = re.search("[0-9]+/[0-9]+", word)
                if match:
                    container_set.add(match.group(0))
            print ("Found {n} running pods for {service}".format(n=ready_count, service=service))
            print ("Found {set} running containers for {service}".format(set=container_set, service=service))
            if ready_count != 3 or len(container_set) != 1:
                succeed = False
        if succeed:
            return
    print "Cluster pods failed to start. Please check your cluster for the pods using the following commands:"
    for service in services:
        print "kubectl --context {context} -n {ns} get pods | grep ^{service}".format(
            ns=NAMESPACE,
            context=CONTEXT,
            service=service
        )
    sys.exit("Exiting")


def patch_upgrade_yaml(yaml_file, storageclass_name):
    dicts = get_yaml_objects(yaml_file)
    for item in dicts:
        if item["kind"] == "PersistentVolumeClaim":
            if "spec" in item and "storageClassName" in item["spec"]:
                item["spec"]["storageClassName"] = storageclass_name
    return dicts


def get_yaml_objects(yaml_file):
    dicts = []
    with open(yaml_file, 'r') as stream:
        docs = yaml.safe_load_all(stream)
        for doc in docs:
            y = doc.copy()
            dicts.append(y)
    return dicts


def apply_yaml(json_contents):
    # kubectl apply --force -f
    if not isinstance(json_contents, list):
        json_contents = [json_contents]
    for item in json_contents:
        yaml_contents = yaml.dump(item, default_flow_style=False)
        yaml_contents = str(yaml_contents).replace("\"", "\\\"").replace("$", "\$")
        # pprint.pprint(yaml_contents)
        cmd = "echo \"{yaml_contents}\" | kubectl --context {context} -n {ns} apply --force -f -".format(
            ns=NAMESPACE,
            context=CONTEXT,
            yaml_contents=yaml_contents
        )
        # print (cmd)
        out, err, return_code = run_command(cmd, shell=True)
        if err:
            print "------ kubectl command got an error ----------"
            print "out = {out}".format(out=out)
            print "err = {err}".format(err=err)
            print "return code = {rc}".format(rc=return_code)


def patch_service(yaml_file, postfix_string):
    # pull service yaml out of the file
    # return service section adding the postfix_string to the end of the service name
    dicts = get_yaml_objects(yaml_file)
    for doc in dicts:
        if "kind" in doc and str(doc["kind"]).lower() == "service":
            doc["metadata"]["name"] = "{name}{postfix}".format(name=doc["metadata"]["name"], postfix=postfix_string)
            return doc


def wait_for_upgrade(job_name):
    cmd = "kubectl --context {context} -n {ns} wait --for=condition=complete --timeout=1800s job/{name}".format(
        ns=NAMESPACE,
        context=CONTEXT,
        name=job_name
    )
    out, err, return_code = run_command(cmd, shell=True)


def cleanup_job(job_name):
    cmd = "kubectl --context {context} -n {ns} delete job {name}".format(
        ns=NAMESPACE,
        context=CONTEXT,
        name=job_name
    )
    out, err, return_code = run_command(cmd, shell=True)


if __name__ == "__main__":
    args = parse_cli()
    if not DRY_RUN:
        check_for_executables(['kubectl'])

    print ("Checking input files")
    for file in [args.upgrade_yaml, args.router_yaml, args.cluster_yaml, args.deployment_yaml]:
        if not os.path.isfile(file):
            sys.exit("File provided does not exist: {file}".format(file=file))
    deployment_service = get_service_yaml(args.deployment_yaml)

    # output modified yamls (mysql router service needs to have it's service name changed to
    # {deplpoyment_service}-8 to not collide with existing mysql service)
    tmp_mysql8_service = "{ds}-8".format(ds=deployment_service)

    print ("Deploying router yaml")
    # apply a modified router yaml that has its service name changed to tmp_mysql8_service
    modified_router_yaml = patch_router_yaml(args.router_yaml, tmp_mysql8_service)
    apply_yaml(modified_router_yaml)

    print ("Deploying cluster yaml")
    # apply a modified cluster yaml that has its storageclassname set
    modified_cluster_yaml = patch_cluster_yaml(args.cluster_yaml, args.storageclass_name)
    apply_yaml(modified_cluster_yaml)

    # wait for 3 pods ready for the following sts/deployment (prefix values in a list)
    print ("Waiting for mysql cluster")
    if not DRY_RUN:
        wait_for_3_pods(["sysdigcloud-mysql-cluster", "sysdigcloud-mysql-router"])
    print ("Mysql HA cluster is running")

    # start the upgrade using the upgrade yaml and set the storageclassname
    print ("Running the mysql dump and restore to mysql8")
    start = int(time.time())
    modified_upgrade_yaml = patch_upgrade_yaml(args.upgrade_yaml, args.storageclass_name)
    apply_yaml(modified_upgrade_yaml)
    wait_for_upgrade("mysql-upgrade-pod")
    end = int(time.time())
    print ("Database dump and restore took {n:.1f} mins".format(n=(end - start) / float(60)))
    if not args.dont_cleanup_job:
        cleanup_job("mysql-upgrade-pod")

    print ("Moving old mysql service aside (now called sysdigcloud-mysql-old)")
    # modify old 5.6 service name from sysdigcloud-mysql to sysdigcloud-mysql-old
    patched_service_yaml = patch_service(args.deployment_yaml, "-old")
    apply_yaml(patched_service_yaml)

    print ("Moving new mysql HA service into place for components to talk to")
    # modify new 8.0 service from sysdigcloud-mysql-8 to sysdigcloud-mysql
    cmd = "kubectl --context {context} -n {ns} delete service {service}".format(
        service=deployment_service,
        context=CONTEXT,
        ns=NAMESPACE
    )
    run_command(cmd, shell=True)
    mysql_service_yaml = patch_service(args.router_yaml, "")
    apply_yaml(mysql_service_yaml)
    cmd = "kubectl --context {context} -n {ns} delete service {service}".format(
        service=tmp_mysql8_service,
        context=CONTEXT,
        ns=NAMESPACE
    )
    run_command(cmd, shell=True)

    # TODO optionally leave old mysql database running
    print ("Leaving old mysql deployment running at sysdigcloud-mysql-old endpoint")
    print ("Once this migration is verified, delete the old deployment and service")

    print("Done")
