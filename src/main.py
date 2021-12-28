import json


def hello(event, context):
    body = {
        "message": "Some Changes!!",
        "input": event,
    }

    response = {"statusCode": 200, "body": json.dumps(body)}

    return response