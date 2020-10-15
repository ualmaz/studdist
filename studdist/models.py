from datetime import date
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser


class User(models.Model):
    first_name = models.CharField(verbose_name="First name", max_length=255)
    last_name = models.CharField(verbose_name="Last name", max_length=255)
    country = models.CharField(verbose_name="Country name", max_length=255)
    city = models.CharField(verbose_name="City name", max_length=255)
    email = models.EmailField(verbose_name="Email", max_length=255)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)


    def __str__(self):
        return '{} {}' .format(self.first_name, self.last_name)

class Table(models.Model):
    name = models.CharField(verbose_name='name', max_length=255)

    def __str__(self):
        return self.name