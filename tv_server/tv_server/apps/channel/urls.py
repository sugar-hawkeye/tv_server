from django.conf.urls import url,include

from rest_framework import routers,serializers,viewsets

from models import Channel

class ChannelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Channel
        fields = ('title','icon','priority','is_publish')

class ChannelViewSet(viewsets.ModelViewSet):
    queryset = Channel.objects.all().filter(is_publish=True)
    serializer_class =  ChannelSerializer


router = routers.DefaultRouter()
router.register(r'get_channel',ChannelViewSet)

urlpatterns = [
    url(r'^channel/', include(router.urls)),
]
