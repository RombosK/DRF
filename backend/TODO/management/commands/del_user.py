from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from TODO.models import User


class Command(BaseCommand):
    help = 'Удаляет пользователей'

    def add_arguments(self, parser):
        parser.add_argument('user_id', nargs='+', type=int, help='ID пользователя')

    def handle(self, *args, **kwargs):
        users_ids = kwargs['user_id']

        for user_id in users_ids:
            try:
                user = User.objects.get(pk=user_id)
                user.delete()
                self.stdout.write(f'Пользователь {user.username} c ID {user_id} был удален!')
            except User.DoesNotExist:
                self.stdout.write(f'Пользователь с ID {user_id} не существует.')