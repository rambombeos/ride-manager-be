from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer

# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed, created, edited, or deleted.
    
    Supported HTTP methods:
    - GET /api/users/: Retrieve a list of users or a specific user via API
    - POST /api/users/: Create a new user via API
    - PUT/PATCH /api/users/{id}/: Update an existing user via API
    - DELETE /api/users/{id}/: Remove a user via API
    
    Payload for POST, PUT, PATCH:
    {
        "username": "string",
        "email": "user@example.com",
        "first_name": "string",
        "last_name": "string",
        "password": "string"
    }
    
    Note: Password field is write-only and will not be returned in GET requests.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
