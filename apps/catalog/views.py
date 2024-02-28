from rest_framework.viewsets import ModelViewSet

from apps.catalog.models import Category, Color, Size
from apps.catalog.serializer import GetCategorySerializer, GetColorSerializer, GetSizeSerializer, \
    PostCategorySerializer, PostSizeSerializer, PostColorSerializer
from config.utils.permissions import LandingPage


class CategoryModelViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = PostCategorySerializer
    permission_classes = (LandingPage,)


class ColorModelViewSet(ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = PostColorSerializer
    permission_classes = (LandingPage,)


class SizeModelViewSet(ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = PostSizeSerializer
    permission_classes = (LandingPage,)

    def get_serializer(self, *args, **kwargs):
        return super().get_serializer(*args, **kwargs)


