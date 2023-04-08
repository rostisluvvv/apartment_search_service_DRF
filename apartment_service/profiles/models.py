from django.db import models
from django.contrib.auth.models import AbstractUser


class ServiceUser(AbstractUser):
    # username
    # first_name
    # last_name
    # email
    # user_permissions
    # last_login
    # date_joined
    avatar = models.ImageField(upload_to='user/avatar/',
                               blank=True,
                               null=True)
    middle_name = models.CharField(max_length=50, blank=True, null=True)
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.username


class Favorites(models.Model):
    service_user = models.ForeignKey(ServiceUser,
                                     related_name='favorites',
                                     on_delete=models.CASCADE)
    city = models.CharField(max_length=250, blank=True, null=True)
    apartment_area_gte = models.FloatField(blank=True,
                                           null=True)
    apartment_area_lte = models.FloatField(blank=True,
                                           null=True)
    price_gte = models.FloatField(blank=True, null=True)
    price_lte = models.FloatField(blank=True, null=True)
