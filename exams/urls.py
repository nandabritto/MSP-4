from django.urls import path
from .views import (
    ExamListView,
    exam_view
)

app_name = 'exams'

# Exam app specific urls

urlpatterns = [
    path('examlist', ExamListView.as_view(), name='exam-view'),
    path('examlist<pk>/', exam_view, name='exam_view')
]