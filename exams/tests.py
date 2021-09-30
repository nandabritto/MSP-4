from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from . import views

# Create your tests here.
# Tests the url for the exam list page
# class ExamListPageTests(TestCase):

#     def test_home_page_status_code(self):
#         response = self.client.get('/exams')
#         self.assertEquals(response.status_code, 200)

#     def test_view_url_by_name(self):
#         response = self.client.get(reverse('exams:exams-view'))
#         self.assertEquals(response.status_code, 200)

#     def test_view_uses_correct_template(self):
#         response = self.client.get(reverse('exams:exams-view'))
#         self.assertEquals(response.status_code, 200)
#         self.assertTemplateUsed(response, 'exam-list.html')