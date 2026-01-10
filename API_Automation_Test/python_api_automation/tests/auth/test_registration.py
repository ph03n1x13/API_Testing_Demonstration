import pytest

from config.endpoints import REGISTER
from core.payload_factory import PayloadFactory
def test_registration_user_happy_path(api_client):
    """
    Happy Path Testing with valid payload for user registration
    - Return code should be 200
    - An ID should exist upon successful registration
    - There should be a temporary validation token for further steps

    """
    payload = PayloadFactory.valid_registration_payload()
    response = api_client.post(
        endpoint= REGISTER,
        json= payload
    )
    response_body = response.json()

    # Assert expected criteria
    assert response.status_code == 200, "Expected HTTP 200 for a valid registration"
    assert "id" in response_body, "A unique user id is expected up successful registration"
    assert "token" in response_body, "token must be in the response body"
    assert response_body['token'], "Token must not be empty"

def test_extra_field_adding_during_registration(api_client):
    """
    Try to add an extra field during registration for manipulating user role
    - Inject an unauthorised role in the paylaod
    - Expected behaviour:
       a) API should reject the request with HTTP 403 Forbidden or HTTP 400 bad request
       b) API should not return any temporary token for further steps even if the response is HTTP 200
    """
    payload = PayloadFactory.registration_payload_with_extra_field()
    response = api_client.post(
        endpoint= REGISTER,
        json= payload
    )
    response_body = response.json()
    assert response.status_code == 400, "Expected Status Code is HTTP 400"
    assert "token" not in response_body, "No token should be in response body"
    assert not response_body["token"], "No token should be present in the token key"