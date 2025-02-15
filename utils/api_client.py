import requests
import base64


class APIClient:
    def __init__(self, base_url, auth_type=None, auth_token=None, username=None, password=None):
        self.base_url = base_url
        self.auth_type = auth_type
        self.auth_token = auth_token
        self.username = username
        self.password = password
    
    def _set_headers(self):
        try:
            headers = {"Content-Type": "application/json"}

            if self.auth_type == "bearer":
                if not self.auth_token:
                    raise ValueError("Bearer authentication requires a token.")
                headers["Authorization"] = f"Bearer {self.auth_token}"
            
            elif self.auth_type == "basic":
                if not self.username or not self.password:
                    raise ValueError("Basic authentication requires both username and password.")
                auth_string = f"{self.username}:{self.password}"
                encoded_auth = base64.b64encode(auth_string.encode()).decode()
                headers["Authorization"] = f"Basic {encoded_auth}"

            return headers
        except Exception as e:
            raise e

    def get(self, endpoint, params=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.get(url, params=params, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise e
            

    def post(self, endpoint, data=None):
        url = f"{self.base_url}/{endpoint}"
        try:
            response = requests.post(url, json=data, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise e
    