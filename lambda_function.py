import random

def handler(event, context):
    return random.randint(0, 1000)
