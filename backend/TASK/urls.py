from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import ProjectModelViewSet, TodoModelViewSet

app_name = 'TASK'

router = DefaultRouter()
router.register('projects', ProjectModelViewSet)
router.register('todos', TodoModelViewSet)


urlpatterns = [
    path('', include(router.urls)),
]