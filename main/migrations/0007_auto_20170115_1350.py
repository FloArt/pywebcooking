# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170114_2230'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='url',
            field=models.CharField(unique=True, max_length=100),
        ),
    ]
