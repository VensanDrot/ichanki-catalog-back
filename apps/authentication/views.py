from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.authentication.models import User
from apps.authentication.serializer import JWTObtainPairSerializer, GetUserSerializer, PostUserSerializer
from config.utils.permissions import LandingPage
from config.views import ModelViewSetPack


class JWTObtainPairView(TokenObtainPairView):
    serializer_class = JWTObtainPairSerializer
    permission_classes = [AllowAny, ]


class UserModelViewSet(ModelViewSetPack):
    queryset = User.objects.all()
    serializer_class = GetUserSerializer
    post_serializer_class = PostUserSerializer
    permission_classes = (LandingPage,)

    @swagger_auto_schema(request_body=PostUserSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostUserSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
