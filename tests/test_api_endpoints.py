from utils.api_client import APIClient


client = APIClient()

def test_get_all_products():
    """Test to verify that all products are retrieved from the API."""
    response = client.get("products")
    assert response.status_code == 200
    data = response.json()
    assert "products" in data
    assert len(data["products"]) > 0  # Ensure products are returned
