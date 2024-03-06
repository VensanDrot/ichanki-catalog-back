from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.shopping.views import StoreModelViewSet

router = DefaultRouter()
router.register(r'store', StoreModelViewSet, basename='store')
app_name = 'shopping'
urlpatterns = [
    # path()
]
urlpatterns += router.urls
