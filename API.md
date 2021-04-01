# Lambda Rest APIs
----
## Customer APIs
----
### login

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
    

### logout

* **URL**
  : http://www.url.com/logout

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ username : 'customer1@hotmail.com' }`
* **Success Response:**

  * **Code:** 200 <br />


### registerCustomer

* **URL**
  : http://www.url.com/registerCustomer

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    email : 'customer1@hotmail.com', password : 'passw0rd123',
    name: 'TAN AH SENG', uin: 'S1234567X',
    addr: '1 Happy Street', contactNo: '12345678'
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:**  <br />
    **Content:** ``
    
### updateCustomerInfo
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
    email : 'customer1@hotmail.com', name: 'newname',
    addr: '5 Apple Drive', contactNo: '43215678'
  }`
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in failed. Incorrect username or password" }`
    
### joinQueue
   Customer joins the queue for a branch
* **URL**
  : http://www.url.com/joinQueue

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    branchId : 5,
    customerId: 1
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:** 200 <br />
    **Content:** `Already in another queue`
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`
    
### leaveQueue
   Customer leaves the queue for a branch
* **URL**
  : http://www.url.com/leaveQueue

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    branchId : 5,
    customerId : 10
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`
        
### getJoinedQueueStatus
   Customer checks current position in the queue
* **URL**
  : http://www.url.com/getJoinedQueueStatus

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    branchId : 5,
    customerId : 10
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`

### searchNearby (KIV)
  System automatically suggests a branch for the customer to queue at based on distance, queue length.
  
  * **URL**
  : http://www.url.com/searchNearby
* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    
    `{
      branchId:5,
      queueNumber: 6
    }`
 
* **Error Response:**
    
  * **Code:** <br />
    **Content:** ``


### searchFilter   (KIV)
  Customer filters based on preferences
  
  * **URL**
  : http://www.url.com/searchFilter
* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    district : 'N',
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**
    
  * **Code:** <br />
    **Content:** ``

### listOfClinics
   Returns with a list of all Clinics.
* **URL**
  : http://www.url.com/listOfClinics

* **Method:**
  :`POST`
  
* **Request Payload**
  
  ``
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[
    {
      "id": 3,
      "name": "Parkway Shenton"
    },
    {
      "id": 7,
      "name": "QM Dental"
    }
  ]`
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`
    
### listOfBranches
   Returns a list of all branches.
* **URL**
  : http://www.url.com/listOfBranches

* **Method:**
  :`POST`
  
* **Request Payload**
  
  ``
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[
    {
      "id": 1,
      "name": "punggol",
      "district": "north",
      "address": "apple street",
      "contactNo": "lol",
      "clinicId": 3
    }
  ]`
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`
    
### listOfBranchesWithClinicId
   Returns a list of Branches based on Clinic ID.
* **URL**
  : http://www.url.com/listOfBranchesWithClinicId

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{
      "clinicId": 1
    }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `[
    {
      "id": 1,
      "name": "punggol",
      "district": "north",
      "address": "apple street",
      "contactNo": "lol",
      "clinicId": 3
    }
  ]`
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`
----
## Staff APIs
----

### staffLogin

* **URL**
  : http://www.url.com/staffLogin

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ email : 'staff1@hotmail.com', password : 'passw0rd123' }`
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{ id : 12 }`
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in failed. Incorrect username or password" }`
    
### staffLogout

* **URL**
  : http://www.url.com/staffLogout

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ username : 'staff1@hotmail.com' }`
* **Success Response:**

  * **Code:** 200 <br />
 
### registerStaffToNewClinic
   Self-registration to start a new clinic
* **URL**
  : http://www.url.com/registerNewStaffNewClinic

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    email : 'staff1@hotmail.com', password : 'passw0rd123',
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

### registerStaffToExistingClinic
   Self-registration for a staff to an already existing clinic/branch
* **URL**
  : http://www.url.com/registerStaffExistingClinic

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    email : 'staff1@hotmail.com', password : 'passw0rd123',
    name: 'DOCTOR TAN', uin: 'S1234567X',
    branchId: 5,
    contactNo: '12345678',
    job 'd'
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:**  <br />
    **Content:** ``
    
### activatePendingStaff
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
    
### addOpeningHours
   Clinic admin can set the opening hours of the branch
* **URL**
  : http://www.url.com/addOpeningHours

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    branchId : 5,
    opens: '08:00',
    closes: '18:00',
    dayOfWeek: 1
    
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** ``

### deleteOpeningHours
   Clinic admin can remove opening hours for a particular day of a branch
* **URL**
  : http://www.url.com/deleteOpeningHours

* **Method:**
  :`DELETE`
  
* **Request Payload**
  
  `{ 
    branchId : 5,
    dayOfWeek: 1 
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** ``

### updateOpeningHours
   Clinic admin can set the opening hours of the branch
* **URL**
  : http://www.url.com/updateOpeningHours

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    branchId : 5,
    opens: '08:00',
    closes: '18:00',
    dayOfWeek: 1
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** ``


### updateQueueStatus
   Staff advances the queue to its next stage (q - queue/d - doctor/p - payment/c - complete/r -cancel/m - missed)
* **URL**
  : http://www.url.com/updateQueueStatus

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ 
    branchId : 5,
    customerId : 10,
    status: "q"
   }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`


