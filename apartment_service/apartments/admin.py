from django.contrib import admin

from .models import ApartmentInfo


class ApartmentInfoAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'price')
    list_display_links = ('title', 'city', 'price')


admin.site.register(ApartmentInfo, ApartmentInfoAdmin)
