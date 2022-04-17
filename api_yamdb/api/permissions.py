from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Object-level permission to only allow authors of an object to edit it.
    Assumes the model instance has an `author` attribute.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class ReadOnly(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.method in permissions.SAFE_METHODS


class IsAdmin(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'Admin':
            return True
        return False


class IsModer(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'Moder':
            return True
        return False


class IsUser(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'User':
            return True
        return False
