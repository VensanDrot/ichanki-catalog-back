from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.catalog.views import SizeModelViewSet, ColorModelViewSet, CategoryModelViewSet, CatalogModelViewSet, \
    SpecificationModelViewSet, SearchProductsAPIView

router = DefaultRouter()
router.register(r'category', CategoryModelViewSet, basename='category')
router.register(r'color', ColorModelViewSet, basename='color')
router.register(r'size', SizeModelViewSet, basename='size')
router.register(r'product', CatalogModelViewSet, basename='product')
router.register(r'specification', SpecificationModelViewSet, basename='specification')

app_name = 'catalog'
urlpatterns = [
    path('products-search/', SearchProductsAPIView.as_view(), name='products_search')
]
urlpatterns += router.urls
