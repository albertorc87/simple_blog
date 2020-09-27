# Django
from django.test import TestCase
from django.test import Client

# Python
from http import HTTPStatus

# Models
from django.contrib.auth.models import User

class UserTestCase(TestCase):

    def setUp(self):
        self.c = Client()

    def test_is_ok_page_login(self):
        response = self.c.get('/login')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_is_ok_page_register(self):
        response = self.c.get('/registro')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_login_user(self):
        credentials = {
            'username': 'Alber Login',
            'password': '4ABXX4S9CuB3rgVM'
        }

        user = User.objects.create_user(**credentials)
        response = self.c.post('/login', credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)

    def test_register_user(self):

        data = {
            'username': 'TestAlber',
            'email': 'alber@cosasdedevs.com',
            'password': '4ABXX4S9CuB3rgVM',
            'password_confirmation': '4ABXX4S9CuB3rgVM',
        }

        response = self.c.post('/registro', data)

        try:
            user = User.objects.get(username=data['username'])
        except User.DoesNotExist:
            user = NULL

        self.assertIsInstance(user, User)


