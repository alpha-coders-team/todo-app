from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', login_required(views.TaskList.as_view()), name='index'),
    path('add-task/', login_required(views.CreateTask.as_view()),
         name='add-task'),
]
