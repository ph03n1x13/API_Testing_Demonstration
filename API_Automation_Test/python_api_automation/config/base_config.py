"""
Base configuration for API automation.

Responsibilities:
- Store environment-independent configuration
- Centralize base URL and default settings
- Keep test files clean and readable

Note:
Environment switching (dev/stage/prod) can be added later if required.
"""

BASE_URL = "https://reqres.in/api"

DEFAULT_TIMEOUT = 13

DEFAULT_HEADERS = {
    "x-api-key":"your_reqres_api_key_is_here"
    } # we'll use .env later for further improvement