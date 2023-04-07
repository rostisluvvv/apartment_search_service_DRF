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
    phone_number = models.IntegerField(max_length=13)
    favorites = models.ManyToManyField('Favorites',
                                       related_name='service_users')

    def __str__(self):
        return self.username


class Favorites(models.Model):
    pass
