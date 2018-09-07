from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class MyUser(AbstractUser):
    email = models.CharField(
        max_length=100,
        unique=True
    )
    icon = models.ImageField(
        upload_to="icon"
    )
    phone = models.CharField(
        max_length=13,
        null=True,
        blank=True
    )
    is_delate = models.BooleanField(
        default=False
    )
    # address = models.ForeignKey(
    #     # Address,
    #     null=True
    # )