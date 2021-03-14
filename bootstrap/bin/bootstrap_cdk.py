import json
import inquirer
import boto3
import os
import sys
import subprocess

def select_account():
  orga_client = boto3.client('organizations')
  accounts = []
  paginator = orga_client.get_paginator('list_accounts')
  page_iterator = paginator.paginate()
  for page in page_iterator:
    for account in page['Accounts']:
      accounts.append(account)
  choice = inquirer.list_input(
    "Select an AWS Account",
    choices=list(map(lambda acc: (acc['Name'], acc['Id'], acc['Status']), accounts))
  )
  return choice

def select_region(account_id):

  client = _assumed_role(account_id, 'selectRegion', 'ec2')
  regions = [region['RegionName'] for region in client.describe_regions()['Regions']]
  choice = inquirer.list_input(
    "Select an AWS Region",
    choices=regions,
    default='eu-central-1'
  )
  return choice
def _assumed_role(account_id, role_name, client=None):
  role_arn = f"arn:aws:iam::{account_id}:role/OrganizationAccountAccessRole"
  assumed_role = boto3.client('sts').assume_role(
    RoleArn=role_arn,
    RoleSessionName=role_name
  )
  if(client):
    return boto3.client(
      client,
      aws_access_key_id=assumed_role['Credentials']['AccessKeyId'],
      aws_secret_access_key=assumed_role['Credentials']['SecretAccessKey'],
      aws_session_token=assumed_role['Credentials']['SessionToken'],
    )
  return {
    'keyId': assumed_role['Credentials']['AccessKeyId'],
    'secretId': assumed_role['Credentials']['SecretAccessKey'],
    'sessionToken': assumed_role['Credentials']['SessionToken']
  }
def deploy_cdk(account, aws_region, infra_account_id):
  print(f">> Accessing Account: {account[0]} with ID: {account[1]} for region {aws_region}")
  aws_session = _assumed_role(account[1], 'cdk_role')
  my_env = os.environ.copy()
  my_env['AWS_ACCESS_KEY_ID'] = aws_session['keyId']
  my_env['AWS_SECRET_ACCESS_KEY'] = aws_session['secretId']
  my_env['AWS_SESSION_TOKEN'] = aws_session['sessionToken']
  my_env['CDK_NEW_BOOTSTRAP'] = '1'

  process = subprocess.run(
    [
      'cdk',
      'bootstrap',
      '--cloudformation-execution-policies',
      'arn:aws:iam::aws:policy/AdminstratorAccess',
      '--trust',
      infra_account_id,
      f'aws://{account[1]}/aws_region'
    ],
    stdout=sys.stdout,
    stderr=sys.stderr,
    stdin=subprocess.DEVNULL,
    env=my_env,
    universal_newlines=True
  )



account = select_account()
region = select_region(account[1])
deploy_cdk(account, region, "1111111111111")
