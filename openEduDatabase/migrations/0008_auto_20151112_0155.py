# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openEduDatabase', '0007_auto_20151112_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='breakpointscore',
            name='breakpoint',
            field=models.ForeignKey(related_name='breakpoint_scores', to='openEduDatabase.Breakpoint'),
        ),
        migrations.AlterField(
            model_name='breakpointscore',
            name='student',
            field=models.ForeignKey(related_name='breakpoint_scores', to='openEduDatabase.Student'),
        ),
    ]
