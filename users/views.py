from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import UserSignUp, SignInForm, ChangePasswordForm
from tasks.models import User


class SignUp(CreateView):
    form_class = UserSignUp
    success_url = reverse_lazy('signin')
    template_name = 'users/signup.html'


class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')


class LogoutView(LogoutView):
    success_url = reverse_lazy('index')


class UserDelete(DeleteView):
    model = User
    template_name = 'users/account_delete_confirm.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        obj = get_object_or_404(User, id=self.request.user.id)
        return obj


class ChangePasswordView(PasswordChangeView):
    form_class = ChangePasswordForm
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('change_password_done')
    title = 'Password change'


class ChangePasswordDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
    title = 'Password change successful'
