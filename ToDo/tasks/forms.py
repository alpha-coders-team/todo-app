from django import forms
from .models import Task, Category


class TaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(owner=user)

    class Meta:
        model = Task
        fields = ['title', 'deadline', 'priority', 'category']
        widgets = {
            'title': forms.TextInput(attrs={"class": "form-control"}),
            'deadline': forms.DateInput(attrs={"class": "form-control"}),
            'priority': forms.NumberInput(attrs={"class": "form-control"}),
            'category': forms.Select(attrs={"class": "form-control"}),
        }
