### 🎯 Purpose of This Postman Automation   
This Postman automation is intentionally limited in scope and designed to demonstrate:  
- Where Postman is the best tool
- How far Postman automation should realistically go  

Clean usage of:  
- Environment variables
- Test scripts   

⚠️ Important:
Login and Registration APIs are already automated using `Python + Pytest`.
They are intentionally excluded from Postman to avoid duplication and tool overlap.   

#### Endpoint 1: Get Users List  
Endpoint: `GET /api/users?page=X`   

**Why Postman is used**  
- Simple query parameter handling
- Fast validation of response structure
- No business workflow dependency  

**Automation Scope**  
- Validate the response code is `HTTP 200`  
- Response time should be less than `100ms`  
- Basic contact validation that `page`, `per_page`, `total`, etc. keys are present in response JSON body  