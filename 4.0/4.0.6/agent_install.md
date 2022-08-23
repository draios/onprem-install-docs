# Agent Install

The Sysdig agent can be installed along with Sysdig Monitor and/or Sysdig Secure, or by itself. This is determined by the value `apps` in the `values.yaml` file.

If you use the installer to add agent(s), note that not all of the agent configurations are enabled. You may need to do further edits in the agent config files. 

This section assumes you will run the agent container as a Kubernetes pod, which then enables the Sysdig agent automatically to detect and monitor your Kubernetes environment. To set up the agent, you need the api key for agent from the settings menu in Sysdig Monitor/Sysdig Secure. Instructions for retrieving the api key can be found [here](https://docs.sysdig.com/en/agent-installation--overview-and-key.html).

If you are setting up both Monitor and Agent together, you can provide a blank value for the `agent.apiKey`. The agent will be launched with the appropriate api key and the value updated in the `values.yaml` file.

- Copy the current version sysdig-chart/values.yaml to your working directory.

  ```bash
  wget https://raw.githubusercontent.com/draios/sysdigcloud-kubernetes/installer/installer/values.yaml
  ```

- The following values are necessary for setting up Sysdig Agent. Edit the values.yaml to contain the following values:

  - [`apps`](configuration_parameters.md#apps): Specifies the Sysdig Platform components to be installed. Make sure `agent` is one of the values here.
  - [`size`](configuration_parameters.md#size): Specifies the size of the cluster. Size
    defines CPU and Memory limits for the Agent Pods. Valid options are: small, medium and
    large.
  - [`agent.apiKey`](configuration_parameters.md#agentapikey): Sysdig Agent api key for running agents.
  - [`agent.collectorEndpoint`](configuration_parameters.md#agentcollectorendpoint): Sysdig Collector Address
