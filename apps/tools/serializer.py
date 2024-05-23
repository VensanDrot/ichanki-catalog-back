from rest_framework import serializers

from apps.tools.models import ActionLog
from apps.catalog.serializer import GetCategorySerializer, GetColorSerializer, GetSizeSerializer, GetCatalogSerializer
from apps.content.serializer import GetNewsSerializer, GetArticleSerializer
from apps.shopping.serializer import SearchStoreSerializer, ApplicationListSerializer


class ActionLogListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActionLog
        fields = ['id',
                  'username',
                  'section',
                  'action',
                  'item',
                  'created_at', ]


class AdminSiteGlobalSearchResponseSerializer(serializers.Serializer):
    categories = GetCategorySerializer(many=True, allow_null=True)
    colors = GetColorSerializer(many=True, allow_null=True)
    sizes = GetSizeSerializer(many=True, allow_null=True)
    products = GetCatalogSerializer(many=True, allow_null=True)
    news = GetNewsSerializer(many=True, allow_null=True)
    articles = GetArticleSerializer(many=True, allow_null=True)
    stores = SearchStoreSerializer(many=True, allow_null=True)
    applications = ApplicationListSerializer(many=True, allow_null=True)


class UserSiteGlobalSearchResponseSerializer(serializers.Serializer):
    catalogs = GetCatalogSerializer(many=True, allow_null=True)
    news = GetNewsSerializer(many=True, allow_null=True)
    articles = GetArticleSerializer(many=True, allow_null=True)
    stores = SearchStoreSerializer(many=True, allow_null=True)


class UserSiteGlobalSearchCountResponseSerializer(serializers.Serializer):
    catalogs = serializers.IntegerField(allow_null=True)
    news = serializers.IntegerField(allow_null=True)
    articles = serializers.IntegerField(allow_null=True)
