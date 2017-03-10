from django.test import Client, TestCase
from django.contrib.auth.models import User


class LoginPageTestCase(TestCase):
    def setUp(self):
        super().tearDown()

        self.client = Client()

        user = User.objects.create(username='test', password='test')
        user.save()

    def test_availability(self):
        response = self.client.get('/accounts/login/')
        self.assertEqual(response.status_code, 200)

    def test_send_post_data(self):
        response = self.client.post('/accounts/login/', {'username': 'test', 'password': 'test'})
        self.assertEqual(response.status_code, 200)