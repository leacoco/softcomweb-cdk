#!/usr/bin/env node
import * as cdk from '@aws-cdk/core';
import * as setting from '../common/settings'
import { SoftcomwebCdkStack } from '../lib/softcomweb-cdk-stack';

const app = new cdk.App();

cdk.Tags.of(app).add("team", "dev", {
  applyToLaunchedInstances: true,
});

cdk.Tags.of(app).add("service", "softcomwebservice", {
  applyToLaunchedInstances: true
})

new SoftcomwebCdkStack(app, 'SoftcomwebCdkStack', {
  bucketName: "softcomweb-bucket",
  bucketVersioning: false
});
