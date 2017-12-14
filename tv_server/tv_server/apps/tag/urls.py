from django.conf.urls import url,include

from .views import TagList,TagInfoList





urlpatterns = [
    url(r'^taglist/(?P<channelId>[0-9]+)/$', TagList.as_view()),
    url(r'^taglist/(?P<channelId>[0-9]+)/(?P<tagId>[0-9]+)/$', TagInfoList.as_view()),
]

