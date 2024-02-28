from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet

from apps.catalog.models import Category, Color, Size
from apps.catalog.serializer import GetCategorySerializer, GetColorSerializer, GetSizeSerializer, \
    PostCategorySerializer, PostSizeSerializer, PostColorSerializer
from config.utils.permissions import LandingPage


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = GetCategorySerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostCategorySerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostCategorySerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return PostCategorySerializer(data=kwargs.get('data'), context={'request': self.request})
        elif self.action == 'update':
            return PostCategorySerializer(self.get_object(), data=kwargs.get('data'),
                                          context={'request': self.request})
        elif self.action == 'partial_update':
            return PostCategorySerializer(self.get_object(), data=kwargs.get('data'),
                                          context={'request': self.request}, partial=True)
        return super().get_serializer(*args, **kwargs)


class ColorModelViewSet(ModelViewSet):
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


class SizeModelViewSet(ModelViewSet):
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
