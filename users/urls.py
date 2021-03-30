from django.urls import path
from . import views


urlpatterns = [
    path('delete-user/', views.UserDelete.as_view(), name='user_delete'),
    path('signin/', views.LoginView.as_view(), name='signin'),
    path('signup/', views.SignUp.as_view(), name='signup')
]
