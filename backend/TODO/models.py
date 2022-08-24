from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

NULLABLE = {'blank': True, 'null': True}


class User(AbstractUser):
    username = models.CharField(max_length=64, unique=True, **NULLABLE)
    first_name = models.CharField(max_length=64, **NULLABLE)
    last_name = models.CharField(max_length=64, **NULLABLE)
    email = models.EmailField(verbose_name=_('email'), unique=True, **NULLABLE)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


"""Superuser - login: django
password: geekbrains"""

