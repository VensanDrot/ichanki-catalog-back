from django.db import models

from apps.catalog.models import Specification, Catalog
from apps.content.models import News
from apps.shopping.models import Store
from config.models import BaseModel


class File(BaseModel):
    name = models.CharField(max_length=300, null=True)
    gen_name = models.CharField(max_length=100, null=True)
    size = models.FloatField(null=True)
    path = models.TextField(null=True)
    content_type = models.CharField(max_length=100, null=True)
    extension = models.CharField(max_length=30, null=True)

    catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, null=True, blank=True, related_name='files')
    # specification = models.ForeignKey(Specification, on_delete=models.SET_NULL, null=True, blank=True,
    #                                   related_name='files')
    news = models.ForeignKey(News, on_delete=models.SET_NULL, null=True, blank=True, related_name='files')
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True, related_name='files')

    class Meta:
        db_table = "File"
