from django.shortcuts import render, redirect, get_object_or_404
from .models import Organization, Invoice, Contract, Productdetails, CompanyDetails, CommercialOffer, RegularPayment, \
    Invoice
from django.http import JsonResponse
from django.core.mail import send_mail
from django.utils.timezone import now


def product_details(request):
    product = Productdetails.objects.first()  # Предположим, что у нас один проект
    return render(request, 'client_zone/product-details.html',
                  {'product': product})  # Создайте шаблон product_details.html


def invoices(request):
    # Получаем данные из базы
    commercial_offers = CommercialOffer.objects.all()
    invoices = Invoice.objects.all()
    company_details = CompanyDetails.objects.first()  # Предположим, у нас одно поле с реквизитами
    regular_payments = RegularPayment.objects.all()

    # Передаем данные в шаблон через контекст
    context = {
        'commercial_offers': commercial_offers,
        'invoices': invoices,
        'company_details': company_details,
        'regular_payments': regular_payments,
    }
    return render(request, 'client_zone/invoices.html')  # Создайте шаблон invoices.html


def billing(request):
    company_details = CompanyDetails.objects.first()
    return render(request, 'client_zone/billing.html',
                  {'company_details': company_details})  # Создайте шаблон billing.html


def users(request):
    return render(request, 'client_zone/users.html')  # Создайте шаблон users.html


def help(request):
    return render(request, 'client_zone/help.html')  # Создайте шаблон help.html


def overview(request):
    organization = Organization.objects.first()
    invoices = Invoice.objects.all()[:3]
    contract = Contract.objects.first()
    context = {
        'organization': organization,
        'invoices': invoices,
        'contract': contract,
    }
    return render(request, 'client_zone/overview.html', context)


def support_page(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        question = request.POST.get('question')
        answer = request.POST.get('answer')
        file = request.FILES.get('file')

        try:
            # Отправка письма
            send_mail(
                subject=f'Новый тикет: {subject}',
                message=f'Что беспокоит: {question}\nЧто бы вы хотели: {answer}',
                from_email='x.xxxx46.XX@yandex.ru',
                recipient_list=['x.xxxx46.XX@yandex.ru']
            )
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)})

        # Пример данных для нового тикета
        ticket_data = {
            'subject': subject,
            'id': '12345',  # Можете добавить логику генерации ID тикета
            'priority': 'Средний',
            'status': 'Открыто',
            'date': now().strftime('%d.%m.%Y')
        }

        return JsonResponse({'success': True, 'ticket': ticket_data})

    # Если GET-запрос — рендерим страницу
    return render(request, 'help.html')