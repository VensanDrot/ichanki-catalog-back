from drf_yasg.utils import swagger_auto_schema

from apps.catalog.models import Category, Color, Size, Catalog, Specification
from apps.catalog.serializer import GetCategorySerializer, GetColorSerializer, GetSizeSerializer, \
    PostCategorySerializer, PostSizeSerializer, PostColorSerializer, GetCatalogSerializer, PostCatalogSerializer, \
    PostSpecificationSerializer, GetSpecificationSerializer
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
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostColorSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostColorSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return PostColorSerializer(data=kwargs.get('data'), context={'request': self.request})
        elif self.action == 'update':
            return PostColorSerializer(self.get_object(), data=kwargs.get('data'),
                                       context={'request': self.request})
        elif self.action == 'partial_update':
            return PostColorSerializer(self.get_object(), data=kwargs.get('data'),
                                       context={'request': self.request}, partial=True)
        return super().get_serializer(*args, **kwargs)


class SizeModelViewSet(ModelViewSetPack):
    queryset = Size.objects.all()
    serializer_class = GetSizeSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostSizeSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostSizeSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return PostSizeSerializer(data=kwargs.get('data'), context={'request': self.request})
        elif self.action == 'update':
            return PostSizeSerializer(self.get_object(), data=kwargs.get('data'),
                                      context={'request': self.request})
        elif self.action == 'partial_update':
            return PostSizeSerializer(self.get_object(), data=kwargs.get('data'),
                                      context={'request': self.request}, partial=True)
        return super().get_serializer(*args, **kwargs)


class CatalogModelViewSet(ModelViewSetPack):
    queryset = Catalog.objects.all()
    serializer_class = GetCatalogSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostCatalogSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostCatalogSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return PostCatalogSerializer(data=kwargs.get('data'), context={'request': self.request})
        elif self.action == 'update':
            return PostCatalogSerializer(self.get_object(), data=kwargs.get('data'),
                                         context={'request': self.request})
        elif self.action == 'partial_update':
            return PostCatalogSerializer(self.get_object(), data=kwargs.get('data'),
                                         context={'request': self.request}, partial=True)
        return super().get_serializer(*args, **kwargs)


class SpecificationModelViewSet(ModelViewSetPack):
    queryset = Specification.objects.all()
    serializer_class = GetSpecificationSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostSpecificationSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostSpecificationSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return PostSpecificationSerializer(data=kwargs.get('data'), context={'request': self.request})
        elif self.action == 'update':
            return PostSpecificationSerializer(self.get_object(), data=kwargs.get('data'),
                                               context={'request': self.request})
        elif self.action == 'partial_update':
            return PostSpecificationSerializer(self.get_object(), data=kwargs.get('data'),
                                               context={'request': self.request}, partial=True)
        return super().get_serializer(*args, **kwargs)
