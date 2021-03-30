from django.shortcuts import get_object_or_404
from django.views.generic import CreateView, DeleteView
from django.urls import reverse_lazy

from .forms import CreationForm
from tasks.models import User


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'users/signup.html'


class UserDelete(DeleteView):
    model = User
    template_name = 'registration/account_delete_confirm.html'
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        obj = get_object_or_404(User, id=self.request.user.id)
        return obj
