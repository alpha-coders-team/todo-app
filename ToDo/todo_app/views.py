from django.views.generic import ListView

from .models import Task


class IndexPage(ListView):
    template_name = 'todo_app/index.html'
    model = Task
    queryset = Task.objects.all()
    context_object_name = 'tasks'
    paginate_by = 10

