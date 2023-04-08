from rest_framework import serializers

from .models import ApartmentInfo


class ApartmentInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ApartmentInfo
        fields = ('title',
                  'landlord',
                  # 'favorites',
                  'city',
                  'address',
                  'apartment_area',
                  'price',
                  'published')
