from django_filters.rest_framework import FilterSet, CharFilter
from .models import User


class UserFilter(FilterSet):
    username = CharFilter(lookup_expr='contains')

    class Meta:
        model = User
        fields = ['username']


