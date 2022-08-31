import random
from django.test import TestCase
from rest_framework import status
from TASK.models import Project
from TASK.views import ProjectModelViewSet
from TODO.models import User
from TODO.views import UserModelViewSet
from rest_framework.test import force_authenticate, APIRequestFactory, APIClient, APITestCase, APISimpleTestCase
from mixer.backend.django import mixer


class TestUserViewSet(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_superuser(username='django', password='geekbrains')
        self.project = mixer.blend(Project, project_name=mixer.sequence(lambda c: int(random.random() * 10)))
        # self.project = Project.objects.create(project_name='Object', description='Blabla', project_url='www.gb.ru')

    # APIRequestFactory

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/users/')
        view = UserModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_project_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        force_authenticate(request, user=self.user)
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_user_guest(self):
        factory = APIRequestFactory()
        request = factory.post('/api/users/', {'username': 'Test', 'email': 'user@gb.ru'}, format='json')
        force_authenticate(request, user=self.user)
        view = UserModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    # APIClient
    def test_get_user_detail(self):
        user = User.objects.create(username='Test', email='user@gb.ru')
        client = APIClient()
        response = client.get(f'/api/users/{user.id}/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_edit_guest(self):
        user = User.objects.create(username='Test', email='user@gb.ru')
        client = APIClient()
        response = client.put(f'/api/users/{user.id}/', {'email': 'user_2@gb.ru'})
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_get_list_2(self):
        self.client.force_login(user=self.user)
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.client.logout()
        response = self.client.get('/api/users/')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class TestProjectViewSet(APITestCase):  # APITestCase
    def test_get_list(self):
        response = self.client.get('/api/projects/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_edit_mixer(self):
        project = mixer.blend(Project)
        User.objects.create_superuser('admin', 'admin@gb.ru', 'geekbrains')
        self.client.login(username='admin', password='geekbrains')
        response = self.client.put(f'/api/projects/{project.id}/',
                                   {'project_name': 'test', 'project_url': 'test_url'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project = Project.objects.get(id=project.id)
        self.assertEqual(project.project_name, 'test')






