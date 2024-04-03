from django.contrib import admin

from apps.content.models import News, Article

admin.site.register(News)
admin.site.register(Article)