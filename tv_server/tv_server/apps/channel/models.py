# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

from tv_server.libs import UploadUtils

class Channel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    edited_at = models.DateTimeField(auto_now=True,verbose_name="最好编辑时间")
    created_by = models.ForeignKey(User,editable=False,on_delete=models.SET_NULL,verbose_name="创建人",null=True,blank=True)

    title = models.CharField(max_length=10,verbose_name="标题",unique=True)
    cover = models.ImageField(upload_to=UploadUtils.channel_path,verbose_name="图标")
    priority = models.IntegerField(verbose_name="排列顺序")
    is_publish = models.BooleanField(default=False,verbose_name="是否发布")


    class Meta:
        db_table = "channel"
        get_latest_by = "created_at"
        ordering = ['created_at']
        permissions = (
            ("channel_publish", "Can publish channel"),
        )
        verbose_name = '频道'
        verbose_name_plural = '频道'

    def __unicode__(self):
        return self.title

