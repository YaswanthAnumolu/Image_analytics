# myapp/forms.py

from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField()

class QuestionForm(forms.Form):
    question = forms.CharField(max_length=255, label='Ask a question about the image:')
