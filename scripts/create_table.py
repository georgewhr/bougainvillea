import boto3
session = boto3.Session(profile_name='george')
# dynamodb = session.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
dynamodb = session.resource('dynamodb', region_name='us-west-2')
table = dynamodb.create_table(
    TableName='Plants',
    KeySchema=[
        {
            'AttributeName': 'plant_id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'name',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'plant_id',
            'AttributeType': 'N'
        },
        {
            'AttributeName': 'name',
            'AttributeType': 'S'
        },

    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 10
    }
)