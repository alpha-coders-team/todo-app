from django import forms
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline', 'priority', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'deadline': forms.DateInput(attrs={"class": "form-control"}),
            'priority': forms.NumberInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }
