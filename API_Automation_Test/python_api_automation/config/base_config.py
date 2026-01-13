"""
Base configuration for API automation.

Responsibilities:
- Store environment-independent configuration
- Centralize base URL and default settings
- Keep test files clean and readable

Note:
Environment switching (dev/stage/prod) can be added later if required.
"""
import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = "https://reqres.in/api"

DEFAULT_TIMEOUT = 13

DEFAULT_HEADERS = {
    "x-api-key": os.getenv("REQRES_API_KEY")
    }