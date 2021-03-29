from django.urls import path
from . import views


urlpatterns = [
    path('delete-user/', views.UserDelete.as_view(), name='user_delete'),
    path('logout/', views.LogoutView.as_view(), name='customlogout'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    path('password_change/',
         views.CustomPasswordChangeView.as_view(),
         name='custom_password_change'),
    path('change_password/done/',
         views.CustomPasswordChangeDoneView.as_view(),
         name='custom_password_change_done_view'),
]
