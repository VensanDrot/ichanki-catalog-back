from drf_yasg.utils import swagger_auto_schema

from apps.shopping.models import Store
from apps.shopping.serializer import GetStoreSerializer, PostStoreSerializer
from config.utils.permissions import LandingPage
from config.views import ModelViewSetPack


class StoreModelViewSet(ModelViewSetPack):
    queryset = Store.objects.all()
    serializer_class = GetStoreSerializer
    permission_classes = (LandingPage,)
    http_method_names = ['patch', 'post', 'get', 'delete']

    @swagger_auto_schema(request_body=PostStoreSerializer)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @swagger_auto_schema(request_body=PostStoreSerializer)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            return PostStoreSerializer(data=kwargs.get('data'), context={'request': self.request})
        elif self.action == 'update':
            return PostStoreSerializer(self.get_object(), data=kwargs.get('data'),
                                       context={'request': self.request})
        elif self.action == 'partial_update':
            return PostStoreSerializer(self.get_object(), data=kwargs.get('data'),
                                       context={'request': self.request}, partial=True)
        return super().get_serializer(*args, **kwargs)
