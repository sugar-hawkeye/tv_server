from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from tv_server.apps.channel.models import Channel

content_type = ContentType.objects.get_for_model(Channel)
permission = Permission.objects.create(
    codename='can_publish',
    name='Can Publish Posts',
    content_type=content_type,
)