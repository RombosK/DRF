
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from rest_framework import permissions
from rest_framework.routers import DefaultRouter
from TASK.views import ProjectModelViewSet, TodoModelViewSet
from TODO.views import UserModelViewSet
# from TODO.views import CustomAuthToken
from rest_framework.authtoken import views
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from graphene_django.views import GraphQLView

from backend import settings

schema_view = get_schema_view(
    openapi.Info(
        title='TODO',
        description='Includes users list, projects & notes',
        default_version='1',
        contact=openapi.Contact(email='Test@gb.ru'),
        license=openapi.License(name='MIT License'),
    ),
    public=True,
)

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('todos', TodoModelViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('api-auth-token/', views.obtain_auth_token),

    # path('api-auth-token/', CustomAuthToken.as_view())
    # path('api/1/users/', include('TODO.urls', namespace='1')),
    # path('api/2/users/', include('TODO.urls', namespace='2')),

    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('graphql/', GraphQLView.as_view(graphiql=True)),
    path('', TemplateView.as_view(template_name='index.html')),
    path('users/', TemplateView.as_view(template_name='index.html')),
    path('projects/', TemplateView.as_view(template_name='index.html')),
    path('todos/', TemplateView.as_view(template_name='index.html')),
    path('create_project/', TemplateView.as_view(template_name='index.html')),
    path('login/', TemplateView.as_view(template_name='index.html')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

