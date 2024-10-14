from django.shortcuts import render


def overview(request):
    return render(request, 'client_zone/overview.html')  # Создайте шаблон overview.html


def product_details(request):
    return render(request, 'client_zone/product-details.html')  # Создайте шаблон product_details.html


def invoices(request):
    return render(request, 'client_zone/invoices.html')  # Создайте шаблон invoices.html


def billing(request):
    return render(request, 'client_zone/billing.html')  # Создайте шаблон billing.html


def users(request):
    return render(request, 'client_zone/users.html')  # Создайте шаблон users.html


def help(request):
    return render(request, 'client_zone/help.html')  # Создайте шаблон help.html
