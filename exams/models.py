from django.db import models
from django.contrib.auth.models import User
import random
from providers.models import Providers

# Allowed difficulty selections
DIFF_CHOICES = (
    ('Childsplay', 'Childsplay'),
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
    ('OMG!!!', 'OMG!!!'),
)

# Allowed topic selections
TOPIC_CHOICES = (
    ('language', 'laguages'),
    ('computers', 'computers'),
    ('testing', 'testing'),
    ('mathematics', 'mathematics'),
    ('blockchain', 'blockchain'),
    ('scrum', 'scrum'),
    ('hacking', 'hacking'),
)

# DB Model for Exam details
class Exam(models.Model):
    name = models.CharField(max_length=50)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    description = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=10, choices=DIFF_CHOICES)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Time limit (in minutes)")
    required_score_to_pass = models.IntegerField(help_text="Pass Mark as %")


    def __str__(self):
        return f"{self.name}-{self.topic}"

    # Function enables randomised selection of questions
    # within the number_of_questions
    def get_questions(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Exams'


# Model for each question
class Question(models.Model):
    text = models.CharField(max_length=400)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

# Model for each answer pair to a question
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