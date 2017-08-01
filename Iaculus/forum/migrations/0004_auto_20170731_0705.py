# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 07:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_auto_20170730_0829'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='parent_posts',
        ),
        migrations.AddField(
            model_name='post',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='forum.Post'),
        ),
    ]
