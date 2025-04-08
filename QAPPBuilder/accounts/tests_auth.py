# # tests_auth.py (accounts)
# # !/usr/bin/env python3
# # coding=utf-8
# # young.daniel@epa.gov

# """
# Test cases for user authentication in the accounts app.

# Available functions:
# - Test user login
# - Test user registration
# - Test password reset
# """

# from django.test import Client, TestCase
# from django.contrib.auth.models import User
# from django.urls import reverse
# from teams.models import Team


# class UserAuthenticationTest(TestCase):
#     """Test cases for user authentication."""

#     def setUp(self):
#         """Set up test data."""
#         self.client = Client()
#         self.user = User.objects.create_user(
#             username='testuser',
#             email='test@example.com',
#             password='testpass123'
#         )
#         self.team = Team.objects.create(
#             name='Test Team',
#             created_by=self.user,
#             last_modified_by=self.user
#         )

#     def test_user_login(self):
#         """Test user login functionality."""
#         # Test successful login
#         response = self.client.post(
#             reverse('login'),
#             {'username': 'testuser', 'password': 'testpass123'}
#         )
#         self.assertEqual(response.status_code, 302)  # Redirect after login

#         # Test failed login
#         response = self.client.post(
#             reverse('login'),
#             {'username': 'testuser', 'password': 'wrongpassword'}
#         )
#         self.assertEqual(response.status_code, 200)  # Stay on login page

#         # Test login with non-existent user
#         response = self.client.post(
#             reverse('login'),
#             {'username': 'nonexistent', 'password': 'testpass123'}
#         )
#         self.assertEqual(response.status_code, 200)  # Stay on login page

#     def test_user_logout(self):
#         """Test user logout functionality."""
#         # Login first
#         self.client.login(username='testuser', password='testpass123')

#         # Test logout
#         response = self.client.get(reverse('logout'))
#         self.assertEqual(response.status_code, 302)  # Redirect after logout

#         # Verify user is logged out
#         response = self.client.get(reverse('home'))
#         self.assertNotIn('testuser', str(response.content))

#     def test_user_registration(self):
#         """Test user registration functionality."""
#         # Test successful registration
#         response = self.client.post(
#             reverse('register'),
#             {
#                 'username': 'newuser',
#                 'email': 'newuser@example.com',
#                 'password1': 'newpass123',
#                 'password2': 'newpass123'
#             }
#         )
#         self.assertEqual(response.status_code, 302)  # Redirect after registration

#         # Verify user was created
#         self.assertTrue(User.objects.filter(username='newuser').exists())

#         # Test registration with existing username
#         response = self.client.post(
#             reverse('register'),
#             {
#                 'username': 'testuser',  # Already exists
#                 'email': 'another@example.com',
#                 'password1': 'newpass123',
#                 'password2': 'newpass123'
#             }
#         )
#         self.assertEqual(response.status_code, 200)  # Stay on registration page

#         # Test registration with mismatched passwords
#         response = self.client.post(
#             reverse('register'),
#             {
#                 'username': 'anotheruser',
#                 'email': 'another@example.com',
#                 'password1': 'newpass123',
#                 'password2': 'differentpass'  # Mismatched
#             }
#         )
#         self.assertEqual(response.status_code, 200)  # Stay on registration page

#     def test_password_reset(self):
#         """Test password reset functionality."""
#         # Test password reset request
#         response = self.client.post(
#             reverse('password_reset'),
#             {'email': 'test@example.com'}
#         )
#         self.assertEqual(response.status_code, 302)  # Redirect after request

#         # Test password reset with non-existent email
#         response = self.client.post(
#             reverse('password_reset'),
#             {'email': 'nonexistent@example.com'}
#         )
#         self.assertEqual(response.status_code, 302)  # Still redirect for security