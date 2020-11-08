from django import forms
from .models import AccTestUploads


class TestUpload(forms.ModelForm):
    class Meta:
        model = AccTestUploads
        fields = ('description', 'file',)
