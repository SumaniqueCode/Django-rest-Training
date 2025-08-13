from rest_framework import viewsets, status, response
from .models import Project
from .serializers import ProjectSerializer
from .permissions import *
from rest_framework.decorators import action

class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsProjectOwnerOrReadOnly, ]
    
    @action(detail=True, methods=['post', 'get'],name='Join', permission_classes=[])
    def join(self, request, pk=None):
        try:
            project = self.get_object()
            user = request.user
            if not user in project.assigned_to.all():
                project.assigned_to.add(user)
                return response.Response({'message': 'You have been assigned to this project'}, status=status.HTTP_202_ACCEPTED)
            else:
                return response.Response({'message': 'You are already assigned to this project'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return response.Response({'error': str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)