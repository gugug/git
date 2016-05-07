# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuqing', '0002_auto_20160411_1510'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('blog_id', models.CharField(max_length=20, serialize=False, verbose_name=b'\xe5\x8d\x9a\xe6\x96\x87id', primary_key=True)),
                ('event_id', models.CharField(max_length=20, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6id')),
                ('content', models.TextField(verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe5\x86\x85\xe5\xae\xb9')),
            ],
            options={
                'db_table': 'content',
            },
        ),
        migrations.CreateModel(
            name='Participate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_id', models.CharField(max_length=20, verbose_name=b'\xe7\x94\xa8\xe6\x88\xb7id')),
                ('event_id', models.CharField(max_length=20, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6id')),
            ],
            options={
                'db_table': 'participate',
            },
        ),
        migrations.RenameField(
            model_name='increment',
            old_name='id',
            new_name='iid',
        ),
        migrations.RenameField(
            model_name='networkscale',
            old_name='corpus',
            new_name='corpus_dir',
        ),
        migrations.RenameField(
            model_name='networkscale',
            old_name='id',
            new_name='nid',
        ),
        migrations.RemoveField(
            model_name='event',
            name='content',
        ),
        migrations.RemoveField(
            model_name='networkscale',
            name='topic',
        ),
        migrations.RemoveField(
            model_name='networkscale',
            name='total_comment',
        ),
        migrations.RemoveField(
            model_name='networkscale',
            name='total_like',
        ),
        migrations.RemoveField(
            model_name='networkscale',
            name='total_repost',
        ),
        migrations.AddField(
            model_name='networkscale',
            name='event_id',
            field=models.CharField(default=0, max_length=20, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6id'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='participate',
            unique_together=set([('user_id', 'event_id')]),
        ),
    ]
