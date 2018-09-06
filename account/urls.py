from django.urls import path,include
from .views import AccountViewset
from rest_framework import routers


router = routers.DefaultRouter(trailing_slash=False)
router.register('account', AccountViewset)


urlpatterns = [
    path('', include(router.urls)),
    
]