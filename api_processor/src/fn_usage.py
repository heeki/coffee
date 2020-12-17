import base64
import boto3
import json
import os


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

    if method == "GET":
        status = 200
        output = build_response(status, json.dumps(event))
    
    elif method == "POST":
        status = 200
        output = build_response(status, json.dumps(event))

    print(output)
    return output
