import json
import random

def handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps(random.randint(0, 1000))
    }
