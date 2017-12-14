from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from views import channel_list,channel_detail


urlpatterns = [
    url(r'channels/$', channel_list),
    url(r'channels/(?P<pk>[0-9]+)/$', channel_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)