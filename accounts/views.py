from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User


def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, 'Пользователь с таким email не найден')
            return render(request, 'your_app/login.html')

        user = authenticate(request, username=user.username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Замените 'dashboard' на нужный URL
        else:
            messages.error(request, 'Неверный пароль')

    return render(request, 'your_app/login.html')
