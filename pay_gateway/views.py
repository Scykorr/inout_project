import uuid
import logging
from django.conf import settings
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import AddOn, UserProfile
from .forms import AddOnForm, UserProfileForm
from django.db import IntegrityError
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


def choose_plan(request):
    request.session.flush()
    request.session['session_id'] = str(uuid.uuid4())
    logger.info("New session_id created: %s", request.session['session_id'])
    return render(request, 'pay_gateway/botton_choose_plan.html')


def add_on_view(request):
    session_id = request.session.get('session_id')
    if request.method == 'POST':
        form = AddOnForm(request.POST)
        if form.is_valid():
            add_on = form.save(commit=False)
            add_on.session_id = session_id
            add_on.save()
            logger.info("AddOn saved with session_id: %s", session_id)
            return redirect('add_users')
        else:
            logger.error("Form is not valid: %s", form.errors)
    else:
        form = AddOnForm()

    return render(request, 'pay_gateway/add_ons.html', {'form': form})


def user_profile_view(request):
    session_id = request.session.get('session_id')
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.session_id = session_id
            profile.save()
            messages.success(request, 'Ваши данные успешно сохранены!')
            logger.info("User Profile saved with session_id: %s", session_id)
            return redirect('payment')
        else:
            logger.error("Form is not valid: %s", form.errors)
    else:
        form = UserProfileForm()

    return render(request, 'pay_gateway/add_user.html', {'form': form})


def payment(request):
    return render(request, 'pay_gateway/payment.html')


def send_payment_email(email, session_id, payment_status):
    subject = f'Статус вашей оплаты: {payment_status}'
    message = (
        f'Здравствуйте!\n\n'
        f'Ваш статус оплаты: {payment_status}.\n'
        f'Сессия ID: {session_id}.\n\n'
        'Спасибо за использование нашего сервиса!'
    )
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])


def accept_payment(request):
    session_id = request.session.get('session_id')
    payment_successful = True  # Эта переменная должна быть результатом проверки успешности оплаты

    if payment_successful:
        temp_profiles = UserProfile.objects.filter(session_id=session_id)
        if temp_profiles.exists():
            addons = AddOn.objects.filter(session_id=session_id)
            for temp_profile in temp_profiles:
                domain_name = temp_profile.domain_name.strip()
                if UserProfile.objects.filter(domain_name=domain_name).exists():
                    logger.warning("Профиль с domain_name %s уже существует. Пропускаем создание.", domain_name)
                    messages.warning(request, f'Профиль с domain_name {domain_name} уже существует.')
                    continue

                try:
                    user = UserProfile.objects.create(
                        email=temp_profile.email,
                        organization_name=temp_profile.organization_name,
                        phone_number=temp_profile.phone_number,
                        country=temp_profile.country,
                        city=temp_profile.city,
                        legal_address=temp_profile.legal_address,
                        inn=temp_profile.inn,
                        domain_name=domain_name,
                        payment_method=temp_profile.payment_method,
                        session_id=session_id,
                        payment_status='successful',
                    )

                    for addon in addons:
                        user.addon_set.create(
                            plan=addon.plan,
                            user_amount=addon.user_amount,
                            help_desk=addon.help_desk,
                            dms=addon.dms,
                            risk_management=addon.risk_management,
                            custom_branding=addon.custom_branding,
                            gitlab_integration=addon.gitlab_integration,
                            b2b_crm=addon.b2b_crm,
                            knowledge_base=addon.knowledge_base,
                            asset_management=addon.asset_management,
                            private_cloud=addon.private_cloud,
                            billing=addon.billing,
                        )

                except IntegrityError as e:
                    logger.error("Ошибка при создании профиля: %s", e)
                    messages.error(request, 'Ошибка при создании профиля.')
                    return redirect('some_view')

            send_payment_email(temp_profile.email, session_id, 'успешная')
            temp_profiles.delete()
            addons.delete()

            messages.success(request, 'Оплата прошла успешно, данные сохранены!')
            logger.info("Payment successful, data saved for session_id: %s", session_id)
        else:
            messages.error(request, 'Профиль не найден.')
            logger.error("Profile not found for session_id: %s", session_id)
            return redirect('some_view')
    else:
        messages.error(request, 'Оплата не прошла, данные сохранены, но статус оплаты неуспешный.')
        logger.error("Payment failed, but data saved for session_id: %s", session_id)

    request.session.pop('session_id', None)
    return render(request, 'pay_gateway/accept_payment.html')


def unsuccess_payment(request):
    return render(request, 'pay_gateway/unsuccess_paymant.html')
