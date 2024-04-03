from django.contrib import admin

from apps.shopping.models import Store, OrderedProduct, Application

admin.site.register(Store)
admin.site.register(OrderedProduct)
admin.site.register(Application)
