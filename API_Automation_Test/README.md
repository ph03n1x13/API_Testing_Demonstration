### 🧭 My API Automation Strategy: `Postman` and `Python`   

`Context`  
This repository demonstrates my approach to API test automation using both `Postman` and `Python`.  
The goal is **not to fully automate everything**, but to use the right tool at the right stage, showing clear understanding of `capabilities`, `limits`, and `trade-offs`.   

### 🛂 When I Use `Postman` Automation  
I use `Postman` primarily for early-stage, exploratory, and communication-focused testing.
For me, `Postman` suits in the following scenarios:  
- Quick validation of API behaviour
- Exploratory and learning-focused testing  
- Demonstrating API flows clearly  
- Inter-collaboration with `SQA`, `BA` and `PM`  

### `Postman` Strengths    
- Fast setup, no codebase required
- Visual and interactive  
`Built-in supports for:`
    - Environment variables
    - Pre and Post request scripts
    - Basic assertions
    - Collection Runner

`Good for:`  
    - Smoke tests  
    - Happy path flows  
    - Token handling  
    - Basic Contract sanity checks


### `Postman` Limitations  

`Not suitable for:`  
- Sharing among large team for free  
- Large-scale test suites   
- Complex data-driven testing  
- Advanced reporting
- CI/CD-heavy workflows

`Limited support for:`   
- Advanced security testing
- Custom frameworks
- Complex validations  

### What I Automate in Postman

- Exploratory API testing
- Sharing testing thoughts among `Devs`, `DevOps`, `PMs`, and `BAs`
- Happy path validations
- Basic negative testing
- Token extraction and reuse of other environment variables
- Basic Response schema checks
- Simple chained requests with `Postman Runner`      

> Note: `Postman` automation is excellent for API exploration and quick communications among teams. 
But it is not for building long-term scalable frameworks where a group of testers are contributing automation codes.   

### 🐍 When I Use Python Automation    
I switch to `Python` when automation` requires depth`, `structure`, `collaboration` and `scalability`.  
I also consider of the following scenarios when using `Python`:      
- Sharing, updating, and contributing code among testers  
- Test logic becomes complex
- Reusability and scalability matter
- Advanced contract and data validations are needed, e.g. validating a specific type in response `JSON` body, dynamic data generation and validation etc. 
- CI/CD integration is required
- Security and misuse scenarios are automated  

### Python Strengths    
- Control of execution with a programming/scripting language 
- Excellent libraries like `requests`, `pytest`, `pytest-html`, and `json`  
- Easy integration with `Reports`, `Logs` etc.  
- 

`Good for:`  
   - Testing with different and custom type data  
   - Negative and edge-case testing  
   - Security-oriented test automation  
   - Rate limit and misuse simulation

### Python Limitation   
- Initial setup requires time 
- Requires coding knowledge  
- Overkill for simple exploratory testing  

### What I Automate in `Python`  
- Automating complex logical flows
- Sharing tests among teammates 
- Core API flows
- Negative and edge cases
- Advanced contract and schema validation
- Security misuse scenarios automation 
- Data consistency checks
- Reusable test components

> Note: I use `Python` for maintainability, reusability, complex logic control, and depth of test automation.   

### How much do I automate  
`What I Do Automate`     
- Stable API behaviours
- Reproducible bugs
- Regression-prone areas
- Security-relevant areas with known flows
- Complex contract validations

### What I Don’t Automate   
- One-time exploratory tests
- Demo API inconsistencies (expected in `reqres`, but shown here for demonstration purpose)
- UI-like validations on API level
- Known non-deterministic behaviours  

> Note: I automate what gives confidence, what is predictable--- not what gives coverage numbers.     

| Scenario                                  | Tool    |
|-------------------------------------------| ------- |
| Learning, Understanding, and Exploration  | Postman |
| API flow visualisation                    | Postman |
| Smoke testing                             | Postman |
| Regression testing                        | Python  |
| Data-driven testing                       | Python  |
| Security testing automation               | Python  |
| CI/CD integration                         | Python  |
| Long-term maintenance, team collaboration | Python  |

`In a word`     
> I use `Postman` to quickly understand and communicate API behaviour 
and `Python` when automation needs to be scalable, reusable, collaborative, and known security-focused paths/flows.     
> 
