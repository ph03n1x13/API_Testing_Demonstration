### 🎯 Purpose of This Postman Automation   
This Postman automation is intentionally limited in scope and designed to demonstrate:  
- Where Postman is the most feasible tool
- How far Postman automation should realistically be used  

Clean usage of:  
- Environment variables (`setting` and `getting`)
- Test scripts   

⚠️ Important:
Login and Registration APIs are already automated using `Python + Pytest`.
They are intentionally excluded from Postman to avoid duplication and tool overlap.   

**Why Postman is used**  
- Simple query parameter handling
- Fast validation of response structure
- No business workflow dependency  


#### Endpoint 1: Get Users List  
Endpoint: `GET /api/users?page=X`   


**Automation Scope**  
- Validate the response code is `HTTP 200`  
- Response time should be less than `100ms`  
- Basic contact validation that `page`, `per_page`, `total`, etc. properties are present in response JSON body  

#### Endpoint 2: Delete a User    
Endpoint: `DELETE /users/{{userID}}`  

**Automation Scope**    
- Ensuring response code only  
- Ensuring a successful request only returns an empty body  

