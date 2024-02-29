from rest_framework import serializers


class FileSerializerCreate(serializers.BaseSerializer):
    file = serializers.FileField(required=True)
