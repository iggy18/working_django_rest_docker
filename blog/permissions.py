from rest_framework import permissions

class IsAuthorized(permissions.BasePermission):
    def has_permission(self, request, view, obj):
        # return super().has_permission(request, view, obj)
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
        