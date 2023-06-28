import django_filters
from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter, CharFilter
from .models import Post, Category
from django.forms import DateTimeInput


class PostFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Заголовок'
    )

    categoryType = django_filters.ModelChoiceFilter(
        field_name='categoryType',
        queryset=Category.objects.all(),
        label='Категории',
        empty_label='Выберите категорию ',
    )

    dataCreation_after = DateTimeFilter(
        field_name='dataCreation',
        lookup_expr='gt',
        label='Дата',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
