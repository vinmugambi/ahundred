from django.contrib import admin

# Register your models here.

from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]

# customizing questions admin form
admin.site.register(Question, QuestionAdmin)
