from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import UserSignUp, SignInForm
from tasks.models import User


class SignUp(CreateView):
    form_class = UserSignUp
    success_url = reverse_lazy('signin')
    template_name = 'users/signup.html'


class UserDelete(DeleteView):
    model = User
    template_name = 'users/account_delete_confirm.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        obj = get_object_or_404(User, id=self.request.user.id)
        return obj


class SignInView(LoginView):
    form_class = SignInForm
    template_name = 'users/login.html'
    success_url = reverse_lazy('index')
