from rest_framework.viewsets import ModelViewSet
from apps.tools.utils.logs import update_log
from config.utils.pagination import APIPagination


class ModelViewSetPack(ModelViewSet):
    http_method_names = ['get', 'post', 'patch', 'delete']
    serializer_action_prefix = 'Post'
    pagination_class = APIPagination
    post_serializer_class = None

    def get_serializer(self, *args, **kwargs):
        if self.action == 'create':
            serializer = self.post_serializer_class(data=kwargs.get('data'), context={'request': self.request})
        elif self.action == 'update':
            serializer = self.post_serializer_class(self.get_object(), data=kwargs.get('data'),
                                                    context={'request': self.request})
        elif self.action == 'partial_update':
            serializer = self.post_serializer_class(self.get_object(), data=kwargs.get('data'),
                                                    context={'request': self.request}, partial=True)
        else:
            serializer = super().get_serializer(*args, **kwargs)
        return serializer

    def perform_create(self, serializer):
        instance = serializer.save()
        update_log(self.request, instance)

    def perform_update(self, serializer):
        instance = serializer.save()
        update_log(self.request, instance)

    def perform_destroy(self, instance):
        update_log(self.request, instance)
        instance.delete()
