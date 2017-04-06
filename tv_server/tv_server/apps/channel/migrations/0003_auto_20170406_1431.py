# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 06:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0002_auto_20170405_1021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'get_latest_by': 'created_at', 'ordering': ['created_at'], 'permissions': (('channel_publish', 'Can publish channel'),), 'verbose_name': '\u9891\u9053', 'verbose_name_plural': '\u9891\u9053'},
        ),
        migrations.RenameField(
            model_name='channel',
            old_name='icon',
            new_name='cover',
        ),
    ]
