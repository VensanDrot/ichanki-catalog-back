from django_filters import FilterSet, CharFilter

from apps.catalog.models import Catalog


class ProductFilter(FilterSet):
    size = CharFilter(field_name='specs__size', lookup_expr='exact')
    color = CharFilter(field_name='specs__color', lookup_expr='exact')

    class Meta:
        model = Catalog
        fields = ['category',
                  'color',
                  'size', ]
