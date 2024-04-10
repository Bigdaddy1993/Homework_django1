from django.contrib.auth.models import AbstractUser
from django.db import models

from catalog.models import NULLABLE


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='почта')

    avatar = models.ImageField(upload_to='users/', verbose_name='изображение', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='телефон')
    country = models.CharField(max_length=30, verbose_name='страна')
    token = models.CharField(max_length=10, verbose_name='верификация', **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

