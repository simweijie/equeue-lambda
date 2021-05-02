# Lambda Rest APIs
----
## Customer APIs
----
### login (Slide 11)

* **URL**
  : http://www.url.com/login

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ email : 'customer1@hotmail.com', password : 'passw0rd123' }`
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
  "data": [
    {
      "id": 1,
      "email": "customer1@hotmail.com",
      "uin": "S1234567X",
      "name": "customer1",
      "addr": "APPLE STREET",
      "postal": null,
      "contactNo": "12345678"
    }
  ]
}`
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in failed. Incorrect username or password" }`
    

### logout

* **URL**
  : http://www.url.com/logout

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ id : 10 }`
* **Success Response:**

  * **Code:** 200 <br />


### registerCustomer (slide 8)

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
    
### joinQueue (Slide 6)
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
    **Content:** `{
    "error": "Already in queue for Branch 4: tampines",
    "branchId": 4,
    "branchName": "tampines"
  }`
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`
    
### leaveQueue (Slide 10)
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
        
### getJoinedQueueStatus (Slide 9)
   Customer checks current position in the queue
   Note currentQueue refers to the queue number doctor is currently serving.
* **URL**
  : http://www.url.com/getJoinedQueueStatus

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{
  "customerId": 1
  }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
  "data": [
    {
      "status": "Q",
      "yourQueueNumber": 3,
      "branchId": 1,
      "branchName": "ncs",
      "branchAddr": "ncs street",
      "branchPostal": "569141",
      "clinicId": 1,
      "clinicName": "QM DENTAL",
      "customerId": 3,
      "currentQueueNumber": 1
    }
  ]
}`
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`

### smartSearch
  System automatically suggests a branch for the customer to queue at based on distance, queue length.
  
  * **URL**
  : http://www.url.com/smartSearch
* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{
  "latt": "52.2296756",
  "longt": "21.0122287"
}`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    
    `{
  "data": [
    {
      "id": 1,
      "name": "ncs",
      "district": "N",
      "addr": "ncs street",
      "postal": "569141",
      "contactNo": "12345678",
      "latt": 1.38761,
      "longt": 103.84381,
      "clinicId": 1,
      "queueLength": 2,
      "opens": "0:00:00",
      "closes": "23:59:00"
    }
  ]
}`
 
* **Error Response:**
    
  * **Code:** <br />
    **Content:** ``


### searchFilter
  Customer filters based on preferences
  
  * **URL**
  : http://www.url.com/searchFilter
* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{
  "clinicId": "1",
  "district": "N"
}`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
  "data": [
    {
      "branchId": 2,
      "branchName": "northpoint",
      "district": "N",
      "addr": "northpoint street",
      "postal": "769098",
      "contactNo": "12345678",
      "latt": 1.4296,
      "longt": 103.83565,
      "clinicId": 1,
      "opens": "0:00:00",
      "closes": "4:00:00",
      "queueLength": 3
    }
  ]}`
 
* **Error Response:**
    
  * **Code:** <br />
    **Content:** `{
  "error": "No clinic available"
}`

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
    **Content:** 
        
    `{
  "data": [
    {
      "id": 2,
      "name": "Parkway Shenton"
    },
    {
      "id": 1,
      "name": "QM DENTAL"
    }
  ]
}`
 
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
    **Content:** `{
  "data": [
    {
      "id": 1,
      "name": "Branch1",
      "district": "N",
      "addr": "Dental Street",
      "postal": "123456",
      "contactNo": "12345678",
      "latt": 1.4296,
      "longt": 103.83565,
      "clinicId": 1
    },
    {
      "id": 2,
      "name": "newbranchtest17",
      "district": "west",
      "addr": "21 Jurong Town Hall Rd",
      "postal": "123456",
      "contactNo": "22223333",
      "latt": 52.2296756,
      "longt": 21.0122287,
      "clinicId": 2
    },
    {
      "id": 3,
      "name": "newbranchtest18",
      "district": "west",
      "addr": "21 Jurong Town Hall Rd",
      "postal": "123456",
      "contactNo": "22223333",
      "latt": 52.2296756,
      "longt": 21.0122287,
      "clinicId": 2
    },
    {
      "id": 4,
      "name": "jurong east",
      "district": "W",
      "addr": "Shenton Family Medical Clinic - Jurong East, Jurong Gateway Rd, #01-263, Blk 131, Singapore 600131",
      "postal": "600131",
      "contactNo": "54545454",
      "latt": 1.33472,
      "longt": 103.74004,
      "clinicId": 3
    },
    {
      "id": 5,
      "name": "Citylink",
      "district": "S",
      "addr": "12 Marina Boulevard, #17-05 Marina Bay Financial Centre Tower 3, 018982",
      "postal": "018982",
      "contactNo": "54154565",
      "latt": 1.27911,
      "longt": 103.8543,
      "clinicId": 4
    },
    {
      "id": 6,
      "name": "HOME 1",
      "district": "E",
      "addr": "Blk 491 Admiralty Link #09-195",
      "postal": "750491",
      "contactNo": "98765432",
      "latt": 1.45611,
      "longt": 103.81772,
      "clinicId": 5
    },
    {
      "id": 7,
      "name": "newbranchtest21",
      "district": "W",
      "addr": "21 Jurong Town Hall Rd",
      "postal": "123456",
      "contactNo": "22223333",
      "latt": 52.2296756,
      "longt": 21.0122287,
      "clinicId": 7
    },
    {
      "id": 8,
      "name": "newbranchtest22",
      "district": "W",
      "addr": "21 Jurong Town Hall Rd",
      "postal": "123456",
      "contactNo": "22223333",
      "latt": 52.2296756,
      "longt": 21.0122287,
      "clinicId": 7
    },
    {
      "id": 9,
      "name": "GOING BRANCH",
      "district": "N",
      "addr": "Blk 491 Admiralty Link #09-195",
      "postal": "750491",
      "contactNo": "98765432",
      "latt": 1.45611,
      "longt": 103.81772,
      "clinicId": 8
    },
    {
      "id": 10,
      "name": "MAKE BRANCH",
      "district": "N",
      "addr": "Blk 491 Admiralty Link #09-195",
      "postal": "750491",
      "contactNo": "98765432",
      "latt": 1.45611,
      "longt": 103.81772,
      "clinicId": 9
    }
  ]
}`
 
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
    **Content:** `{
  "data": [
    {
      "id": 1,
      "name": "punggol",
      "district": "N",
      "address": "apple street",
      "contactNo": "lol",
      "clinicId": 3
    }
  ]}`
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`
    
### listOfStaffInClinic (Slide 24)
   Returns a list of Staff that is working under the same Clinic as staff used in input.
* **URL**
  : http://www.url.com/listOfStaffInClinic

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{
  "staffId": 2
  }`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
  "data": [
    {
      "id": 3,
      "email": "branch2staff@hotmail.com",
      "name": "branch2staff",
      "addr": "WORKER STREET UPDATED",
      "contactNo": "01234567",
      "job": "D",
      "status": "A",
      "isAdmin": "Y",
      "branchId": 4,
      "branchName": "tampines",
      "clinicId": 1,
      "clinicName": "QM Dental"
    },
    {
      "id": 9,
      "email": "stafftoexistclinic@hotmail.com",
      "name": "stafftoexistclinic",
      "addr": "Doctor Street",
      "contactNo": "77778888",
      "job": "N",
      "status": "P",
      "isAdmin": "N",
      "branchId": 4,
      "branchName": "tampines",
      "clinicId": 1,
      "clinicName": "QM Dental"
    }
  ]}`
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`
----
## Staff APIs
----

### staffLogin (Slide 18)

* **URL**
  : http://www.url.com/staffLogin

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ email : 'staff1@hotmail.com', password : 'passw0rd123' }`
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
  "{
  "data": [
    {
      "id": 1,
      "email": "staff1@hotmail.com",
      "name": "staff1",
      "addr": "WORKER STREET",
      "postal": null,
      "contactNo": "01234567",
      "job": "D",
      "status": "A",
      "isAdmin": "Y",
      "branchId": 1
    }
  ]
}`
 
* **Error Response:**

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "Log in failed. Incorrect username or password" }`
    
