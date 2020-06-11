from django.contrib import admin

from .models import Choice, Question

class ChoiceInLine(admin.StackedInline):
  model = Choice
  extra = 3

class QuestionAdmin(admin.ModelAdmin):

  list_display = ('question_text', 'pub_date', 'was_published_recently')
  fieldsets = [
    (None,  {'fields': ['question_text']}),
    ('Date Information', {'fields': ['pub_date']}),
  ]
  inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)