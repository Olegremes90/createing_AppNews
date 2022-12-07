from django_filters import FilterSet, DateTimeFilter, ModelChoiceFilter, CharFilter
from .models import Post, Category
from django.forms import DateTimeInput


# Создаем свой набор фильтров для модели Product.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.
class PostFilter(FilterSet):
    time_field = DateTimeFilter(
        field_name='time_creation',
        lookup_expr='gt',
        label='опубликовано позже:',
        widget = DateTimeInput(
            format = '%Y-%m-%dT%H:%M',
            attrs={'type':'datetime-local'},
        ),
    )
    type_category=ModelChoiceFilter(
        field_name='category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label = 'все категории',
    )
    title=CharFilter(
        field_name='title',
        label='название',
    )

