from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    AuthenticationForm,
    PasswordChangeForm
)
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserSignUp(UserCreationForm):
    username = forms.CharField(
        label='Имя пользователя',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label='e-mail',
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label='пароль',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label='подтверждение пароля',
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'password1', 'password2')


class SignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'autofocus': True,
                                      'class': 'form-control'}))
    password = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
    )


class ChangePasswordForm(PasswordChangeForm):
    pass
