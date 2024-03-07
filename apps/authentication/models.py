from django.contrib.auth.models import AbstractUser
from django.db import models

from config.models import BaseModel


class User(AbstractUser, BaseModel):
    first_name = None
    last_name = None

    fullname = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'User'
