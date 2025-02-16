def test_search_products(api_get_access_token):
    """
    Test searching for products using query parameters.
    """
    response = api_get_access_token.get("products/search", params={"q": "laptop"})

    assert response is not None, "Response should not be None"
    assert "products" in response, "Response should contain 'products'"
    assert isinstance(response["products"], list), "Products should be a list"
    assert len(response["products"]) > 0, "Products list should not be empty"
    