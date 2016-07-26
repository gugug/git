# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuqing', '0006_auto_20160501_0736'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='keywords',
            field=models.TextField(null=True, verbose_name=b'\xe4\xba\x8b\xe4\xbb\xb6\xe5\x85\xb3\xe9\x94\xae\xe8\xaf\x8d'),
        ),
    ]
