from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    age = models.PositiveIntegerField(null=True)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
