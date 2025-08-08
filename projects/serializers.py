from rest_framework import serializers
from .models import Project
from django.contrib.auth.models import User

class ProjectSerializer(serializers.ModelSerializer):
    user = serializers.HyperlinkedRelatedField( queryset = User.objects.all(), many=False, view_name='user-detail')
    assigned_to = serializers.HyperlinkedRelatedField(queryset = User.objects.all(), many=True, view_name='user-detail')
    class Meta:
        model = Project
        fields = ['id','url', 'title', 'description','user', 'assigned_to', 'image','status', 'priority','start_date', 'due_date', 'created_at', 'updated_at']