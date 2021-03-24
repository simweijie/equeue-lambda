import sys
import logging
import rds_config
import pymysql
import json

#rds settings
rds_endpoint  = "database-1.cqyrle3kurs0.ap-southeast-1.rds.amazonaws.com"
username = rds_config.db_username
password = rds_config.db_password
db_name = rds_config.db_name

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
