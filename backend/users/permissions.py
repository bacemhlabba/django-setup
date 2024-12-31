from rest_framework.permissions import BasePermission

class AllowAny(BasePermission):
    """
    Custom permission to allow any user to access the registration endpoint.
    """

    def has_permission(self, request, view):
        return True  # Allow access to everyone
