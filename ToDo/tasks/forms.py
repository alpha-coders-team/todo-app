from django import forms
from .models import Task, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {'text': forms.TextInput(attrs={"class": "form-control"})}
