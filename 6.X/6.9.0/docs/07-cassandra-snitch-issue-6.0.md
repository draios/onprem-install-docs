<!-- Space: TOOLS -->
<!-- Parent: Installer -->
<!-- Title: Cassandra Snitch Issue When Upgrading to 6.0 -->
<!-- Layout: plain -->

<br />

<!-- Include: ac:toc -->

<br />

# Potential Breaking Changes to the Cassandra Snitch for Existing 6.X installations

- In OnPrem 6.0 we are making changes to the Cassandra snitch we use for MultiAZ environments

- Below is an example of how to work around this issue when running in AWS's `us-east-1` region

- The Cassandra snitch is how Cassandra determines the "rack" or availability zone (AZ) for each node, a datum that needs to be extracted from the Kubernetes worker where the Cassandra Pod will be running and is used by Cassandra for the correct data distribution and redundancy

- In the past, we used 3 types of snitches:

    - `Ec2Snitch` for AWS

    - `GoogleCloudSnitch` for GKE

    - `customGossipingPropertyFileSnitch` A custom snitch based on our own tool to extract AZ from the Kubernetes Nodes

- Starting from 6.x, we will use `customGossipingPropertyFileSnitch` on all environments.

- This could however cause issues in certain cases because the way the AZ is extracted from the Kubernetes worker could change between snitch types and cause a Cassandra blocking error during its bootstrap:

```
Cannot start node if snitch's rack (us-east-1b) is different from the previous rack (1b)
```

- The error is already informative about what's happening: we used to provide Cassandra with a rack of `1b` but now we are providing a value of `us-east-1b`: it looks like we need to remove `us-east-`

- The workaround is to adapt (or provide) the extract command `.sysdig.cassandra.snitch.extractCMD` so that it will produce the same result as what is already in the rack:

    - get a nodetool status and check the rack values

```
kubectl exec -n sysdig -c cassandra sysdigcloud-cassandra-0 -- nodetool status
Datacenter: us-east
===================
Status=Up/Down
|/ State=Normal/Leaving/Joining/Moving
--  Address         Load       Tokens       Owns (effective)  Host ID                               Rack
UN  100.125.83.62   21.11 GiB  256          100.0%            7dd82145-e7fd-48c0-beb1-80a8dea1aa79  1a
UN  100.96.88.26    21.48 GiB  256          100.0%            a5f59a17-037c-4aaf-a024-e2c24e9df1fc  1d
UN  100.103.18.141  20.97 GiB  256          100.0%            03e38629-5a31-470a-9513-e7c5fdd40040  1b
```

  - get the content of the label (either from the Kubernetes workers or from executing the following command after exec'ing inside the Cassandra Pod, container `cassandra`:

```
kubectl exec -n sysdig -c cassandra sysdigcloud-cassandra-0 -- bash -c "cat /node-labels/failure-domain.beta.kubernetes.io/zone || cat /node-labels/topology.kubernetes.io/zone"
us-east-1b
```

  - submit the label content to the shell command to extract the correct value (the following is just an example and does not constitute a standard to follow):

```
echo "us-east-1b" | sed 's/us-east-//'
1b
```

  - You can now use the command in `.sysdig.cassandra.snitch.extractCMD` in your `values.yaml` (keeping in mind this is executed inside the `cassandra` container during the Cassandra bootstrap:

```
sysdig:
  cassandra:
    snitch:
      extractCMD: "cat /node-labels/failure-domain.beta.kubernetes.io/zone || cat /node-labels/topology.kubernetes.io/zone | sed 's/us-east-//'"
```

  - please keep in mind that at this stage we are not showing this change in the `installer diff` output because the value is being calculated at run time inside the Cassandra container.
