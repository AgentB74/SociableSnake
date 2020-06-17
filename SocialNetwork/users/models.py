from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager

from datetime import datetime
from datetime import timedelta
from django.core import validators

from django.conf import settings
# import jwt


# Create your models here.
class CustomUser(AbstractUser):
    telephone_numb = models.CharField(max_length=12, null=True, blank=True, unique=True)

    def __str__(self):
        """
        Возвращает строковое представление этого `User`.
        Эта строка используется, когда в консоли выводится `User`.
        """
        return self.username
