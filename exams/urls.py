from django.urls import path
from django.conf.urls.static import static
from .views import (
    ExamListView,
    exam_view,
    exam_data_view,
    save_exam_view
)

app_name = 'exams'

# Exam app specific urls

urlpatterns = [
    path('exams', ExamListView.as_view(), name='list-view'),
    path('exams<pk>/', exam_view, name='exam_view'),
    path('exams<pk>/data/', exam_data_view, name='exam-data-view'),
    path('exams<pk>/save/', save_exam_view, name='save-view'),
]
