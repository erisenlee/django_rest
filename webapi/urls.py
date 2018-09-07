from django.urls import path, include
from rest_framework import routers
from .views import HostViewSet,EndpointViewSet

router = routers.SimpleRouter(trailing_slash=False)

router.register(r'hosts',HostViewSet, base_name='host')
router.register(r'endpoints',EndpointViewSet ,base_name='endpoint')


urlpatterns = [
    path('', include(router.urls)),
    
]


