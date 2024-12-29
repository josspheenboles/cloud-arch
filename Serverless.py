def lambda_handler(event, context):
    return {"statusCode": 200, "body": "Hello from Lambda!"}
import boto3

lambda_client = boto3.client('lambda')

with open('lambda_function.py', 'rb') as f:
    zip_content = f.read()

response = lambda_client.create_function(
    FunctionName='DemoLambdaFunction',
    Runtime='python3.9',
    Role='arn:aws:iam::your-account-id:role/execution-role',  # Replace with your role ARN
    Handler='lambda_function.lambda_handler',
    Code={'ZipFile': zip_content},
)
print("Lambda function created:", response['FunctionArn'])

