import boto3
import json
import os
from lib.response import success, failure


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
    output = success(json.dumps(payload)) if status == 200 else failure(json.dumps(payload))
    return output


# initialization, mapping
initialization()
