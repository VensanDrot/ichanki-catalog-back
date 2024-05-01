from rest_framework.generics import ListAPIView

from apps.tools.models import ActionLog
from apps.tools.serializer import ActionLogListSerializer


class ActionLogListAPIView(ListAPIView):
    queryset = ActionLog.objects.order_by('-id').exclude(action__isnull=True)
    serializer_class = ActionLogListSerializer
