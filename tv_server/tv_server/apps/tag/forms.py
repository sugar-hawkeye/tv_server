from django import forms
from tv_server.apps.channel.models import Channel
from .models import Tag



class CustomChoiceField(forms.ModelChoiceField):

    def label_from_instance(self, obj):
        return obj.title


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = "__all__"
