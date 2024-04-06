from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.authentication.views import JWTObtainPairView, UserModelViewSet

router = DefaultRouter()
router.register(r'user-manipulation', UserModelViewSet, basename='user_manipulation')

app_name = 'authentication'
urlpatterns = [
    path('token/', JWTObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
urlpatterns += router.urls
