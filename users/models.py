from django.db import models
from django.contrib.auth.models import User

def generateImagePath( instance, file):
    return f'images/users/{instance.username}/{file}'
class Profile(models.Model):
    class RoleOptions(models.TextChoices):
        Employer= 'E', 'Employer'
        Worker= 'W', 'Worker'
        
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(choices=RoleOptions, default=RoleOptions.Worker, max_length=1)
    address = models.CharField(blank=True, null=True, max_length=50)
    dob = models.DateField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to=generateImagePath, default='images/users/default_user.jpg')
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
    