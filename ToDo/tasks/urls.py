from django.contrib.auth.decorators import login_required
from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='index'),
    path('add-task/', views.CreateTask.as_view(),
         name='add-task'),
    path('<str:username>/<int:post_id>/', views.view_task, name='view-task'),
]
