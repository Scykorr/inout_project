# myapp/models.py

from django.db import models


class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)  # Храните пароли безопасно (хэшируйте их в реальных приложениях)

    def __str__(self):
        return self.full_name


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


class Invoice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50)  # Например, "оплачено", "не оплачено"

    def __str__(self):
        return f'Invoice {self.id} for {self.user.full_name}'


class CommercialProposal(models.Model):
    invoice = models.ForeignKey(Invoice, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Proposal for {self.invoice.id}: {self.subject}'
