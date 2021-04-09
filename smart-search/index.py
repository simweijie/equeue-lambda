import sys
import logging
import pymysql
import json
import os
from math import sin, cos, sqrt, atan2, radians
import geopy.distance

#rds settings
rds_endpoint = os.environ['rds_endpoint']
username=os.environ['username']
password=os.environ['password']
db_name=os.environ['db_name']

logger = logging.getLogger()
logger.setLevel(logging.INFO)

#Connection
try:
    connection = pymysql.connect(host=rds_endpoint, user=username,
        passwd=password, db=db_name)
except pymysql.MySQLError as e:
    logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
    logger.error(e)
    sys.exit()
logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

def handler(event, context):
    cur = connection.cursor()  
## Retrieve Data
    latt1 = radians(float(event['latt']))
    longt1 = radians(float(event['longt']))
    query = "SELECT id,latt,longt FROM Branch"    
    cur.execute(query)
    connection.commit()
## Construct body of the response object
# https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude
    branchList = []
    rows = cur.fetchall()
    id = 0
    latt = 0
    longt = 0
    # R = 6373.0
    for row in rows:
        print("TEST {0} {1} {2}".format(row[0],row[1],row[2]))
        id = row[0]
        latt2 = radians(row[1])
        longt2 = radians(row[2])
    #     dlon = longt2 - longt1
    #     dlat = latt2 - latt1
    #     a = sin(dlat / 2)**2 + cos(latt1) * cos(latt2) * sin(dlon / 2)**2
    #     c = 2 * atan2(sqrt(a), sqrt(1 - a))
    #     distance = R * c
    #     print("Result:", distance)
        coords_1=(latt1,longt1)
        coords_2=(latt2,longt2)
        print ("GEOPY DISTANCE: ", geopy.distance.distance(coords_1, coords_2).km)




# Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type']='application/json'
    responseObject['headers']['Access-Control-Allow-Origin']='*'
    responseObject['body']= branchList
    # responseObject['body'] = json.dumps(transactionResponse, sort_keys=True,default=str)
    
    #k = json.loads(responseObject['body'])
    #print(k['uin'])

    return responseObject

