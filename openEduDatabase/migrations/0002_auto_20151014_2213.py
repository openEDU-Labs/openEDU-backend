# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openEduDatabase', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lecture',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lecture_name', models.CharField(max_length=50)),
                ('lecture_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quiz_name', models.CharField(max_length=50)),
                ('quiz_description', models.CharField(max_length=500)),
                ('lecture', models.ForeignKey(to='openEduDatabase.Lecture')),
            ],
        ),
        migrations.CreateModel(
            name='QuizScore',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.IntegerField(default=0)),
                ('quiz', models.ForeignKey(to='openEduDatabase.Quiz')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('student_name', models.CharField(max_length=50)),
                ('student_school', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentInCourse',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.RenameModel(
            old_name='Class',
            new_name='Course',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='class_description',
            new_name='course_description',
        ),
        migrations.RenameField(
            model_name='course',
            old_name='class_name',
            new_name='course_name',
        ),
        migrations.AddField(
            model_name='studentincourse',
            name='course',
            field=models.ForeignKey(to='openEduDatabase.Course'),
        ),
        migrations.AddField(
            model_name='studentincourse',
            name='student',
            field=models.ForeignKey(to='openEduDatabase.Student'),
        ),
        migrations.AddField(
            model_name='quizscore',
            name='student',
            field=models.ForeignKey(to='openEduDatabase.Student'),
        ),
        migrations.AddField(
            model_name='lecture',
            name='course',
            field=models.ForeignKey(to='openEduDatabase.Course'),
        ),
    ]
