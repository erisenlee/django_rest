from rest_framework import serializers
from .models import *

class HostSerializer(serializers.HyperlinkedModelSerializer):
    login_url=serializers.URLField(source='get_login_url',read_only=True)
    class Meta:
        model = Host
        fields = ['id', 'created', 'title', 'login_endpoint','login_url', 'username', 'password', 'is_delete']
        # fields='__all__'
        
class EndpointSerializer(serializers.ModelSerializer):
    class Meta:
        model = EndPoint
        fields=['id','created','endpoint','description','host']