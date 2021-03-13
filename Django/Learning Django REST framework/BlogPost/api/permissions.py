from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Return `True` if permission is granted, `False` otherwise.
        """
        # Only GET method is allowed to anonymous user, read-only
        # permissions.SAFE_METHODS is tuple of (GET, OPTION, HEAD)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Everything except read-only
        # here to check the who has created the post we need to use -- owner method
        return obj.author == request.user