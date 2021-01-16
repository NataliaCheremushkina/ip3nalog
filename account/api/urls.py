from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)

app_name = 'account'

urlpatterns = [
    path('', include(router.urls)),
]
