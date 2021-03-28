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

## DDL database setup
    cur = connection.cursor()
    cur.execute("CREATE TABLE Customer (id int PRIMARY KEY AUTO_INCREMENT,email varchar(255) UNIQUE,password varchar(255),uin varchar(255) UNIQUE,name varchar(255),addr varchar(255),contactNo varchar(255))")
    cur.execute("CREATE TABLE Clinic (id int PRIMARY KEY AUTO_INCREMENT,name varchar(255) UNIQUE)")
    cur.execute("CREATE TABLE Branch (id int PRIMARY KEY AUTO_INCREMENT,name varchar(255) UNIQUE,district varchar(255),address varchar(255),contactNo varchar(255),clinicId int,FOREIGN KEY(clinicId) REFERENCES Clinic(id))")
    cur.execute("CREATE TABLE Staff (id int PRIMARY KEY AUTO_INCREMENT,email varchar(255) UNIQUE,password varchar(255),name varchar(255),addr varchar(255),contactNo varchar(255),job varchar(255),branchId int,FOREIGN KEY(branchId) REFERENCES Branch(id))")
    cur.execute("CREATE TABLE OpeningHours (opens time,closes time,dayOfWeek int,branchId int,PRIMARY KEY(dayOfWeek, branchId),FOREIGN KEY(branchId) REFERENCES Branch(id))")
    cur.execute("CREATE TABLE Queue (id int PRIMARY KEY AUTO_INCREMENT,status varchar(255),queueNumber int,createdDT date,customerId int,branchId int,FOREIGN KEY(customerId) REFERENCES Customer(id),FOREIGN KEY(branchId) REFERENCES Branch(id))")
## Dummy data    
    cur.execute("INSERT INTO Customer(username,password,uin,name,dob,sex,addr,contactNo,email) VALUES('customer1','password','S1234567X','customer1',STR_TO_DATE('1-01-2012', '%d-%m-%Y') ,'M','APPLE STREET','12345678','customer1@hotmail.com')")
    cur.commit()
## Test dummy data retrieval    
    cur.execute("SELECT * from Customer")
    rows = cursor.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0],row[1],row[2]))
