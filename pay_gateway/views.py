from django.shortcuts import render, redirect
import logging
from pay_gateway.forms import AddOnForm, UserProfileForm
from django.contrib import messages
from django.utils.crypto import get_random_string

logger = logging.getLogger(__name__)


def choose_plan(request):
    return render(request, 'pay_gateway/botton_choose_plan.html')  # Рендерим шаблон add_ons.html


def start_session(request):
    plan = request.GET.get('plan')
    if plan:
        session_id = get_random_string(16)
        request.session['session_id'] = session_id
        request.session['selected_plan'] = plan
    return redirect('add_ons')

def add_on_view(request):
    if request.method == 'POST':
        logger.debug(request.POST)  # Логирование данных POST
        form = AddOnForm(request.POST)
        if form.is_valid():
            add_on = form.save()
            return redirect('add_users')
        else:
            logger.error("Form is not valid: %s", form.errors)  # Логирование ошибок формы
    else:
        form = AddOnForm()

    return render(request, 'pay_gateway/add_ons.html', {'form': form})


def user_profile_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваши данные успешно сохранены!')
            return redirect(
                'accept_payment')  # Замените 'success_url' на URL, куда вы хотите перенаправить пользователя
        else:
            logger.error("Form is not valid: %s", form.errors)  # Логирование ошибок формы
    else:
        form = UserProfileForm()

    return render(request, 'pay_gateway/add_user.html', {'form': form})


def payment(request):
    return render(request, 'pay_gateway/payment.html')  # Рендерим шаблон payment.html


def accept_payment(request):
    return render(request, 'pay_gateway/accept_payment.html')  # Рендерим шаблон accept_payment.html


def unsuccess_payment(request):
    return render(request, 'pay_gateway/unsuccess_paymant.html')  # Рендерим шаблон unsuccess_payment.html
