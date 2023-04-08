from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from .models import ServiceUser, Favorites


class FavoritesSerializer(serializers.ModelSerializer):
    service_user = serializers.SlugRelatedField(slug_field='first_name',
                                                read_only=True, )

    class Meta:
        model = Favorites
        fields = ('service_user',
                  'city',
                  'apartment_area_gte',
                  'apartment_area_lte',
                  'price_gte',
                  'price_lte')


class ServiceUserSerializer(serializers.ModelSerializer):
    favorites = FavoritesSerializer(many=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = ServiceUser
        fields = ('id',
                  'is_staff',
                  'password',
                  'username',
                  'first_name',
                  'phone_number',
                  'favorites')

    def validate_password(self, value):
        validate_password(value)
        return value

    def validate(self, data):
        if not data.get('password'):
            raise serializers.ValidationError("Password is required")
        return data
