### Testing Scope  
`Swagger URL`:  https://reqres.in/api-docs/  
`Base URL`: https://reqres.in/api  

- User List
- Getting specific user info
- User Registration 
- Login 
- Delete the created user  

### Test Plan  
1. Test the `/users` endpoint  
2. Get information about a specific user  
3. Register a new user  
4. Delete the user  

### Sample Test Case Ideas  
`GET` Method: 
- Valid request → 200 OK
- Invalid page number
- Missing params
- Response schema validation
- Empty data handling

`POST` Method: 
- Valid payload → 201
- Missing fields → 400
- Invalid data type
- Extra fields or Data Staffing

### Considerations  
a) Consider any inconsistent API endpoint behaviour   
b) Document inconsistencies with PoCs  