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

def handler(event, context):
    cur = connection.cursor()  
## Retrieve Data
    query1 = "INSERT INTO Clinic(name) VALUES ('{}')".format(event['clinicName'])
    cur.execute(query1)
    # connection.commit()
    query2 = "SELECT id from Clinic where name = '{}'".format(event['clinicName'])
    cur.execute(query2)
    # connection.commit()
    clinicId = cur.fetchone()[0]
    print("clinicId: ", clinicId)
    query3 = "INSERT INTO Branch(name,district,address,contactNo,clinicId) VALUES('{}','{}','{}','{}','{}')".format(event['branchName'],event['district'],event['addr'],event['contactNo'],clinicId)
    cur.execute(query3)
    # connection.commit()
    query4 = "SELECT id from Branch where name = '{}'".format(event['branchName'])
    cur.execute(query4)
    # connection.commit()
    branchId = cur.fetchone()[0]
    print("branchId: ", branchId)
    query5 = "INSERT INTO Staff(email,password,name,addr,contactNo,job,status,isAdmin,branchId) \
        VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}')"\
        .format(event['email'], event['password'], event['name'], event['addr'], event['contactNo'], event['job'],'A','Y',branchId)
    cur.execute(query5)
    connection.commit()
    print(cur.rowcount, "record(s) affected")
## Construct body of the response object
    transactionResponse = {}
# Construct http response object
    responseObject = {}
    responseObject['statusCode'] = 200
    responseObject['headers'] = {}
    responseObject['headers']['Content-Type']='application/json'
    responseObject['headers']['Access-Control-Allow-Origin']='*'
    responseObject['body'] = json.dumps(transactionResponse, sort_keys=True,default=str)
    
    #k = json.loads(responseObject['body'])
    #print(k['uin'])

    return responseObject