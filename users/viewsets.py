from rest_framework import viewsets
from .models import Profile
from .serializers import ProfileSerializer, UserSerializer
from django.contrib.auth.models import User
from .permissions import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsUserOwnerOrGetPost,]
    
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsProfileOwnerOrGetPost,]