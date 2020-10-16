from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

LIST_USERS_URL = reverse('users:list')
CREATE_USER_URL = reverse('users:create')
TOKEN_URL = reverse('users:token')
ME_URL = reverse('users:me')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTests(TestCase):
    """Test the users API (public)"""

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """Test creating user with valid payload is successful"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'name': 'test name'
        }
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)
        self.assertIn('email', res.data)
        self.assertIn('name', res.data)

    def test_user_exists(self):
        """Test creating a user that already exists fails"""
        payload = {
            'email': 'test@example.com',
            'password': 'testpassword',
            'name': 'test name',
        }
        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)


class PrivateUserApiTests(TestCase):
    """Test API requests that require authentication"""

    def setUp(self):
        self.user = create_user(
            email='test@example.com',
            password='testpassword',
            name='name name'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_list_users_success(self):
        """Test listing users for logged in used"""
        res = self.client.get(LIST_USERS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": 1,
                    "email": "test@example.com",
                    "name": "name name"
                }
            ]
        })
