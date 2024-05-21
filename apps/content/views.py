from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.permissions import AllowAny

from apps.content.models import News, Article, Banner
from apps.content.serializer import GetNewsSerializer, PostNewsSerializer, GetArticleSerializer, PostArticleSerializer, \
    RetrieveNewsSerializer, GetBannerSerializer, PostBannerSerializer, RetrieveBannerSerializer, \
    BannerMainPageSerializer, NewsMainPageSerializer
from config.utils.pagination import APIPagination
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


class NewsLandingListAPIView(ListAPIView):
    queryset = News.objects.filter(is_draft=False).order_by('-id')[:3]
    serializer_class = NewsMainPageSerializer
    permission_classes = [AllowAny, ]


class NewsPageListAPIView(ListAPIView):
    queryset = News.objects.filter(is_draft=False).order_by('-id')
    serializer_class = NewsMainPageSerializer
    permission_classes = [AllowAny, ]
    pagination_class = APIPagination


class NewsLandingRetrieveAPIView(RetrieveAPIView):
    queryset = News.objects.filter(is_draft=False)
    serializer_class = GetNewsSerializer
    permission_classes = [AllowAny, ]


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


class BannerModelViewSet(ModelViewSetPack):
    queryset = Banner.objects.all()
    serializer_class = GetBannerSerializer
    post_serializer_class = PostBannerSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostBannerSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostBannerSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class BannerRetrieveAPIView(RetrieveAPIView):
    queryset = Banner.objects.all()
    serializer_class = RetrieveBannerSerializer


class BannerMainPageAPIView(ListAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerMainPageSerializer
    permission_classes = [AllowAny, ]
