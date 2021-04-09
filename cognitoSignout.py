import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import json
  
def lambda_handler(event, context):
    client = boto3.client('cognito-idp')
    if event.get("access_token") is None:
            return  {"error": True, 
                "success": False, 
                "message": "access_token is required", 
                "data": None}
    resp = client.global_sign_out(AccessToken=event.get("access_token"))
    print(resp)