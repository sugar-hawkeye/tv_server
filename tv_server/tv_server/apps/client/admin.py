from django.contrib import admin

# Register your models here.
from models import Client,ClientAuth

from forms import ClientAuthForm,ClientForm


class ClientAdmin(admin.StackedInline):
    model = Client
    form = ClientForm

class ClientAuthAdmin(admin.ModelAdmin):
    form = ClientAuthForm
    list_display = ('identifier','identity_type')
    inlines = [
        ClientAdmin,
    ]

# admin.site.register(Client,ClientAdmin)
admin.site.register(ClientAuth,ClientAuthAdmin)