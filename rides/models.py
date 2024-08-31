from django.db import models
from identity.models import User

STATUS_CHOICES = [
    ('en-route', 'En Route'),
    ('pickup', 'Pickup'),
    ('dropoff', 'Dropoff'),
]

class Ride(models.Model):
    id_ride = models.AutoField(primary_key=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    id_rider = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_rider')
    id_driver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='rides_as_driver')
    pickup_latitude = models.FloatField()
    pickup_longitude = models.FloatField()
    dropoff_latitude = models.FloatField()
    dropoff_longitude = models.FloatField()
    pickup_time = models.DateTimeField()
    dropoff_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Ride {self.id_ride}: {self.status}"

    class Meta:
        db_table = 'ride'
        indexes = [
            models.Index(fields=['status']),
            models.Index(fields=['pickup_time']),
        ]

class RideEvent(models.Model):
    id_ride_event = models.AutoField(primary_key=True)
    id_ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='events')
    description = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Event {self.id_ride_event} for Ride {self.id_ride.id_ride}: {self.description}"

    class Meta:
        db_table = 'ride_event'
        indexes = [
            models.Index(fields=['created_at']),
        ]
