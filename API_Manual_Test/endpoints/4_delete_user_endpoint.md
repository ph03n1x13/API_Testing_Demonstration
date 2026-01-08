### Note
Please note that reqres is a demo API. So, standard behaviour is not expected like real life. 
We try to simulate for learning purpose.     

---   

### Found Behaviours   
1. A delete action returns `HTTP 204` code according to the documentation.  
2. The response body is empty as expected  

`PoC:`  
[](../Screenshots/delete_api/sucess.png)   





### Inconsistent Behaviours    
1. `Data Inconsistency`   
Deleted users are found in `users` endpoint
`Expected:`   
A deleted user should not be found in the `users` endpoint response
`Actual:`  
Deleted user is found after hitting the `users` API endpoint    
`Impact:`  
This will create inconsistency in the system.  

2. `Unwanted Entity Creation via Unsupported HTTP Method`   
If the method is changed into `POST`, a user can create a random data entry with a valid JSON body.  
`PoC`   
[](../Screenshots/delete_api/element_creation.png)   

`Expected:`   
- The `delete` endpoint should return an `HTTP 405` Method not Allowed error.  
- No arbitrary data should be created through the `delete` endpoint
`Actual:`  
- Arbitrary data creation is possible through `delete` endpoint
`Impact:`  
- System is polluted with unwanted data  
- Security issues with the creation of malicious users 
- Unwanted user creation with elevated privilege.  