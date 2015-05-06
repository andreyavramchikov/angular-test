# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20150304_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
