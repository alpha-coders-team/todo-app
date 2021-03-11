from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='index'),
    path('add-task/', login_required(views.CreateTask.as_view()), name='add-task'),
]