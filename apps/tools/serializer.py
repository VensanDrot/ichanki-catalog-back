from rest_framework import serializers

from apps.tools.models import ActionLog


class ActionLogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionLog
        fields = ['id',
                  'username',
                  'section',
                  'action',
                  'item',
                  'created_at', ]
