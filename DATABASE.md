# Database Details
----
## Schema Diagram
https://dbdiagram.io/d/6033a69afcdcb6230b20ec45
----
## Script
CREATE DATABASE EQUEUE;
USE EQUEUE;

CREATE TABLE Customer (
  id int PRIMARY KEY AUTO_INCREMENT,
  email varchar(255) UNIQUE,
  password varchar(255),
  uin varchar(255) UNIQUE,
  name varchar(255),
  addr varchar(255),
  contactNo varchar(255)
);


CREATE TABLE Staff (
  id int PRIMARY KEY AUTO_INCREMENT,
  email varchar(255) UNIQUE,
  password varchar(255),
  name varchar(255),
  addr varchar(255),
  contactNo varchar(255),
  job varchar(255),
  status varchar(1),
  isAdmin varchar(1),
  branchId int,
  FOREIGN KEY(branchId) REFERENCES Branch(id)
);

CREATE TABLE Clinic (
  id int PRIMARY KEY AUTO_INCREMENT,
  name varchar(255) UNIQUE
);

CREATE TABLE Branch (
  id int PRIMARY KEY AUTO_INCREMENT,
  name varchar(255) UNIQUE,
  district varchar(255),
  address varchar(255),
  contactNo varchar(255),
  clinicId int,
  FOREIGN KEY(clinicId) REFERENCES Clinic(id)
); 

CREATE TABLE OpeningHours (
  dayOfWeek int,
  branchId int,
  opens time,
  closes time,
  PRIMARY KEY(dayOfWeek, branchId),
  FOREIGN KEY(branchId) REFERENCES Branch(id)
);

CREATE TABLE Queue (
  id int PRIMARY KEY AUTO_INCREMENT,
  status varchar(255),
  queueNumber int,
  createdDT date,
  customerId int,
  branchId int,
  FOREIGN KEY(customerId) REFERENCES Customer(id),
  FOREIGN KEY(branchId) REFERENCES Branch(id)
);