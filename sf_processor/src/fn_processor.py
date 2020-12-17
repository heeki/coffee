import base64
import boto3
import json
import os
from lib.image import Image


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


# function: lambda invoke handler
def handler(event, context):
    payload = []
    for record in event:
        print(json.dumps(record))
    # response = build_response(status, payload)
    return payload
