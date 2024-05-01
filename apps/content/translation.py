from modeltranslation.translator import TranslationOptions, translator

from .models import News, Article


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content',)


class ArticleTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(News, NewsTranslationOptions)
translator.register(Article, ArticleTranslationOptions)
