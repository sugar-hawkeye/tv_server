# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 06:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0002_auto_20170405_1021'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'get_latest_by': 'created_at', 'ordering': ['created_at'], 'verbose_name': '\u4e00\u7ea7\u6807\u7b7e', 'verbose_name_plural': '\u4e00\u7ea7\u6807\u7b7e'},
        ),
        migrations.AlterModelOptions(
            name='taginfo',
            options={'get_latest_by': 'created_at', 'ordering': ['created_at'], 'verbose_name': '\u4e8c\u7ea7\u6807\u7b7e', 'verbose_name_plural': '\u4e8c\u7ea7\u6807\u7b7e'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='title',
            field=models.CharField(max_length=15, verbose_name='\u4e00\u7ea7\u6807\u7b7e\u540d'),
        ),
        migrations.AlterField(
            model_name='taginfo',
            name='tag_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='tag.Tag', verbose_name='\u4e00\u7ea7\u6807\u7b7e'),
        ),
        migrations.AlterField(
            model_name='taginfo',
            name='title',
            field=models.CharField(max_length=15, verbose_name='\u4e8c\u7ea7\u6807\u7b7e\u540d'),
        ),
    ]