import json
import boto3
import logging

logging.basicConfig(format='%(levelname)s %(message)s', level=logging.INFO)

#def lambda_handler(event, context):
def main():
    client = boto3.client('cloudfront')
    response = client.list_distributions(
        MaxItems='10000'
    )
    
    logging.debug(response['DistributionList']['Items'])
    distributionListLen = len(response['DistributionList']['Items'])
    logging.info('CloudFront Distributions: %s', distributionListLen)
    
    #return {
    #    'statusCode': 200,
    #    'body': json.dumps(response)
    #    'body': len(response.keys())
    #}

# Calling Main     
if __name__ == '__main__': 
    main() 