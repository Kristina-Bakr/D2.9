from django.forms import DateTimeInput
from .models import Post
from django_filters import FilterSet, DateTimeFilter


class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='dateCreation',
        lookup_expr='gt',
        label='Дата публикации',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )

    class Meta:
       model = Post
       fields = {
           'title': ['contains'],
       }

