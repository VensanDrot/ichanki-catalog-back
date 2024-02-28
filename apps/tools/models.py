from django.db import models

from config.models import BaseModel


class Region(BaseModel):
    class Meta:
        db_table = 'Region'


class District(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts', verbose_name='region')

    class Meta:
        db_table = 'District'


class ActionLog(BaseModel):
    CREATE = 'CREATE'
    CONFIRM = 'CONFIRM'
    EDIT = 'EDIT'
    DELETE = 'DELETE'
    ACTION_CHOICES = [

    ]
    action = models.CharField(max_length=7, choices=ACTION_CHOICES, null=True, blank=True)
    username = models.CharField(max_length=50)
    section = models.CharField(max_length=255)
    item = models.CharField(max_length=255)

    class Meta:
        db_table = 'ActionLog'
