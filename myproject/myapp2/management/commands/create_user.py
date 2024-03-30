from django.core.management.base import BaseCommand
import myproject
from myapps2.models import User


class Command(BaseCommand):
    help = "Create user"

    def handle(self, *args, **kwargs):
        user = User(name = 'Jorgh', email = 'jo@example.com', password = 'secret', age = 25)
        user.save()
        self.stdout.write(f'{user}')
