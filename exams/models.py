from django.db import models
from django.contrib.auth.models import User
import random
from providers.models import Providers


DIFF_CHOICES = (
    # Allowed difficulty selections
    ('Childsplay', 'Childsplay'),
    ('Easy', 'Easy'),
    ('Medium', 'Medium'),
    ('Hard', 'Hard'),
    ('OMG!!!', 'OMG!!!'),
)


TOPIC_CHOICES = (
    # Allowed topic selections
    ('language', 'laguages'),
    ('computers', 'computers'),
    ('testing', 'testing'),
    ('mathematics', 'mathematics'),
    ('blockchain', 'blockchain'),
    ('scrum', 'scrum'),
    ('hacking', 'hacking'),
)


class Exam(models.Model):
    # DB Model for Exam details
    name = models.CharField(max_length=50)
    topic = models.CharField(max_length=20, choices=TOPIC_CHOICES)
    description = models.CharField(max_length=200)
    difficulty = models.CharField(max_length=10, choices=DIFF_CHOICES)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="Time limit (in minutes)")
    required_score_to_pass = models.IntegerField(help_text="Pass Mark as %")

    def __str__(self):
        return f"{self.name}-{self.topic}"

    def get_questions(self):
        # Function enables randomised selection of questions
        # within the number_of_questions
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.number_of_questions]

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Exams'


class Question(models.Model):
    # Model for each question
    text = models.CharField(max_length=400)
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()


class Answer(models.Model):
    # Model for each answer pair to a question
    text = models.CharField(max_length=400)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"question: {self.question.text}, \
            answer: {self.text}, correct: {self.correct}"


class Result(models.Model):
    # Model for the results
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField()

    def __str__(self):
        return str(self.pk)
