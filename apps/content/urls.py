from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.content.views import NewsModelViewSet, ArticleModelViewSet, ArticleRetrieveAPIView, NewsRetrieveAPIView

router = DefaultRouter()
router.register(r'news', NewsModelViewSet, basename='news')
router.register(r'article', ArticleModelViewSet, basename='article')

app_name = 'content'
urlpatterns = [
    path('article/<int:pk>/all/', ArticleRetrieveAPIView.as_view(), name='article_retrieve_all'),
    path('news/<int:pk>/all/', NewsRetrieveAPIView.as_view(), name='news_retrieve_all'),
]
urlpatterns += router.urls
