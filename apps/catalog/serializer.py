from rest_framework import serializers

from apps.catalog.models import Size, Color, Category, Catalog, Specification
from apps.files.models import File
from apps.files.serializer import FileSerializer


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
                  'list',
                  'roll', ]


class PostSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['list_uz',
                  'list_ru',
                  'list_en',
                  'roll_uz',
                  'roll_ru',
                  'roll_en', ]


class GetCatalogSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)
    category = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Catalog
        fields = ['id',
                  'name',
                  'description',
                  'files',
                  'shape',
                  'material',
                  'category', ]


class PostCatalogSerializer(serializers.ModelSerializer):
    files = serializers.SlugRelatedField(slug_field='id', many=True, queryset=File.objects.all())

    class Meta:
        model = Catalog
        fields = ['name_uz',
                  'name_ru',
                  'name_en',
                  'description_uz',
                  'description_ru',
                  'description_en',
                  'files',
                  'category', ]


class GetSpecificationSerializer(serializers.ModelSerializer):
    miniature = serializers.CharField(source='miniature.path', allow_null=True)
    catalog = serializers.CharField(source='catalog.name')
    roll = serializers.CharField(source='size.roll')
    list = serializers.CharField(source='size.list')
    color = serializers.CharField(source='color.name')
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)

    class Meta:
        model = Specification
        fields = ['is_active',
                  'vendor_code',
                  'price',
                  'discount',
                  'miniature',
                  'catalog',
                  'roll',
                  'list',
                  'color',
                  'files', ]


class PostSpecificationSerializer(serializers.ModelSerializer):
    files = serializers.SlugRelatedField(slug_field='id', many=True, queryset=File.objects.all())

    class Meta:
        model = Specification
        fields = ['is_active',
                  'vendor_code',
                  'price',
                  'discount',
                  'miniature',
                  'catalog',
                  'size',
                  'color',
                  'files', ]


class ProductSpecificationSerializer(serializers.ModelSerializer):
    miniature = FileSerializer(many=True, read_only=True, required=False, allow_null=True)
    color = serializers.CharField(source='color.name')
    size_list = serializers.CharField(source='size.list')
    size_roll = serializers.CharField(source='size.roll')

    class Meta:
        model = Specification
        fields = ['price',
                  'discount',
                  'color',
                  'size_list',
                  'size_roll',
                  'vendor_code',
                  'miniature', ]


class SearchProductSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)
    category = serializers.CharField(source='category.name')
    specs = ProductSpecificationSerializer(many=True, allow_null=True)

    class Meta:
        model = Catalog
        fields = ['id',
                  'name',
                  'description',
                  'files',
                  'category',
                  'specs', ]
