# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.mail import send_mail
from .forms import LoginForm, PasswordResetForm
from django.urls import reverse
from django.http import JsonResponse
from django.contrib.auth.views import PasswordResetView
from django.urls import reverse_lazy
from .forms import LoginForm
from .models import Login

from .forms import LoginForm


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)  # Используем нашу кастомную форму
        if form.is_valid():
            email = form.cleaned_data.get('username')  # 'username' теперь — это email
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('http://other-application.com/dashboard')  # Редирект после логина
            else:
                messages.error(request, 'Неверная почта или пароль.')
        else:
            messages.error(request, 'Неверная почта или пароль.')
    else:
        form = LoginForm()

    return render(request, 'accouts/login.html', {'form': form})


class CustomPasswordResetView(PasswordResetView):
    form_class = PasswordResetForm  # Используйте стандартную форму сброса пароля
    template_name = 'accouts/reset_password.html'  # Шаблон страницы сброса пароля
    email_template_name = 'accouts/password_reset_email.html'  # Шаблон email для сброса
    success_url = reverse_lazy('login')  # URL после успешной отправки

    def form_valid(self, form):
        # Отправляем сообщение об успешной отправке ссылки для восстановления пароля
        messages.success(self.request, 'Ссылка для восстановления пароля была отправлена на вашу почту.')
        return super().form_valid(form)
