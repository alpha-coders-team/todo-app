from django.urls import path
from . import views


urlpatterns = [
    path('delete-user/', views.UserDelete.as_view(), name='user_delete'),
    path('logout/', views.LogoutView.as_view(), name='customlogout'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signup/', views.SignUp.as_view(), name='signup')
]
