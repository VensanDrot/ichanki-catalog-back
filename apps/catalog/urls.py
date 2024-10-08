from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.catalog.views import SizeModelViewSet, ColorModelViewSet, CategoryModelViewSet, CatalogModelViewSet, \
    SpecificationModelViewSet, SearchProductsAPIView, CategoryRetrieveAPIView, ColorRetrieveAPIView, \
    SizeRetrieveAPIView, CatalogRetrieveAPIView, SizeTypeSelectAPIView, LandingProductsAPIView, SameProductsAPIView, \
    ColorSelectorAPIView

router = DefaultRouter()
router.register(r'category', CategoryModelViewSet, basename='category')
router.register(r'color', ColorModelViewSet, basename='color')
router.register(r'size', SizeModelViewSet, basename='size')
router.register(r'product', CatalogModelViewSet, basename='product')
router.register(r'specification', SpecificationModelViewSet, basename='specification')

app_name = 'catalog'
urlpatterns = [
    path('products-search/', SearchProductsAPIView.as_view(), name='products_search'),
    path('products/landing-page/', LandingProductsAPIView.as_view(), name='products_landing_page'),
    path('products/same-products/<int:product_id>/', SameProductsAPIView.as_view(), name='same_products'),
    path('category/<int:pk>/all/', CategoryRetrieveAPIView.as_view(), name='category_retrieve_all'),
    path('color/<int:pk>/all/', ColorRetrieveAPIView.as_view(), name='color_retrieve_all'),
    path('color/selector/', ColorSelectorAPIView.as_view(), name='color_selector'),
    path('size/<int:pk>/all/', SizeRetrieveAPIView.as_view(), name='size_retrieve_all'),
    path('size-types/', SizeTypeSelectAPIView.as_view(), name='size_types'),
    path('product/<int:pk>/all/', CatalogRetrieveAPIView.as_view(), name='product_retrieve_all'),
]
urlpatterns += router.urls
