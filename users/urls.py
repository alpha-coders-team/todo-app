from django.urls import path
from . import views


urlpatterns = [
    path('delete-user/', views.UserDelete.as_view(), name='user_delete'),
    path('logout/', views.LogoutView.as_view(), name='customlogout'),
    path('signin/', views.SignInView.as_view(), name='signin'),
    path('signup/', views.SignUp.as_view(), name='signup'),

    path('password_change/',
         views.ChangePasswordView.as_view(),
         name='password_changing'),
    path('change_password/done/',
         views.ChangePasswordDoneView.as_view(),
         name='change_password_done'),

    # path('password_reset/', views.ResetPasswordView.as_view(), name='reset_password'),
    # path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]
