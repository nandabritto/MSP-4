from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User, AnonymousUser
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
    # Testes to confirm Providers create redirects for Anon user
    def test_provider_create_page_status_code(self):
        response = self.client.get('/providers/create/')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,'/')

    def test_provider_create_page_url_by_name(self):
        response = self.client.get(reverse('providers:providers-create'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,'/')


class ProvidersUpdatePageTest(TestCase):
    # Testes to confirm Providers create redirects for Anon user
    def test_provider_create_page_status_code(self):
        response = self.client.get('/providers/update/1')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,'/')


class ProvidersDeletePageTest(TestCase):
    # Testes to confirm Providers create redirects for Anon user
    def test_provider_create_page_status_code(self):
        response = self.client.get('/providers/delete/1')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response,'/')
