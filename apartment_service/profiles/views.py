from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from profiles.models import ServiceUser, Favorites
from profiles.serializers import ServiceUserSerializer, FavoritesSerializer


class ServiceUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = ServiceUser.objects.all()
    serializer_class = ServiceUserSerializer


class FavoritesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
