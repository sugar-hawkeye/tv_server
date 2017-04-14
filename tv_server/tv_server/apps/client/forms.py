
from django import forms
from django.forms.widgets import PasswordInput
from tv_server.libs.widgets import SingleImageInput

from models import Client,ClientAuth

class ClientAuthForm(forms.ModelForm):
    class Meta:
        model = ClientAuth
        fields = '__all__'
        widgets = {
            'credential': PasswordInput,
        }

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'headshot': SingleImageInput,
        }

