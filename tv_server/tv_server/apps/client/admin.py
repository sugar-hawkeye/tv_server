from django.contrib import admin

# Register your models here.
from models import Client,ClientAuth

class ClientAdmin(admin.ModelAdmin):
    pass

class ClientAuthAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client,ClientAdmin)
admin.site.register(ClientAuth,ClientAuthAdmin)