from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.utils import timezone
from wagtail.admin.panels import FieldPanel
from wagtail.models import Page


class Productdetails(models.Model):
    name = models.CharField(max_length=255)
    paid_until = models.DateField()
    solution_type = models.CharField(max_length=255)
    package = models.CharField(max_length=255)
    user_count = models.IntegerField(default=0)
    active_user_count = models.IntegerField(default=0)
    subscription_until = models.DateField()
    services_ordered = models.TextField(default="Услуги не были ещё заказаны")

    def __str__(self):
        return self.name


class CompanyDetails(models.Model):
    legal_address = models.CharField(max_length=255)
    inn = models.CharField(max_length=12)
    email = models.EmailField()
    actual_address = models.CharField(max_length=255, blank=True, null=True)
    payment_account = models.CharField(max_length=255, blank=True, null=True)
    bik = models.CharField(max_length=9, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return self.legal_address


class CommercialOffer(models.Model):
    created_date = models.DateField(verbose_name="Дата создания")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    subject = models.CharField(max_length=255, verbose_name="Предмет КП")

    panels = [
        FieldPanel('created_date'),
        FieldPanel('amount'),
        FieldPanel('subject'),
    ]

    def __str__(self):
        return self.subject


class CommercialOffersPage(Page):
    offers = models.ManyToManyField(CommercialOffer, verbose_name="Коммерческие предложения")

    content_panels = Page.content_panels + [
        FieldPanel('offers'),
    ]


class Invoice(models.Model):
    status = models.CharField(max_length=50, choices=[('paid', 'Оплачено'), ('unpaid', 'Не оплачено')],
                              verbose_name="Статус")
    number = models.CharField(max_length=100, verbose_name="Номер")
    created_date = models.DateField(verbose_name="Дата создания")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")
    subject = models.CharField(max_length=255, verbose_name="Предмет")

    panels = [
        FieldPanel('status'),
        FieldPanel('number'),
        FieldPanel('created_date'),
        FieldPanel('amount'),
        FieldPanel('subject'),
    ]

    def __str__(self):
        return self.number


class InvoicesPage(Page):
    invoices = models.ManyToManyField(Invoice, verbose_name="Счета на оплату")

    content_panels = Page.content_panels + [
        FieldPanel('invoices'),
    ]


class RegularPayment(models.Model):
    status = models.CharField(max_length=50, choices=[('active', 'Активно'), ('inactive', 'Неактивно')],
                              verbose_name="Статус")
    contact_id = models.CharField(max_length=100, verbose_name="Контактный ID")
    product = models.CharField(max_length=255, verbose_name="Продукт")
    payment_method = models.CharField(max_length=100, verbose_name="Способ оплаты")
    next_payment = models.DateField(verbose_name="Следующий платеж")
    period = models.CharField(max_length=50, verbose_name="Период")
    amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Сумма")

    panels = [
        FieldPanel('status'),
        FieldPanel('contact_id'),
        FieldPanel('product'),
        FieldPanel('payment_method'),
        FieldPanel('next_payment'),
        FieldPanel('period'),
        FieldPanel('amount'),
    ]

    def __str__(self):
        return self.product


class RegularPaymentsPage(Page):
    regular_payments = models.ManyToManyField(RegularPayment, verbose_name="Регулярные платежи")

    content_panels = Page.content_panels + [
        FieldPanel('regular_payments'),
    ]


class Organization(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    inn = models.CharField(max_length=12)
    email = models.EmailField()


class Contract(models.Model):
    project_name = models.CharField(max_length=255)
    user_count = models.IntegerField()
    paid_until = models.DateField()
