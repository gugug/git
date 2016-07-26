# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuqing', '0005_auto_20160501_0702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='topic_words',
            field=models.CharField(max_length=300, verbose_name=b'\xe4\xb8\xbb\xe9\xa2\x98\xe8\xaf\x8d'),
        ),
    ]
