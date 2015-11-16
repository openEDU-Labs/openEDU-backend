# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openEduDatabase', '0008_auto_20151112_0155'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='lecture_data',
            field=models.TextField(default=' '),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='lecture_link',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
