from django.conf.urls import url,include

from rest_framework import routers,serializers,viewsets

from models import Tag,TagInfo

class TagSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tag
        fields = ('title','priority','channel_id','is_publish')

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all().filter(is_publish=True)
    serializer_class =  TagSerializer


tag_router = routers.DefaultRouter()
tag_router.register(r'get_tags',TagViewSet)

class TagInfoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TagInfo
        fields = ('tag_id','title','priority','is_publish')

class TagInfoViewSet(viewsets.ModelViewSet):
    queryset = TagInfo.objects.all().filter(is_publish=True)
    serializer_class =  TagInfoSerializer


taginfo_router = routers.DefaultRouter()
taginfo_router.register(r'get_taginfos',TagInfoViewSet)

urlpatterns = [
    url(r'^tag/', include(tag_router.urls)),
    url(r'^tag_info/', include(taginfo_router.urls)),
]

