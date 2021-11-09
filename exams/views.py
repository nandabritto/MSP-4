from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.http import JsonResponse
from .models import Question, Answer, Result, Exam
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from members import urls


class ExamListView(ListView):
    # Displays all currently available exams
    paginate_by = 6
    model = Exam
    template_name = 'exam-list.html'


@login_required()
# Ensures only available to logged in Users
def exam_view(request, pk):
    # displays the individual exam page to a logged in user
    exam = Exam.objects.get(pk=pk)
    return render(request, 'exam-display.html', {'obj': exam})


@login_required()
# Ensures only available to logged in Users
def exam_data_view(request, pk):
    # Shows each question that is available for that particular exam
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


@login_required()
# Ensures only available to logged in Users
def save_exam_view(request, pk):
    # The following details the actual exam
    # Question randomisation in the models.py,
    if request.is_ajax():
        questions = []
        data = request.POST
        data_ = dict(data.lists())
        data_.pop('csrfmiddlewaretoken')

        for k in data_.keys():
            question = Question.objects.get(text=k)
            questions.append(question)

        user = request.user
        exam = Exam.objects.get(pk=pk)

        # The following will confirm the overall results
        score = 0
        multiplier = 100 / exam.number_of_questions
        results = []
        correct_answer = None

        for q in questions:
            # obtains the users selected answer
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
                    # if not correct, obtain correct answer
                    else:
                        if a.correct:
                            correct_answer = a.text

                results.append({str(q): {
                    'correct_answer': correct_answer,
                    'answered': a_selected}})
            else:
                # Response if no answer received from user
                results.append({str(q): 'not answered'})

        score_ = score * multiplier
        Result.objects.create(exam=exam, user=user, score=score_)

        # Pass exam logic
        if score_ >= exam.required_score_to_pass:
            return JsonResponse({
                'passed': True,
                'score': score_,
                'results': results})
        else:
            return JsonResponse({
                'passed': False,
                'score': score_,
                'results': results})
