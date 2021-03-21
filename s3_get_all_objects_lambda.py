# import the JSON utility package since we will be working with a JSON object
import json
import boto3

s3 = boto3.resource('s3')

# define the handler function that the Lambda service will use an entry point
def lambda_handler(event, context):
    result = []
    bucket = s3.Bucket('grandexchangeitems')
    for obj in bucket.objects.all():
        key = obj.key
        body = obj.get()['Body'].read().decode("utf-8") 
        result.append(body)

# return a properly formatted JSON object
    return {
    'statusCode': 200,
    'body': result
    }