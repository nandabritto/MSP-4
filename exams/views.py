from django.shortcuts import render
from .models import Exam
from django.views.generic import ListView

class ExamListView(ListView):
    model = Exam
    template_name = 'exam-list.html'

def exam_view(request, pk):
    exam = Exam.objects.get(pk=pk)
    return render(request, 'exam-display.html', {'obj': exam})

