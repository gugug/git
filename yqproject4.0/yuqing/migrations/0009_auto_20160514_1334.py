# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuqing', '0008_remove_networkscale_data_dir'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='topic',
            new_name='etopic',
        ),
        migrations.RemoveField(
            model_name='event',
            name='topic_words',
        ),
        migrations.AddField(
            model_name='content',
            name='topic',
            field=models.CharField(max_length=100, null=True, verbose_name=b'[]\xe9\x87\x8c\xe7\x9a\x84\xe5\x8d\x9a\xe6\x96\x87\xe4\xb8\xbb\xe9\xa2\x98'),
        ),
        migrations.AddField(
            model_name='content',
            name='topic_words',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe4\xb8\xbb\xe9\xa2\x98\xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d'),
        ),
        migrations.AddField(
            model_name='networkscale',
            name='sna_dir',
            field=models.CharField(max_length=300, null=True, verbose_name=b'sna\xe5\x9b\xbe\xe7\x9a\x84\xe8\xb7\xaf\xe5\xbe\x84'),
        ),
        migrations.AlterField(
            model_name='content',
            name='event_id',
            field=models.CharField(max_length=20, null=True, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6id'),
        ),
        migrations.AlterField(
            model_name='event',
            name='link',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
        migrations.AlterField(
            model_name='event',
            name='origin',
            field=models.CharField(max_length=100, null=True, verbose_name=b'\xe4\xbc\xa0\xe6\x92\xad\xe6\xba\x90'),
        ),
        migrations.AlterField(
            model_name='networkscale',
            name='corpus_dir',
            field=models.CharField(max_length=300, null=True, verbose_name=b'\xe8\xaf\xad\xe6\x96\x99\xe6\x96\x87\xe6\x9c\xac'),
        ),
        migrations.AlterField(
            model_name='networkscale',
            name='label_dir',
            field=models.CharField(max_length=300, null=True, verbose_name=b'label.xls\xe7\x9a\x84\xe8\xb7\xaf\xe5\xbe\x84'),
        ),
        migrations.AlterField(
            model_name='networkscale',
            name='leader',
            field=models.CharField(max_length=50, null=True, verbose_name=b'\xe6\xa0\xb8\xe5\xbf\x83\xe4\xba\xba\xe7\x89\xa9'),
        ),
    ]
