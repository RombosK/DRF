from django.core.management import BaseCommand
from TODO.models import User
from django.utils.crypto import get_random_string
from randomuser import RandomUser
import random
import string

for i in range(1, 11):
    def random_char(char_num):
        email = ''.join(random.choice(string.ascii_letters) for _ in range(char_num))
        return email


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        users_list = RandomUser.generate_users(5)
        for i in range(1, 10):
            email_list = [random_char(5) + '@gb.ru']  # ['1@gb.ru', '2@gb.ru', '3@gb.ru']
            for el in email_list:
                el = el
                users_list.append(User.objects.create_user(username=get_random_string(), first_name=get_random_string(),
                                                           last_name=get_random_string(), email=el))
