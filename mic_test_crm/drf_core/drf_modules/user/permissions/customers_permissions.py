from rest_framework.permissions import BasePermission

class IsCustomer(BasePermission):
    """
    Cho phép truy cập nếu user có role là 'customer'.
    """
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'customer'