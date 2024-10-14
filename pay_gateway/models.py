from django.db import models

class ForDelete(models.Model):
    name = models.CharField(max_length=120)

# Модель для плана
class Plan(models.Model):
    name = models.CharField(max_length=100)  # Имя плана
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена

    def __str__(self):
        return self.name


# Модель для дополнительных опций (add-ons)
class AddOn(models.Model):
    name = models.CharField(max_length=100)  # Название опции
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена

    def __str__(self):
        return self.name


# Модель для пользователей
class User(models.Model):
    name = models.CharField(max_length=100)  # Имя пользователя
    email = models.EmailField()  # Почта
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)  # План, который выбрал пользователь

    def __str__(self):
        return self.name


# Модель для платежей
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Кто оплатил
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)  # Какой план оплачен
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма платежа
    status = models.CharField(max_length=20,
                              choices=[('accepted', 'Accepted'), ('unsuccessful', 'Unsuccessful')])  # Статус платежа

    def __str__(self):
        return f'Payment by {self.user.name} for {self.plan.name} - {self.status}'
