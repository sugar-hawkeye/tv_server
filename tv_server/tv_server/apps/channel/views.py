# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from serializers import ChannelSerializer
from .models import Channel

@api_view(['GET'])
def channel_list(request,format=None):
    if request.method == 'GET':
        channels = Channel.objects.filter(is_publish=True)
        serializer = ChannelSerializer(channels,many=True)
        return Response(serializer.data)


@api_view(['GET'])
def channel_detail(request,pk):
    try:
        channels = Channel.objects.get(pk=pk)
    except Channel.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ChannelSerializer(channels)
        return Response(serializer.data)
