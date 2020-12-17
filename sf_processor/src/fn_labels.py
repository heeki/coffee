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


def get_s3_bucket_key(record):
    bucket = ""
    okey = ""
    if "s3" in record:
        if "bucket" in record["s3"] and "name" in record["s3"]["bucket"]:
            bucket = record["s3"]["bucket"]["name"]
        if "object" in record["s3"] and "key" in record["s3"]["object"]:
            okey = record["s3"]["object"]["key"]
    return (bucket, okey)


# function: lambda invoke handler
def handler(event, context):
    payload = []
    for record in event["Records"]:
        (bucket, okey) = get_s3_bucket_key(record)
        print(json.dumps({"bucket": bucket, "okey": okey}))
        img = Image(bucket)
        data = img.get_labels(okey)
        status = data["ResponseMetadata"]["HTTPStatusCode"]
        payload.append(img.get_values(data))
    # response = build_response(status, payload)
    return payload
