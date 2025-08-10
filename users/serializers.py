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
    password = serializers.CharField(write_only = True, required = False)
    
    def create(self, validated_data):
        try:
            password = validated_data.pop('password')
            user = User.objects.create(**validated_data)
            user.set_password(password)
            user.save()
        except Exception as err:
            raise serializers.ValidationError({'error': str(err)})
        
        return user
    
    def update( self, instance, validated_data):
        try:
            user = instance
            if 'password' in validated_data:
                password = validated_data.pop('password')
                user.set_password(password)
                user.save()
        except Exception as err:
            raise serializers.ValidationError({'error': str(err)})
            
    class Meta:
        model = User
        fields = ['id','url', 'username','first_name','last_name','username', 'email', 'password', 'profile']
