from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveAPIView

from apps.content.models import News, Article
from apps.content.serializer import GetNewsSerializer, PostNewsSerializer, GetArticleSerializer, PostArticleSerializer, \
    RetrieveNewsSerializer
from config.utils.permissions import LandingPage
from config.views import ModelViewSetPack


class NewsModelViewSet(ModelViewSetPack):
    queryset = News.objects.all()
    serializer_class = GetNewsSerializer
    post_serializer_class = PostNewsSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostNewsSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostNewsSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class NewsRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = RetrieveNewsSerializer


class ArticleModelViewSet(ModelViewSetPack):
    queryset = Article.objects.all()
    serializer_class = GetArticleSerializer
    post_serializer_class = PostArticleSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostArticleSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostArticleSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class ArticleRetrieveAPIView(RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = PostArticleSerializer
