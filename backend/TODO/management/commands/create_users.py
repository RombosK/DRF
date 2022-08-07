from django.core.management import BaseCommand
from TODO.models import User
from django.utils.crypto import get_random_string
from randomuser import RandomUser


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users_list = RandomUser.generate_users(3)
        email_list = ['1@gb.ru', '2@gb.ru', '3@gb.ru']
        for x in email_list:
            x = x
            users_list.append(User.objects.create_user(username=get_random_string(), first_name=get_random_string(),
                                                       last_name=get_random_string(), email=x))
