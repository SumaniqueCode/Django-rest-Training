from rest_framework import routers
from .viewsets import TaskViewSet

app_name = 'tasks'

router = routers.DefaultRouter()
router.register('task', TaskViewSet)