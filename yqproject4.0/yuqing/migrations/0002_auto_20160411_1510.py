# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuqing', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='headhunter',
            name='blog_num',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\xbe\xae\xe5\x8d\x9a\xe6\x95\xb0'),
        ),
        migrations.AddField(
            model_name='headhunter',
            name='fans_num',
            field=models.IntegerField(default=0, verbose_name=b'\xe7\xb2\x89\xe4\xb8\x9d\xe6\x95\xb0'),
        ),
        migrations.AddField(
            model_name='headhunter',
            name='follow_num',
            field=models.IntegerField(default=0, verbose_name=b'\xe5\x85\xb3\xe6\xb3\xa8\xe6\x95\xb0'),
        ),
        migrations.AddField(
            model_name='headhunter',
            name='tag',
            field=models.CharField(default=b'\xe6\x97\xa0', max_length=200, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
        migrations.AddField(
            model_name='networkscale',
            name='total_comment',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\x80\xbb\xe8\xaf\x84\xe8\xae\xba\xe6\x95\xb0'),
        ),
        migrations.AddField(
            model_name='networkscale',
            name='total_like',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\x80\xbb\xe7\x82\xb9\xe8\xb5\x9e\xe6\x95\xb0'),
        ),
        migrations.AddField(
            model_name='networkscale',
            name='total_repost',
            field=models.IntegerField(default=0, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe6\x80\xbb\xe8\xbd\xac\xe5\x8f\x91\xe6\x95\xb0'),
        ),
    ]
