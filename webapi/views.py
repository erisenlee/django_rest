from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializer import HostSerializer,EndpointSerializer
from .models import Host,EndPoint
from django.db.models import Q

# Create your views here.

class HostViewSet(viewsets.ModelViewSet):
    lookup_field='id'
    queryset = Host.objects.all()
    serializer_class = HostSerializer
    
class EndpointViewSet(viewsets.ModelViewSet):
    lookup_field='id'
    queryset = EndPoint.objects.all()
    serializer_class = EndpointSerializer

    @action(detail=False)
    def search(self, request):
        q = request.query_params
        if not q:
            return Response({'result': 'search param empty'})
        queryset = EndPoint.objects.filter(Q(endpoint__contains=q['q'])|Q(description__contains=q['q']))
        serializer=self.get_serializer(queryset,many=True)
        return Response(serializer.data)
         


        
    
