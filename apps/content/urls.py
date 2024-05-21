from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.content.views import NewsModelViewSet, ArticleModelViewSet, ArticleRetrieveAPIView, NewsRetrieveAPIView, \
    BannerModelViewSet, BannerRetrieveAPIView, BannerMainPageAPIView, NewsLandingListAPIView, \
    NewsLandingRetrieveAPIView, NewsPageListAPIView

router = DefaultRouter()
router.register(r'news', NewsModelViewSet, basename='news')
router.register(r'article', ArticleModelViewSet, basename='article')
router.register(r'banner', BannerModelViewSet, basename='banner')

app_name = 'content'
urlpatterns = [
    path('article/<int:pk>/all/', ArticleRetrieveAPIView.as_view(), name='article_retrieve_all'),
    path('news/<int:pk>/all/', NewsRetrieveAPIView.as_view(), name='news_retrieve_all'),
    path('news/landing-page/', NewsLandingListAPIView.as_view(), name='news_landing_page'),
    path('news/landing-page/<int:pk>/', NewsLandingRetrieveAPIView.as_view(), name='news_landing_page_retrieve'),
    path('news/page/', NewsPageListAPIView.as_view(), name='news_page'),
    path('banner/<int:pk>/all/', BannerRetrieveAPIView.as_view(), name='banner_retrieve_all'),
    path('banner/main-page/', BannerMainPageAPIView.as_view(), name='banner_main_page'),
]
urlpatterns += router.urls
