from django.test import TestCase
from rest_framework.test import APITestCase
from .models import UserProfile


class UserProfileAPITestCase(APITestCase):

    def setUp(self):
        UserProfile.objects.create(email="sknitt654@gmail.com",
                                   name="Dinesh Raj",
                                   mobile_number="9430089034",
                                   address="Patna, Bihar",
                                   password="admin123")

    def test_get_method(self):
        url = 'http://127.0.0.1:8000/api/profile/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        qs = UserProfile.objects.filter(name="Dinesh Raj")
        self.assertEqual(qs.count(), 1)
