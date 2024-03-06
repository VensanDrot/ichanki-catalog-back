from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.authentication.models import User
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


class Application(BaseModel):
    DELIVERY = 'DELIVERY'
    PICKUP = 'PICKUP'
    DELIVERY_PICKUP_CHOICES = [
        (DELIVERY, 'Delivery'),
        (PICKUP, 'Pickup')
    ]
    ACCEPTED = 'ACCEPTED'
    PROCESSED = 'PROCESSED'
    STATUS_CHOICES = [
        (ACCEPTED, 'Accepted'),
        (PROCESSED, 'Processed')
    ]

    fullname = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=30)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=ACCEPTED)
    sender_language = models.CharField(max_length=2, choices=settings.LANGUAGES, default='en')
    delivery_pickup = models.CharField(max_length=8, choices=DELIVERY_PICKUP_CHOICES, default=DELIVERY)
    address = models.TextField(null=True, blank=True)
    map_link = models.TextField('map link', null=True, blank=True)
    total_price = models.FloatField(null=True, blank=True)
    delivery_price = models.FloatField(null=True, blank=True)

    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    store = models.ForeignKey(Store, on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True, blank=True, related_name='applications')

    class Meta:
        db_table = 'Application'
