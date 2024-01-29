import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

class Command(BaseCommand):
    help = 'Create a superuser if it does not already exist'

    def handle(self, *args, **options):
        email = 'admin@gmail.com'
        User = get_user_model()

        if not User.objects.filter(email=email).exists():
            User.objects.create_superuser(email, 'admin@123')
            self.stdout.write(self.style.SUCCESS(f'Superuser created with email: {email}'))
        else:
            self.stdout.write(self.style.SUCCESS('Superuser already exists'))
