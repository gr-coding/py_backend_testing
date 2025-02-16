from utils.api_client import APIClient


class AuthHelper:
    """Helper class to manage authentication for API tests."""

    @staticmethod
    def get_authenticated_client():
        """
        Authenticates and returns an APIClient instance with a valid JWT token.

        Returns:
            APIClient: An authenticated API client.
        """
        client = APIClient(base_url="https://dummyjson.com", auth_type="bearer", 
                           username="sophiab", password="sophiabpass")

        if not client.auth_token:
            raise Exception("Authentication failed! Could not retrieve JWT token.")
        
        print(f"Authenticated successfully! Token: {client.auth_token}")
        return client  # Return authenticated client
