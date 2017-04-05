# -*- coding: utf-8 -*-

from django.forms import ModelForm

from models import Channel

from tv_server.libs.widgets import SingleImageInput

class ChannelForm(ModelForm):


    def __init__(self, *args, **kwargs):
        super(ChannelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Channel
        fields = '__all__'
        widgets = {
            'icon' : SingleImageInput
        }