from django.db import models
from django.utils.translation import gettext_lazy as _

from config.models import BaseModel


class Region(BaseModel):
    name_uz = models.CharField(max_length=30, blank=True, null=True)
    name_ru = models.CharField(max_length=30, blank=True, null=True)
    name_en = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'Region'


class District(BaseModel):
    name_uz = models.CharField(max_length=100, blank=True, null=True)
    name_ru = models.CharField(max_length=100, blank=True, null=True)
    name_en = models.CharField(max_length=100, blank=True, null=True)

    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts', verbose_name='region')

    class Meta:
        db_table = 'District'


class ActionLog(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    CREATE = 'CREATE'
    CONFIRM = 'CONFIRM'
    EDIT = 'EDIT'
    DELETE = 'DELETE'
    ACTION_CHOICES = [
        (CREATE, _('Create')),
        (CONFIRM, _('Confirm')),
        (EDIT, _('Edit')),
        (DELETE, _('Delete'))
    ]
    uuid = models.UUIDField(null=True, blank=True)
    action = models.CharField(max_length=7, choices=ACTION_CHOICES, null=True, blank=True)
    username = models.CharField(max_length=50, null=True)
    section = models.CharField(max_length=255, null=True)
    item = models.CharField(max_length=255, null=True)

    class Meta:
        db_table = 'ActionLog'
