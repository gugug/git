# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuqing', '0003_auto_20160416_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='post_time',
            field=models.DateTimeField(null=True, verbose_name=b'\xe5\x8d\x9a\xe6\x96\x87\xe5\x8f\x91\xe8\xa1\xa8\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
