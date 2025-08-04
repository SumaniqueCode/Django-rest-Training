from django.db import models
from django.contrib.auth.models import User
from projects.models import Project

def generateAttachmentPath(instance, file):
 return f"attachments/tasks/{instance.user.username}/{file}"

class Task(models.Model):
    class statusOptions(models.TextChoices):
        PENDING = "P", "Pending"
        IN_PROGRESS = "I", "In Progress"
        COMPLETED = "C", "Completed"
        CANCELED = "X", "Canceled"
        
    class priorityOptions(models.TextChoices):
        LOW = "L", "Low"
        MEDIUM = "M", "Medium"
        HIGH = "H", "High"
        
    title = models.CharField(max_length=30)
    description = models.TextField(blank=True, null=True)
    assigned_to = models.ManyToManyField( User, blank=True, null=True, related_name='tasks_assigned')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tasks", null=True, blank=True)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tasks", blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    due_date = models.DateField(blank=True, null=True)
    status = models.CharField( max_length=1, choices=statusOptions.choices, default=statusOptions.PENDING )
    priority = models.CharField( max_length=1, choices=priorityOptions.choices, default=priorityOptions.MEDIUM)
    attachment = models.FileField(blank=True, null=True, upload_to=generateAttachmentPath)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    
    def __str__(self):
       return self.title
