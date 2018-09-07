from django.urls import path,include
from .views import AccountViewset,account_list
from rest_framework import routers


router = routers.SimpleRouter(trailing_slash=False)
router.register('account', AccountViewset)


urlpatterns = [
    path('', include(router.urls)),
    path('list/',account_list,name='account-list'),
]