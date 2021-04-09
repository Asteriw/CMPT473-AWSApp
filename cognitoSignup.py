import boto3
import botocore.exceptions
import hmac
import hashlib
import base64
import json
USER_POOL_ID = 'us-east-1_b6HnaK2eM'
CLIENT_ID = '4tnka15q9dfg2si6rd9d44mncc'
CLIENT_SECRET = '1i3e81c7nqnjqkl9dcnd48ebmn629ieivs3umi37ib3lv9907n8r'
def get_secret_hash(username):
    msg = username + CLIENT_ID
    dig = hmac.new(str(CLIENT_SECRET).encode('utf-8'), 
        msg = str(msg).encode('utf-8'), digestmod=hashlib.sha256).digest()
    d2 = base64.b64encode(dig).decode()
    return d2

def lambda_handler(event, context):
    for field in ["username", "password"]:
        if not event.get(field):
            return {"error": False, "success": True, 'message': f"{field} is not present", "data": None}
    username = event['username']
    password = event["password"]
    client = boto3.client('cognito-idp')
    try:
        resp = client.sign_up(
            ClientId=CLIENT_ID,
            SecretHash=get_secret_hash(username),
            Username=username,
            Password=password, 
            UserAttributes=[
            {
                'Name': "name",
                'Value': username
            }
            ]
        )

        print(resp)
    
    
    except client.exceptions.UsernameExistsException as e:
        return {"error": False, 
               "success": True, 
               "message": "This username already exists", 
               "data": None}
    except client.exceptions.InvalidPasswordException as e:
        
        return {"error": False, 
               "success": True, 
               "message": "Password should have Caps,\
                          Special chars, Numbers", 
               "data": None}
    except client.exceptions.UserLambdaValidationException as e:
        return {"error": False, 
               "success": True, 
               "message": "Email already exists", 
               "data": None}
    
    except Exception as e:
        return {"error": False, 
                "success": True, 
                "message": str(e), 
               "data": None}
    
    return {"error": False, 
            "success": True, 
            "message": "You have successfully signed up", 
            "data": None}