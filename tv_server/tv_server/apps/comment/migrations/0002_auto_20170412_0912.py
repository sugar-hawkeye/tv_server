# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-12 01:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'get_latest_by': 'created_at', 'ordering': ['created_at'], 'verbose_name': '\u8bc4\u8bba', 'verbose_name_plural': '\u8bc4\u8bba'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='client_id',
            field=models.IntegerField(verbose_name='\u5ba2\u6237id'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(verbose_name='\u5185\u5bb9'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='from_source',
            field=models.CharField(choices=[('I', 'IPhone'), ('A', 'Android'), ('P', 'PC')], max_length=1, verbose_name='\u8bc4\u8bba\u6765\u6e90'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='video_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video', verbose_name='\u89c6\u9891id'),
        ),
    ]
