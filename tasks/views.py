from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.detail import DetailView

from .models import Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    login_url = '/users/signin/'
    paginate_by = 2

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    template_name = 'tasks/add-task.html'
    login_url = '/users/signin/'
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
