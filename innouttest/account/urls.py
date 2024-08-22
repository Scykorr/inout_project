# accounts/urls.py

from django.urls import path, include
from wagtail import urls as wagtail_urls
from . import views


# Поскольку LoginPage наследуется от Wagtail Page, используем стандартный рендеринг через Wagtail
urlpatterns = [
    path('login/', views.login_page_view, name='login_page'),
    path('password_reset/', views.password_reset_view, name='password_reset_page'),
    path('', include(wagtail_urls)),  # Добавляем обработку всех остальных страниц через Wagtail
]
