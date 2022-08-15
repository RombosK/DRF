from django_filters.rest_framework import FilterSet, CharFilter, DateFromToRangeFilter, NumberFilter
from .models import Project, Todo


class ProjectFilter(FilterSet):
    project_name = CharFilter(lookup_expr='contains')

    class Meta:
        model = Project
        fields = ['project_name']


class TodoFilter(FilterSet):
    created = DateFromToRangeFilter()
    note_project = NumberFilter()

    class Meta:
        model = Todo
        fields = ['created', 'note_project']

