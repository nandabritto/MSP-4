from django.contrib import admin
from .models import Exam, Question, Answer, Result

# The following allows for exams to be added via django admin portal

class AnswerInline(admin.TabularInline):
    model = Answer

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Result)
admin.site.register(Exam)
