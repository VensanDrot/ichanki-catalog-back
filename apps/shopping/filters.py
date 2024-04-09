from django_filters import FilterSet, ChoiceFilter, DateFilter

from apps.shopping.models import Application, DELIVERY_PICKUP_CHOICES


class ApplicationFilter(FilterSet):
    type = ChoiceFilter(field_name='delivery_pickup', lookup_expr='exact', choices=DELIVERY_PICKUP_CHOICES)

    class Meta:
        model = Application
        fields = ['type',
                  'status', ]
