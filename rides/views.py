from rest_framework import viewsets, filters    
from rest_framework.pagination import PageNumberPagination
from django.db.models import F, ExpressionWrapper, FloatField
from django.db.models.functions import Power, Sqrt
from .models import Ride, RideEvent
from .serializers import RideSerializer, RideEventSerializer
from identity.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from core.response import BaseResponse
from rest_framework.permissions import IsAuthenticated

class RidePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all().select_related('id_rider', 'id_driver').prefetch_related('events')
    serializer_class = RideSerializer
    pagination_class = RidePagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['pickup_time', 'distance']

    def get_queryset(self):
        try:
            queryset = super().get_queryset()
            
            status = self.request.query_params.get('status')
            rider_email = self.request.query_params.get('rider_email')
            lat = self.request.query_params.get('latitude')
            lon = self.request.query_params.get('longitude')
            
            if status:
                queryset = queryset.filter(status=status)
            
            if rider_email:
                queryset = queryset.filter(id_rider__email=rider_email)
            
            if lat and lon:
                try:
                    lat = float(lat)
                    lon = float(lon)
                    
                    # Calculate distance using the Haversine formula
                    queryset = queryset.annotate(
                        distance=ExpressionWrapper(
                            6371 * Sqrt(
                                Power(F('pickup_latitude') - lat, 2) +
                                Power((F('pickup_longitude') - lon) * 0.7, 2)
                            ),
                            output_field=FloatField()
                        )
                    )
                except ValueError:
                    raise ValueError("Invalid latitude or longitude values")
                
            ordering = self.request.query_params.get('ordering')

            if ordering:
                queryset = queryset.order_by(ordering)
            
            return queryset
        except Exception as e:
            raise Exception(f"Error in get_queryset: {str(e)}")

    def list(self, request, *args, **kwargs):
        try:
            response = super().list(request, *args, **kwargs)
            
            # Add User details to the response
            for ride in response.data['results']:
                try:
                    ride_obj = Ride.objects.get(id_ride=ride['id_ride'])
                    ride['id_rider'] = UserSerializer(ride_obj.id_rider).data
                    ride['id_driver'] = UserSerializer(ride_obj.id_driver).data
                except Ride.DoesNotExist:
                    raise ValueError(f"Ride with id {ride['id_ride']} does not exist")
            
            return BaseResponse( success=True, message="Rides retrieved successfully", data=response.data, status=status.HTTP_200_OK )
        except Exception as e:
            return BaseResponse( success=False, message="Failed to retrieve rides", error=str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR )
    
    def create(self, request, *args, **kwargs):
        try:
            response = super().create(request, *args, **kwargs)
            
            # Create a RideEvent for the new ride
            ride = Ride.objects.get(id_ride=response.data['id_ride'])
            RideEvent.objects.create(
                id_ride=ride,
                description='Status changed to pickup'
            )
            
            return BaseResponse(success=True, message="Ride created successfully", data=response.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            return BaseResponse( success=False, message="Failed to create ride", error=str(e), status=status.HTTP_400_BAD_REQUEST )
    
    def update(self, request, *args, **kwargs):
        try:
            # Get the original ride object
            instance = self.get_object()
            original_status = instance.status

            # Perform the update
            response = super().update(request, *args, **kwargs)
            
            # Check if the status has changed
            updated_instance = self.get_object()
            if updated_instance.status != original_status:
                # Create a new RideEvent
                if updated_instance.status == 'en-route':
                    description = 'Status changed to en-route'
                elif updated_instance.status == 'pickup':
                    description = 'Status changed to pickup'
                elif updated_instance.status == 'dropoff':
                    description = 'Status changed to dropoff'
                else:
                    description = f'Status changed to {updated_instance.status}'
                
                RideEvent.objects.create(
                    id_ride=updated_instance,
                    description=description
                )

            return BaseResponse(success=True, message="Ride updated successfully", data=response.data, status=status.HTTP_200_OK)
        except Exception as e:
            return BaseResponse(success=False, message="Failed to update ride", error=str(e), status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        try:
            super().destroy(request, *args, **kwargs)
            return BaseResponse( success=True, message="Ride deleted successfully", status=status.HTTP_204_NO_CONTENT )
        except Exception as e:
            return BaseResponse( success=False, message="Failed to delete ride", error=str(e), status=status.HTTP_400_BAD_REQUEST )

