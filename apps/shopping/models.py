from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _, get_language

from apps.authentication.models import User
from apps.catalog.models import Specification
from apps.tools.models import Region
from config.models import BaseModel


class Store(BaseModel):
    name = models.CharField(max_length=155)
    description = models.TextField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=30)
    work_schedule = models.CharField('work schedule', max_length=100, null=True, blank=True)
    map_link = models.TextField('map link', null=True, blank=True)

    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='stores')

    # photos ForeignKey inside File model

    class Meta:
        db_table = 'Store'


class OrderedProduct(BaseModel):
    quantity = models.SmallIntegerField(default=1)
    product = models.ForeignKey(Specification, on_delete=models.SET_NULL, null=True, blank=True,
                                related_name='ordered_products')

    class Meta:
        db_table = 'OrderedProduct'


class Application(BaseModel):
    DELIVERY = 'DELIVERY'
    PICKUP = 'PICKUP'
    DELIVERY_PICKUP_CHOICES = [
        (DELIVERY, _('Delivery')),
        (PICKUP, _('Pickup'))
    ]
    ACCEPTED = 'ACCEPTED'
    PROCESSED = 'PROCESSED'
    STATUS_CHOICES = [
        (ACCEPTED, _('Accepted')),
        (PROCESSED, _('Processed'))
    ]

    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACCEPTED)
    comment = models.TextField(null=True, blank=True)
    sender_language = models.CharField(max_length=2, choices=settings.LANGUAGES)
    delivery_pickup = models.CharField(max_length=8, choices=DELIVERY_PICKUP_CHOICES, default=DELIVERY)
    address = models.TextField(null=True, blank=True)
    # map_link = models.TextField('map link', null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    delivery_price = models.FloatField(null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    ordered_product = models.ManyToManyField(OrderedProduct, related_name='applications')

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        if not self.id:
            try:
                self.sender_language = get_language()
            except Exception as exc:
                self.sender_language = 'en'
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        db_table = 'Application'
