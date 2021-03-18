from django import forms

from .models import Category, Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'deadline', 'priority', 'category']

    new_category = forms.CharField(
        max_length=30, required=False, label="New Category Name"
    )

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['category'].required = False
        self.fields['category'].queryset = Category.objects.filter(
            owner=self.user)

    def clean(self):
        category = self.cleaned_data.get('category')
        new_category = self.cleaned_data.get('new_category')
        if not category:
            category, created = Category.objects.get_or_create(
                title=new_category, owner=self.user)
            self.cleaned_data['category'] = category

        return super(TaskForm, self).clean()
