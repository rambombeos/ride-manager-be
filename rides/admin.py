from django.contrib import admin

# Register your models here.
from .models import Ride, RideEvent

class RideEventInline(admin.TabularInline):
    model = RideEvent
    extra = 1

@admin.register(Ride)
class RideAdmin(admin.ModelAdmin):
    list_display = ('id_ride', 'status', 'id_rider', 'id_driver', 'pickup_time', 'dropoff_time')
    list_filter = ('status',)
    search_fields = ('id_ride', 'id_rider', 'id_driver')
    inlines = [RideEventInline]

@admin.register(RideEvent)
class RideEventAdmin(admin.ModelAdmin):
    list_display = ('id_ride_event', 'id_ride', 'description', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('id_ride_event', 'id_ride', 'description')
