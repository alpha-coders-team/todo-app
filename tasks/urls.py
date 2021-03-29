from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='index'),
    path('add-task/', views.CreateTask.as_view(),
         name='add-task'),
    path('<str:owner>/<int:pk>/', views.TaskDetailView.as_view(),
         name='view-task'),
]
