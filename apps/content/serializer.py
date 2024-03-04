from rest_framework import serializers

from apps.content.models import News, Article
from apps.files.models import File
from apps.files.serializer import FileSerializer


class GetNewsSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)

    class Meta:
        model = News
        fields = ['is_draft',
                  'title',
                  'description',
                  'content',
                  'files', ]


class PostNewsSerializer(serializers.ModelSerializer):
    files = serializers.SlugRelatedField(slug_field='id', many=True, queryset=File.objects.all())

    class Meta:
        model = News
        fields = ['is_draft',
                  'title_uz',
                  'title_en',
                  'title_ru',
                  'description_uz',
                  'description_en',
                  'description_ru',
                  'content_uz',
                  'content_en',
                  'content_ru',
                  'files', ]


class GetArticleSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)

    class Meta:
        model = Article
        fields = ['is_draft',
                  'title',
                  'description',
                  'content',
                  'files', ]


class PostArticleSerializer(serializers.ModelSerializer):
    files = serializers.SlugRelatedField(slug_field='id', many=True, queryset=File.objects.all())

    class Meta:
        model = Article
        fields = ['is_draft',
                  'title_uz',
                  'title_en',
                  'title_ru',
                  'description_uz',
                  'description_en',
                  'description_ru',
                  'content_uz',
                  'content_en',
                  'content_ru',
                  'files', ]
