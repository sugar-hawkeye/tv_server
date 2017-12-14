from django.conf.urls import url
from .views import ClientAuthView,ClientLogin

urlpatterns = [
    url(r'^addclient/$', ClientAuthView.as_view()),
    url(r'^login/$', ClientLogin.as_view()),
]