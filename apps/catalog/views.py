from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.openapi import Parameter, TYPE_STRING, IN_QUERY
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.catalog.filters import ProductFilter
from apps.catalog.models import Category, Color, Size, Catalog, Specification, SIZE_CHOICES
from apps.catalog.serializer import GetCategorySerializer, GetColorSerializer, GetSizeSerializer, \
    PostCategorySerializer, PostSizeSerializer, PostColorSerializer, GetCatalogSerializer, PostCatalogSerializer, \
    PostSpecificationSerializer, GetSpecificationSerializer, SearchProductSerializer, RetrieveCatalogSerializer, \
    MultiLanguageCatalogSerializer, MultiLanguageCategorySerializer
from config.utils.pagination import APIPagination
from config.utils.permissions import LandingPage
from config.views import ModelViewSetPack


class CategoryModelViewSet(ModelViewSetPack):
    queryset = Category.objects.all()
    serializer_class = GetCategorySerializer
    post_serializer_class = PostCategorySerializer
    permission_classes = (LandingPage,)
    filter_backends = [DjangoFilterBackend, SearchFilter, ]
    search_fields = ['name_en', 'name_uz', 'name_ru', ]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = self.perform_create(serializer)
            response_serializer = MultiLanguageCategorySerializer(instance=instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PostCategorySerializer)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        new_instance = self.get_object()
        response_serializer = MultiLanguageCategorySerializer(instance=new_instance)
        response = response_serializer.data
        return Response(response)

    @swagger_auto_schema(request_body=PostCategorySerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class CategoryRetrieveAPIView(RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = PostCategorySerializer


class ColorModelViewSet(ModelViewSetPack):
    queryset = Color.objects.all()
    serializer_class = GetColorSerializer
    post_serializer_class = PostColorSerializer
    permission_classes = (LandingPage,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = self.perform_create(serializer)
            response_serializer = PostColorSerializer(instance=instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PostColorSerializer)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        new_instance = self.get_object()
        response_serializer = PostColorSerializer(instance=new_instance)
        response = response_serializer.data
        return Response(response)

    @swagger_auto_schema(request_body=PostColorSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class ColorRetrieveAPIView(RetrieveAPIView):
    queryset = Color.objects.all()
    serializer_class = PostColorSerializer


class SizeModelViewSet(ModelViewSetPack):
    queryset = Size.objects.all()
    serializer_class = GetSizeSerializer
    post_serializer_class = PostSizeSerializer
    permission_classes = (LandingPage,)

    def get_queryset(self):
        queryset = super().get_queryset()
        size_type = self.request.query_params.get('size_type', None)
        if size_type:
            queryset = queryset.filter(size_type=size_type)
        return queryset

    @swagger_auto_schema(manual_parameters=[
        Parameter('size_type', IN_QUERY, description="Size type, ROLL or LIST", type=TYPE_STRING),
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = self.perform_create(serializer)
            response_serializer = PostSizeSerializer(instance=instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PostSizeSerializer)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        new_instance = self.get_object()
        response_serializer = PostSizeSerializer(instance=new_instance)
        response = response_serializer.data
        return Response(response)

    @swagger_auto_schema(request_body=PostSizeSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class SizeRetrieveAPIView(RetrieveAPIView):
    queryset = Size.objects.all()
    serializer_class = PostSizeSerializer


class SizeTypeSelectAPIView(APIView):
    def get(self, request, *args, **kwargs):
        size_types = SIZE_CHOICES
        response = []
        for size in size_types:
            response.append({
                'value': size[0],
                'label': size[1],
            })
        return Response(response)


class CatalogModelViewSet(ModelViewSetPack):
    queryset = Catalog.objects.all()
    serializer_class = GetCatalogSerializer
    post_serializer_class = PostCatalogSerializer
    permission_classes = (LandingPage,)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'retrieve':
            return RetrieveCatalogSerializer(args[0])
        return super().get_serializer(*args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = self.perform_create(serializer)
            response_serializer = RetrieveCatalogSerializer(instance=instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=PostCatalogSerializer)
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        new_instance = self.get_object()
        response_serializer = RetrieveCatalogSerializer(instance=new_instance)
        response = response_serializer.data
        return Response(response)

    @swagger_auto_schema(request_body=PostCatalogSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class CatalogRetrieveAPIView(RetrieveAPIView):
    queryset = Catalog.objects.all()
    serializer_class = MultiLanguageCatalogSerializer


class SpecificationModelViewSet(ModelViewSetPack):
    queryset = Specification.objects.all()
    serializer_class = GetSpecificationSerializer
    post_serializer_class = PostSpecificationSerializer
    permission_classes = (LandingPage,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = self.perform_create(serializer)
            response_serializer = PostSpecificationSerializer(instance=instance)
            return Response(response_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

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
