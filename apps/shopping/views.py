from drf_yasg.utils import swagger_auto_schema

from apps.shopping.models import Store
from apps.shopping.serializer import GetStoreSerializer, PostStoreSerializer
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
