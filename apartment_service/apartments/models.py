from django.db import models

from profiles.models import ServiceUser


class ApartmentInfo(models.Model):
    landlord = models.ForeignKey(ServiceUser,
                                 on_delete=models.CASCADE,
                                 related_name='apartments')
    title = models.CharField(max_length=150)
    content = models.TextField(max_length=500, null=True, blank=True)
    photo = models.ImageField(upload_to='uploads/%Y/%m/%d/', null=True)
    city = models.CharField(max_length=250)
    address = models.CharField(max_length=100)
    apartment_area = models.FloatField(max_length=30)
    price = models.FloatField(max_length=30)
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published']


