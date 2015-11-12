# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openEduDatabase', '0006_course_students'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='breakpoint',
            name='course',
        ),
        migrations.RemoveField(
            model_name='breakpoint',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='lecture',
            name='teacher',
        ),
    ]
