from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.content.views import NewsModelViewSet

router = DefaultRouter()
router.register(r'news', NewsModelViewSet, basename='news')

app_name = 'content'
urlpatterns = [
    # path()
]
urlpatterns += router.urls
