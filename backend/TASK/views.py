from rest_framework.pagination import PageNumberPagination
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Project, Todo
from .serializer import ProjectModelSerializer, ToDoModelSerializer
from .filters import ProjectFilter, TodoFilter
from rest_framework.pagination import LimitOffsetPagination

""" модель Project: доступны все варианты запросов; для постраничного вывода
установить размер страницы 10 записей; добавить фильтрацию по совпадению части
названия проекта;
 модель ToDo: доступны все варианты запросов; при удалении не удалять ToDo, а
выставлять признак, что оно закрыто; добавить фильтрацию по проекту; для
постраничного вывода установить размер страницы 20"""


# class ProjectOffsetPagination(LimitOffsetPagination):
#     default_limit = 10


# class TodoOffsetPagination(LimitOffsetPagination):
#     default_limit = 20


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()
    filter_set_class = ProjectFilter

    # pagination_class = ProjectOffsetPagination

    @action(detail=True, methods=['get'])
    def get_project_name(self, request, pk):
        project_name = get_object_or_404(Project, pk=pk)
        return Response({'project_name': str(project_name.project_name)})

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class TodoModelViewSet(ModelViewSet):
    serializer_class = ToDoModelSerializer
    queryset = Todo.objects.all()
    filter_set_class = TodoFilter

    # pagination_class = TodoOffsetPagination

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
