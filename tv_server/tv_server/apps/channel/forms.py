# -*- coding: utf-8 -*-

from django.forms import ModelForm

from models import Channel

from tv_server.libs.widgets import SingleImageInput

class ChannelForm(ModelForm):


    class Meta:
        model = Channel
        fields = '__all__'
        widgets = {
            'cover' : SingleImageInput
        }