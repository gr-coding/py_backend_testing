def test_create_cart(api_get_access_token):
    """
    Test creating a new cart for an authenticated user.
    """
    cart_data = {
        "userId": 1,
        "products": [
            {"id": 1, "quantity": 2},
            {"id": 5, "quantity": 1}
        ]
    }

    response = api_get_access_token.post("carts/add", data=cart_data)

    assert response is not None, "Response should not be None"
    assert "id" in response, "Response should contain 'id'"
    assert "products" in response, "Response should contain 'products'"
 