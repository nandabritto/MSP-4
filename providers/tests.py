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

# Testes to confirm Providers create page loads
class ProvidersCreatePageTests(TestCase):

    def test_provider_create_page_status_code(self):
        response = self.client.get('/providers/create/')
        self.assertEquals(response.status_code, 200)

    def test_provider_create_page_url_by_name(self):
        response = self.client.get(reverse('providers:providers-list'))
        self.assertEquals(response.status_code, 200)

    def test_provider_create_page_uses_correct_template(self):
        response = self.client.get(reverse('providers:providers-create'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'create.html')

# Tests the url for the page where a specific exam is displayed
class ProviderAmendPageTests(TestCase):

    def setUp(self):
        Providers.objects.create(
            name='Test Provider',
            description='Test description for the providers for unit testing',
            url='www.test.test',
        )

    def test_provider_update_status_code(self):
        response = self.client.get('providers/update/<pk>',args=[1])
        self.assertEquals(response.status_code, 200)

    def test_provider_update_url_by_name(self):
        response = self.client.get(reverse('providers:providers-update', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_provider_update_uses_correct_template(self):
        response = self.client.get(reverse('providers:providers-update', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')