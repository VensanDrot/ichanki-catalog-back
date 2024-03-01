from rest_framework import serializers

from apps.catalog.models import Size, Color, Category, Catalog, Specification


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


class GetCatalogSerializer(serializers.ModelSerializer):
    file = serializers.CharField(source='file.path')

    class Meta:
        model = Catalog
        fields = ['id',
                  'name',
                  'description',
                  'file',
                  'category', ]


class PostCatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['name_uz',
                  'name_ru',
                  'name_en',
                  'description_uz',
                  'description_ru',
                  'description_en',
                  'file',
                  'category', ]


class GetSpecificationSerializer(serializers.ModelSerializer):
    miniature = serializers.CharField(source='miniature.path')
    photo = serializers.CharField(source='photo.path')
    catalog = serializers.CharField(source='catalog.name')
    size = serializers.CharField(source='size.name')
    color = serializers.CharField(source='color.name')

    class Meta:
        model = Specification
        fields = ['is_active',
                  'vendor_code',
                  'price',
                  'discount',
                  'miniature',
                  'photo',
                  'catalog',
                  'size',
                  'color', ]


class PostSpecificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specification
        fields = ['is_active',
                  'vendor_code',
                  'price',
                  'discount',
                  'miniature',
                  'photo',
                  'catalog',
                  'size',
                  'color', ]