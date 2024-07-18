from django.db import models
from django.utils.translation import gettext_lazy as _

from config.models import BaseModel


class BaseModelName(BaseModel):
    name = models.CharField(_('name'), max_length=155)

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


LIST = 'LIST'
ROLL = 'ROLL'
SIZE_CHOICES = [
    (LIST, _('List')),
    (ROLL, _('Roll')),
]


class Size(BaseModelName):
    size_type = models.CharField(choices=SIZE_CHOICES, max_length=4)

    # list = models.CharField('list', max_length=155)
    # roll = models.CharField('roll', max_length=155)

    class Meta:
        db_table = 'Size'


class Catalog(BaseModel):
    name = models.CharField('name', max_length=155)
    description = models.TextField('description', null=True, blank=True)
    material = models.CharField('material', max_length=100, null=True, blank=True)
    shape = models.CharField('shape', max_length=55, null=True, blank=True)
    visits = models.PositiveIntegerField(null=True, blank=True, default=0)
    is_popular = models.BooleanField(default=False)
    is_newest = models.BooleanField(default=False)

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='category', related_name='catalogs')

    # objects = CatalogManager()

    class Meta:
        db_table = 'Catalog'

    def __str__(self):
        return self.name


class Specification(BaseModel):
    is_active = models.BooleanField('is active', default=True)
    vendor_code = models.CharField('vendor code', max_length=100)
    price = models.FloatField('price')
    discount = models.FloatField('discount', null=True, blank=True)

    files = models.ForeignKey('files.File', on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='specs', verbose_name='miniature')
    # photos ForeignKey inside File model
    # photo = models.ForeignKey(File, on_delete=models.SET_NULL, null=True, blank=True,
    #                           related_name='photo_specs', verbose_name='photo')
    catalog = models.ForeignKey(Catalog, on_delete=models.CASCADE, verbose_name='catalog', related_name='specs')
    color = models.ForeignKey(Color, on_delete=models.CASCADE, verbose_name='color', related_name='specs')
    size = models.ManyToManyField(Size, related_name='specs')

    class Meta:
        db_table = 'Specification'
