from rest_framework import serializers

from .models import Video,Cover,VideoList,VideoCount

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        exclude = ('created_by',)

class CoverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cover
        exclude = ('created_by',)


class VideoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoList
        exclude = ('created_by',)

class VideoCountSerializer(serializers.ModelSerializer):
    class Meta:
        model = VideoCount
        fields = '__all__'