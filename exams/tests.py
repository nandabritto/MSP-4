from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .models import *
from . import views


class ExamListPageTests(TestCase):
    # Tests the url for the exam list page
    def test_exam_list_page_status_code(self):
        response = self.client.get('/exams')
        self.assertEquals(response.status_code, 200)

    def test_exam_list_url_by_name(self):
        response = self.client.get(reverse('exams:list-view'))
        self.assertEquals(response.status_code, 200)

    def test_exam_list_uses_correct_template(self):
        response = self.client.get(reverse('exams:list-view'))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'exam-list.html')
