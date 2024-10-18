import django_filters
import computer_hardware_store.models
from django.db.models import Q

class Computer(django_filters.FilterSet):
    term = django_filters.CharFilter(method='filter_term', label='Поиск')
    available = django_filters.BooleanFilter(method='filter_available', label='В наличии')
    price_range = django_filters.RangeFilter(field_name='storage__price', label='Цена от и до')


    class Meta:
        model = computer_hardware_store.models.Computer
        fields = ['title', 'description', 'builder', 'price_range']

    def filter_available(self, queryset, name, value):
        criteria = Q()
        if value is None:
            return queryset
        if value:
            return queryset.filter(storage__amount__gt=0)
        criteria &= Q(storage__amount=0)|Q(storage__amount__isnull=True)
        return queryset.filter(criteria)

    def filter_term(self, queryset, name, value):
        criteria = Q()
        for term in value.split():
            criteria &= Q(title__icontains=term)|Q(description__icontains=term)|Q(builder__first_name__icontains=term)|Q(builder__surname__icontains=term)|Q(builder__patronymic__icontains=term)
        return  queryset.filter(criteria).distinct()