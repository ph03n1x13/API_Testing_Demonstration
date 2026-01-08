### Found Behaviours
1. User data can be updated successfully with a valid JSON body.  
[](../Screenshots/update_api/update_ok.png)

### Inconsistent Behaviours

1. `Lack of Data Type Validation`  
The `update` endpoint accepts any valid JSON payload without validating data types.

`Expected:`
- Field values should be validated according to data type.
- Invalid data types should be rejected with an `HTTP 400` response.

`Actual:`
- Update succeeds even with invalid data types.

`Impact:`
- May lead to data inconsistency and corruption.

---

2. `Missing API Contract Enforcement`  
The `update` endpoint does not enforce any documented schema or field restrictions in `Swagger`.

`Expected:`
- Only documented and allowed fields should be updatable.

`Actual:`
- Any valid JSON body updates user data.

[](../Screenshots/update_api/documentation.png)

`Impact:`
- This can break API contract and reduces reliability for API consumers.

---

3. `Update with Unexpected / Restricted Fields`  
A user can be updated with unauthorized fields such as `"role": "admin"`.

[](../Screenshots/update_api/unexpected_value.png)

`Expected:`
- Restricted or unknown fields should be rejected with `HTTP 400` response.

`Actual:`
- Update succeeds with unauthorised fields.

`Impact:`
- Potential security risk due to unauthorised role or privilege manipulation.
