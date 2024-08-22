# accounts/views.py


from django.shortcuts import get_object_or_404
from wagtail.models import Page
from django.http import Http404
from .models import LoginPage, PasswordResetPage


def login_page_view(request):
    # Получаем экземпляр страницы авторизации из базы данных
    page = get_object_or_404(LoginPage)
    return page.serve(request)


def password_reset_view(request):
    page = get_object_or_404(PasswordResetPage)
    return page.serve(request)