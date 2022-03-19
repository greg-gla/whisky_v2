from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class LoginViewTests(TestCase):
    def test_login_view_is_valid(self):
        response = self.client.get(reverse('accounts:login'))

        self.assertEqual(response.status_code, 200)

class logoutViewTests(TestCase):
    def test_logout_view_source_is_valid(self):
        response = self.client.get(reverse('accounts:logout'))

        self.assertEqual(response.status_code, 302)

class registerViewTests(TestCase):
    def test_register_view_is_valid(self):
        response = self.client.get(reverse('accounts:register'))

        self.assertEqual(response.status_code, 200)

class profileViewTests(TestCase):
    def test_profile_view_source_is_valid(self):
        response = self.client.get(reverse('accounts:profile'))

        self.assertEqual(response.status_code, 302)