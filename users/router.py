from rest_framework import routers
from .viewsets import ProfileViewSet, UserViewSet

app_name = "users"
router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)