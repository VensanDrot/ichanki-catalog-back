from django.db import models

from config.models import BaseModel


class BaseModelName(BaseModel):
    name = models.CharField('name', max_length=155)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class Category(BaseModelName):
    class Meta:
        db_table = 'Category'


class Color(BaseModelName):
    class Meta:
        db_table = 'Color'


class Size(BaseModel):
    list = models.CharField('name', max_length=155)
    roll = models.CharField('name', max_length=155)

    class Meta:
        db_table = 'Size'


class Catalog(BaseModel):
    name = models.CharField('name', max_length=155)
    description = models.TextField('description', null=True, blank=True)
    material = models.CharField('material', max_length=100, null=True, blank=True)
    shape = models.CharField('material', max_length=55, null=True, blank=True)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category', related_name='catalogs')

    class Meta:
        db_table = 'Catalog'


class Specification(BaseModel):
    is_active = models.BooleanField('is active', default=True)
    vendor_code = models.CharField('vendor code', max_length=100)
    price = models.FloatField('price')
    discount = models.FloatField('discount', null=True, blank=True)

    miniature = models.ForeignKey('files.File', on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='miniature_specs', verbose_name='miniature')
    # photos ForeignKey inside File model
    # photo = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True,
    #                           related_name='photo_specs', verbose_name='photo')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='catalog', related_name='specs')
    size = models.ForeignKey(Size, on_delete=models.CASCADE, verbose_name='size', related_name='specs')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='color', related_name='specs')

    class Meta:
        db_table = 'Specification'
