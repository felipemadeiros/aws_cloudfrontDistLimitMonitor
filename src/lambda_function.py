import json
import boto3
import logging

logging.basicConfig(format='%(levelname)s %(message)s', level=logging.INFO)

def publish_metric(metricValue):
    client = boto3.client('cloudwatch')
    client.put_metric_data(
        Namespace='CloudFront',
        MetricData=[
            {
                'MetricName': 'resourceCount',
                'Dimensions': [
                    {
                        'Name': 'Distribution Metrics',
                        'Value': 'Distributions'
                    },
                ],
                'Value': metricValue,
                'Unit': 'Count'
            },
        ]
    )

#def lambda_handler(event, context):
def main():
    client = boto3.client('cloudfront')
    response = client.list_distributions(
        MaxItems='10000'
    )
    
    logging.debug(response['DistributionList']['Items'])
    distributionListLen = len(response['DistributionList']['Items'])
    logging.info('CloudFront Distributions: %s', distributionListLen)
    
    publish_metric(distributionListLen)
    
    return {
        'statusCode': 200
    }

# Calling Main     
if __name__ == '__main__': 
    main() 