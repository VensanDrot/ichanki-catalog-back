from modeltranslation.translator import TranslationOptions, translator

from apps.tools.models import Region, District


class RegionTranslationOptions(TranslationOptions):
    fields = ('name',)


translator.register(Region, RegionTranslationOptions)
translator.register(District, RegionTranslationOptions)
