from rest_framework import permissions


class IsEmployeeOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'employee') or request.user.is_staff
