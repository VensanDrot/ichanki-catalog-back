from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.catalog.views import SizeModelViewSet, ColorModelViewSet, CategoryModelViewSet, CatalogModelViewSet, \
    SpecificationModelViewSet, SearchProductsAPIView, CategoryRetrieveAPIView, ColorRetrieveAPIView, \
    SizeRetrieveAPIView, CatalogRetrieveAPIView

router = DefaultRouter()
router.register(r'category', CategoryModelViewSet, basename='category')
router.register(r'color', ColorModelViewSet, basename='color')
router.register(r'size', SizeModelViewSet, basename='size')
router.register(r'product', CatalogModelViewSet, basename='product')
router.register(r'specification', SpecificationModelViewSet, basename='specification')

app_name = 'catalog'
urlpatterns = [
    path('products-search/', SearchProductsAPIView.as_view(), name='products_search'),
    path('category/<int:pk>/all/', CategoryRetrieveAPIView.as_view(), name='category_retrieve_all'),
    path('color/<int:pk>/all/', ColorRetrieveAPIView.as_view(), name='color_retrieve_all'),
    path('size/<int:pk>/all/', SizeRetrieveAPIView.as_view(), name='size_retrieve_all'),
    path('product/<int:pk>/all/', CatalogRetrieveAPIView.as_view(), name='product_retrieve_all'),
]
urlpatterns += router.urls
