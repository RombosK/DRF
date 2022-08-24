# from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
# from django_filters import rest_framework as filters
from rest_framework.permissions import BasePermission, IsAuthenticated, DjangoModelPermissions
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializer import UserModelSerializer
from .filters import UserFilter
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, \
    DestroyModelMixin

"""Представление, которое возвращает подсчет активных пользователей в JSON
"""


# class CustomPermissions(BasePermission):
#
#     def has_permission(self, request, view):
#         return request.user and request.user.username == 'django(super)'


class UserCountView(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        user_count = User.objects.filter(active=True).count()
        content = {'user_count': user_count}
        return Response(content)


"""ViewSet модель User: есть возможность просмотра списка и каждого пользователя в
    отдельности, можно вносить изменения, нельзя удалять и создавать;
    """


class UserModelViewSet(RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, DestroyModelMixin,
                       GenericViewSet):
    serializer_class = UserModelSerializer
    queryset = User.objects.all()
    filter_set_class = UserFilter
    permission_classes = [DjangoModelPermissions]

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
