# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('yuqing', '0007_content_keywords'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkscale',
            name='data_dir',
        ),
    ]
