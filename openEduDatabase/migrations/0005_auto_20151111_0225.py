# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openEduDatabase', '0004_auto_20151102_2117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentincourse',
            name='course',
        ),
        migrations.RemoveField(
            model_name='studentincourse',
            name='student',
        ),
        migrations.RemoveField(
            model_name='breakpointscore',
            name='student_in_course',
        ),
        migrations.AddField(
            model_name='breakpoint',
            name='course',
            field=models.ForeignKey(related_name='breakpoints', default=1, to='openEduDatabase.Course'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breakpoint',
            name='teacher',
            field=models.ForeignKey(related_name='breakpoints', default=1, to='openEduDatabase.Teacher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='breakpointscore',
            name='student',
            field=models.ForeignKey(related_name='breakpoint_score', default=3, to='openEduDatabase.Student'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='teacher',
            field=models.ForeignKey(related_name='lectures', default=None, to='openEduDatabase.Teacher'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='breakpoint',
            name='lecture',
            field=models.ForeignKey(related_name='breakpoints', to='openEduDatabase.Lecture'),
        ),
        migrations.AlterField(
            model_name='breakpointscore',
            name='breakpoint',
            field=models.ForeignKey(related_name='breakpoint_score', to='openEduDatabase.Breakpoint'),
        ),
        migrations.AlterField(
            model_name='course',
            name='teacher',
            field=models.ForeignKey(related_name='courses', to='openEduDatabase.Teacher'),
        ),
        migrations.AlterField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(related_name='lectures', to='openEduDatabase.Course'),
        ),
        migrations.DeleteModel(
            name='StudentInCourse',
        ),
    ]
