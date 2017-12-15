# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import time

from django.db import models
from django.db import connection

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




    @classmethod
    def getlist(self, videoId, commentId=None):
        with connection.cursor() as cursor:
            if commentId:
                cursor.execute("select * from comment  where comment.id in (select descendant_id from comment_path where comment_id=%s)",commentId)
                columns = [col[0] for col in cursor.description]
                return [dict(zip(columns, row)) for row in cursor.fetchall()]
            else:
                cursor.execute(
                    "select * from comment right join comment_path on comment.id=comment_path.comment_id where comment_path.descendant_id in (select descendant_id from comment_path group by descendant_id having count(*)=1) and comment.video_id=%s",videoId)
                columns = [col[0] for col in cursor.description]
                return [dict(zip(columns, row)) for row in cursor.fetchall()]



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

    @classmethod
    def c_insert(self,descendant,parent):
        with connection.cursor() as cursor:
            cursor.execute('insert into comment_path(comment_id,descendant_id,level) select comment_id,%s,level+1 from comment_path where descendant_id=%s',(descendant,parent))
            connection.commit()
        return

    class Meta:
        db_table = "comment_path"