from rest_framework import serializers

from .models import ServiceUser, Favorites


class FavoritesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Favorites
        fields = ('service_user',
                  'city',
                  'apartment_area_gte',
                  'apartment_area_lte',
                  'price_gte',
                  'price_lte')


class ServiceUserSerializer(serializers.ModelSerializer):
    favorites = FavoritesSerializer()

    class Meta:
        model = ServiceUser
        fields = ('first_name', 'phone_number', 'favorites')
        read_only_fields = ('favorites', )



