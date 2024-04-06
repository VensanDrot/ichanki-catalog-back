from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.openapi import Parameter, TYPE_STRING, IN_QUERY
from drf_yasg.utils import swagger_auto_schema
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.permissions import AllowAny

from apps.catalog.filters import ProductFilter
from apps.catalog.models import Category, Color, Size, Catalog, Specification
from apps.catalog.serializer import GetCategorySerializer, GetColorSerializer, GetSizeSerializer, \
    PostCategorySerializer, PostSizeSerializer, PostColorSerializer, GetCatalogSerializer, PostCatalogSerializer, \
    PostSpecificationSerializer, GetSpecificationSerializer, SearchProductSerializer, RetrieveCatalogSerializer
from config.utils.pagination import APIPagination
from config.utils.permissions import LandingPage
from config.views import ModelViewSetPack


class CategoryModelViewSet(ModelViewSetPack):
    queryset = Category.objects.all()
    serializer_class = GetCategorySerializer
    post_serializer_class = PostCategorySerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostCategorySerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostCategorySerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class ColorModelViewSet(ModelViewSetPack):
    queryset = Color.objects.all()
    serializer_class = GetColorSerializer
    post_serializer_class = PostColorSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostColorSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostColorSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class SizeModelViewSet(ModelViewSetPack):
    queryset = Size.objects.all()
    serializer_class = GetSizeSerializer
    post_serializer_class = PostSizeSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostSizeSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostSizeSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class CatalogModelViewSet(ModelViewSetPack):
    queryset = Catalog.objects.all()
    serializer_class = GetCatalogSerializer
    post_serializer_class = PostCatalogSerializer
    permission_classes = (LandingPage,)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'retrieve':
            return RetrieveCatalogSerializer(args[0])
        return super().get_serializer(*args, **kwargs)

    @swagger_auto_schema(request_body=PostCatalogSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostCatalogSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class SpecificationModelViewSet(ModelViewSetPack):
    queryset = Specification.objects.all()
    serializer_class = GetSpecificationSerializer
    post_serializer_class = PostSpecificationSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostSpecificationSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostSpecificationSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class SearchProductsAPIView(ListAPIView):
    queryset = Catalog.objects.distinct('id')
    serializer_class = SearchProductSerializer
    filterset_class = ProductFilter
    pagination_class = APIPagination
    permission_classes = [AllowAny, ]
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    search_fields = ['name', 'category__name', 'specs__vendor_code', 'specs__color__name', 'specs__size__list',
                     'specs__size__roll']

    @swagger_auto_schema(manual_parameters=[
        Parameter('category', IN_QUERY, description="Category filter", type=TYPE_STRING),
        Parameter('color', IN_QUERY, description="Color filter", type=TYPE_STRING),
        Parameter('size_roll', IN_QUERY, description="Size roll filter", type=TYPE_STRING),
        Parameter('size_list', IN_QUERY, description="Size list filter", type=TYPE_STRING),
    ])
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
