from rest_framework import permissions

class AdminOnReadOnly(permissions.IsAdminUser):
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        return request.method == "GET" or admin_permission

class EditUserOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            print(obj)
            return obj.title == "Brahmastra"

# Check permissions for write request