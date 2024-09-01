from rest_framework import viewsets
from .models import User
from .serializers import UserSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import status
from core.permissions import superuser_authenticated
from core.response import BaseResponse


@superuser_authenticated
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request, *args, **kwargs):
        users = User.objects.all()
        serializer = self.serializer_class(users, many=True)
        return BaseResponse(status=status.HTTP_200_OK, message="Users fetched successfully", success=True, data=serializer.data)
    
class SuperUserObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        try:
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']
            if not user.is_superuser:
                return BaseResponse(success=False, error="Only superusers can obtain tokens",
                                    status=status.HTTP_403_FORBIDDEN)
            
            # Delete the existing token if it exists
            Token.objects.filter(user=user).delete()
            
            # Create a new token
            token = Token.objects.create(user=user)
            return BaseResponse(success=True, status=status.HTTP_200_OK, message="Token created successfully", token=token.key)
        except Exception as e:
            return BaseResponse(success=False, error=str(e), status=status.HTTP_400_BAD_REQUEST, message="An error occurred")