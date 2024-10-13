from django.shortcuts import render
from .models import Plan, AddOn, User, Payment

# Представление для выбора плана
from django.shortcuts import render


def plan_view(request):
    return render(request, 'pay_gateway/bottom_choose_plan.html')  # Рендерим шаблон choose_plan.html


def add_ons(request):
    return render(request, 'pay_gateway/add_ons.html')  # Рендерим шаблон add_ons.html


def add_users(request):
    return render(request, 'pay_gateway/add_user.html')  # Рендерим шаблон add_users.html


def payment(request):
    return render(request, 'pay_gateway/payment.html')  # Рендерим шаблон payment.html


def accept_payment(request):
    return render(request, 'pay_gateway/accept_payment.html')  # Рендерим шаблон accept_payment.html


def unsuccess_payment(request):
    return render(request, 'pay_gateway/unsuccess_paymant.html')  # Рендерим шаблон unsuccess_payment.html
