from django.db import models
from django.contrib.auth.models import User
import random

# Allowed choices for the difficulty field
DIF_CHOICES = (
    ('Childsplay', 'Childsplay'),
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
    ('OMG!!!', 'OMG!!!'),
)

# Database model for the Practise exams
class Exam(models.Model):
    name = models.CharField(max_length=50)
    topic = models.CharField(max_length=50)
    difficulty = models.CharField(max_length=10, choices=DIF_CHOICES)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Time-Limit in minutes")
    required_score_to_pass = models.IntegerField(help_text="Pass Mark as %")
 
    def __str__(self):
        return f"{self.name}-{self.topic}"

    # The following function will randomise the questions selected for each exam
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        verbose_name_plural = 'Exams'

# Database model for the exam questions
# Links back to the exam model
class Question(models.Model):
    test = models.CharField(max_length=400)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answers_set.all()

# Database model for the question answer
# Links back to the question model
class Answer(models.Model):
    text = models.CharField(max_length=300)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"

# Database model for the results
class Result(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)
