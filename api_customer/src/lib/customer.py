import json
import uuid

class Customer:
    def __init__(self, ddb, table):
        self.ddb = ddb
        self.table = table
        self.uid = None
        self.given_name = None
        self.family_name = None
        self.birthdate = None
        self.email = None
        self.phone_number = None
        self.phone_number_verified = False

    def __repr__(self):
        return {
            "uid": self.uid,
            "given_name": self.given_name,
            "family_name": self.family_name,
            "birthdate": self.birthdate,
            "email": self.email,
            "phone_number":  self.phone_number,
            "phone_number_verified": self.phone_number_verified
        }

    def __str__(self):
        return json.dumps(self.__repr__())

    def set_uid(self, value):
        self.uid = value
    
    def set_given_name(self, value):
        self.given_name = value
    
    def set_family_name(self, value):
        self.family_name = value

    def set_birthdate(self, value):
        self.birthdate = value

    def set_email(self, value):
        self.email = value

    def set_phone_number(self, value):
        self.phone_number = value

    def set_phone_number_verified(self, value):
        self.phone_number_verified = value

    def exists(self, email):
        response = self.ddb.query(
            TableName = self.table,
            IndexName = "lu_email",
            KeyConditionExpression = "email = :val1",
            ExpressionAttributeValues = {
                ":val1": {
                    "S": email
                }
            }
        )
        item_count = len(response["Items"])
        return item_count

    def create(self):
        self.uid = str(uuid.uuid4())
        if (self.exists(self.email) == 0):
            response = self.ddb.put_item(
                TableName = self.table,
                Item = {
                    "uid": { "S": self.uid },
                    "given_name": { "S": self.given_name },
                    "family_name": { "S": self.family_name },
                    "birthdate": { "S": self.birthdate },
                    "email": { "S": self.email },
                    "phone_number": { "S": self.phone_number },
                    "phone_number_verified": { "BOOL": self.phone_number_verified }
                }
            )
        else:
            response = {
                "ResponseMetadata": {
                    "ErrorMessage": "Email already exists",
                    "ErrorType": "InputError",
                    "HTTPStatusCode": 500
                }
            }
        return response

    def update(self, uid):
        self.uid = uid
        update_expr = ["set "]
        update_vals = {}
        for k, v in self.__repr__():
            update_expr.append(f"{k} = :{k},")
            update_vals[f":{k}"] = v
        print("".join(update_expr[:-1]))
        print(dict(update_vals))
        response = self.ddb.update_item(
            TableName = self.table,
            Key = {
                "uid": { "S": self.uid }
            },
            UpdateExpression = "".join(update_expr[:-1]),
            ExpressionAttributeValues = dict(update_vals)
        )
        return response