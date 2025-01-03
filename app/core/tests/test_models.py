"""
Tests for mmodels
"""
from decimal import Decimal # Used to store one of the values of oor recipe object.
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

class ModelTests(TestCase):
    """Test Models."""

    def test_create_user_with_email_successful(self):
        """Test Creating a user with email is successful."""

        email = "test@example.com"
        password = "testpassword"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_is_normalized(self):
        """Test the email of a user is normalized"""

        sample_email = [
            ["test1@EXAMPLE.com", "test1@example.com"],
            ["Test2@Example.com", "Test2@example.com"],
            ["TEST3@EXAMPLE.COM", "TEST3@example.com"],
            ["test4@example.COM", "test4@example.com"],
        ]

        for email, expected in sample_email:
            user = get_user_model().objects.create_user(email, "sample123")
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_raise_error(self):
        """Test that creating a user without an email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user("", "test123")

    def test_create_superuser(self):
        """Test creating a superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com", "test123",
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_recipe(self):
        """Test creating a recipe is successful"""
        user = get_user_model().objects.create_user(
            "test@exaple.com",
            "testpassword",
        )

        recipe = models.Recipe.objects.create(
            user=user,
            title="Sample recipe name",
            time_minutes=5,
            price=Decimal('5.99'),
            description="Sample recipe description",
        )

        self.assertEqual(str(recipe), recipe.title)