from django.db import models
from django.contrib.auth.models import AbstractUser


class ServiceUser(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # password
    # user_permissions
    # last_login
    # date_joined
    avatar = models.ImageField(upload_to='user/avatar/',
                               blank=True,
                               null=True)
    middle_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=14)
    favorites = models.OneToOneField('Favorites',
                                     on_delete=models.CASCADE,
                                     related_name='service_users')

    def __str__(self):
        return self.username


class Favorites(models.Model):
    city = models.CharField(max_length=250)
    apartment_area_gte = models.FloatField(max_length=30)
    apartment_area_lte = models.FloatField(max_length=30)
    price_gte = models.FloatField(max_length=30)
    price_lte = models.FloatField(max_length=30)
