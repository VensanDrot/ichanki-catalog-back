from modeltranslation.translator import TranslationOptions, translator

from .models import Category, Color, Size, Catalog


class NameTranslationOptions(TranslationOptions):
    fields = ('name',)


# class SizeTranslationOptions(TranslationOptions):
#     fields = ('list', 'roll',)


class CatalogTranslationOptions(TranslationOptions):
    fields = ('name', 'description', 'material', 'shape',)


translator.register(Category, NameTranslationOptions)
translator.register(Color, NameTranslationOptions)
# translator.register(Size, NameTranslationOptions)

translator.register(Catalog, CatalogTranslationOptions)
