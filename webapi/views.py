from django.shortcuts import render
from rest_framework import viewsets
from .serializer import *
from .models import *

# Create your views here.

class HostViewSet(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    
class EndpointViewSet(viewsets.ModelViewSet):
    queryset = EndPoint.objects.all()
    serializer_class=EndpointSerializer