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
    if "version" in event and event["version"] == "2.0":
        method = event["requestContext"]["http"]["method"]
    else:
        method = event["requestContext"]["httpMethod"]

    if method == "GET":
        status = 200
        body = json.dumps(event)
        output = build_response(status, body)

    elif method == "POST":
        status = 200
        body = json.dumps(event)
        output = build_response(status, body)

    print(output)
    return output
