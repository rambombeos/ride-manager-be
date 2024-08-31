from rest_framework import viewsets, filters
from rest_framework.pagination import PageNumberPagination
from django.db.models import F, ExpressionWrapper, FloatField
from django.db.models.functions import Power, Sqrt
from .models import Ride
from .serializers import RideSerializer
from identity.serializers import UserSerializer
from rest_framework.response import Response
from rest_framework import status
from core.response import BaseResponse

class RidePagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

class RideViewSet(viewsets.ModelViewSet):
    queryset = Ride.objects.all().select_related('id_rider', 'id_driver').prefetch_related('events')
    serializer_class = RideSerializer
    pagination_class = RidePagination
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['pickup_time']

    def get_queryset(self):
        queryset = super().get_queryset()
        
        status = self.request.query_params.get('status')
        rider_email = self.request.query_params.get('id_rider__email')
        lat = self.request.query_params.get('latitude')
        lon = self.request.query_params.get('longitude')
        
        if status:
            queryset = queryset.filter(status=status)
        
        if rider_email:
            queryset = queryset.filter(id_rider__email=rider_email)
        
        if lat and lon:
            lat = float(lat)
            lon = float(lon)
            
            # Calculate distance using the Haversine formula
            queryset = queryset.annotate(
                distance=ExpressionWrapper(
                    Sqrt(
                        Power(F('pickup_latitude') - lat, 2) +
                        Power(F('pickup_longitude') - lon, 2)
                    ),
                    output_field=FloatField()
                )
            )
            
            # Add distance to ordering options
            self.ordering_fields += ['distance']
        
        return queryset

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)
        
        # Add User details to the response
        for ride in response.data['results']:
            ride['id_rider'] = UserSerializer(Ride.objects.get(id_ride=ride['id_ride']).id_rider).data
            ride['id_driver'] = UserSerializer(Ride.objects.get(id_ride=ride['id_ride']).id_driver).data
        
        return BaseResponse(
            success=True,
            message="Rides retrieved successfully",
            data=response.data,
            status=status.HTTP_200_OK
        )
