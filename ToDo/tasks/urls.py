from django.urls import path

from . import views

urlpatterns = [
    path('', views.TaskList.as_view(), name='index'),
    path('add-task/', views.CreateTask.as_view(),
         name='add-task'),
    path('<str:owner>/<int:pk>/update_task/', views.UpdateTask.as_view(),
         name='update-task'),
    path('<str:owner>/<int:pk>/delete_task/', views.DeleteTask.as_view(),
         name='delete-task'),
    path('<str:owner>/<int:pk>/', views.TaskDetailView.as_view(),
         name='view-task'),
    path('add-category/', views.CreateCategory.as_view(), name='add-category'),
    path('<str:owner>/<int:pk>/add_comment/',
         views.AddComment.as_view(), name='add_comment'),
]
