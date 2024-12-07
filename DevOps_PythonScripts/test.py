import json

def lambda_handler(event, context):
    query_params = event.get('queryStringParameters', {})  # Corrected key name
    name = query_params.get("name", "Guest")
    message = f"Hello {name}, Welcome to AWS Lambda"

    response = {
        "statusCode": 200,  # Fixed typo: 'statuscode' -> 'statusCode'
        "headers": {"Content-Type": "application/json"},  # Fixed 'header' and key-value pair
        "body": json.dumps({"message": message})
    }

    return response  # Indentation fixed for 'return'
