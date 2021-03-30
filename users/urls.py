from django.urls import path
from . import views


urlpatterns = [
    path('delete-user/', views.UserDelete.as_view(), name='user_delete'),
    path('signup/', views.SignUp.as_view(), name='signup')
]
