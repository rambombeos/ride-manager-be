from django.core.management.base import BaseCommand
from django.utils.crypto import get_random_string
from identity.models import User
import random

class Command(BaseCommand):
    help = 'Creates sample users'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of users to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        for i in range(total):
            role = random.choice(['driver', 'rider'])
            first_name = f'User{i}'
            last_name = f'Last{i}'
            email = f'{first_name}@example.com'
            phone_number = f'+1{random.randint(1000000000, 9999999999)}'

            try:
                user = User.objects.create(
                    role=role,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone_number=phone_number
                )
                self.stdout.write(self.style.SUCCESS(f'Created user: {first_name} ({role})'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'Failed to create user: {first_name}. Error: {str(e)}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} sample users'))
