from rest_framework import serializers
from .models import Ride, RideEvent

class RideEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = RideEvent
        fields = ['id_ride_event', 'id_ride', 'description', 'created_at']

class RideSerializer(serializers.ModelSerializer):
    events = RideEventSerializer(many=True, read_only=True)

    class Meta:
        model = Ride
        fields = ['id_ride', 'status', 'id_rider', 'id_driver', 'pickup_latitude', 
                  'pickup_longitude', 'dropoff_latitude', 'dropoff_longitude', 
                  'pickup_time', 'dropoff_time', 'events']
