from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from profiles.permissions import IsServiceUserOrReadOnly
from profiles.models import ServiceUser, Favorites
from profiles.serializers import ServiceUserSerializer, FavoritesSerializer


class ServiceUserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsAdminUser]
    queryset = ServiceUser.objects.all()
    serializer_class = ServiceUserSerializer


class FavoritesViewSet(viewsets.ModelViewSet):
    permission_classes = [IsServiceUserOrReadOnly]
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
