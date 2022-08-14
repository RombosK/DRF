from rest_framework.viewsets import ModelViewSet
from .models import Project, Todo
from .serializer import ProjectModelSerializer, ToDoModelSerializer


class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()


class TodoModelViewSet(ModelViewSet):
    serializer_class = ToDoModelSerializer
    queryset = Todo.objects.all()






