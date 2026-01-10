import requests
from typing import Dict, Any, Optional

class APIClient:
    """
    An HTTP implementation for API automation.

    Responsibilities:
    - Send HTTP requests
    - Handle headers and timeouts
    - Return raw response object from explicit assertion in test_ files

    Out of Scope
    - Assert response
    - Schema validation
    - Business Logic
    """

    def __init__(self,
                 base_url: str,
                 default_headers: Optional[Dict[str, str]] = None,
                 timeout: int = 13):

        self.base_url = base_url.rstrip("/") # strip the leading forward slash for sanity
        self.default_headers = default_headers or {
            "Content-Type": "application/json"
        }
        self.timeout = timeout


    def _request(self,
                 method: str,
                 endpoint: str,
                 headers: Optional[Dict[str, str]] = None,
                 params: Optional[Dict[str, Any]] = None,
                 json: Optional[Dict[str, Any]] = None
                 ):
        """
        This method returns the response  body in APIClient HTTP methods,
        A wrapper around the requests builtin

        """
        url = f"{self.base_url}/{endpoint.lstrip('/')}"

        merged_headers = self.default_headers.copy()
        if headers:
            merged_headers.update(headers)

        http_response = requests.request(
            method= method,
            url= url,
            headers= merged_headers,
            params= params,
            json= json,
            timeout= self.timeout
        )

        return http_response # return the requests response object

    # =================== APIClient HTTP Wrappers of requests ===================

    def get(self,
            endpoint: str,
            headers: Optional[Dict[str, str]] = None,
            params: Optional[Dict[str, Any]] = None
            ):
        """
        This wrapper returns the response of a GET request
        """
        return self._request(
            method= "GET",
            endpoint= endpoint,
            headers= headers,
            params= params
        )

    def post(self,
            endpoint: str,
            headers: Optional[Dict[str, str]] = None,
            json: Optional[Dict[str, Any]] = None
            ):
        """
        This wrapper returns the response of a POST request
        """
        return self._request(
            method= "POST",
            endpoint= endpoint,
            headers= headers,
            json= json
        )

    def put(self,
            endpoint: str,
            headers: Optional[Dict[str, str]] = None,
            json: Optional[Dict[str, Any]] = None
            ):
        """
        This wrapper returns the response of a PUT request
        """
        return self._request(
            method= "PUT",
            endpoint= endpoint,
            headers= headers,
            json= json
        )

    def delete(self,
            endpoint: str,
            headers: Optional[Dict[str, str]] = None,
            ):
        """
        This wrapper returns the response of a DELETE request
        """
        return self._request(
            method= "DELETE",
            endpoint= endpoint,
            headers= headers
        )