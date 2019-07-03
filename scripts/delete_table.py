import boto3
session = boto3.Session(profile_name='george')
dynamodb = session.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
table = dynamodb.Table('Plants')
table.delete()