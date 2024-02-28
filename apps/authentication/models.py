from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    first_name = None
    last_name = None

    fullname = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'User'
