# Cloud Custodian Policies

[![CircleCI](https://circleci.com/gh/jimrazmus/c7n-policies/tree/master.svg?style=svg)](https://circleci.com/gh/jimrazmus/c7n-policies/tree/master)

This repo contains policy documents that Cloud Custodian will consume.

Cloud Custodian is a tool that unifies the dozens of tools and scripts most organizations use for managing their AWS accounts into one open source tool. It’s a stateless rules engine for policy definition and enforcement, with metrics and detailed reporting for AWS.

Read the [Cloud Custodian documentation](http://www.capitalone.io/cloud-custodian/docs/) for more details.

## Policy Validation

Policies are automatically validated via [CircleCI](https://circleci.com/gh/jimrazmus/c7n-policies/tree/master). It runs Cloud Custodian in a Docker container that includes:

* Python version 2.7.14
* Cloud Custodian version 0.8.43.1

## AWS Account Installation

Leverage CloudFormation and these templates as a reference for creating message queues and a role for the lambdas to run:

* [c7nSQSMessageQueues-CloudFormation.yml](c7n-core/c7nSQSMessageQueues-CloudFormation.yml)
* [c7nLambdaExecutionRole-CloudFormation.yml](c7n-core/c7nLambdaExecutionRole-CloudFormation.yml)

## Policy Anatomy

One or more policies are defined in a yaml file. A policy specifies the following items:

* The type of resource to run the policy against
* Filters to select the set of target resources
* Actions to take on the filtered set of resources

Policies can be run from your laptop or as AWS Lambdas.
