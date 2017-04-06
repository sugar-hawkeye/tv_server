# -*- coding: utf-8 -*-

from django.forms import ModelForm

from models import Cover

from tv_server.libs.widgets import SingleImageInput

class CoverForm(ModelForm):


    class Meta:
        model = Cover
        fields = '__all__'
        widgets = {
            'cover_pic' : SingleImageInput
        }