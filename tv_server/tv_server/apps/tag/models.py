# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from tv_server.apps.channel.models import Channel
from django.contrib.auth.models import User


from smart_selects.db_fields import ChainedForeignKey


class Tag(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人",null=True,blank=True)

    title = models.CharField(max_length=15,verbose_name='一级标签名')
    priority = models.IntegerField(verbose_name="排列顺序")
    is_publish = models.BooleanField(default=False, verbose_name="是否发布")
    channel_id = models.ForeignKey(Channel, on_delete=models.SET_NULL, verbose_name="所属频道",null=True)

    def __unicode__(self):
        return self.title
        return unicode(self.channel_id) + u'--' + self.title

    class Meta:
        db_table="tag"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '一级标签'
        verbose_name_plural = '一级标签'

class TagInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User,editable=False,on_delete=models.SET_NULL,verbose_name="创建人",null=True,blank=True)

    channel_id = models.ForeignKey(Channel, on_delete=models.SET_NULL, verbose_name="所属频道", null=True)
    # tag_id = models.ForeignKey(Tag,on_delete=models.SET_NULL,verbose_name='一级标签',null=True)
    tag_id = ChainedForeignKey(
        Tag,
        chained_field="channel_id",
        chained_model_field="channel_id",
        sort=True,
        verbose_name='所属一级标签'
    )

    title = models.CharField(max_length=15,verbose_name="二级标签名")
    priority = models.IntegerField(verbose_name="排列顺序")

    is_publish = models.BooleanField(default=False,verbose_name="是否发布")

    class Meta:
        db_table="tag_info"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '二级标签'
        verbose_name_plural = '二级标签'

    def __unicode__(self):
        return unicode(self.tag_id) + u'---' + self.title



