# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuqing', '0004_content_post_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkscale',
            name='corpus_dir',
            field=models.CharField(max_length=300, verbose_name=b'\xe8\xaf\xad\xe6\x96\x99\xe6\x96\x87\xe6\x9c\xac'),
        ),
        migrations.AlterField(
            model_name='networkscale',
            name='data_dir',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='networkscale',
            name='label_dir',
            field=models.CharField(max_length=300),
        ),
    ]
