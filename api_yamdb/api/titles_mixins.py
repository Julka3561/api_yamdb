from rest_framework import viewsets

from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.mixins import DestroyModelMixin

class CreateListDestroyViewSet(
    CreateModelMixin,
    ListModelMixin,
    DestroyModelMixin,
    viewsets.GenericViewSet,
):
    pass
