from django.shortcuts import render
from .serializer import AccountSerializer
from .models import Account
from rest_framework import viewsets
# Create your views here.

class AccountViewset(viewsets.ReadOnlyModelViewSet):
    lookup_field='id'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

def account_list(request):
    account_list = Account.objects.all()
    return render(request,'account/account_list.html',context={"account_list":account_list})


