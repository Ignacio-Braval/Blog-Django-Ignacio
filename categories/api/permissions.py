from rest_framework.permissions import BasePermission

# Esta clase le permite solo a los admin ocupar el CRUD
# de lo contrario solo podra ver los datos


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        else:
            return request.user.is_staff
