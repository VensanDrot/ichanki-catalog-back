from drf_yasg.utils import swagger_auto_schema
from rest_framework.viewsets import ModelViewSet

from apps.content.models import News
from apps.content.serializer import GetNewsSerializer, PostNewsSerializer
from config.utils.permissions import LandingPage


class NewsModelViewSet(ModelViewSet):
    queryset = News.objects.all()
    serializer_class = GetNewsSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostNewsSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostNewsSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return PostNewsSerializer(data=kwargs.get('data'), context={'request': self.request})
        elif self.action == 'update':
            return PostNewsSerializer(self.get_object(), data=kwargs.get('data'),
                                               context={'request': self.request})
        elif self.action == 'partial_update':
            return PostNewsSerializer(self.get_object(), data=kwargs.get('data'),
                                               context={'request': self.request}, partial=True)
        return super().get_serializer(*args, **kwargs)
