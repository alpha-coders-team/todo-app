from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404

from .models import Subtask, Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    login_url = '/auth/login/'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/add-task.html'
    login_url = '/auth/login/'
    success_url = reverse_lazy('index')
    fields = ('title', 'deadline', 'priority')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    slug_field = 'pk'

    def get_object(self):
        object = super(TaskDetailView, self).get_object()
        if not self.request.user == object.owner:
            raise Http404
        return object


class CreateSubtask(LoginRequiredMixin, CreateView):
    model = Subtask
    template_name = 'tasks/add-subtask.html'
    login_url = '/auth/login/'
    fields = ('title', 'deadline')

    def form_valid(self, form):
        task_id = self.kwargs['pk']
        task = get_object_or_404(Task, pk=task_id)
        if not self.request.user == task.owner:
            raise Http404
        form.instance.owner = self.request.user
        form.instance.task_id = task_id
        return super().form_valid(form)

    def get_success_url(self):
        data = {
            'owner': self.kwargs['owner'],
            'pk': self.kwargs['pk']
        }
        return reverse_lazy('view-task', kwargs=data)
