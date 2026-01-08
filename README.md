# API Testing Practice – ReqRes Demo APIs  
## 📌 Overview

This repository contains **API testing practice artifacts** created using the public demo API provided by **ReqRes**.

> ⚠️ **Important Note:**  
> This is **NOT a full or production-grade test report**.

This repository is a high level demonstration of **how I approach API testing** — including **thinking process, planning, execution, and analysis** — rather than to provide exhaustive test cases and test case execution.

---

## 🎯 Purpose of This Repository

- To showcase **my API testing methodology**
- To demonstrate **exploratory and critical testing mindset**
- To present a **step-by-step approach** to API testing

⚠️This repository represents a **draft-style testing overview**, _not a finalized QA deliverable_.

---

## 🧪 API Under Test

- **API Provider:** ReqRes (Public Demo API)
- **Base URL:** https://reqres.in/api
- **Swagger Docs:** https://reqres.in/api-docs

> ℹ️ ReqRes is a **mock/demo API**, widely used for learning and practicing API testing.  
> Some inconsistencies are expected and are intentionally used here to demonstrate **testing and analysis skills**.

---

## 🔍 Scope of Testing

The repository covers testing of the following endpoints:

- Users List (`GET /users`)
- Single User Retrieval
- User Registration
- User Login
- User Update
- User Deletion

---

## 🧠 Testing Approach Demonstrated

This repository touches multiple testing layers **in a small but structured and progressive way**:

### ✅ Core Testing Concepts
- Requirement understanding
- API contract validation
- Happy path & negative testing

### ⚙️ Regular API Testing
- Request/response validation
- HTTP method handling
- Status code verification
- Pagination testing
- Data persistence checks

### 🚀 Advanced Testing
- Schema inconsistency detection
- Data integrity validation
- Duplicate data handling
- Token behavior analysis

### 🔐 Security-Oriented Thinking
- Improper input validation
- Unauthorised field manipulation
- Privilege escalation risks
- Method misuse
- Data exposure concerns

> The focus is on **thinking like a tester**, not just executing requests and test cases with a tool.

---

## 📁 Repository Structure (High-Level)

- Endpoint-wise findings documented in Markdown
- Screenshots used as Proof of Concepts (PoCs)
- Clear separation of:
  - Found Behaviours
  - Inconsistent Behaviours
  - Expected vs Actual vs Impact

---

## 📌 What This Repository Is NOT

- ❌ Not a complete test report
- ❌ Not a full security audit
- ❌ Not automation-focused 

`Automation` and `load testing` will be added as **future extensions**.

---

## 🧩 Why This Repo Exists   

This repository is intended to show a sample of:

- How I **think before testing**
- How I **identify risks**
- How I **document findings clearly**
- How I **communicate issues with impact**
- How I balance **functional, advanced, and security perspectives**

---

## 🚀 Future Enhancements (Optional)

- API automation using **Python + pytest**
- Load testing using **Locust**

---

## 👤 Author
[Ishtiaque Foysol](https://www.linkedin.com/in/ishtiaque-foysol-8899947b/)     

Focused on:   
- API Testing
- Automation
- Security-aware testing
- Exploratory and risk-based testing

---

## 📢 Disclaimer

All findings are based on a **public demo API** and are used **solely for learning and demonstration purposes**.
No real user data or production systems are involved.
