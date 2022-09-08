from unicodedata import name
from django import forms
from .models import File


class UploadForm(forms.ModelForm):

    class Meta:
        model = File
        fields = ['filename', 'raw_data']
