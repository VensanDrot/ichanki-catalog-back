from django.contrib import admin

from apps.catalog.models import Category, Color, Size, Catalog, Specification

admin.site.register(Category)
admin.site.register(Color)
admin.site.register(Size)
admin.site.register(Catalog)
admin.site.register(Specification)
