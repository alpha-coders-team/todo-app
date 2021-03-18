from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView

from .models import Task
from .forms import TaskForm


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    login_url = '/auth/login/'

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/add-task.html'
    login_url = '/auth/login/'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super(CreateTask, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs


class TaskDetailView(LoginRequiredMixin, DetailView):
    model = Task
    slug_field = 'pk'

    def get_object(self):
        object = super(TaskDetailView, self).get_object()
        if not self.request.user == object.owner:
            raise Http404
        return object
