from rest_framework import serializers

from .models import ServiceUser, Favorites


class ServiceUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServiceUser
        fields = ('first_name', 'phone_number', 'favorites')
        read_only_fields = ('favorites', )


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = ('city',
                  'apartment_area_gte',
                  'apartment_area_lte',
                  'price_gte',
                  'price_lte')
