# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-08 05:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0007_auto_20170407_1600'),
    ]

    operations = [
        migrations.RenameField(
            model_name='videolist',
            old_name='player_url',
            new_name='video_url',
        ),
    ]