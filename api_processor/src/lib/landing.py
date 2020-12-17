import boto3
import botocore.exceptions
import uuid

class Landing:
    def __init__(self):
        self.s3_client = boto3.client("s3")
    
    def create_presigned_url_put(self, bucket, expiration=300):
        okey = str(uuid.uuid4())
        try:
            response = self.s3_client.generate_presigned_url(
                ClientMethod="put_object",
                Params={
                    "Bucket": bucket,
                    "Key": okey
                },
                ExpiresIn=expiration)
            payload = {
                "bucket": bucket,
                "key": okey,
                "presigned_url": response
            }
        except botocore.exceptions.ClientError as e:
            print(f"error={e}")
            return None
        return payload
