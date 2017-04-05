# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from tv_server.libs import UploadUtils
from tv_server.apps.video.models import Video

# Create your models here.

class ClientAuth(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    type_choice = (
        ('P', 'Phone'),
        ('W', 'Weibo'),
        ('C', 'WeChat'),
        ('Q', 'QQ'),
        ('U', "Username")
    )
    identity_type = models.CharField(max_length=1, choices=type_choice,verbose_name='登录类型')
    identifier = models.CharField(max_length=100,verbose_name='用户名')
    credential = models.CharField(max_length=250,verbose_name='密码')
    verified = models.BooleanField(default=False)

    class Meta:
        db_table="client_auth"
        get_latest_by = 'identity_type'

class Client(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    email = models.EmailField(unique=True,null=True,blank=True)
    phone = models.CharField(max_length=20,unique=True,null=True,blank=True)
    client_id = models.OneToOneField(ClientAuth, on_delete=models.CASCADE,primary_key=True)
    nickname = models.CharField(max_length=20,null=True,blank=True)
    headshot = models.ImageField(upload_to=UploadUtils.avator_path, null=True, blank=True)

    class Meta:
        db_table="client"
        get_latest_by = 'created_at'
        ordering = ['created_at']


class VideoFavorite(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    client_id = models.IntegerField()
    video_id = models.IntegerField()

    class Meta:
        db_table="video_favorite"
        get_latest_by = 'created_at'
        ordering = ['created_at']


class VideoHistory(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    client_id = models.IntegerField()
    video_id = models.IntegerField()
    play_time = models.IntegerField()
    is_serial = models.BooleanField()
    video_list_id = models.IntegerField()

    class Meta:
        db_table="video_history"
        get_latest_by = 'created_at'
        ordering = ['created_at']

