from django.db import models
import uuid
from urllib.parse import urljoin
# Create your models here.
class Host(models.Model):
    id=models.UUIDField('id',primary_key=True,default=uuid.uuid4,editable=False)
    title = models.CharField('host', max_length=200)
    login_endpoint = models.CharField('login', max_length=200, blank=True, null=True)
    username = models.CharField('login_user', max_length=200, blank=True, null=True)
    password = models.CharField('login_password', max_length=200, blank=True, null=True)
    is_delete=models.BooleanField('delete',default=False)
    created=models.DateTimeField('created',auto_now_add=True)

    def get_login_url(self):
        return urljoin(self.title,self.login_endpoint)

    def __str__(self):
        return self.title

class EndPoint(models.Model):
    id=models.UUIDField('id',primary_key=True,default=uuid.uuid4,editable=False)
    created = models.DateTimeField('created', auto_now_add=True)
    endpoint = models.CharField('endpoint', max_length=200)
    host = models.ForeignKey('Host', on_delete=models.CASCADE)
    description = models.CharField('descrpition', max_length=300, blank=True, null=True)
    
    def __str__(self):
        return '{}'.format(self.endpoint)
    class Meta:
        ordering = ('created',)
