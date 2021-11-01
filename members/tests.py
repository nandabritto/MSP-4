from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from . import views

# Test for the registration page load
class MemberRegistrationPageTests(TestCase):
    
    def test_registration_page_status_code(self):
        response = self.client.get('/members/register')
        self.assertEquals(response.status_code, 200)

    def test_registration_url_by_name(self):
        response = self.client.get(reverse('members:member-register'))
        self.assertEquals(response.status_code, 200)

    def test_registration_uses_correct_template(self):
        response = self.client.get(reverse('members:member-register'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'register.html')

# Test for the signin page load
class MemberSigninPageTests(TestCase):
    
    def test_signin_page_status_code(self):
        response = self.client.get('/members/signin')
        self.assertEquals(response.status_code, 200)

    def test_signin_url_by_name(self):
        response = self.client.get(reverse('members:member-signin'))
        self.assertEquals(response.status_code, 200)

    def test_signin_uses_correct_template(self):
        response = self.client.get(reverse('members:member-signin'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'signin.html')
