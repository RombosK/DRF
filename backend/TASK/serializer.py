from rest_framework.serializers import ModelSerializer, Serializer, CharField
from .models import Project, Todo
from TODO.serializer import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    managers = UserModelSerializer(many=True)

    class Meta:
        model = Project
        fields = '__all__'


class ToDoModelSerializer(ModelSerializer):
    note_project = ProjectModelSerializer(many=False)
    note_worker = UserModelSerializer(many=False)

    class Meta:
        model = Todo
        fields = '__all__'
