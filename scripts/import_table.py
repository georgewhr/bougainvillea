import boto3
import json
import decimal
session = boto3.Session(profile_name='george')
dynamodb = session.resource('dynamodb', region_name='us-west-2', endpoint_url="http://localhost:8000")
# dynamodb = session.resource('dynamodb', region_name='us-west-2')
table = dynamodb.Table('Plants')
with open("../data/plant.json") as json_file:
    plants = json.load(json_file, parse_float = decimal.Decimal)
    for i in plants:
        table.put_item(
           Item={
                'plant_id': i['plant_id'],
                'name': i['name'],
                'common_name': i['common_name'],
                'habit':i['habit'],
                'soil_level':i['soil_level'],
                "sun_level":i['sun_level'],
                "water_level":i['water_level'],
                "mch":i['mch'],
                "mrc":i['mrc'],
                "flower_time":i['flower_time'],
                "fruiting_time":i['fruiting_time'],
                "order":i['order'],
                "family":i['family'],
                "genus":i['genus']
            }
        )