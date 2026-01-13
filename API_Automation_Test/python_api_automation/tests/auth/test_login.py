import pytest
from samba.dcerpc.dcerpc import payload

from config.endpoints import LOGIN
from core.payload_factory import PayloadFactory

def test_user_login_happy_path(api_client):
    """
    Happy Path Testing with valid payload for user login
    - Return code should be 200
    """
    payload = PayloadFactory.valid_login_payload()
    response = api_client.post(endpoint= LOGIN,
                               json= payload
                               )
    assert response.status_code == 200, "Expected Status Code 200"

def test_user_login_without_password(api_client):
    """
    Try  to login without a password
    - Should return a 400 bad request
    -  Should return a message that password is needed
    """
    payload = PayloadFactory.missing_password_login_payload()
    response = api_client.post(endpoint= LOGIN,
                               json= payload
                               )

    assert response.status_code == 400, "Expected Status Code is 400"
    assert "Missing password" in response.text

def test_user_login_with_invalid_data_type(api_client):
    """
    Here username type is int, and password is string.
    - Expected response 400
    - Expected a message that user name can't be int
    """
    payload = PayloadFactory.invalid_login_payload_wrong_type()
    response = api_client.post(
        endpoint= LOGIN,
        json= payload
    )

    assert response.status_code == 400, "Expected Status Code is 400"
    assert "user not found" in response.text, "Error message missing"
