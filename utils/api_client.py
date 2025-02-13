import requests
from .config import BASE_URL

class APIClient:
    def __init__(self, base_url=BASE_URL):
        self.base_url = base_url

    def get(self, endpoint, params=None):
        return requests.get(f"{self.base_url}/{endpoint}", params=params)

    def post(self, endpoint, data=None):
        return requests.post(f"{self.base_url}/{endpoint}", json=data)
    