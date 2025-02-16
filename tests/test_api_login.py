

class TestAPILogin: 
    """
    Test class for API Login tests
    """


    def test_get_user_profile(self, api_get_access_token):
        """
        Test retrieving authenticated user profile.
        """
        response = api_get_access_token.get("auth/me")
        
        assert response is not None, "Response should not be None"
        assert "id" in response, "Response should contain 'id'"
        assert "username" in response, "Response should contain 'username'"
        print("User profile fetched successfully:", response)
