from __future__ import division

def lambda_handler(event, context):
   customer_id = event['customer_id']
   geo_location = event['geolocation']

   

   return {
       "customer_id": customer_id,
       "geolocation":geo_location
   }