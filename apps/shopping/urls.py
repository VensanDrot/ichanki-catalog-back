from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.shopping.views import StoreModelViewSet, GiveApplicationAPIView, ApplicationListAPIView

router = DefaultRouter()
router.register(r'store', StoreModelViewSet, basename='store')
app_name = 'shopping'
urlpatterns = [
    path('apply/', GiveApplicationAPIView.as_view(), name='apply'),
    path('applications/', ApplicationListAPIView.as_view(), name='apply'),
]
urlpatterns += router.urls
