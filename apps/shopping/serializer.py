from rest_framework import serializers

from apps.files.models import File
from apps.files.serializer import FileSerializer
from apps.shopping.models import Store, Application, OrderedProduct


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
        fields = ['fullname',
                  'phone_number',
                  'delivery_pickup',
                  'region',
                  'address',
                  'comment',
                  'total_price',
                  'delivery_price',
                  'order', ]


class ApplicationListSerializer(serializers.ModelSerializer):
    sender_language = serializers.CharField(source='get_sender_language_display')
    delivery_pickup = serializers.CharField(source='get_delivery_pickup_display')
    status = serializers.CharField(source='get_status_display')
    store = serializers.CharField(source='store.name')

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
                  'status', ]
