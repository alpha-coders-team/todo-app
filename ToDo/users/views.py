from django.contrib.auth import get_user_model
from django.contrib.auth.views import (
    LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView)
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import UserSignUp, SignInForm, CustomPasswordChangeForm

User = get_user_model()


class SignUp(CreateView):
    form_class = UserSignUp
    success_url = reverse_lazy('signin')
    template_name = 'users/signup.html'


class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'users/signin.html'
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


class CustomPasswordChangeView(PasswordChangeView):
    form_class = CustomPasswordChangeForm
    template_name = 'registration/password_change_form.html'
    success_url = reverse_lazy('custom_password_change_done_view')
    title = 'Password change'


class CustomPasswordChangeDoneView(PasswordChangeDoneView):
    template_name = 'registration/password_change_done.html'
    title = 'Password change successful'
