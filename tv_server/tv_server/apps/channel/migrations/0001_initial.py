# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-05 01:24
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import tv_server.libs.UploadUtils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('edited_at', models.DateTimeField(auto_now=True, verbose_name='\u6700\u597d\u7f16\u8f91\u65f6\u95f4')),
                ('title', models.CharField(max_length=10, unique=True, verbose_name='\u6807\u9898')),
                ('icon', models.ImageField(blank=True, null=True, upload_to=tv_server.libs.UploadUtils.channel_path, verbose_name='\u56fe\u6807')),
                ('priority', models.IntegerField(verbose_name='\u6392\u5217\u987a\u5e8f')),
                ('is_publish', models.BooleanField(default=False, verbose_name='\u662f\u5426\u53d1\u5e03')),
                ('created_by', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='\u521b\u5efa\u4eba')),
            ],
            options={
                'ordering': ['created_at'],
                'db_table': 'channel',
                'get_latest_by': 'created_at',
                'permissions': (('channel_publish', 'Can publish channel'),),
            },
        ),
    ]
