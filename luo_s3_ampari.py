AWSTemplateFormatVersion: 2010-09-09
Description: Mikon CloudFormation Demo

Resources:
    Ampari:
        Type: AWS::S3::Bucket

            Properties:
                BucketName: mikon-cloudformation-ampari


#validate template