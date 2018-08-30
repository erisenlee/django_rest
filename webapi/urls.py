from django.urls import path, include
from rest_framework import routers
from .views import *

router = routers.DefaultRouter(trailing_slash=False)

router.register(r'hosts',HostViewSet)
router.register(r'endpoints',EndpointViewSet)


urlpatterns = [
    path('', include(router.urls)),
    
]


