from django.db import models
from django.contrib.auth.models import User

def generateImagePath( instance, file):
    return f'images/projects/{instance.user.username}/{file}'

class Project(models.Model):
    class StatusOptions(models.TextChoices):
        IN_PROGRESS = 'IP', 'In Progress'
        COMPLETED = 'CP', 'Completed'
        PENDING = 'P', 'Pending'
        CANCELED = 'C', 'Canceled'
    
    class PriorityOptions(models.TextChoices):
        LOW = 'L', 'Low'
        MEDIUM = 'M', 'Medium'
        HIGH = 'H', 'High'
        
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    assigned_to = models.ManyToManyField(User, blank=True, null=True, related_name='assigned_projects')
    status = models.CharField(max_length=2, choices=StatusOptions.choices, default=StatusOptions.PENDING)
    priority = models.CharField(max_length=1, choices=PriorityOptions.choices, default=PriorityOptions.MEDIUM)
    image = models.ImageField(upload_to=generateImagePath, blank=True, null=True, default='images/projects/default.jpg')
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField( auto_now_add=True, editable=False)
    updated_at = models.DateTimeField( auto_now=True, editable=False)
    
    def __str__(self):
        return self.title
