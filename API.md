# Lambda Rest APIs
----
## login

* **URL**
  : http://www.url.com/login

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ username : 'customer1@hotmail.com', password : 'passw0rd123' }`
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12 }`
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in failed. Incorrect username or password" }`
    
## staffLogin

* **URL**
  : http://www.url.com/stafflogin

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ username : 'staff1@hotmail.com', password : 'passw0rd123' }`
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12 }`
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in failed. Incorrect username or password" }`
    
## logout

* **URL**
  : http://www.url.com/logout

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ username : 'customer1@hotmail.com' }`
* **Success Response:**

  * **Code:** 200 <br />

## stafflogout

* **URL**
  : http://www.url.com/stafflogout

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ username : 'staff1@hotmail.com' }`
* **Success Response:**

  * **Code:** 200 <br />
 
## registerCustomer

* **URL**
  : http://www.url.com/register

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    username : 'customer1@hotmail.com', password : 'passw0rd123',
    name: 'TAN AH SENG', uin: 'S1234567X',
    dob: '17/12/1993', sex: 'm',
    addr: '1 Happy Street', contactNo: '12345678'
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:**  <br />
    **Content:** ``
    
## updateCustomerInfo
  Allows customer to update personal information.
  
* **URL**
  : http://www.url.com/updateCustomerInfo

* **Method:**
  :`POST`
  
* **Request Payload**
  
  * username (mandatory) <br />
  * name (optional) <br />
  * addr (optional) <br />
  * contactNo (optional) <br />
  `{ 
    username : 'customer1@hotmail.com', name: 'newname',
    addr: '5 Apple Drive', contactNo: '43215678'
  }`
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in failed. Incorrect username or password" }`

## registerNewStaffNewClinic
   Self-registration to start a new clinic
* **URL**
  : http://www.url.com/registerNewStaffNewClinic

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    username : 'staff1@hotmail.com', password : 'passw0rd123',
    name: 'DOCTOR TAN', uin: 'S1234567X',
    clinicName: 'Parkway Shenton',
    branchName: 'Jurong',
    district: 'west',
    addr: '21 Jurong Town Hall Rd',
    contactNo: '12345678',
    job 'd'
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:**  <br />
    **Content:** ``

## registerStaffToExistingClinic
   Self-registration for a staff to an already existing clinic/branch
* **URL**
  : http://www.url.com/registerStaffExistingClinic

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    username : 'staff1@hotmail.com', password : 'passw0rd123',
    name: 'DOCTOR TAN', uin: 'S1234567X',
    branchId: '5',
    contactNo: '12345678',
    job 'd'
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:**  <br />
    **Content:** ``
    
## activatePendingStaff
   Clinic admin can confirm registration of staff to existing clinic
* **URL**
  : http://www.url.com/activatePendingStaff

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    username : 'staff1@hotmail.com'
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:**  <br />
    **Content:** ``
