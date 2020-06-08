from django import forms
from .models import AccQuestions

class QuestionForm(forms.ModelForm):
    class Meta:
        model = AccQuestions
        fields = ('qdesc', 'opt1_desc',)