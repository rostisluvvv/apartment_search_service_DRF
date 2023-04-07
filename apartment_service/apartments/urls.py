from django.urls import include, path
from rest_framework import routers
from rest_framework.authtoken import views

from .views import ApartmentInfoViewSet


router = routers.DefaultRouter()

router.register('apartments', ApartmentInfoViewSet, basename='apartments')


urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls)),
]
