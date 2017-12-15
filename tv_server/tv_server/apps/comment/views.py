from django.shortcuts import render
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Comment,CommentPath

from .serializers import CommentSerializer

class CommentList(APIView):
    def get(self, request, videoId, commentId=None,format=None):
        if commentId:
            videos = Comment.getlist(videoId,commentId)
        else:
            videos = Comment.getlist(videoId)
        return Response(videos)

class CommentDetail(APIView):
    def post(self,request,commentId=None,format=None):

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()

            obj1 = CommentPath(comment_id=obj.id,descendant_id=obj.id,level=0)
            obj1.save()
            if commentId:
                CommentPath.c_insert(obj.id,commentId)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)