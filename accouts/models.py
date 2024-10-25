from wagtail.admin.panels import FieldPanel
from wagtail.fields import RichTextField
from wagtail.models import Page
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, check_password


class Login(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def save(self, *args, **kwargs):
        # Храните пароль в зашифрованном виде
        if not self.pk:  # Если пользователь новый, храним зашифрованный пароль
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Проверка пароля
        return check_password(raw_password, self.password)

    def __str__(self):
        return self.email
