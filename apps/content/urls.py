from rest_framework.routers import DefaultRouter

from apps.content.views import NewsModelViewSet, ArticleModelViewSet

router = DefaultRouter()
router.register(r'news', NewsModelViewSet, basename='news')
router.register(r'article', ArticleModelViewSet, basename='article')

app_name = 'content'
urlpatterns = [
    # path()
]
urlpatterns += router.urls
