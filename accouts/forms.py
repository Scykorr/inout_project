from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import gettext_lazy as _


class LoginForm(AuthenticationForm):
    username = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'email',
            'placeholder': 'Почта',
            'id': 'email'
        }),
        label="Почта"
    )

    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'password',
            'placeholder': 'Пароль',
            'id': 'password'
        }),
        label="Пароль"
    )


class PasswordResetForm(forms.Form):
    email = forms.EmailField(label='Почта')

