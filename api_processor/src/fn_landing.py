import base64
import boto3
import json
import os
from lib.landing import Landing

# helper functions
def build_response(code, body):
    # headers for cors
    headers = {
        "Access-Control-Allow-Origin": "amazonaws.com",
        "Access-Control-Allow-Credentials": True
    }

    # lambda proxy integration
    response = {
        'isBase64Encoded': False,
        'statusCode': code,
        'headers': headers,
        'body': body
    }

    return response

# function: lambda invoker handler
def handler(event, context):
    print(json.dumps(event))
    method = event["requestContext"]["http"]["method"] 
    l = Landing()

    if method == "GET":
        payload = l.create_presigned_url_put(bucket)
        output = build_response(200, json.dumps(payload))
    else:
        output = build_response(200, json.dumps(event))

    print(output)
    return output

# initialization
bucket = os.environ["BUCKET"]