#create the custom permissions for the Post/Blog table.

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Allow read access to any user
        if request.method in permissions.SAFE_METHODS:
            return True

        # Restrict write access to the owner of the post/blog
        return obj.user == request.user