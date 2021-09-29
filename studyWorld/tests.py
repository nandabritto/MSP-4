from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from . import views

class HomePageTests(SimpleTestCase):

    def test_home_status(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

    def test_home_by_name(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)

    def test_home_template(self):
        response = self.client.get(reverse('index'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')