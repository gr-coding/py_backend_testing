import requests
import base64


class APIClient:
    """Reusable API client for interacting with REST APIs with authentication support."""

    def __init__(self, base_url, auth_type=None, username=None, password=None):
        """
        Initializes the APIClient.

        Args:
            base_url (str): The base URL of the API.
            auth_type (str, optional): Type of authentication ('bearer' or 'basic'). Defaults to None.
            username (str, optional): Username for authentication. Defaults to None.
            password (str, optional): Password for authentication. Defaults to None.
        """
        self.base_url = base_url
        self.auth_type = auth_type
        self.username = username
        self.password = password
        self.auth_token = None  # Initialize token as None
        self.headers = {"Content-Type": "application/json"}  # Default headers
        
        if self.auth_type == "bearer":
            self.authenticate("auth/login", {"username": self.username, "password": self.password})


    def _update_auth_header(self):
        """Updates the Authorization header after successful authentication."""
        if self.auth_type == "bearer" and self.auth_token:
            self.headers["Authorization"] = f"Bearer {self.auth_token}"
        elif self.auth_type == "basic" and self.username and self.password:
            auth_string = f"{self.username}:{self.password}"
            encoded_auth = base64.b64encode(auth_string.encode()).decode()
            self.headers["Authorization"] = f"Basic {encoded_auth}"


    def authenticate(self, endpoint, credentials):
        """
        Handles authentication by sending credentials to a specified endpoint and updates headers.

        Args:
            endpoint (str): Authentication API endpoint.
            credentials (dict): Dictionary containing authentication credentials.

        Returns:
            str or None: Authentication token if successful, None otherwise.
        """
        response = self.post(endpoint, data=credentials)

        if response and "accessToken" in response:  # 🔹 Updated to use "accessToken"
            self.auth_token = response["accessToken"]  # 🔹 Correct key
            self._update_auth_header()  # 🔹 Update headers with the new token
            print(f"Authenticated successfully! Token: {self.auth_token}")
        return self.auth_token

        print(f"Authentication failed: {response}")
        return None


    def get(self, endpoint, params=None):
        """Sends a GET request to the API."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"GET request failed: {e}")
            return None


    def post(self, endpoint, data=None):
        """Sends a POST request to the API."""
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"POST request failed: {e}")
            return None
