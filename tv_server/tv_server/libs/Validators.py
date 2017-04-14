# -*- coding: utf-8 -*-

import re

from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _



def validate_video_url(value):
    if not value:
        raise ValidationError(_('播放地址不能为空'))
    if not re.match(r'^https?:/{2}\w.+$',value):
        raise ValidationError(_('%(value)不是一个可访问的播放地址'),params={'value':value},)

def validate_phone(value):
    if not re.match(r'”1[3458]\\d{4}(\\d)\\1{4}"',value):
        raise ValidationError(_('%(value)不是一个有效手机号'), params={'value': value}, )