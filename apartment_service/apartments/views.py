from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .permissions import IsLandlordOrReadOnly
from .serializers import ApartmentInfoSerializer
from .models import ApartmentInfo


class ApartmentInfoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated, IsLandlordOrReadOnly]
    queryset = ApartmentInfo.objects.all()
    serializer_class = ApartmentInfoSerializer
