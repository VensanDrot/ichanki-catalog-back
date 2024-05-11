from modeltranslation.translator import TranslationOptions, translator

from .models import News, Article, Banner


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content',)


class ArticleTranslationOptions(TranslationOptions):
    fields = ('name',)


class BannerTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'button',)


translator.register(News, NewsTranslationOptions)
translator.register(Article, ArticleTranslationOptions)
translator.register(Banner, BannerTranslationOptions)
