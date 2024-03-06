from drf_yasg.utils import swagger_auto_schema

from apps.content.models import News, Article
from apps.content.serializer import GetNewsSerializer, PostNewsSerializer, GetArticleSerializer, PostArticleSerializer
from config.utils.permissions import LandingPage
from config.views import ModelViewSetPack


class NewsModelViewSet(ModelViewSetPack):
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


class ArticleModelViewSet(ModelViewSetPack):
    queryset = Article.objects.all()
    serializer_class = GetArticleSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostArticleSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostArticleSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return PostArticleSerializer(data=kwargs.get('data'), context={'request': self.request})
        elif self.action == 'update':
            return PostArticleSerializer(self.get_object(), data=kwargs.get('data'),
                                         context={'request': self.request})
        elif self.action == 'partial_update':
            return PostArticleSerializer(self.get_object(), data=kwargs.get('data'),
                                         context={'request': self.request}, partial=True)
        return super().get_serializer(*args, **kwargs)
