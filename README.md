# softcomweb-cdk

## Bootstrap directory
This directory contains scripts to bootstrap our AWS accounts for usage with AWS CDK

### Usage
To bootstrap a new AWS Account,
1. get credentials via awsume
2. run ./bin/bootstrap-deploy

The last command will create a new cloudformation stack called `CDKToolKit`

NOTE: You can create a cdk-bootstrap.yaml file and modify this to suite you need by running the following command `npx cdk bootstrap --show-template > cdk-bootstrap.yaml`

