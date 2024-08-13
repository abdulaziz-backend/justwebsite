from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'points', 'button_link']
        widgets = {
            'button_link': forms.URLInput(attrs={'placeholder': 'Enter button URL'})
        }
