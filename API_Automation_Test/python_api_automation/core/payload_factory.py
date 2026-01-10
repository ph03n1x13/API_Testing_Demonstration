"""
Payload Factory
----------------
This factory class generates request payloads for API endpoints.
Generates valid, invalid, and security-focused payload variations.
"""

class PayloadFactory:
    # Login Payloads
    @staticmethod
    def valid_login_payload():
        return {
            "email": "eve.holt@reqres.in",
            "password": "12345"
        }

    @staticmethod
    def missing_password_login_payload():
        return {
            "email": "eve.holt@reqres.in"
        }

    @staticmethod
    def invalid_login_payload_wrong_type():
        return {
            "email": 12345,
            "password": True
        }

    # Registration payloads
    @staticmethod
    def valid_registration_payload():
        return {
            "email": "eve.holt@reqres.in",
            "password": "12345"
        }

    @staticmethod
    def registration_payload_with_integer_password():
        return {
            "email": "sydney@fife",
            "password": 123456
        }

    @staticmethod
    def registration_payload_with_extra_field():
        return {
            "email": "eve.holt@reqres.in",
            "password": "12345",
            "role": "ADMIN"
        }

    @staticmethod
    def empty_registration_payload():
        return {}

    @staticmethod
    def registration_payload_missing_email():
        return {
            "password": "hello world"
        }
