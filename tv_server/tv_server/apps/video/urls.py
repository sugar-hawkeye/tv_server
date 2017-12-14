from django.conf.urls import url,include

from .views import VideoSet,VideoDetail,CoverDetail,VideoListDetail,VideoCountDetail

urlpatterns = [
    url(r'^videolist/(?P<channelId>[0-9]+)/$', VideoSet.as_view()),
    url(r'^videolist/(?P<channelId>[0-9]+)/(?P<tagId>[0-9]+)/$', VideoSet.as_view()),
    url(r'^videolist/(?P<channelId>[0-9]+)/(?P<tagId>[0-9]+)/(?P<tagInfo>[0-9]+)/$', VideoSet.as_view()),
    # url(r'^videolist/(?P<channelId>[0-9]+)/(?P<tagId>[0-9]+)/$', TagInfoList.as_view()),

    url(r'^videodetail/(?P<videoId>[0-9]+)/$', VideoDetail.as_view()),
    url(r'^coverdetail/(?P<videoId>[0-9]+)/$', CoverDetail.as_view()),
    url(r'^videoset/(?P<videoId>[0-9]+)/$', VideoListDetail.as_view()),
    url(r'^videocount/(?P<videoId>[0-9]+)/$', VideoCountDetail.as_view()),
]



