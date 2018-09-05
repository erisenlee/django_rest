from django.db import models
import uuid

# Create your models here.


class Account(models.Model):    
    id = models.UUIDField('id', default=uuid.uuid4(), primary_key=True, editable=False)
    
    

    def __str__(self):
        return 

    def __unicode__(self):
        return 
