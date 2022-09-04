from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserModelViewSet

app_name = 'TODO'

router = DefaultRouter
router.register('users', UserModelViewSet.as_view())

urlpatterns = [
    path('', include(router.urls)),
]
