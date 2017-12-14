from rest_framework import serializers

from .models import Tag,TagInfo

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('id','title','priority','channel_id')


class TagInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagInfo
        fields = ('id','title','priority','channel_id','tag_id')