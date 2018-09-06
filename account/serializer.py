from rest_framework import serializers
from .models import Account


class AccountSerializer(serializers.ModelSerializer):
    url=serializers.CharField(source='get_absolute_url',read_only=True)
    class Meta:
        model = Account
        fields = ['id', 'name', 'url_link', 'username', 'password', 'created','url']
        