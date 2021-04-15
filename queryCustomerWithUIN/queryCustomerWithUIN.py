import sys
import logging
import pymysql
import json
import os

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

def lambda_handler(event, context):
    cur = connection.cursor()  
## Retrieve Data    
    query = "SELECT * FROM Customer where uin = '{}'".format(event['uin'])
    cur.execute(query)

## Construct body of the response object
    transactionResponse = {}
    rows = cur.fetchall()
    for row in rows:
        print("TEST {0} {1} {2}".format(row[0],row[1],row[2]))
        transactionResponse['id'] = row[0]
        transactionResponse['username'] = row[1]
        transactionResponse['password'] = row[2]
        transactionResponse['uin'] = row[3]
        transactionResponse['name'] = row[4]
        transactionResponse['dob'] = row[5]
        transactionResponse['sex'] = row[6]
        transactionResponse['addr'] = row[7]
        transactionResponse['contactNo'] = row[8]
        transactionResponse['email'] = row[9]
    
# Construct http response object
    responseObject = {}
    # responseObject['statusCode'] = 200
    # responseObject['headers'] = {}
    # responseObject['headers']['Content-Type']='application/json'
    # responseObject['headers']['Access-Control-Allow-Origin']='*'
    responseObject['data'] = json.dumps(transactionResponse, sort_keys=True,default=str)
    
    #k = json.loads(responseObject['body'])
    #print(k['uin'])

    return responseObject