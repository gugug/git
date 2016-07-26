# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('event_id', models.CharField(max_length=20, serialize=False, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6id', primary_key=True)),
                ('post_time', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe8\xb5\xb7\xe6\x97\xb6\xe9\x97\xb4')),
                ('topic', models.CharField(max_length=100, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe4\xb8\xbb\xe9\xa2\x98')),
                ('topic_words', models.CharField(max_length=100, verbose_name=b'\xe4\xb8\xbb\xe9\xa2\x98\xe8\xaf\x8d')),
                ('origin', models.CharField(max_length=100, verbose_name=b'\xe4\xbc\xa0\xe6\x92\xad\xe6\xba\x90')),
                ('link', models.CharField(max_length=100, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe9\x93\xbe\xe6\x8e\xa5')),
                ('content', models.TextField()),
            ],
            options={
                'db_table': 'event',
            },
        ),
        migrations.CreateModel(
            name='Headhunter',
            fields=[
                ('user_id', models.CharField(max_length=20, serialize=False, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7id', primary_key=True)),
                ('user_name', models.CharField(max_length=20, verbose_name=b'\xe6\x98\xb5\xe7\xa7\xb0')),
                ('gender', models.CharField(default=b'\xe6\x9c\xaa\xe7\x9f\xa5', max_length=6, verbose_name=b'\xe6\x80\xa7\xe5\x88\xab')),
                ('birth', models.DateField(verbose_name=b'\xe7\x94\x9f\xe6\x97\xa5')),
                ('vip_state', models.CharField(default=b'\xe9\x9d\x9e\xe8\xae\xa4\xe8\xaf\x81\xe7\x94\xa8\xe6\x88\xb7', max_length=30, verbose_name=b'\xe8\xae\xa4\xe8\xaf\x81\xe4\xbf\xa1\xe6\x81\xaf')),
                ('location', models.CharField(max_length=10, verbose_name=b'\xe5\x9c\xb0\xe5\x8c\xba')),
                ('profile', models.TextField(max_length=300, verbose_name=b'\xe7\xae\x80\xe4\xbb\x8b')),
            ],
            options={
                'db_table': 'headhunter',
            },
        ),
        migrations.CreateModel(
            name='Increment',
            fields=[
                ('id', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('event_id', models.CharField(max_length=20, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6id')),
                ('check_time', models.DateTimeField(verbose_name=b'\xe6\xa3\x80\xe6\xb5\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('comment_num', models.IntegerField(default=0, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba\xe6\x95\xb0')),
                ('repost_num', models.IntegerField(default=0, verbose_name=b'\xe8\xbd\xac\xe5\x8f\x91\xe6\x95\xb0')),
                ('like_num', models.IntegerField(default=0, verbose_name=b'\xe7\x82\xb9\xe8\xb5\x9e\xe6\x95\xb0')),
            ],
            options={
                'db_table': 'increment',
            },
        ),
        migrations.CreateModel(
            name='NetworkScale',
            fields=[
                ('id', models.IntegerField(serialize=False, auto_created=True, primary_key=True)),
                ('topic', models.CharField(max_length=100, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe4\xb8\xbb\xe9\xa2\x98')),
                ('check_time', models.DateTimeField(verbose_name=b'\xe6\xa3\x80\xe6\xb5\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('corpus', models.CharField(max_length=200, verbose_name=b'\xe8\xaf\xad\xe6\x96\x99\xe6\x96\x87\xe6\x9c\xac')),
                ('data_dir', models.CharField(max_length=200)),
                ('label_dir', models.CharField(max_length=200)),
                ('leader', models.CharField(max_length=50, verbose_name=b'\xe6\xa0\xb8\xe5\xbf\x83\xe4\xba\xba\xe7\x89\xa9')),
            ],
            options={
                'db_table': 'networkscale',
            },
        ),
    ]
