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


# function: initialization
def initialization():
    pass


# function: lambda invoker handler
def handler(event, context):
    status = 200
    payload = event
    # payload = {
    #     "message": "hello world",
    #     "path": event["path"],
    #     "resource": event["resource"],
    #     "requestContext.path": event["requestContext"]["path"],
    #     "requestContext.resourcePath": event["requestContext"]["resourcePath"]
    # }
    output = build_response(status, json.dumps(payload))
    return output


# initialization, mapping
initialization()
