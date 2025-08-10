from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Task
from .permissions import *

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsTaskOwnerOrReadOnly,]