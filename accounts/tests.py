from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages


class LoginLogoutViewTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse("login_view")
        self.teams_list_url = reverse("teams_list")
        self.user = User.objects.create_user(
            username="testuser", email="test@example.com", password="testpassword"
        )

    def test_login_view_post_success(self):
        response = self.client.post(
            self.login_url, {"username": "testuser", "password": "testpassword"}
        )
        self.assertRedirects(response, self.teams_list_url)
        user = authenticate(username="testuser", password="testpassword")
        self.assertIsNotNone(user)
        self.assertTrue(user.is_authenticated)

    def test_login_view_post_failure(self):
        response = self.client.post(
            self.login_url, {"username": "testuser", "password": "wrongpassword"}
        )
        self.assertRedirects(response, self.login_url)

    def test_logout_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("logout_view"))
        self.assertRedirects(response, self.login_url)
