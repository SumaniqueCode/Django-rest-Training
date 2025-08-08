from rest_framework import permissions

class IsProjectOwnerOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        
        # #gives permission to everyone to read the data in safe method i.e get, head, option
        # if request.method in permissions.SAFE_METHODS:
        #     return True
        
        #gives permission to the owner of the project to edit the project
        if not request.user.is_anonymous:
            return request.user == obj.user
        
        if request.user in obj.assigned_to.all():
            return request.method in permissions.SAFE_METHODS
        
        return False