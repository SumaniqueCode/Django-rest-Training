from rest_framework import serializers
from .models import Profile
from django.contrib.auth.models import User


class ProfileSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField(read_only=True, many=False, view_name='user-detail')
    class Meta:
        model = Profile
        fields = ['id','url', 'role', 'address', 'dob', 'user', 'profile_image']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(read_only = True)
    class Meta:
        model = User
        fields = ['id','url', 'username','first_name','last_name','username', 'email', 'password', 'profile']
