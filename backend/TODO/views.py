# from django.shortcuts import render
# from rest_framework.viewsets import ModelViewSet
# from django_filters import rest_framework as filters
from rest_framework.permissions import BasePermission, IsAuthenticated, DjangoModelPermissions
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import GenericViewSet
from .models import User
from .serializer import UserModelSerializer, UserModelSerializerV2
from .filters import UserFilter
from rest_framework.mixins import RetrieveModelMixin, ListModelMixin, UpdateModelMixin, CreateModelMixin, \
    DestroyModelMixin
from rest_framework.response import Response

# from rest_framework.authtoken.views import ObtainAuthToken
# from rest_framework.authtoken.models import Token
#
#
# class CustomAuthToken(ObtainAuthToken):
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.serializer_class(data=request.data,
#                                            context={'request': request})
#         serializer.is_valid(raise_exception=True)
#         user = serializer.validated_data['user']
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({
#             'token': token.key,
#             'user_id': user.pk,
#             'email': user.email
#         })


"""Представление, которое возвращает подсчет активных пользователей в JSON
"""


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
    # serializer_class = UserModelSerializer
    filter_set_class = UserFilter
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == '2.0':
            return UserModelSerializerV2
        return UserModelSerializer

    # permission_classes = [DjangoModelPermissions]

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()
