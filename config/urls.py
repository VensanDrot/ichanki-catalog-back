from django.contrib import admin
from django.urls import path, include

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="ICHANKI Swagger",
        default_version='v1',
        description="Swagger for ICHANKI project, token authorization: user __/auth/token/__ API then click authorize "
                    "button and type __Bearer {token}__.",
        terms_of_service="https://domen.uz/",
        contact=openapi.Contact(email="help@domen.uz"),
        license=openapi.License(name="ICHANKI License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny, ],
    # **SWAGGER_SETTINGS
)

urlpatterns = [
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

    path('control-panel/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('content/', include('apps.content.urls')),
    path('files/', include('apps.files.urls')),
    path('shopping/', include('apps.shopping.urls')),
    path('tools/', include('apps.tools.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
