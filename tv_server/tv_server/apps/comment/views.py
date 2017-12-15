from django.shortcuts import render
from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Comment,CommentPath

from .serializers import CommentSerializer

class CommentList(APIView):
    def get(self, request, videoId, format=None):
        video = Comment.objects.filter(video_id=videoId)
        serializer = CommentSerializer(video,many=True)
        return Response(serializer.data)

class CommentDetail(APIView):
    def post(self,request,commentId=None,format=None):

        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            obj = serializer.save()
            obj1 = CommentPath(comment_id=obj.id,descendant_id=obj.id)
            obj1.save()
            if commentId:
                sql = 'select count(*) from comment_path where descendant_id=%s AND comment_id!=%s;'% (obj.id,obj.id)
                num = CommentPath.objects.ra
                obj2 = CommentPath(comment_id=commentId,descendant_id=obj.id,level=)
                obj2.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)