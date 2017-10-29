# Cloud Custodian Policies

This repo contains the policy documents that the Cloud Custodian program will consume.

Cloud Custodian is a tool that unifies the dozens of tools and scripts most organizations use for managing their AWS accounts into one open source tool. It’s a stateless rules engine for policy definition and enforcement, with metrics and detailed reporting for AWS.

Read the [Cloud Custodian documentation](http://www.capitalone.io/cloud-custodian/docs/) for more details.

## Client Installation

### Cloud Custodian

I use the [developer installation](http://www.capitalone.io/cloud-custodian/docs/developer/installing.html) of Cloud Custodian to keep up with the rapid improvements and new features.

You will find the 'custodian' program in your path when the installation is completed successfully. Verify by running the following command.

```
#> custodian version
```

### c7n Policies Repository

Check out a copy of this code repository if you haven't already. All policy documents are managed here.

## AWS Account Installation

### Message Queues and Lambda Execution Role

Leverage CloudFormation to install these templates:

* [c7nSQSMessageQueues-CloudFormation.yml](c7n-core/c7nSQSMessageQueues-CloudFormation.yml)
* [c7nLambdaExecutionRole-CloudFormation.yml](c7n-core/c7nLambdaExecutionRole-CloudFormation.yml)

## Policy Anatomy

One or more policies are defined in a yaml file. A policy specifies the following items:

* The type of resource to run the policy against
* Filters to narrow down the set of resources
* Actions to take on the filtered set of resources

Policies can be run from your laptop or as AWS Lambdas.
