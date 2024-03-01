from modeltranslation.translator import TranslationOptions, translator

from .models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description', 'content',)


translator.register(News, NewsTranslationOptions)
