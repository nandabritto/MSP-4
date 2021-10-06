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

class ResourceMediaTests(SimpleTestCase):

    def test_media_status(self):
        response = self.client.get('/resources/media')
        self.assertEquals(response.status_code, 200)

    def test_media_by_name(self):
        response = self.client.get(reverse('resources-media'))
        self.assertEquals(response.status_code, 200)

    def test_media_template(self):
        response = self.client.get(reverse('resources-media'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources/media.html')

class ResourceIDETests(SimpleTestCase):

    def test_ide_status(self):
        response = self.client.get('/resources/ide')
        self.assertEquals(response.status_code, 200)

    def test_ide_by_name(self):
        response = self.client.get(reverse('resources-ide'))
        self.assertEquals(response.status_code, 200)

    def test_ide_template(self):
        response = self.client.get(reverse('resources-ide'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources/ide.html')