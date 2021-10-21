from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .models import Providers
from . import views

# Create your tests here.
# Tests the url for the exam list page
class ProvidersListPageTests(TestCase):

    def test_provider_list_page_status_code(self):
        response = self.client.get('/providers/')
        self.assertEquals(response.status_code, 200)

    def test_provider_list_page_url_by_name(self):
        response = self.client.get(reverse('providers:providers-list'))
        self.assertEquals(response.status_code, 200)

    def test_provider_list_page_uses_correct_template(self):
        response = self.client.get(reverse('providers:providers-list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'provider-list.html')