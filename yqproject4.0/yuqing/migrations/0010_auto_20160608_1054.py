# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuqing', '0009_auto_20160514_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headhunter',
            name='tag',
            field=models.CharField(max_length=200, verbose_name=b'\xe6\xa0\x87\xe7\xad\xbe'),
        ),
        migrations.AlterField(
            model_name='headhunter',
            name='vip_state',
            field=models.CharField(max_length=30, verbose_name=b'\xe8\xae\xa4\xe8\xaf\x81\xe4\xbf\xa1\xe6\x81\xaf'),
        ),
    ]
