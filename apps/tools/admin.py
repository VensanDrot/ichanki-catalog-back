from django.contrib import admin

from apps.tools.models import Region, District, ActionLog

admin.site.register(Region)
admin.site.register(District)
admin.site.register(ActionLog)
