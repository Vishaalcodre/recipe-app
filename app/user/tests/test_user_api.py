"""
    Tests for the user API
"""
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


CREATE_USER_URL = reverse("user:create") #This will return the URL for the create user endpoint
TOKEN_URL = reverse("user:token") #This will return the URL for the token endpoint

def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

class PublicUserApiTests(TestCase):
    """Test the public feature of the user API"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a new user with valid payload is successful"""
        payload = {
            "email": "test@example.com",
            "password": "test_password",
            "name": "Test User"
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email = payload["email"])
        self.assertTrue(user.check_password(payload["password"]))
        self.assertNotIn("password", res.data)

    def test_user_with_user_email_exists_error(self):
        """Test that creating a user with an existing email returns an error"""
        payload = {
            "email": "test@example.com",
            "password": "test_password",
            "name": "Test User"
        }
        create_user(**payload) #Create a user with the same email
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test that creating a user with a password that is too short returns an error"""
        payload = {
            "email": "test@example.com",
            "password": "test",
            "name": "Test User"
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload["email"]
        ).exists()
        self.assertFalse(user_exists)

    def test_create_token_for_user(self):
        """Test that a token is created for the valid user credentials"""

        user_details = {
            "name": "Test User",
            "email": "test@example.com",
            "password": "test_password"
        }

        create_user(**user_details)

        payload = {
            "email": user_details["email"],
            "password": user_details["password"]
        }

        res = self.client.post(TOKEN_URL, payload)

        self.assertIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_token_error_for_bad_credentials(self):
        """Test that token is not created for invalid credentials"""

        create_user(email="test@example.com", password="goodpassword")

        payload = {"email": '',
                   "password": "wrong_password"}
        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_token_error_for_empty_password(self):
        """Test that token is not created for empty password"""

        payload = {
            "email": 'test@example.com',
            "password": ""
            }

        res = self.client.post(TOKEN_URL, payload)
        self.assertNotIn("token", res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)