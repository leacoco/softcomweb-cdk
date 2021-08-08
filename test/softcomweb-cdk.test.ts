import { expect as expectCDK, matchTemplate, MatchStyle } from '@aws-cdk/assert';
import * as cdk from '@aws-cdk/core';
import * as SoftcomwebCdk from '../lib/softcomweb-cdk-stack';

test('Empty Stack', () => {
    const app = new cdk.App();
    // WHEN
    const stack = new SoftcomwebCdk.SoftcomwebCdkStack(app, 'MyTestStack', {
      bucketName: "test-bucket",
      bucketVersioning: false
    });
    // THEN
    expectCDK(stack).to(matchTemplate({
      "Resources": {}
    }, MatchStyle.EXACT))
});
