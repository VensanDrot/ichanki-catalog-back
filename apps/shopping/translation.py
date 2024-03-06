from modeltranslation.translator import TranslationOptions, translator

from apps.shopping.models import Store


class StoreTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'address',)


translator.register(Store, StoreTranslationOptions)
