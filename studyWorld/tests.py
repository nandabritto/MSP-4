from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from . import views


class HomePageTests(SimpleTestCase):
    # Status check of the websites landing page
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


class ResourceListTests(SimpleTestCase):
    # Status check of the websites resources list page
    def test_resources_status(self):
        response = self.client.get('/resources/')
        self.assertEquals(response.status_code, 200)

    def test_resources_by_name(self):
        response = self.client.get(reverse('resources-list'))
        self.assertEquals(response.status_code, 200)

    def test_resources_template(self):
        response = self.client.get(reverse('resources-list'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources/resources.html')


class ResourceMediaTests(SimpleTestCase):
    # Status check of the media page for the resources section of the site
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
    # Status check of the IDE page for the resources section of the site
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


class ResourceFrameworksTests(SimpleTestCase):
    # Status check of the Frameworks page for the resources section of the site
    def test_frameworks_status(self):
        response = self.client.get('/resources/frameworks')
        self.assertEquals(response.status_code, 200)

    def test_frameworks_by_name(self):
        response = self.client.get(reverse('resources-frameworks'))
        self.assertEquals(response.status_code, 200)

    def test_frameworks_template(self):
        response = self.client.get(reverse('resources-frameworks'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources/frameworks.html')


class ResourceBadgesTests(SimpleTestCase):
    # Status check of the badges page for the resources section of the site
    def test_badges_status(self):
        response = self.client.get('/resources/badges')
        self.assertEquals(response.status_code, 200)

    def test_badges_by_name(self):
        response = self.client.get(reverse('resources-badges'))
        self.assertEquals(response.status_code, 200)

    def test_badges_template(self):
        response = self.client.get(reverse('resources-badges'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources/badges.html')


class ResourceLearningTests(SimpleTestCase):
    # Status check of the learning page for the resources section of the site
    def test_learning_status(self):
        response = self.client.get('/resources/learning')
        self.assertEquals(response.status_code, 200)

    def test_learning_by_name(self):
        response = self.client.get(reverse('resources-learning'))
        self.assertEquals(response.status_code, 200)

    def test_learning_template(self):
        response = self.client.get(reverse('resources-learning'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources/learning.html')


class ResourceToolsTests(SimpleTestCase):
    # Status check of the tools page for the resources section of the site
    def test_tools_status(self):
        response = self.client.get('/resources/tools')
        self.assertEquals(response.status_code, 200)

    def test_tools_by_name(self):
        response = self.client.get(reverse('resources-tools'))
        self.assertEquals(response.status_code, 200)

    def test_tools_template(self):
        response = self.client.get(reverse('resources-tools'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'resources/tools.html')
