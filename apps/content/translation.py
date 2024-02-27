from modeltranslation.translator import TranslationOptions, translator

from .models import News


class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description',)


translator.register(News, NewsTranslationOptions)
