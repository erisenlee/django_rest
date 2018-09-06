from django.db import models
import uuid

# Create your models here.


class Account(models.Model):    
    id = models.UUIDField('id', default=uuid.uuid4(), primary_key=True, editable=False)
    name = models.CharField('name', max_length=255)
    url_link = models.URLField('link', blank=True, null=True)
    username = models.CharField('account_name', max_length=255)
    password = models.CharField('account_password', max_length=255)
    created = models.DateTimeField('created', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['crated']
