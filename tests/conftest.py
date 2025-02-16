import pytest
from utils.auth_helper import AuthHelper


@pytest.fixture(scope="module")
def api_get_access_token():
    """
    Pytest fixture that returns an authenticated APIClient instance.

    Returns:
        APIClient: An authenticated API client with a valid JWT token.
    """
    return AuthHelper.get_authenticated_client()
