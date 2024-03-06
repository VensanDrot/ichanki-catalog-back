from rest_framework import serializers

from apps.files.models import File
from apps.files.serializer import FileSerializer
from apps.shopping.models import Store


class GetStoreSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)

    class Meta:
        model = Store
        fields = ['name',
                  'description',
                  'address',
                  'phone_number',
                  'work_schedule',
                  'map_link',
                  'region',
                  'files', ]


class PostStoreSerializer(serializers.ModelSerializer):
    files = serializers.SlugRelatedField(slug_field='id', many=True, queryset=File.objects.all())

    class Meta:
        model = Store
        fields = ['name_uz',
                  'name_en',
                  'name_ru',
                  'description_uz',
                  'description_en',
                  'description_ru',
                  'address_uz',
                  'address_en',
                  'address_ru',
                  'phone_number',
                  'work_schedule',
                  'map_link',
                  'region',
                  'files', ]
