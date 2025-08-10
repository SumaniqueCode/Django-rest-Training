from rest_framework import permissions

class IsTaskOwnerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow owners of a task or read-only access."""
    
    def has_permission(self, request, view):
        return request.user.is_authenticated
    
    def has_object_permission(self, request, view, obj):
        if request.user in obj.assigned_to.all():
            return request.method in permissions.SAFE_METHODS
        
        if obj.user == request.user:
            return True
        
        # if not request.user.is_anonymous:
        #     return request.user == obj.user
        
        return False