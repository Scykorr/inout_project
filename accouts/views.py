from django.shortcuts import render

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        # Логика обработки формы для входа
        pass
    return render(request, 'accouts/login.html')

# Представление для страницы восстановления пароля
def reset_password_view(request):
    if request.method == 'POST':
        # Логика обработки формы для восстановления пароля
        pass
    return render(request, 'accouts/reset_password.html')