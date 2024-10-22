from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Добавьте дополнительные поля, если необходимо

    def __str__(self):
        return self.user.username
