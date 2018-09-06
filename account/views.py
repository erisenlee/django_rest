from django.shortcuts import render
from .serializer import AccountSerializer
from .models import Account
from rest_framework import viewsets
# Create your views here.

class AccountViewset(viewsets.ReadOnlyModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
    
