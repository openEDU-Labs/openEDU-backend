# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openEduDatabase', '0003_auto_20151016_0222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breakpointscore',
            name='student',
        ),
        migrations.AddField(
            model_name='breakpointscore',
            name='student_in_course',
            field=models.ForeignKey(default=None, to='openEduDatabase.StudentInCourse'),
            preserve_default=False,
        ),
    ]
