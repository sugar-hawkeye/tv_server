from django.conf.urls import url
from .views import CommentList,CommentDetail

urlpatterns = [
    url(r'^comment/(?P<videoId>[0-9]+)/$', CommentList.as_view()),
    url(r'^addcomment/(?P<commentId>[0-9]+)/$', CommentDetail.as_view()),

]