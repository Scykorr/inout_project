from django.db import models

# accounts/models.py

from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import redirect
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from django.urls import reverse_lazy
from wagtail.models import Page
from wagtail.admin.panels import FieldPanel


class LoginPage(Page):
    template = "account/login.html"

    # Поля для CMS
    subpage_types = []  # Запрещаем создание подстраниц

    def serve(self, request):
        # Обрабатываем POST-запрос
        if request.method == 'POST':
            form = AuthenticationForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                # После успешного входа перенаправляем на клиентскую зону или на главную страницу
                return redirect('/client-zone/' if self.client_zone_exists() else '/')
        else:
            form = AuthenticationForm()

        # Рендерим страницу с формой
        return super().serve(request, context_overrides={'form': form})

    content_panels = Page.content_panels + [
        # Добавим панели для ввода данных, если нужно (например, заголовок)
    ]

    # Проверка наличия клиентской зоны
    def client_zone_exists(self):
        # Логика для проверки существования страницы клиентской зоны
        # Можете заменить её на конкретную проверку
        return Page.objects.filter(title="Client Zone").exists()


class PasswordResetPage(Page):
    template = "account/password_reset.html"

    subpage_types = []  # Запрещаем создание подстраниц

    def serve(self, request):
        # Обрабатываем запрос на восстановление пароля
        if request.method == 'POST':
            form = PasswordResetForm(data=request.POST)
            if form.is_valid():
                form.save(
                    request=request,
                    use_https=request.is_secure(),
                    email_template_name='account/password_reset_email.html'
                )
                return redirect(self.url + 'done/')  # Перенаправление после успешного запроса
        else:
            form = PasswordResetForm()

        return super().serve(request, context_overrides={'form': form})

    content_panels = Page.content_panels + [
        # Добавим панели для ввода данных, если нужно (например, заголовок)
    ]
