import base64
import boto3
import json
import os
from lib.response import success, failure
from lib.customer import Customer


# function: lambda invoker handler
def handler(event, context):
    # TODO: need to implement request body validation
    body = json.loads(base64.b64decode(event["body"]))
    customer = Customer(ddb, table)
    customer.set_given_name(body["given_name"])
    customer.set_family_name(body["family_name"])
    customer.set_birthdate(body["birthdate"])
    customer.set_email(body["email"])
    customer.set_phone_number(body["phone_number"])
    customer.set_phone_number_verified(body["phone_number_verified"])

    response = customer.create()
    status = response["ResponseMetadata"]["HTTPStatusCode"]
    payload = json.dumps(response)
    output = success(payload) if status == 200 else failure(payload)
    print(output)
    return output


# initialization, mapping
ddb = boto3.client("dynamodb")
table = os.environ["TABLE"]