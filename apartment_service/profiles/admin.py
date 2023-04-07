from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin

from .models import ServiceUser, Favorites


class ServiceUserAdmin(UserAdmin):
    list_display = ('username',
                    'email',
                    'phone_number',
                    'first_name',
                    'last_name',
                    'is_staff')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name',
                                         'last_name',
                                         'middle_name',
                                         'email',
                                         'phone_number')}),
        (_('Permissions'),
         {
             'fields': (
                 'is_active',
                 'is_staff',
                 'is_superuser',
                 'groups',
                 'user_permissions',
             ),
         },),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
        (_('info'), {'fields': ('avatar', 'favorites')}),
    )


class FavoritesAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'city',
                    'apartment_area_gte',
                    'apartment_area_lte',
                    'price_gte',
                    'price_lte')


admin.site.register(ServiceUser, ServiceUserAdmin)
admin.site.register(Favorites, FavoritesAdmin)
