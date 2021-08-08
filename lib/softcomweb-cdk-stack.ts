import * as cdk from '@aws-cdk/core';
import * as s3 from '@aws-cdk/aws-s3';
import * as dynamodb from '@aws-cdk/aws-dynamodb';

interface SoftcomwebCDKInterface {
  bucketName: string,
  bucketVersioning?: boolean,
}
export class SoftcomwebCdkStack extends cdk.Stack {
  constructor(scope: cdk.App, id: string, props: SoftcomwebCDKInterface) {
    super(scope, id);

    // Create an s3 bucket for softcomweb
    const bucket = new s3.Bucket(this, 'SoftcomwebBucket', {
      versioned: false,
      bucketName: props.bucketName,
      encryption: s3.BucketEncryption.S3_MANAGED,
      publicReadAccess: true,
      removalPolicy: cdk.RemovalPolicy.DESTROY
    });

    console.log(bucket);
    // // Create a dynamodb table
    // table = new dynamodb.Table(this, "SoftcomwebTable", {
    //   partitionKey: {
    //     name: 'pk',
    //     type: dynamodb.AttributeType.STRING
    //   }
    // })
  }
}
