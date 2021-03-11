from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView

from .models import Task


class TaskList(ListView):
    model = Task
    template_name = 'tasks/index.html'


class CreateTask(CreateView):
    model = Task
    template_name = 'tasks/add-task.html'
    success_url = reverse_lazy('index')
    fields = ('title',)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
