# myapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.overview, name='overview'),  # Главная страница или обзор
    path('product-details/', views.product_details, name='product-details'),  # Информация о продукте
    path('invoices/', views.invoices, name='invoices'),  # Счета и КП
    path('billing/', views.billing, name='billing'),  # Детали выставления счета
    path('users/', views.users, name='users'),  # Пользователи
    path('help/', views.help, name='help'),  # Центр поддержки
]
