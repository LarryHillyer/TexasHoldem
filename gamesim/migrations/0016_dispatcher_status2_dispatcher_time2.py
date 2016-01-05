# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamesim', '0015_analyzed_jobs'),
    ]

    operations = [
        migrations.CreateModel(
            name='dispatcher_status2',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('status', models.CharField(default='Stopped', max_length=8, choices=[('Stopped', 'Stopped'), ('Idle', 'Idle'), ('Running', 'Running'), ('Finished', 'Finished')])),
                ('job_name', models.CharField(max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='dispatcher_time2',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('time_delta', models.TimeField(null=True)),
            ],
        ),
    ]
