from rest_framework import serializers

from apps.content.models import News, Article, Banner, KnowledgeBase
from apps.files.models import File
from apps.files.serializer import FileSerializer


class GetArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id',
                  'name', ]


class PostArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['id',
                  'name_uz',
                  'name_ru',
                  'name_en', ]


class GetNewsSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)
    date = serializers.SerializerMethodField(allow_null=True)

    @staticmethod
    def get_date(obj):
        if obj.created_at:
            return obj.created_at.date()
        return None

    class Meta:
        model = News
        fields = ['id',
                  'title',
                  'description',
                  'content',
                  'files',
                  'is_draft',
                  'date', ]


class PostNewsSerializer(serializers.ModelSerializer):
    files = serializers.SlugRelatedField(slug_field='id', many=True, queryset=File.objects.all())

    class Meta:
        model = News
        fields = ['id',
                  'is_draft',
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


class GetKnowledgeBaseSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)
    date = serializers.SerializerMethodField(allow_null=True)
    article = serializers.CharField(source='article.name', allow_null=True)

    @staticmethod
    def get_date(obj):
        if obj.created_at:
            return obj.created_at.date()
        return None

    class Meta:
        model = KnowledgeBase
        fields = ['id',
                  'title',
                  'description',
                  'content',
                  'is_draft',
                  'files',
                  'article',
                  'date', ]


class KnowledgeBaseMainPageSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)
    artice = serializers.CharField(source='article.name', allow_null=True)

    class Meta:
        model = News
        fields = ['id',
                  'title',
                  'description',
                  'files',
                  'artice', ]


class PostKnowledgeBaseSerializer(serializers.ModelSerializer):
    files = serializers.SlugRelatedField(slug_field='id', many=True, queryset=File.objects.all())

    class Meta:
        model = KnowledgeBase
        fields = ['id',
                  'is_draft',
                  'title_uz',
                  'title_en',
                  'title_ru',
                  'description_uz',
                  'description_en',
                  'description_ru',
                  'content_uz',
                  'content_en',
                  'content_ru',
                  'article',
                  'files', ]


class RetrieveNewsSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)

    class Meta:
        model = News
        fields = ['id',
                  'is_draft',
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


class KnowledgeBaseNewsSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)
    article = PostArticleSerializer(allow_null=True)

    class Meta:
        model = KnowledgeBase
        fields = ['id',
                  'is_draft',
                  'title_uz',
                  'title_en',
                  'title_ru',
                  'description_uz',
                  'description_en',
                  'description_ru',
                  'content_uz',
                  'content_en',
                  'content_ru',
                  'article',
                  'files', ]


class NewsMainPageSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True, read_only=True, required=False, allow_null=True)
    date = serializers.SerializerMethodField(allow_null=True)

    @staticmethod
    def get_date(obj):
        if obj.created_at:
            return obj.created_at.date()
        return None

    class Meta:
        model = News
        fields = ['id',
                  'title',
                  'description',
                  'files',
                  'date', ]


class GetBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = ['id',
                  'name',
                  'description', ]


class PostBannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = [
            'id',
            'name_uz',
            'name_ru',
            'name_en',
            'description_uz',
            'description_ru',
            'description_en',
            'button_uz',
            'button_ru',
            'button_en',
            'button_link',
            'background_picture',
            'focus_picture',
        ]


class RetrieveBannerSerializer(serializers.ModelSerializer):
    background_picture = FileSerializer(allow_null=True)
    focus_picture = FileSerializer(allow_null=True)

    class Meta:
        model = Banner
        fields = ['id',
                  'name_uz',
                  'name_ru',
                  'name_en',
                  'description_uz',
                  'description_ru',
                  'description_en',
                  'button_uz',
                  'button_ru',
                  'button_en',
                  'button_link',
                  'background_picture',
                  'focus_picture', ]


class BannerMainPageSerializer(serializers.ModelSerializer):
    background_picture = FileSerializer(allow_null=True)
    focus_picture = FileSerializer(allow_null=True)

    class Meta:
        model = Banner
        fields = ['id',
                  'name',
                  'description',
                  'button',
                  'button_link',
                  'background_picture',
                  'focus_picture', ]
