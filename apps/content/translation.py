from modeltranslation.translator import TranslationOptions, translator

from .models import News, Article


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content',)


translator.register(News, NewsTranslationOptions)
translator.register(Article, NewsTranslationOptions)
