## 🧪 `Python` API Automation Test Plan — `Reqres`  

### `1. Objective`   
The objective of this `Python` automation is to validate API behavior beyond `exploratory` and `happy-path` testing,
focusing on the following:   
- Logical correctness of api endpoints under test
- Contract enforcement
- Data consistency
- Security misuse scenarios that can be automated
- Regression-prone behaviours

> This automation is not intended to fully validate `Reqres API`, as `Reqres` is a demo platform.
Instead, it demonstrates **how I design and scope API automation in real-world projects.**   

---   
### `2. Scope of Automation`    

`In Scope`  
Core API behaviors that are:
- Predictable
- Reproducible
- Suitable for automation
- Negative and edge-case scenarios
- API contract and schema validation
- Security-relevant misuse patterns

`Out of Scope`    
- Basic happy-path validations (covered in [manual testing repository](https://github.com/ph03n1x13/API_Testing_Demonstration/tree/draft/API_Manual_Test))
- One-time exploratory findings
- Known demo API inconsistencies
- UI-like validations at API level
- Performance/load testing (covered separately with Locust in [api load test section](https://github.com/ph03n1x13/API_Testing_Demonstration/tree/draft/API_Load_Test))

---   
### 3. Tooling  

| Area              | Tool                                |
| ----------------- |-------------------------------------|
| Language          | `Python`                            |
| HTTP Client       | `requests`                          |
| Test Framework    | `pytest`                            |
| Reporting         | `pytest-html`                       |
| Schema Validation | `JSON` assertions / custom validators |
| CI/CD Readiness   | Later                               |

---   


### 4. Design Principles     
- Single responsibility per test
- Readable test names
- Explicit assertions
- No over-engineering

---    

## Test Coverage Breakdown   

### 📝 Registration API (`/register`)    
`Automation Focus`  
- Schema enforcement
- Security risks
- Data consistency  

`Test Scenarios`  
- Token uniqueness validation
- Password data type validation
- Duplicate email behavior
- Extra field injection (e.g., `role=ADMIN`)
- Response id data type validation  

### 🔐 Login API (/login)
`Automation Focus`  
- Contract validation
- Error handling
- Method misuse
- Documentation vs implementation mismatch

`Test Scenarios`   
- Valid login returns non-empty token
- Empty payload returns correct error
- Missing required fields validation
- Unsupported HTTP methods (GET, PUT)
- Payload contract mismatch detection

---   
### Validation Levels  

`Automation validates:`  
- HTTP status codes
- Response body structure
- Data types
- Required fields
- Side effects across endpoints
- Security implications

`Reporting Strategy`   
- `HTML` reports using `pytest-html`  
- Descriptive assertion messages  


`Failures highlight`  
- Expected behaviour
- Actual behaviour
- Risk or impact 

---   

### Note:   
- `Reqres` is a demo API with expected inconsistencies
- Some failures are documented intentionally
- Automation prioritises learning and demonstration, not platform validation