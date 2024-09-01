from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class IsSuperUser(permissions.BasePermission):
    def has_permission(self, request, view):
        # Ensure the user is authenticated via token
        auth = TokenAuthentication()
        user_auth_tuple = auth.authenticate(request)
        if user_auth_tuple is None:
            return False
        
        user, _ = user_auth_tuple
        return user and user.is_superuser
    
def superuser_authenticated(cls):
    cls.permission_classes = [IsSuperUser, IsAuthenticated]
    cls.authentication_classes = [TokenAuthentication]
    return cls