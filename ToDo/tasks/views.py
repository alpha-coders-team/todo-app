from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.shortcuts import get_object_or_404, redirect, render

from .models import Task


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


@login_required
def view_task(request, username, post_id):
    task = get_object_or_404(Task, id=post_id, owner__username=username)
    if task.owner == request.user:
        return render(request, 'tasks/single_task.html', {'task': task})
    return redirect('index')
