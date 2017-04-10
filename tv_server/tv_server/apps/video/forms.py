# -*- coding: utf-8 -*-

from django.forms import ModelForm
from django import forms

from models import Cover,VideoList

from tv_server.libs.widgets import SingleImageInput

class CoverForm(ModelForm):

    class Meta:
        model = Cover
        fields = '__all__'

        widgets = {
            'cover_pic' : SingleImageInput
        }



class VideoListForm(ModelForm):
    class Meta:
        model = VideoList
        fields = '__all__'
        widgets = {
            # 'video_url' : SingleImageInput,
            'video_icon':SingleImageInput,
        }