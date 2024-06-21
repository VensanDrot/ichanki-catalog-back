from django.db.models import Sum, Value
from django.db.models.functions import Coalesce
from django.utils.timezone import localtime
from rest_framework import serializers

from apps.files.models import File
from apps.files.serializer import FileSerializer
from apps.shopping.models import Store, Application, OrderedProduct


class GetStoreSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)

    class Meta:
        model = Store
        fields = ['id',
                  'name',
                  'description',
                  'address',
                  'phone_number',
                  'work_schedule',
                  'map_link',
                  'region',
                  'files', ]


class SearchStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id',
                  'name',
                  'address', ]


class PostStoreSerializer(serializers.ModelSerializer):
    files = serializers.SlugRelatedField(slug_field='id', many=True, queryset=File.objects.all())

    class Meta:
        model = Store
        fields = ['id',
                  'name_uz',
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


class StoreMultiLangListSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, allow_null=True)

    class Meta:
        model = Store
        fields = ['id',
                  'name_uz',
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


class OrderedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedProduct
        fields = ['quantity',
                  'product', ]


class GiveApplicationSerializer(serializers.ModelSerializer):
    order = OrderedProductSerializer(many=True, allow_null=True, source='ordered_product')

    def create(self, validated_data):
        ordered_products = validated_data.pop('ordered_product', [])
        obj: Application = super().create(validated_data)
        for ordered_product in ordered_products:
            order = OrderedProduct.objects.create(**ordered_product)
            obj.ordered_product.add(order)
        return obj

    class Meta:
        model = Application
        fields = ['id',
                  'fullname',
                  'phone_number',
                  'delivery_pickup',
                  'delivery_price',
                  'region',
                  'address',
                  'comment',
                  'total_price',
                  'order',
                  'store', ]


class OrderedProductDataSerializer(serializers.ModelSerializer):
    photo = FileSerializer(source='product.files', allow_null=True)
    name = serializers.CharField(source='product.catalog.name', allow_null=True)
    vendor_code = serializers.CharField(source='product.vendor_code', allow_null=True)
    shape = serializers.CharField(source='product.catalog.shape', allow_null=True)
    price = serializers.FloatField(source='product.price', allow_null=True)
    discount = serializers.FloatField(source='product.discount', allow_null=True)
    category = serializers.CharField(source='product.catalog.category.name', allow_null=True)

    class Meta:
        model = OrderedProduct
        fields = ['quantity',
                  'photo',
                  'name',
                  'vendor_code',
                  'shape',
                  'price',
                  'discount',
                  'category', ]


class ApplicationListSerializer(serializers.ModelSerializer):
    sender_language = serializers.CharField(source='get_sender_language_display', allow_null=True)
    delivery_pickup = serializers.CharField(source='get_delivery_pickup_display', allow_null=True)
    status = serializers.CharField(source='get_status_display', allow_null=True)
    store = serializers.CharField(source='store.name', allow_null=True)
    created_at = serializers.SerializerMethodField(allow_null=True)
    ordered_product = OrderedProductDataSerializer(many=True, allow_null=True)
    total_quantity = serializers.SerializerMethodField(allow_null=True)

    @staticmethod
    def get_total_quantity(obj):
        total_quantity = obj.ordered_product.aggregate(
            total_quantity=Coalesce(Sum('quantity'), Value(0))
        )['total_quantity']
        return total_quantity

    @staticmethod
    def get_created_at(obj):
        return localtime(obj.created_at).strftime('%Y-%m-%d %H:%M')

    class Meta:
        model = Application
        fields = ['id',
                  'fullname',
                  'phone_number',
                  'sender_language',
                  'delivery_pickup',
                  'region',
                  'address',
                  'comment',
                  'total_price',
                  'delivery_price',
                  'store',
                  'status',
                  'created_at',
                  'total_quantity',
                  'ordered_product', ]
