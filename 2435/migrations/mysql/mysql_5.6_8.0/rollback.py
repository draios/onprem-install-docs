#!/usr/bin/env python

import argparse
import subprocess

import yaml

CONTEXT = None
NAMESPACE = None
DRY_RUN = False


def parse_cli():
    global CONTEXT, NAMESPACE, DRY_RUN
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--deployment-yaml",
        required=True,
        help="Yaml that contains the existing mysql deployment"
    )
    parser.add_argument(
        "--namespace",
        required=True,
        help="Namespace that sysdig is running in"
    )
    parser.add_argument(
        "--kube-context",
        required=False,
        help="Kubectl context (not required if kubectl context is set before with - kubectl config use-context <context_name>)"
    )
    parser.add_argument(
        "--dry-run",
        default=False,
        action='store_true',
        help="Dry run"
    )
    args = parser.parse_args()
    CONTEXT = args.kube_context
    NAMESPACE = args.namespace
    DRY_RUN = args.dry_run
    return args


def get_yaml_objects(yaml_file):
    dicts = []
    with open(yaml_file, 'r') as stream:
        docs = yaml.safe_load_all(stream)
        for doc in docs:
            y = doc.copy()
            dicts.append(y)
    return dicts


def get_service_yaml(yaml_file):
    dicts = get_yaml_objects(yaml_file)
    for item in dicts:
        if "kind" in item and str(item["kind"]).lower() == "service":
            return item["metadata"]["name"]


def run_command(cmd, shell=False):
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
        return out, err, p.returncode


def apply_yaml(json_contents):
    for item in json_contents:
        yaml_contents = yaml.dump(item, default_flow_style=False)
        yaml_contents = str(yaml_contents).replace("\"", "\\\"").replace("$", "\$")
        # pprint.pprint(yaml_contents)
        cmd = "echo \"{yaml_contents}\" | kubectl --context {context} -n {ns} apply --force -f -".format(
            ns=NAMESPACE,
            context=CONTEXT,
            yaml_contents=yaml_contents
        )
        out, err, return_code = run_command(cmd, shell=True)


if __name__ == "__main__":
    args = parse_cli()
    deployment_service = get_service_yaml(args.deployment_yaml)
    apply_yaml(deployment_service)
