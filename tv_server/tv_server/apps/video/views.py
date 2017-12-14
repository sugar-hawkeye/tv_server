from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Video,Cover,VideoList,VideoCount
from .serializers import VideoSerializer,CoverSerializer,VideoListSerializer,VideoCountSerializer

class VideoSet(APIView):
    def get(self,request,channelId,tagId='0',tagInfo='0',format=None):
        videos = None
        if tagId == '0':
            videos = Video.objects.filter(channel_id=channelId, is_publish=True)
        elif  tagInfo == '0':
            videos = Video.objects.filter(channel_id=channelId, tag_id=tagId, is_publish=True)
        else:
            videos = Video.objects.filter(channel_id=channelId, tag_id=tagId, tag_info=tagInfo, is_publish=True)

        serializer = VideoSerializer(videos,many=True)
        return Response(serializer.data)

class VideoDetail(APIView):
    def get(self, request, videoId, format=None):
        video = Video.objects.get(video_id=videoId)
        serializer = VideoSerializer(video)
        return Response(serializer.data)

class CoverDetail(APIView):
    def get(self, request, videoId, format=None):
        cover = Cover.objects.filter(video_id=videoId)
        serializer = CoverSerializer(cover,many=True)
        return Response(serializer.data)

class VideoListDetail(APIView):
    def get(self, request, videoId, format=None):
        videos = VideoList.objects.filter(video_id=videoId)
        serializer = VideoListSerializer(videos,many=True)
        return Response(serializer.data)

class VideoListDetail(APIView):
    def get(self, request, videoId, format=None):
        videos = VideoList.objects.filter(video_id=videoId)
        serializer = VideoListSerializer(videos,many=True)
        return Response(serializer.data)

class VideoCountDetail(APIView):
    def get(self, request, videoId, format=None):
        videos = VideoCount.objects.get(video_id=videoId)
        serializer = VideoCountSerializer(videos)
        return Response(serializer.data)