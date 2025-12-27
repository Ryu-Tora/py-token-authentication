from rest_framework.permissions import SAFE_METHODS, BasePermission

from cinema.views import OrderViewSet


class IsAdminOrIfAuthenticatedReadOnly(BasePermission):
    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.method in SAFE_METHODS:
            return True

        if (
                request.method == "POST"
                and view.__class__ == OrderViewSet
        ):
            return True

        return request.user.is_staff
