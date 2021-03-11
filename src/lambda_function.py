import os
import json
import boto3
import logging

if 'loglevel' in os.environ:
    loglevel = os.environ['loglevel']
else:
    loglevel = 'INFO'

if len(logging.getLogger().handlers) > 0:
    # The Lambda environment pre-configures a handler logging to stderr. If a handler is already configured,
    # `.basicConfig` does not execute. Thus we set the level directly.
    logging.getLogger().setLevel(loglevel)
else:
    logging.basicConfig(format='%(levelname)s %(message)s', level=loglevel)



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

def main(event, context):
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
    main('event', 'context') #gambi para funcionar local e no lambda