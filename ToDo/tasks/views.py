from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    login_url = '/auth/login/'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class CreateTask(CreateView):
    model = Task
    template_name = 'tasks/add-task.html'
    success_url = reverse_lazy('index')
    fields = ('title',)

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
