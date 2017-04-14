# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models
from tv_server.libs import UploadUtils,Validators
from django.core.validators import EmailValidator
from django.contrib.auth.hashers import check_password,make_password,PBKDF2PasswordHasher


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
    identifier = models.CharField(max_length=100,verbose_name='用户名',unique=True)
    credential = models.CharField(max_length=250,verbose_name='密码')
    verified = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.credential:
            self.credential = make_password(self.credential,None,'pbkdf2_sha256')
        super(ClientAuth,self).save(force_insert,force_update,using,update_fields)


    class Meta:
        db_table="client_auth"
        get_latest_by = 'identity_type'
        verbose_name_plural = '客户认证'
        verbose_name = '客户认证'

    def __unicode__(self):
        return self.identifier



class Client(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    email = models.EmailField(unique=True,null=True,blank=True,verbose_name='邮箱',validators=[EmailValidator])
    phone = models.CharField(max_length=20,unique=True,null=True,blank=True,verbose_name='手机号',validators=[Validators.validate_phone])
    client_id = models.OneToOneField(ClientAuth, on_delete=models.CASCADE,primary_key=True,verbose_name='客户id')
    nickname = models.CharField(max_length=20,null=True,blank=True,verbose_name='昵称')
    headshot = models.ImageField(upload_to=UploadUtils.avator_path, null=True, blank=True,verbose_name='头像')

    class Meta:
        db_table="client"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name_plural='客户详情'
        verbose_name='客户详情'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.nickname:
            self.nickname = self.client_id.identifier
        super(Client,self).save(force_insert,force_update,using,update_fields)

    def __unicode__(self):
        return self.nickname


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

