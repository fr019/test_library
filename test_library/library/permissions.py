from rest_framework import permissions

SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')


class IsAdminUerOrIsAuthenticatedAndReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_authenticated and
            request.user.is_active and
            request.method in SAFE_METHODS
            or
            request.user and
            request.user.is_authenticated and
            request.user.is_active and
            request.user.is_staff
        )
