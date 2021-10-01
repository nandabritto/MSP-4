from django.db import models
from django.contrib.auth.models import User
import random

# Allowed difficulty selections
DIFF_CHOICES = (
    ('Childsplay', 'Childsplay'),
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
    ('OMG!!!', 'OMG!!!'),
)

# add in choices for the topic (to align with the pictures.)

class Exam(models.Model):
    name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=10, choices=DIFF_CHOICES)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Time limit (in minutes)")
    required_score_to_pass = models.IntegerField(help_text="Pass Mark as %")


    def __str__(self):
        return f"{self.name}-{self.topic}"

    # Function enables randomised selection of questions from exam (with max)
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Exams'

# the following models are for the actual exam questions/answers

# Model for the question
class Question(models.Model):
    text = models.CharField(max_length=400)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

# Model for the answer
class Answer(models.Model):
    text = models.CharField(max_length=400)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

# Model for the results
class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)