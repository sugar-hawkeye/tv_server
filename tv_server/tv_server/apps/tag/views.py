from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.forms.models import model_to_dict
from rest_framework import serializers
from .models import Tag,TagInfo
from .serializers import TagSerializer,TagInfoSerializer

# Create your views here.
class TagList(APIView):
    def get(self,request,channelId,format=None):
        tags = Tag.objects.filter(channel_id=channelId,is_publish=True)
        list = []
        for tag in tags:
            taginfo = TagInfo.objects.filter(channel_id=channelId, tag_id=tag.id, is_publish=True).values()
            t = model_to_dict(tag)

            t['taginfo']=taginfo
            list.append(t)
        # serializer = serializers.ser
        return Response(list)


class TagInfoList(APIView):
    def get(self,request,channelId,tagId,format=None):
        taginfo = TagInfo.objects.filter(channel_id=channelId,tag_id=tagId,is_publish=True)
        serializer = TagInfoSerializer(taginfo,many=True)
        return Response(serializer.data)