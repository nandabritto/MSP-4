from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .models import Providers
from . import views
from .forms import providerCreateForm


class ProvidersListPageTests(TestCase):
    # Tests the url for the Providers list page
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


class ProvidersCreatePageTests(TestCase):
    # Testes to confirm Providers create page loads
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


class ProviderAmendPageTests(TestCase):
    # Tests the url for Provider Amend page
    def setUp(self):
        Providers.objects.create(
            name='Test Provider',
            description='Test description for the providers for unit testing',
            url='www.test.test',
        )

    def test_provider_update_status_code(self):
        response = self.client.get('/providers/update/1', args=[1])
        self.assertEquals(response.status_code, 200)

    def test_provider_update_url_by_name(self):
        response = self.client.get(reverse(
            'providers:providers-update', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_provider_update_uses_correct_template(self):
        response = self.client.get(reverse(
            'providers:providers-update', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'update.html')


class ProviderDeletePageTests(TestCase):
    # Tests the url for the Provider delete confirmation page
    def setUp(self):
        Providers.objects.create(
            name='Test Provider delete',
            description='Test description for the providers for unit testing',
            url='www.test.test',
        )

    def test_provider_delete_status_code(self):
        response = self.client.get('/providers/delete/1', args=[1])
        self.assertEquals(response.status_code, 200)

    def test_provider_delete_url_by_name(self):
        response = self.client.get(reverse(
            'providers:providers-delete', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_provider_delete_uses_correct_template(self):
        response = self.client.get(reverse(
            'providers:providers-delete', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'delete.html')
