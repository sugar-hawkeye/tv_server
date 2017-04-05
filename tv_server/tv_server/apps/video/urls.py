from django.conf.urls import url,include

from rest_framework import routers,serializers,viewsets

from models import Video,Cover


class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Video
        fields = ('video_name','tag_id','tag_info')

class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all().filter(is_publish=True)
    serializer_class =  VideoSerializer

video_router = routers.DefaultRouter()
video_router.register(r'get_list',VideoViewSet)

urlpatterns = [
    url(r'^video/', include(video_router.urls)),

]
