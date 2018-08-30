from django.contrib import admin
from .models import Host,EndPoint,DataBase
# Register your models here.

class HostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'login_endpoint', 'is_delete', 'created')
    

admin.site.register(Host, HostAdmin)
admin.site.register(DataBase)
admin.site.register(EndPoint)
