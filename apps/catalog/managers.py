from modeltranslation.manager import MultilingualManager


class CatalogManager(MultilingualManager):
    def get_queryset(self):
        return super().get_queryset().filter(specs__isnull=False)
