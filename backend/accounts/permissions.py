from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    """
    Allow only Admin users
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role and request.user.role.name == 'ADMIN'


class IsRecruiter(permissions.BasePermission):
    """
    Allow only Recruiters
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role and request.user.role.name == 'RECRUITER'


class IsHiringManager(permissions.BasePermission):
    """
    Allow only Hiring Managers
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role and request.user.role.name == 'MANAGER'
