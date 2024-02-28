from rest_framework import serializers

from apps.catalog.models import Size, Color, Category


class GetCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id',
                  'name']


class PostCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name_uz',
                  'name_ru',
                  'name_en', ]


class GetColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['id',
                  'name']


class PostColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name_uz',
                  'name_ru',
                  'name_en', ]


class GetSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['id',
                  'name']


class PostSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name_uz',
                  'name_ru',
                  'name_en', ]
