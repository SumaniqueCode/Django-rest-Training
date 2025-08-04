from rest_framework import serializers
from .models import Task
from projects.serializers import ProjectSerializer

class TaskSerializer(serializers.ModelSerializer):
    title = serializers.CharField(min_length=5, max_length=10)
    user = serializers.HyperlinkedRelatedField(read_only = True, many=False, view_name = 'user-detail')
    assigned_to = serializers.HyperlinkedRelatedField(read_only=True, many=True, view_name = "user-detail")
    project = ProjectSerializer(read_only = True)
    class Meta:
        model = Task
        fields = ['id','url', 'title', 'description', 'user', 'assigned_to', 'project', 'start_date', 'due_date', 'status', 'priority']