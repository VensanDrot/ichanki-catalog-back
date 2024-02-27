from django.db import models

from config.models import BaseModel


class Region(BaseModel):
    class Meta:
        db_table = 'Region'


class District(BaseModel):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name='districts', verbose_name='region')

    class Meta:
        db_table = 'District'
