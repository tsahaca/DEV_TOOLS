import json
import requests

def lambda_handler(event, context):
    url = 'https://www.google.com'
    res = requests.get(url)
    print("html:", res.text)
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
