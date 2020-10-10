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

    # TODO: need to implement request body validation
    if "body" in event:
        body = json.loads(base64.b64decode(event["body"]))
        customer = Customer(ddb, table)
        customer.set_given_name(body["given_name"])
        customer.set_family_name(body["family_name"])
        customer.set_birthdate(body["birthdate"])
        customer.set_email(body["email"])
        customer.set_phone_number(body["phone_number"])
        customer.set_phone_number_verified(body["phone_number_verified"])
        response = customer.create()        
    else:
        response = {
            "ResponseMetadata": {
                "ErrorMessage": "Request body is missing",
                "ErrorType": "InputError",
                "HTTPStatusCode": 500
            }
        }

    status = response["ResponseMetadata"]["HTTPStatusCode"]
    payload = str(customer) if status == 200 else json.dumps(response)
    output = build_response(status, payload)
    return output


# initialization, mapping
ddb = boto3.client("dynamodb")
table = os.environ["TABLE"]