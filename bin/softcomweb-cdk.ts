#!/usr/bin/env node
import 'source-map-support/register';
import * as cdk from '@aws-cdk/core';
import { SoftcomwebCdkStack } from '../lib/softcomweb-cdk-stack';

const app = new cdk.App();
new SoftcomwebCdkStack(app, 'SoftcomwebCdkStack');
