# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='art',
            name='artist',
            field=models.CharField(max_length=120, blank=True),
            preserve_default=True,
        ),
    ]
