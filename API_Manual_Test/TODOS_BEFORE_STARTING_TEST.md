### Before you start  
- Create an account at https://app.reqres.in/
- Generate an API key from your profile  
- Use that key with custom `x-api-key` header with each request to avoid `HTTP 403`
- In `register` endpoint, the payload only accepts  
```json
{
  "email": "string",
  "password": "string"
}
```
Where `email` should be an existing email found in `users` endpoint  