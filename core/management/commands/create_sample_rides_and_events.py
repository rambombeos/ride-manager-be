from django.utils import timezone
from identity.models import User
from rides.models import Ride, RideEvent
import random
from datetime import timedelta
from core.management.commands import BaseCommand

class Command(BaseCommand):
    help = 'Creates sample rides and ride events'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of rides to be created')

    def handle(self, *args, **kwargs):
        total = kwargs['total']
        
        riders = User.objects.filter(role='rider')
        drivers = User.objects.filter(role='driver')

        if not riders or not drivers:
            self.stdout.write(self.style.ERROR('No riders or drivers found. Please create sample users first.'))
            return

        for i in range(total):
            rider = random.choice(riders)
            driver = random.choice(drivers)
            
            status = random.choice(['pending', 'in_progress', 'completed', 'cancelled'])
            pickup_time = timezone.now() + timedelta(hours=random.randint(1, 24))
            dropoff_time = pickup_time + timedelta(minutes=random.randint(15, 120))

            ride = Ride.objects.create(
                status=status,
                id_rider=rider,
                id_driver=driver,
                pickup_latitude=random.uniform(-90, 90),
                pickup_longitude=random.uniform(-180, 180),
                dropoff_latitude=random.uniform(-90, 90),
                dropoff_longitude=random.uniform(-180, 180),
                pickup_time=pickup_time,
                dropoff_time=dropoff_time
            )

            # Create 2-5 events for each ride
            for _ in range(random.randint(2, 5)):
                event_time = timezone.now() + timedelta(minutes=random.randint(0, 120))
                description = random.choice([
                    'Ride requested',
                    'Driver assigned',
                    'Driver arrived at pickup location',
                    'Ride started',
                    'Ride completed',
                    'Ride cancelled'
                ])

                RideEvent.objects.create(
                    id_ride=ride,
                    description=description,
                    created_at=event_time
                )

            self.stdout.write(self.style.SUCCESS(f'Created ride and events: Ride ID {ride.id_ride}'))

        self.stdout.write(self.style.SUCCESS(f'Successfully created {total} sample rides with events'))
