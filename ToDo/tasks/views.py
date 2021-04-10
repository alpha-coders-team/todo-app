from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import Http404
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.views.generic.detail import DetailView

from .forms import TaskForm
from .models import Category, Task


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'tasks/index.html'
    paginate_by = 10

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user).order_by('-id')


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'tasks/add-task.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

    def get_form(self, *args, **kwargs):
        form = super(CreateTask, self).get_form(*args, **kwargs)
        form.fields['category'].queryset = Category.objects.filter(
            owner=self.request.user)
        return form


class CreateCategory(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['title', ]
    template_name = 'tasks/add-category.html'
    success_url = reverse_lazy('add-task')

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


class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    slug_field = 'pk'
    form_class = TaskForm
    template_name = 'tasks/add-task.html'
    success_url = reverse_lazy('index')

    def get_form(self, *args, **kwargs):
        form = super(UpdateTask, self).get_form(*args, **kwargs)
        form.fields['category'].queryset = Category.objects.filter(
            owner=self.request.user)
        return form


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    success_url = reverse_lazy('index')
