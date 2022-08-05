from django.core.management import BaseCommand
from TODO.models import User
from django.utils.crypto import get_random_string


class Command(BaseCommand):
    # help = u'Создание случайного пользователя'
    #
    # def add_arguments(self, parser):
    #     parser.add_argument('total', type=int, help=u'Количество создаваемых пользователей')
    #
    # def handle(self, *args, **kwargs): total = kwargs['total'] for i in range(total): User.objects.create_user(
    # username=get_random_string(), first_name=get_random_string(), last_name=get_random_string())
    def handle(self, *args, **options):
        users_list = []
        for i in range(1, 11):
            users_list.append(User(username=get_random_string(), first_name=get_random_string(), last_name=get_random_string(), email=''))

        User.objects.bulk_create(users_list)
