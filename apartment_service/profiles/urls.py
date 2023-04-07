from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import ServiceUserViewSet, FavoritesViewSet


router = routers.DefaultRouter()

router.register('users', ServiceUserViewSet, basename='apartments')
router.register(r'users/(?P<user_id>\d+)/favorites',
                FavoritesViewSet,
                basename='apartments')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
