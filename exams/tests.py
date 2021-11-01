from django.test import SimpleTestCase, TestCase
from django.urls import reverse, resolve
from .models import *
from . import views

# Tests the url for the exam list page
class ExamListPageTests(TestCase):

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

# Tests the url for the page when a specific exam is selected
# And the questions have been displayed and/or submitted
class ExamDisplayPageTests(TestCase):

    def setUp(self):
        Exam.objects.create(
            name='Test Exam',
            topic='Mathematics',
            description='This is a test exam for unit testing',
            difficulty='hard',
            number_of_questions='5',
            time='2',
            required_score_to_pass='40'
        )

    def test_exam_display_status_code(self):
        response = self.client.get('/exams',args=[1])
        self.assertEquals(response.status_code, 200)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('exams:exam_view', args=[1]))
        self.assertEquals(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('exams:exam_view', args=[1]))
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'exam-display.html')
