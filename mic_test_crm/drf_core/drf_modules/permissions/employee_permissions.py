from rest_framework.permissions import BasePermission

class IsEmployee(BasePermission):
    """
    Cho phép truy cập nếu user có role là 'employee'.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'employee'