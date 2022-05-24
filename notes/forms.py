from django import forms
from .models import Note
from django.core.exceptions import ValidationError

class NotesForms(forms.ModelForm):
   class Meta:
      model = Note
      fields = ('title', 'text')
      labels = {
         'text': 'Write your text here:',
         'title': 'Write a nice title here:'
      }
      