from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.shopping.views import StoreModelViewSet, GiveApplicationAPIView, ApplicationListAPIView, \
    AcceptApplicationAPIView, StoreListAPIView, StoreMultiLangListAPIView

router = DefaultRouter()
router.register(r'store', StoreModelViewSet, basename='store')
app_name = 'shopping'
urlpatterns = [
    path('store/<int:pk>/all/', StoreMultiLangListAPIView.as_view(), name='store_multi_lang_list'),
    path('store/page/', StoreListAPIView.as_view(), name='store_page'),
    path('apply/', GiveApplicationAPIView.as_view(), name='apply'),
    path('applications/', ApplicationListAPIView.as_view(), name='applications'),
    path('accept/application/<int:application_id>/', AcceptApplicationAPIView.as_view(), name='accept_application'),
]
urlpatterns += router.urls
