from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'anons', 'full_text', 'date']

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name of the post'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Short description'
            }),
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Date of publishing'
            }),
            'full_text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Type text here...'
            }),
        }