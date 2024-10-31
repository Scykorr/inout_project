from django.db import models


# Модель для дополнительных опций (add-ons)
class AddOn(models.Model):
    PLAN_CHOICES = [
        ('inout_base', 'INOUT Проект База'),
        ('inout_business', 'INOUT Проект Бизнес'),
        ('inout_platform', 'INOUT Проект Платформа'),
    ]
    session_id = models.CharField(max_length=36, unique=True)
    plan = models.CharField(max_length=20, choices=PLAN_CHOICES)
    user_amount = models.PositiveIntegerField(default=5)  # Значение по умолчанию 5
    help_desk = models.BooleanField(default=False)
    dms = models.BooleanField(default=False)
    risk_management = models.BooleanField(default=False)
    custom_branding = models.BooleanField(default=False)
    gitlab_integration = models.BooleanField(default=False)
    b2b_crm = models.BooleanField(default=False)
    knowledge_base = models.BooleanField(default=False)
    asset_management = models.BooleanField(default=False)
    private_cloud = models.BooleanField(default=False)
    billing = models.CharField(max_length=20, choices=[('in_month', 'Ежемесячно'), ('in_year', 'Ежегодно')])
    def __str__(self):
        return f"{self.plan} Add-On"


class UserProfile(models.Model):
    session_id = models.CharField(max_length=36, unique=True)
    email = models.EmailField()
    organization_name = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    country = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=100, blank=True)
    legal_address = models.TextField(blank=True)
    inn = models.CharField(max_length=12, blank=True)  # ИНН может быть 10 или 12 цифр
    domain_name = models.CharField(max_length=255, unique=True)  # Уникальный домен

    # Метод оплаты
    PAYMENT_METHOD_CHOICES = [
        ('credit_card', 'Банковская карта'),
        ('pay_check', 'Счет на оплату'),
    ]
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES, default='credit_card')

    def __str__(self):
        return f"{self.email} - {self.organization_name}"