# Description
This repository contain a code wrote in Python to check how many CloudFront Distribution are deployed in the AWS account.
Also is available CloudFormation code to deploy the solution.


# Architecture
![Diagrama](/images/cloudfrontDistLimitMonitor-accounts.png)

# Deploy
Step 1:

Create a ZIP file with lambda_function.py and upload to a Bucket S3

Step 2:

Create a CloudFormation stack to deploy all the services of this solution

aws cloudformation create-stack --stack-name cloudFrontLimitsMonitor --template-body file://deploy.yaml --parameters file://params.json --capabilities CAPABILITY_IAM

If necessary some chance use this command

aws cloudformation update-stack --stack-name cloudFrontLimitsMonitor --template-body file://deploy.yaml --parameters file://params.json --capabilities CAPABILITY_IAM
