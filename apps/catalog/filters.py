from django_filters import FilterSet, CharFilter

from apps.catalog.models import Catalog


class ProductFilter(FilterSet):
    size_roll = CharFilter(field_name='specs__size__roll', lookup_expr='icontains')
    size_list = CharFilter(field_name='specs__size__list', lookup_expr='icontains')
    color = CharFilter(field_name='specs__color', lookup_expr='exact')

    def filter_queryset(self, queryset):
        return super().filter_queryset(queryset)

    class Meta:
        model = Catalog
        fields = ['category',
                  'color',
                  'size_roll',
                  'size_list', ]
