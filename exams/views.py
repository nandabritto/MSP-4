from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Question, Answer, Result, Exam
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Displays all currently available exams

class ExamListView(ListView):
    paginate_by = 6
    model = Exam 
    template_name = 'exam-list.html'

# displays the individual exam page to the user
def exam_view(request, pk):
    exam = Exam.objects.get(pk=pk)
    return render(request, 'exam-display.html', {'obj': exam})

# shows each question that is available for that particular exam
def exam_data_view(request, pk):
    exam = Exam.objects.get(pk=pk)
    questions = []
    for q in exam.get_questions():
        answers = []
        for a in q.get_answers():
            answers.append(a.text)
        questions.append({str(q): answers})
    return JsonResponse({
        'data': questions,
        'time': exam.time,
    })

# displays the results
def save_exam_view(request, pk):
    # The following details the actual exam
    # Because of the use of randomisation in the models.py,
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            print('key: ', k)
            question = Question.objects.get(text=k)
            questions.append(question)

        user = request.user
        exam = Exam.objects.get(pk=pk)

    # The following will confirm the results    
        score = 0
        multiplier = 100 / exam.number_of_questions
        results = []
        correct_answer = None

        # compares the answer provided to the correct one
        for q in questions:
            a_selected = request.POST.get(str(q))
            
            # determining behaviour if answer provided
            if a_selected != "":
                question_answers = Answer.objects.filter(question=q)
                for a in question_answers:
                    # if answer matches correct, add to score
                    if a_selected == a.text:
                        if a.correct:
                            score += 1
                            correct_answer = a.text
                    # if not correct, obtain correct to display
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {'correct_answer': correct_answer, 'answered': a_selected}})
            # Response if no answer received from user
            else:
                results.append({str(q): 'not answered'})
            
        score_ = score * multiplier
        Result.objects.create(exam=exam, user=user, score=score_)

        # Pass exam logic
        if score_ >= exam.required_score_to_pass:
            return JsonResponse({'passed': True, 'score': score_, 'results': results})
        else:
            return JsonResponse({'passed': False, 'score': score_, 'results': results})