from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, SuperUserObtainAuthToken

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('token/', SuperUserObtainAuthToken.as_view(), name='token_obtain'),

]
