# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openEduDatabase', '0002_auto_20151014_2213'),
    ]

    operations = [
        migrations.CreateModel(
            name='BreakpointScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
            ],
        ),
        migrations.RenameModel(
            old_name='Quiz',
            new_name='Breakpoint',
        ),
        migrations.RemoveField(
            model_name='quizscore',
            name='quiz',
        ),
        migrations.RemoveField(
            model_name='quizscore',
            name='student',
        ),
        migrations.RenameField(
            model_name='breakpoint',
            old_name='quiz_description',
            new_name='breakpoint_description',
        ),
        migrations.RenameField(
            model_name='breakpoint',
            old_name='quiz_name',
            new_name='breakpoint_name',
        ),
        migrations.DeleteModel(
            name='QuizScore',
        ),
        migrations.AddField(
            model_name='breakpointscore',
            name='breakpoint',
            field=models.ForeignKey(to='openEduDatabase.Breakpoint'),
        ),
        migrations.AddField(
            model_name='breakpointscore',
            name='student',
            field=models.ForeignKey(to='openEduDatabase.Student'),
        ),
    ]
