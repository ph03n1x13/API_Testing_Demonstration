import pytest

from core.api_client import APIClient
from config.base_config import BASE_URL, DEFAULT_HEADERS



@pytest.fixture(scope="session")
def api_client():
    """
    Session scoped API client Fixture

    Responsibilities:
    - Initialize APIClient once per test session
    - Share the same configuration across tests
    - Keep test files clean and focused on assertions

    Returns:
        APIClient instance

    """
    return APIClient(
        base_url= BASE_URL,
        default_headers=  DEFAULT_HEADERS,
        )