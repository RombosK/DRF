import graphene
from TASK.models import Project, Todo
from TODO.models import User
from graphene_django import DjangoObjectType


class UserObjectType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectObjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class TodoObjectType(DjangoObjectType):
    class Meta:
        model = Todo
        fields = '__all__'


class Query(graphene.ObjectType):
    all_users = graphene.List(UserObjectType)

    def resolve_all_users(self, info):
        return User.objects.all()

    all_projects = graphene.List(ProjectObjectType)

    def resolve_all_projects(self, info):
        return Project.objects.all()

    all_todos = graphene.List(TodoObjectType)

    def resolve_all_todos(self, info):
        return Todo.objects.all()

    get_todo_by_id = graphene.Field(TodoObjectType, pk=graphene.Int(required=True))

    def resolve_get_todo_by_id(self, info, pk):
        return Todo.objects.get(pk=pk)

    get_project_by_id = graphene.Field(ProjectObjectType, pk=graphene.Int(required=True))

    # def resolve_get_project_by_id(self, info, pk):
    #     return Project.objects.get(pk=pk)

    def resolve_project_by_id(self, info, pk=None):
        try:
            if pk:
                return Project.objects.get(pk=pk)
        except Exception:
            return None


schema = graphene.Schema(query=Query)
