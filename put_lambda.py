# import the json utility package since we will be working with a JSON object
import json
# import the AWS SDK (for Python the package name is boto3)
import boto3
# import two packages to help us with dates and date formatting
from time import gmtime, strftime
#import uuid for key creation
import uuid

s3 = boto3.resource('s3')


# define the handler function that the Lambda service will use as an entry point
def lambda_handler(event, context):
    
    now = strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
    
    value = uuid.uuid4()
    key = str(value) + '.json'
    object = s3.Object('thegrandexchange', key)
#create new keys for dictionary    
    event['creation_date'] = now
    event['uuid'] = str(value)
#put data into json file
    object.put(Body=json.dumps(event))
    

# return a properly formatted JSON object
    return {
        'statusCode': 200,
        'body': event
    }