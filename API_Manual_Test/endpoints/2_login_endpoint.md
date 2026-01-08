### Found Behaviours    
1. A successful login with expected data returns a token.  
[](../Screenshots/login_api/login_ok.png)  
2. The API returns an `HTTP 400` for a non-existing user  
[](../Screenshots/login_api/bad_request.png)
3. Correct error handling if the payload is empty
[](../Screenshots/login_api)

### Inconsistent Behaviours    
1. `Inconsistency in Documentation:` According to the documentation, the payload of the endpoint is 
```json
{
  "username": "string",
  "email": "string",
  "password": "string"
}
```
but the working payload is 
```json
{
  "email": "string",
  "password": "string"
}
```   

`Expected:`
- API behavior should strictly follow the documented request schema.
- Documentation should accurately reflect required fields.

`Actual:`  
The API ignores the username field requirement.
`Impact:`   
Causes confusion for API consumers and breaks contract reliability.

---   
2. `Endpoint Abuse Leading to Untracked User Creation:` If we change the method into `GET`, it returns a list of colors.  
[](../Screenshots/login_api/data_exposure.png)
`Expected:` 
- If the data are necessary/public, they should be clearly documented
- The endpoint should return an `HTTP 405` "Method not Allowed" if `GET` method was not permitted

`Actual:`
The endpoint responds with unrelated data for an undocumented method.

`Impact:`
Indicates improper method handling and potential unintended data exposure.

---  

3.`Creating User through Endpoint Manipulation:` A user can create a random user by changing the api endpoint. This might allow attackers to create 
an untracked malicious user.  
[](../Screenshots/login_api/untracked_user.png)

`Expected:`
- User creation should only be allowed through the designated endpoint with proper validation.
- Unauthorised endpoint usage should be blocked with `HTTP 403` Forbidden.

`Actual:`
The API allows creation of untracked users through endpoint manipulation.

`Impact:`
Potential security risk allowing creation of malicious or unmanaged users.