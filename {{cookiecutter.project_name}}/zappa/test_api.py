import boto3
import requests
from aws_requests_auth.aws_auth import AWSRequestsAuth

api_id = "CHANGE"
api_route = ""
api_stage = "dev"
aws_profile = "default"
aws_region = "us-east-1"

domain = f"{api_id}.execute-api.{aws_region}.amazonaws.com"
base_url = f"https://{domain}/{api_stage}"


session = boto3.session.Session(profile_name=aws_profile)
creds = session.get_credentials()
auth = AWSRequestsAuth(
    aws_access_key=creds.access_key,
    aws_secret_access_key=creds.secret_key,
    aws_host=domain,
    aws_region=aws_region,
    aws_service="execute-api",
)

response = requests.get(f"{base_url}/{api_route}", auth=auth)
print(response.text)
print(response.headers)
