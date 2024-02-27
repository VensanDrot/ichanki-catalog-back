from django.db import models

from apps.files.models import File
from apps.tools.models import Region
from config.models import BaseModel


class Store(BaseModel):
    name = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    work_schedule = models.CharField('work schedule', max_length=100, null=True, blank=True)
    map_link = models.TextField('map link', null=True, blank=True)

    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='stores')
    photo = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True, related_name='stores')

    class Meta:
        db_table = 'Store'


class Application(BaseModel):
    # TODO: end this model
    class Meta:
        db_table = 'Application'
