# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

from tv_server.apps.client.models import Client
from tv_server.apps.video.models import Video

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    video_id = models.ForeignKey(Video, on_delete=models.CASCADE,verbose_name='视频id')
    content = models.TextField(verbose_name='内容')
    client_id = models.IntegerField(verbose_name='客户id')

    type_choice = (
        ('I', 'IPhone'),
        ('A', 'Android'),
        ('P', 'PC'),
    )
    from_source = models.CharField(max_length=1,choices=type_choice,verbose_name='评论来源')

    class Meta:
        db_table = "comment"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name_plural = '评论'
        verbose_name = '评论'