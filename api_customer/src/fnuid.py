import base64
import boto3
import json
import os
from lib.customer import Customer


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
        uid = event["pathParameters"]["proxy"].rstrip('/')
        response = customer.get_uid(uid)
        status = response["HTTPStatusCode"]
        output = build_response(status, json.dumps(response["ResponseBody"]))

    print(output)
    return output


# initialization, mapping
ddb = boto3.client("dynamodb")
table = os.environ["TABLE"]
customer = Customer(ddb, table)