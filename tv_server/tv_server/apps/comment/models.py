# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import time

from django.db import models


from tv_server.apps.client.models import Client
from tv_server.apps.video.models import Video
from signals import custom_post_save,save_handler

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    video = models.ForeignKey(Video, on_delete=models.CASCADE,verbose_name='视频id')
    content = models.TextField(verbose_name='内容')
    client_id = models.IntegerField(verbose_name='客户id')

    type_choice = (
        ('I', 'IPhone'),
        ('A', 'Android'),
        ('P', 'PC'),
    )
    from_source = models.CharField(max_length=1,choices=type_choice,verbose_name='评论来源',default='P')

    class Meta:
        db_table = "comment"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name_plural = '评论'
        verbose_name = '评论'

    def __unicode__(self):
        return unicode(self.video_id)

    # def save(self, force_insert=False, force_update=False, using=None,
    #          update_fields=None):
    #     model = super(Comment,self).save(force_insert,force_update,using,update_fields)
    #     custom_post_save.send(sender=save_handler,ancestor=)

class CommentPath(models.Model):
    comment_id = models.BigIntegerField()
    descendant_id = models.BigIntegerField()
    level = models.IntegerField(default=0)

    class Meta:
        db_table = "comment_path"