### staffLogout

* **URL**
  : http://www.url.com/staffLogout

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{ id : 8 }`
* **Success Response:**

  * **Code:** 200 <br />
 
### registerStaffToNewClinic (Slide 20,21,22)
   Self-registration to start a new clinic. Note that staff will be registered under first branch in the branches list.
* **URL**
  : http://www.url.com/registerNewStaffNewClinic

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{
  "email": "staff16@hotmail.com",
  "password": "passw0rd123",
  "name": "DOCTOR TAN",
  "addr": "Tan Drive Street Road",
  "contactNo": "12345678",
  "job": "D",
  "clinicName": "newclinictest16",
  "branches": [
    {
      "branchName": "newbranchtest17",
      "district": "W",
      "addr": "21 Jurong Town Hall Rd",
      "postal": "123456",
      "latt": "52.2296756",
      "longt": "21.0122287",
      "contactNo": "22223333",
      "openingHours": [
        {
          "opens": "08:00",
          "closes": "16:00",
          "dayOfWeek": 1
        },
        {
          "opens": "08:00",
          "closes": "12:00",
          "dayOfWeek": 5
        }
      ]
    },
    {
      "branchName": "newbranchtest18",
      "district": "W",
      "addr": "21 Jurong Town Hall Rd",
      "postal": "123456",
      "latt": "52.2296756",
      "longt": "21.0122287",
      "contactNo": "22223333",
      "openingHours": [
        {
          "opens": "08:00",
          "closes": "16:00",
          "dayOfWeek": 1
        }
      ]
    }
  ]
}`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:**  <br />
    **Content:** ``

### registerStaffToExistingClinic (Slide 23)
   Self-registration for a staff to an already existing clinic/branch
* **URL**
  : http://www.url.com/registerStaffExistingClinic

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{
  "email": "stafftoexistclinic@hotmail.com",
  "password": "pwd",
  "name": "stafftoexistclinic",
  "addr": "Doctor Street",
  "contactNo": "77778888",
  "job": "N",
  "branchId": 4
}`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:**  <br />
    **Content:** ``

### updateStaff (Slide 27)
   Update a staff based on staff id
* **URL**
  : http://www.url.com/updateStaff

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{
  "id": "3",
  "email": "branch2staff@hotmail.com",
  "name": "branch2staff",
  "addr": "WORKER STREET UPDATED",
  "contactNo": "01234567",
  "job": "D",
  "status": "A",
  "isAdmin": "Y",
  "branchId": "4"
}`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** ``
 
* **Error Response:**

  * **Code:**  <br />
    **Content:** ``

### deleteStaffWithId
   Delete staff based on staff id.
* **URL**
  : http://www.url.com/deleteStaffWithId

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{
  "id": 2
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
  "id": 4
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

### getBranchQueue (Slide 19)
   Get the whole queue of a branch
* **URL**
  : http://www.url.com/getBranchQueue

* **Method:**
  :`POST`
  
* **Request Payload**
  {
  "staffId": 1
}`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
    `{
  "data": [
    {
      "id": 1,
      "status": "Q",
      "queueNumber": 3,
      "customerId": 3,
      "branchId": 1,
      "customerName": "customer1",
      "customerContactNo": "12345678"
    },
    {
      "id": 2,
      "status": "D",
      "queueNumber": 2,
      "customerId": 2,
      "branchId": 1,
      "customerName": "customer1",
      "customerContactNo": "12345678"
    },
    {
      "id": 3,
      "status": "D",
      "queueNumber": 1,
      "customerId": 1,
      "branchId": 1,
      "customerName": "customer1",
      "customerContactNo": "12345678"
    }
  ]}`
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`
    
### updateQueueStatus (Slide 19)
   Staff advances the queue to its next stage (q - queue/d - doctor/p - payment/c - complete/r -cancel/m - missed)
* **URL**
  : http://www.url.com/updateQueueStatus

* **Method:**
  :`POST`
  
* **Request Payload**
  
  `{
  "newStatus": "Q",
  "branchId": "4",
  "customerId": "3",
  "currentStatus": "D"
}`
   
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** 
 
* **Error Response:**
    
  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `Required to login`


