from drf_yasg.utils import swagger_auto_schema
from rest_framework.generics import CreateAPIView, ListAPIView

from apps.shopping.models import Store, Application
from apps.shopping.serializer import GetStoreSerializer, PostStoreSerializer, GiveApplicationSerializer, \
    ApplicationListSerializer
from config.utils.pagination import APIPagination
from config.utils.permissions import LandingPage
from config.views import ModelViewSetPack


class StoreModelViewSet(ModelViewSetPack):
    queryset = Store.objects.all()
    serializer_class = GetStoreSerializer
    post_serializer_class = PostStoreSerializer
    permission_classes = (LandingPage,)
    http_method_names = ['patch', 'post', 'get', 'delete']

    @swagger_auto_schema(request_body=PostStoreSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostStoreSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)


class GiveApplicationAPIView(CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = GiveApplicationSerializer


class ApplicationListAPIView(ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationListSerializer
    pagination_class = APIPagination
# TODO: end filters here
