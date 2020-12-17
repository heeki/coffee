import boto3
import json


class Image:
    def __init__(self, bucket):
        self.client = boto3.client('rekognition')
        self.bucket = bucket

    def get_labels(self, okey):
        response = self.client.detect_text(
            Image={
                "S3Object": {
                    "Bucket": self.bucket,
                    "Name": okey
                }
            }
        )
        return response

    def get_values(self, response):
        values = []
        for detection in response["TextDetections"]:
            del(detection["Geometry"])
            if detection["Type"] == "WORD":
                try:
                    value = int(detection["DetectedText"])
                    values.append(value)
                except ValueError:
                    continue
        if len(values) == 9:
            keys = ["Total", "Coffee", "Cappuccino", "Espresso", "Latte Macchiato", "Macchiato", "Flat White", "Hot Chocolate", "Extra Milk"]
            output = {}
            for i in range(len(keys)):
                output[keys[i]] = values[i]
        elif len(values) > 1:
            output = {
                "Total": values[0],
                "Extra Milk": values[-1]
            }
        elif len(values) == 1:
            output = {
                "Total": values[0]
            }
        else:
            output = {}
        return output
