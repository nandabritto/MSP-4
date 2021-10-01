from django.shortcuts import render
from .models import Exam
from django.views.generic import ListView
from django.http import JsonResponse

class ExamListView(ListView):
    model = Exam
    template_name = 'exam-list.html'

def exam_view(request, pk):
    exam = Exam.objects.get(pk=pk)
    return render(request, 'exam-display.html', {'obj': exam})

def exam_data_view(request, pk):
    exam = Exam.objects.get(pk=pk)
    questions = []
    for q in exam.get_questions():
        answers = []
        for a in q.get_answer():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': exam.time,
    })

# Displays the results
def save_exam_view(request, ph):
    print(request.POST)
    return JsonResponse({'text': 'works'})
