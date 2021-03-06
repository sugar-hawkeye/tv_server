# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.models import User
from tv_server.apps.tag.models import Tag,TagInfo
from tv_server.apps.channel.models import Channel

from django.core.validators import URLValidator
from tv_server.libs import UploadUtils

from smart_selects.db_fields import ChainedForeignKey,ChainedManyToManyField


class Video(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人",null=True,blank=True)

    video_name = models.CharField(max_length=50,verbose_name="视频标题")
    video_desc = models.TextField(verbose_name="视频描述")
    director = models.CharField(max_length=20,null=True,blank=True,verbose_name="导演")
    player = models.CharField(max_length=50,null=True,blank=True,verbose_name="演员")
    publish_time = models.DateField(verbose_name="上映时间",null=True,blank=True)
    downloadable = models.BooleanField(default=False,verbose_name="是否能下载")
    is_publish = models.BooleanField(default=False,verbose_name="是否发布")
    is_serial = models.BooleanField(default=False,verbose_name="是否是剧集")
    cover_pic = models.ImageField(upload_to=UploadUtils.video_path, verbose_name="图片")
    channel_id = models.ForeignKey(Channel,on_delete=models.PROTECT,verbose_name="所属频道")
    # tag_id = models.ManyToManyField(Tag, verbose_name="一级标签")
    tag_id = ChainedManyToManyField(
        Tag,
        chained_field="channel_id",
        chained_model_field="channel_id",
        verbose_name='一级标签',

    )
    # tag_info = models.ManyToManyField(TagInfo,verbose_name="二级标签")
    tag_info = ChainedManyToManyField(
        TagInfo,
        chained_field="tag_id",
        chained_model_field="tag_id",
        verbose_name="二级标签",

    )


    class Meta:
        db_table="video"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '视频'
        verbose_name_plural = '视频'

    def __unicode__(self):
        return self.video_name

class Cover(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人", null=True,
                                   blank=True)

    type_choice = (
        ('120', '120*120'),
        ('320', '320*150'),
        ('120', '120*400'),
        ('80', '80*80'),

    )

    video_id = models.ForeignKey(Video,on_delete=models.CASCADE,verbose_name="视频id")
    image_type = models.CharField(max_length=10, choices=type_choice,verbose_name="图片类型")
    cover_pic = models.ImageField(upload_to=UploadUtils.video_path,verbose_name="图片")
    is_publish = models.BooleanField(default=False, verbose_name="是否发布")
    class Meta:
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '视频封面'
        verbose_name_plural = '视频封面'

    def __unicode__(self):
        return self.video_id.video_name




class VideoList(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人",null=True,blank=True)

    video_id = models.ForeignKey(Video,on_delete=models.CASCADE,verbose_name='视频id')
    video_name = models.CharField(max_length=50,verbose_name="视频名")
    video_index = models.IntegerField(verbose_name="剧集数",default=0,help_text="如果是剧集则按集数填写")
    video_url = models.URLField(validators=[URLValidator],verbose_name="视频地址")
    video_icon = models.ImageField(upload_to=UploadUtils.video_path,verbose_name="封面")
    desc = models.CharField(max_length=8,null=True,blank=True,help_text="如果是剧集则必须填写",verbose_name="视频描述")
    is_publish = models.BooleanField(default=False, verbose_name="是否发布")

    class Meta:
        db_table="video_list"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '视频列表'
        verbose_name_plural = '视频列表'

    def __unicode__(self):
        return self.video_id.video_name


class VideoCount(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    video_id = models.OneToOneField(Video, on_delete=models.CASCADE)
    play_count = models.IntegerField(default=0,verbose_name="播放数")
    download_count = models.IntegerField(default=0,verbose_name="下载数")
    up_count = models.IntegerField(default=0, verbose_name="点赞数")
    down_count = models.IntegerField(default=0, verbose_name="点踩数")

    class Meta:
        db_table="video_count"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name = '视频统计'
        verbose_name_plural = '视频统计'

# class VideoAbout(models.Model):
#     created_at = models.DateTimeField(auto_now_add=True)
#     edited_at = models.DateTimeField(auto_now=True)
#     created_by = models.ForeignKey(User, editable=False, on_delete=models.SET_NULL, verbose_name="创建人", null=True,
#                                    blank=True)
#
#     # video_id = models.ForeignKey(Video)
#     about_video_id = models.ManyToManyField(Video)
#
#     class Meta:
#         db_table="video_about"
#         verbose_name = '视频相关'
#         verbose_name_plural = '视频相关'