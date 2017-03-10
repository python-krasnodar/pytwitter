from django.test import Client, TestCase
from django.contrib.auth.models import User


class UserListViewTestCase(TestCase):
    def setUp(self):
        super().setUp()

        self.client = Client()

        user = User.objects.create(username='test', email='test@example.com')
        user.save()

        user = User.objects.create(username='test2', email='test2@example.com')
        user.save()

    def test_availability_of_the_list(self):
        response = self.client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_availability_of_the_record(self):
        response = self.client.get('/users/test/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/users/test2/')
        self.assertEqual(response.status_code, 200)
