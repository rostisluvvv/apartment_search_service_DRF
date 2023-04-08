from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
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
    # queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer

    def get_queryset(self):
        user_id = self.kwargs.get('user_id')
        user = get_object_or_404(ServiceUser, pk=user_id)
        queryset = user.favorites.all()
        return queryset

    def perform_create(self, serializer):
        serializer.save(service_user=self.request.user)
