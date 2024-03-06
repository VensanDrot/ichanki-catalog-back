from rest_framework.viewsets import ModelViewSet


class ModelViewSetPack(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
