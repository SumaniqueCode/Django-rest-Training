from rest_framework import viewsets, filters
from .serializers import TaskSerializer
from .models import Task
from .permissions import *
from django_filters import rest_framework as rest_filter

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsTaskOwnerOrReadOnly,]
    filter_backends = [filters.OrderingFilter, filters.SearchFilter,rest_filter.DjangoFilterBackend]
    ordering_fields = ['title', 'description', 'status', 'start_date', 'due_date']
    search_fields = ['title', 'description', 'status','priority']
    filterset_fields = ['status', 'priority']